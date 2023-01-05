from __future__ import unicode_literals
from collections import Counter
from halo import Halo
from tabulate import tabulate
import locale
locale.setlocale(locale.LC_ALL, '')
import random
import time

rowsToGen = int(input('How many AZ Pick rows would you like to play?\n'))
seeAll = str(input('Would you like to see all of the numbers and their occurances (y/n)?\n'))

if seeAll != 'y' or seeAll == "":
	numsOfTop = int(input('How many of the top occuring numbers would you like to see?\n'))

spinner = Halo(text='Calculating Numbers...', spinner='growHorizontal')
lottoNums = []

try:
	spinner.start()
	time.sleep(3)
	spinner.text = "Good luck winning the Pick!"
	time.sleep(2)
	spinner.text = "What you gonna do with all that money!?"
	
	for i in range(0,rowsToGen):
		for i in range(0,6):
		    x = random.randint(1,44)
		    lottoNums.append(x)
	counter = Counter(lottoNums)
	mostCommon = counter.most_common()
	topSixNums = []
	
	if seeAll == 'n':
		for i in range(0,numsOfTop):
			topSixNums.append(mostCommon[i])
	if seeAll == 'y':
		topSixNums = mostCommon
	
	spinner.stop_and_persist(symbol='🦄'.encode('utf-8'), text='Here We Go!')
	print(tabulate(topSixNums, headers=['Number','Occurance']))
	print("Total numbers played:", f'{len(lottoNums):n}')

except (KeyboardInterrupt, SystemExit):
    spinner.stop()
