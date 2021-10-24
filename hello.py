#!/users/rameseka/python2.7/bin/python2.7
import simplejson as json

print("Hello All")
file = open("samp.json","r").read()
data=json.loads(file)
for k,v in data.items():
   print(v)	   
