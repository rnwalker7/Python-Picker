import json
import random
import sys
import glob
import xml.etree.ElementTree as ET

myNames = []

for files in glob.glob("*.xml"):
    tree = ET.parse(files)
    root = tree.getroot()
    startHere = root[0]

    for names in startHere.iter():
        if "Sgt" in str(names.text):
            myNames.append(names.text)

random.shuffle(myNames)
print(len(myNames))

with open("uub.txt", "w") as f:
    for names in myNames:
        f.write("%s\n" % names)

    # try:
    #     x = names.text
    #     print(x)
    #     break
    # except Exception as err1:
    #     pass
    # myNames.append(x)

# print(myNames)

# myFile = open('roster.json')
# data = json.load(myFile)
# myFile.close()

# newData = []

# for names in data:
#     if names["available"] == True:
#         newData.append(names)

# random.seed()

# if len(sys.argv) > 1:
#     if sys.argv[1] == "3":
#         x = random.randint(0, (len(newData) - 1))
#         print("Thursday: " + newData[x]["name"])

# x = random.randint(0, (len(newData) - 1))
# print("Friday: " + newData[x]["name"])

# x = random.randint(0, (len(newData) - 1))
# print("Saturday: " + newData[x]["name"])