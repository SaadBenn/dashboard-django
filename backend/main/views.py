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
    data = {}

    if employeeObj:
        for subject in employeeObj:
    
            # the current user is a subject and has managers under him.
            managerSet = EmployeeRelation.objects.filter(reporting_to_id=int(subject.employee_id))
    
            # if the person below is also a manager
            if managerSet:
                for salesrep in managerSet:
                    temp = {}
                    temp = get_revenue_sum(salesrep.employee.id)
                    logger.debug(temp)
                    data = {**data,**temp}
            else:
                temp = {}
                temp = get_revenue_sum(subject.employee.id)
                logger.debug(temp)
                data = {**data,**temp}

    else:
        data = get_revenue_sum(user_id)

    return JsonResponse({"revenue": data})

def get_revenue_sum(salesrep_id):
    
    salesRepObj = EmployeeRelation.objects.get(employee_id=salesrep_id)
    full_name = salesRepObj.employee.get_full_name()
    revenue = "{:.2f}".format(SalesLines.objects.filter(rep_id=salesrep_id).aggregate(Sum('revenue'))['revenue__sum'])
    return {full_name:revenue}