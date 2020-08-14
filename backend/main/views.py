from django.http import JsonResponse
from typing import List, Union
from django.db.models import Sum, Q
from .models import EmployeeRelation, SalesLines
from datetime import datetime
from backend.helpers import date_range_intersect


def get_revenue_by_sales_rep(request, user_id):
    return JsonResponse({ "revenue": [] })
