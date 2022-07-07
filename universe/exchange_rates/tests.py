from django.test import TestCase
from requests import get, utils
from decimal import Decimal
from datetime import date
import re


# def currency_rates(name):

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)

# ind = content.find(name.upper())
# if ind == -1:
#     return None

cur_date = content[content.find('ValCur')+14:content.find('ValCur')+24]
# current_content = content[ind:ind + 150]
valutes = {}
res = content.split('><Valute')
for valute in res:
    print(valute)
# print(content)



