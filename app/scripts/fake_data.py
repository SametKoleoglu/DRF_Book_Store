from books.api.serializers import *
from faker import Faker
from django.contrib.auth.models import User
import django
import os
import random
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookstore.settings")


django.setup()


def set_user():
    fake = Faker(["tr_TR"])

    f_name = fake.first_name()
    l_name = fake.last_name()
    u_name = f"{f_name}_{l_name}"
    email = f"{u_name}@{fake.domain_name()}"
    print(f"{f_name} {l_name} {u_name} {email}")

    user_check = User.objects.filter(username=u_name)

    while user_check.exists():
        u_name = u_name + str(random.randrange(1, 99))

    user = User(
        username=u_name,
        first_name=f_name,
        last_name=l_name,
        email=email
    )

    user.set_password("1234")
    user.save()


def add_book(subject):
    fake = Faker(["tr_TR"])
    response = requests.get(f"https://openlibrary.org/search.json?q={subject}")

    jsn = response.json()

    books = jsn["docs"]

    for book in books:
        data = {
            "title": book["title"],
            "author": book["author_name"][0],
            "description": fake.paragraph(),
            "release_date": book["first_publish_year"],
            # "updated_date": book["last_modified"]
        }
        
        print(data)

        serializer = BookSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
        else:
            continue
