# Pythonda modul

# import math

# print(math.pi)
# print(math.e)

# from math import pi
# from math import e

# print(pi)
# print(e)

# from math import factorial as f
# import random as r

# print(f(6))
# print(r.randint(1,10))

# from calendar import *

# y = 2022
# m = 10

# print(month(y,m))

# import test

# print(test.m)
# print(test.summa(15,2))

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

app.run(host='0.0.0.0', port=81)