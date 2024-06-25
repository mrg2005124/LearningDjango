from . import jalali
from django.utils import timezone


# convert eng digit to persian
def persian_num(mystr):
    nums={
        '0':'۰',
        '1':'۱',
        '2':'۲',
        '3':'۳',
        '4':'۴',
        '5':'۵',
        '6':'۶',
        '7':'۷',
        '8':'۸',
        '9':'۹'
    }
    for e, p in nums.items():
        mystr = mystr.replace(e,p)
    return mystr

# convert to persian calendar
def jalali_converter(time):
    time = timezone.localtime(time)
    str_time = (f"{time.year},{time.month},{time.day}")
    jmonths = [
        'فروردین',
        'اردیبهشت',
        'خرداد',
        'تیر',
        'مرداد',
        'شهریور',
        'مهر',
        'آبان',
        'آذر',
        'دی',
        'بهمن',
        'اسفند'
    ]
    tuple_time = jalali.Gregorian(str_time).persian_tuple()
    list_time = list(tuple_time)
    for index, month in enumerate(jmonths):
        if list_time[1] == index + 1:
            list_time[1] = month
            break
    
    output = f"{tuple_time[2]} {list_time[1]} {tuple_time[0]} ساعت {time.hour}:{time.minute}"
    return persian_num(output)
    