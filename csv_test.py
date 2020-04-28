"""import csv

#with open("MYfile.csv",w) as bob:
#c = csv.writer(bob, delimiter=',')
c = csv.writer(open("MYfile.csv",'w'), delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
b=["Name","Address","Telephone","Fax","E-mail","Others"]
c.writerow(b)
c.writerow(["a","b","b","d","E","f"])
#c.close()
cr = csv.reader(open("MYFILE.csv","rb"))
for row in cr: 
	print(str(row))"""
import time 
from datetime import datetime
#print("abc"+"Cde")
import csv

c = csv.writer(open("M-Y           .le.csv",'w'), delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)