from django.shortcuts import render
from django.utils import timezone
from django.db.models import F, DurationField, Sum, ExpressionWrapper
from datetime import datetime, time, timedelta
from .models import Times

# Create your views here.

def home_view(request):

    day_since=timezone.now().date()-timedelta(days=7)       
    query_times = Times.objects.filter(end_time__isnull = False).filter(my_date__gte=day_since).annotate(duration=ExpressionWrapper(
                F('end_time') - F('start_time'), output_field=DurationField()))
    total_time = query_times.aggregate(total_time=Sum('duration'))
    print(total_time)
    sum_time=total_time.get('total_time')
    if sum_time is not None:        
            days=sum_time.days*60 
            seconds=sum_time.seconds
            hours=seconds//3600+days
            minutes=(seconds//60)%60       
    else:
            days=0
            seconds=0
            hours=0
            minutes=0

    context= {"query_times": query_times,
                "hours": hours,
                "minutes": minutes}
    
    return render(request, "index.html", context)
