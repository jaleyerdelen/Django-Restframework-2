import os
import random
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "book_shop.settings")

import django
django.setup()

#sıralaması önemli bu düzende yazmamız gerekiyor
#user modelimizi çekebilmek için kullandık yukarıdakileri

from django.contrib.auth.models import User

import os
from dotenv import load_dotenv
load_dotenv()

USER_KEY = str(os.getenv('USER_KEY'))

from faker import Faker
fake = Faker(['en_US'])

def set_user():
    f_name = fake.first_name()
    l_name = fake.last_name()
    u_name = f"{f_name.lower()}_{l_name.lower()}"
    email = f"{u_name}@{fake.domain_name()}"
    print(f_name, l_name, email)

    user_check = User.objects.filter(username=u_name)

    while user_check.exists():
        u_name = u_name + str(random.randrange(1,99)) #eğer username varsa yanına username +  1 ile 99 arasında bir sayı koy
        user_check = User.objects.filter(username=u_name) #eklediği username varsa datada bu sefer false dönecek  
        #ve aşağıdaki koda geçip yeni bir username yaratacak

    user = User(
        username = u_name,
        first_name = f_name,
        last_name = l_name,
        email = email,
        is_staff = fake.boolean(chance_of_getting_true=50)
    )

    user.set_password({USER_KEY})
    user.save()
    print("User is saved", u_name)