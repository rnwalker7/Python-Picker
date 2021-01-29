import json
import random

myFile = open('roster.json')
data = json.load(myFile)
myFile.close()

newData = []

for names in data:
    if names["available"] == True:
        newData.append(names)

x = random.randint(0, (len(newData) - 1))

print("Friday: " + newData[x]["name"])

x = random.randint(0, (len(newData) - 1))

print("Saturday: " + newData[x]["name"])