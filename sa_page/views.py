from django.http import HttpResponseServerError
from django.shortcuts import render
from sa_page.models import *
import copy
import json

WEEK = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二']
DAY = {'Mon': '一', 'Tue': '二', 'Wed': '三', 'Thu':'四', 'Fri': '五', 'Sat': '六', 'Sun': '日'}
TWELVE_WEEK_HEATMAP = [{'day': f'星期{day}', 'hour': str(hour), 'users': '0'}
                        for day in list(DAY.values())
                            for hour in range(24)]


def index(request):
    return render(request, 'sa_index.html')

def usage(request):
    type_name = request.GET.get('type_name', False)
    type_level = request.GET.get('type_level', False)

    if type_name and type_level:
        regular_usage = SaRegularUsersByType.objects.using('ADS')
        regular_usage = regular_usage.filter(
                            type_name = type_name, type_level = type_level
                        ).order_by(
                            'week_number'
                        )
        regular_usage = list(regular_usage.values())
        hourly_usage = SaHourlyUsageByType.objects.using('ADS')
        hourly_usage = hourly_usage.filter(
                            type_name = type_name, type_level = type_level
                        ).order_by(
                            'weekday_name_abbreviated', 'hour'
                        )
        hourly_usage = list(hourly_usage.values())
    else:
        regular_usage = list(SaRegularUsersOverview.objects.using('ADS').order_by('week_number').values())
        hourly_usage = list(SaHourlyUsageOverview.objects.using('ADS').order_by('weekday_name_abbreviated', 'hour').values())

    if(len(regular_usage) != 12): return HttpResponseServerError('資料抓取未滿12週')

    overview = {}
    overview['regular_usage'] = [regular_usage[-1]['regular_percentage'],
                                regular_usage[-1]['avg_usage_over_3_days']]
    overview['twelve_week_avgusers'] = []
    bar_chart = {}
    bar_chart['stack'] = []
    bar_chart['line'] = []
    heatmap = TWELVE_WEEK_HEATMAP

    for idx, usage in enumerate(regular_usage):
        overview['twelve_week_avgusers'].append(
            {
                'week': WEEK[idx],
                'avg_usage_over_3_days': usage['avg_usage_over_3_days']
            }
        )
        bar_chart['stack'].append(
            {
                'week': f'第{WEEK[idx]}週',
                'value': {
                    'avg_usage_1_days': usage['avg_usage_1_days'],
                    'avg_usage_2_days': usage['avg_usage_2_days'],
                    'avg_usage_over_3_days': usage['avg_usage_over_3_days']
                }
            }
        )
        bar_chart['line'].append(
            {
                'week': f'第{WEEK[idx]}週',
                'value': {
                    'avg_usage_over_3_days': usage['avg_usage_over_3_days'],
                    'opened_sa_in_four_weeks': usage['opened_sa_in_four_weeks'],
                    'regular_percentage': usage['regular_percentage']
                }
            }
        )

    heatmap = copy.deepcopy(TWELVE_WEEK_HEATMAP)
    for usage in hourly_usage:
        day = list(DAY)
        data = heatmap[day.index(usage['weekday_name_abbreviated'])*24+usage['hour']]
        data['users'] = str(usage['number_of_users'])

    context = {'overview': overview, 'bar_chart': bar_chart, 'heatmap': heatmap}
    context = json.dumps(context)
    return render(request, 'pd_data.html', {'context': context})
