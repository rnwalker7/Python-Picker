import json
import random
import sys

myFile = open('roster.json')
data = json.load(myFile)
myFile.close()

newData = []

for names in data:
    if names["available"] == True:
        newData.append(names)

random.seed()

if len(sys.argv) > 1:
    if sys.argv[1] == "3":
        x = random.randint(0, (len(newData) - 1))
        print("Thursday: " + newData[x]["name"])

x = random.randint(0, (len(newData) - 1))
print("Friday: " + newData[x]["name"])

x = random.randint(0, (len(newData) - 1))
print("Saturday: " + newData[x]["name"])