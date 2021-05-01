import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','registration.settings')
django.setup()


from testapp.models import *
from faker import Faker
from random import *
fake=Faker()
def populate(n):
    for i in range(n):
        femail=fake.email()
        fpwd=fake.city()
        emp_record=UsersTable.objects.get_or_create(email=femail,password=fpwd)
n=int(input("enter number of users"))
populate(n)
