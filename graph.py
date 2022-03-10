# from hashlib import new
from re import M
import matplotlib.pyplot as plt
import matplotlib
print(matplotlib.__version__)
import numpy as np
plt.style.use('_mpl-gallery')

file = open('CupcakeInvoices.csv')

total = 0 
choc_prof = 0
van_prof = 0
straw_prof = 0
for x in file:
    new_x = x.split(',')
    if new_x[2] == 'Chocolate':
        choc_prof += (float(new_x[3])*float(new_x[4]))
    elif new_x[2] == 'Vanilla':
        van_prof += (float(new_x[3])*float(new_x[4]))
    elif new_x[2] == 'Strawberry':
        straw_prof += (float(new_x[3])*float(new_x[4]))

cupcakes = ['Chocolate', 'Vanilla', 'Strawberry']
profits = [choc_prof, van_prof, straw_prof]

plt.bar(cupcakes, profits, color = 'blue', width = .4)
plt.title('profits')
plt.show()



file.close
