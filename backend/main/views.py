from django.http import JsonResponse
from typing import List, Union
from django.db.models import Sum, Q
from .models import EmployeeRelation, SalesLines
from datetime import datetime
from backend.helpers import date_range_intersect
import logging

logger = logging.getLogger(__name__)

def get_revenue_by_sales_rep(request, user_id):    
    employeeObj = EmployeeRelation.objects.filter(reporting_to_id=user_id)
    data = []

    # user id could be a director or a manager or just a sales rep - hierarchy below
    # - director   - root
    #   - managers
    #       - sales rep
    if employeeObj:
        for subject in employeeObj:
    
            # check if the current user has managers under him.
            managerSet = EmployeeRelation.objects.filter(reporting_to_id=int(subject.employee_id))
    
            # if the person below is also a manager - need to get the sales rep under him/her
            if managerSet:
                for salesrep in managerSet:
                    temp = get_revenue_sum(salesrep.employee.id)
                    data.append(temp)
            else:
                # no managers under this subject - get the revenue directly
                temp = get_revenue_sum(subject.employee.id)
                data.append(temp)

    else:
        # person is a sales rep - assumption (nobody works under a sales rep)
        data.append(get_revenue_sum(user_id))


    return JsonResponse({"revenue": data})

# func to get revenue associated with the id
# returns the full name of the sales rep and the revenue
def get_revenue_sum(salesrep_id):
    salesRepObj = EmployeeRelation.objects.get(employee_id=salesrep_id)
    full_name = salesRepObj.employee.get_full_name()
    # calculate the revenue of the sales rep by browsing through the sales lines table
    sales_revenue = "{:.2f}".format(SalesLines.objects.filter(rep_id=salesrep_id).aggregate(Sum('revenue'))['revenue__sum'])

    return {"name":full_name, "revenue":sales_revenue}

