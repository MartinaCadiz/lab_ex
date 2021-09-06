# -*- coding: utf-8 -*-
"""randomKaomoji.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X-ET1am6SdiPiPZI3qmq_yfCZUCAvHxt
"""

import random
import requests 
import bs4      

res = requests.get('https://www.tldevtech.com/kaomoji/')
soup = bs4.BeautifulSoup(res.text, 'lxml')

kaomoji = []

for bar in soup.find_all('button', attrs={'class': "btn"}):
  kaomoji.append(bar.text )


def random_kaomoji():
  print(kaomoji[random.randint(0, 524)])