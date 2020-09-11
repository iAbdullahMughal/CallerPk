import json
import re

from django.http import HttpResponse

from caller.core.search.search_record import SearchRecord
from caller.models import PhoneNumbersModel

import math

millnames = ['', ' Thousand', ' Million', ' Billion', ' Trillion']


def millify(n):
    n = float(n)
    millidx = max(0, min(len(millnames) - 1,
                         int(math.floor(0 if n == 0 else math.log10(abs(n)) / 3))))

    return '{:.0f}{}'.format(n / 10 ** (3 * millidx), millnames[millidx])


def phone_number_added(request):
    try:
        count = PhoneNumbersModel.objects.all().count()
        count = millify(count)
    except:
        count = 0

    return HttpResponse(count)


def phone_number_scanned(request):
    try:
        #     print(str(CnicNumbersModel.objects.all().count()))
        count = PhoneNumbersModel.objects.filter(has_processed=True).count()
        count = millify(count)
    except:
        count = 0

    return HttpResponse(count)


def ajax_search(request):
    content = {
        'has_error': True,
        'error_message': None,
    }
    phone_number = request.POST.get('phone_number', '')
    mobile_number = '^((\+92)|(0092))-{0,1}\d{3}-{0,1}\d{7}$|^\d{11}$|^\d{10}$|^\d{4}-\d{7}$'

    if not phone_number:
        content['has_error'] = True
        content['error_message'] = {
            'title': 'No phone number found',
            'description': 'Please provide mobile phone number.'
        }
        content = json.dumps(content)
        return HttpResponse(content, content_type="application/json")

    result = re.match(mobile_number, phone_number)

    if result:
        search_obj = SearchRecord(phone_number)
        if not search_obj.is_valid:
            content['has_error'] = True
            content['error_message'] = {
                'title': 'Invalid phone number provided',
                'description': 'Please provide correct phone number. Supported format\n [00923131234567, '
                               '+923131234567, 03131234567, 3131234567]'
            }
            content = json.dumps(content)
            return HttpResponse(content, content_type="application/json")
        status_code, mobile_information = search_obj.get_report()
        if not status_code:
            content['has_error'] = False
            content['has_found'] = False
            content['error_message'] = {
                'title': 'Invalid phone number provided',
                'description': 'Please provide correct phone number. Supported format\n [00923131234567, '
                               '+923131234567, 03131234567, 3131234567]'
            }
            content = json.dumps(content)
            return HttpResponse(content, content_type="application/json")
        else:
            content['has_error'] = False
            content['has_found'] = True
            content['report'] = mobile_information

            content = json.dumps(content)
            return HttpResponse(content, content_type="application/json")
    else:
        content['has_error'] = True
        content['error_message'] = {
            'title': 'Invalid phone number provided',
            'description': 'Please provide correct phone number. Supported format\n [00923131234567, '
                           '+923131234567, 03131234567, 3131234567]'
        }
        content = json.dumps(content)
        return HttpResponse(content, content_type="application/json")
