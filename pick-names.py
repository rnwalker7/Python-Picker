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
