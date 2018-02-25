import string, random
from datetime import timedelta, date

def generator_code(size=6,chars = string.ascii_lowercase+ string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create(instance, size = 6):
    new_code = generator_code(size=size)
    Shortner = instance.__class__
    sh_exist = Shortner.objects.filter(shortcode = new_code).exists()

    if sh_exist:
        return create(size=size)
    return new_code



def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def month_date(start,end, year):
    start_date = date(year, start, 1)
    end_date = date(year, end, 1)
    days = []
    for single_date in daterange(start_date, end_date):
        days.append(single_date.strftime("%Y-%m-%d"))
    return days
