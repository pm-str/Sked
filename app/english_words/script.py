# Англо-русский словарь компьютерных терминов из книги Бьерна Страуструпа по С++:

import re
import django
import os
import requests
import sys

from django.conf import settings

from conf import settings as default_settings

page = requests.get('http://kak-tot.narod.ru/ru/otd-bs2e/dict.htm')
content = page.content.decode()

pattern = re.compile('([a-zA-Z- .,+/]*[a-zA-Z-.,+/]+)[ ]{4,}([а-яА-Я-.,+/]+[а-яА-Я- .,+/]*[а-яА-Я-.,+/]+)\r\n')
data = re.findall(pattern, content)

base = ''

fmt_array = []

for word, translation in data:
    if not word.startswith(6*' '):
        full_phrase = word.strip()
        base = full_phrase
    else:
        full_phrase = base + ' ' + word.strip()

    fmt_array.append((full_phrase, translation.strip()))

sys.path.append(os.path.abspath(os.path.curdir))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
django.setup()

from app.english_words.models import Word
from app.user.models import UserProfile

u = UserProfile.objects.first()

Word.objects.bulk_create(
    Word(user=u, name=i[0], translation=i[1]) for i in fmt_array
)