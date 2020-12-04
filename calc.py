
import re

keywords = ["byr","iyr","eyr","hcl", "hgt","ecl","pid"]
eyeColor = ["amb","blu","brn","gry","grn","hzl","oth"]
validChrs = [0, 1,2,3,4,5,6,7,8,9,"a", "b", "c", "d", "e", "f"]
f = open('input.txt', 'r+')
data = f.read().rstrip().split("\n\n")
badCount = 0

for thing in data:
    newThing = thing.rstrip().replace("\n", " ")
    currDict = {}
    badFlag = False
    print('--------------')
    for preDict in newThing.split():
        temp = preDict.split(":")
        currDict[temp[0]] = temp[1]
    for word in keywords:
        found = newThing.find(word)
        if found == -1:
            # badCount+=1
            badFlag = True
    print(len(currDict))
    if (len(currDict) < 7):
        print("too little info")
        badFlag = True
    if "byr" in currDict:
        print(currDict.get("byr"))
        if int(currDict.get("byr")) < 1920 or int(currDict.get("byr")) > 2002 or len(str(currDict.get("byr"))) != 4:
            print("Bad byr! It is currently" + currDict.get("byr"))
            # badCount+=1
            badFlag = True
    else:
        print("byr not found")
        badFlag = True
    if "iyr" in currDict:
        print(currDict.get("iyr"))
        if int(currDict.get("iyr")) < 2010 or int(currDict.get("iyr")) > 2020 or len(str(currDict.get("iyr"))) != 4:
            print("Bad iyr! It is currently" + currDict.get("iyr"))
            # badCount+=1
            badFlag = True        
    else:
        print("iyr not found")
        badFlag = True
    if "eyr" in currDict:
        print(currDict.get("eyr"))
        if int(currDict.get("eyr")) < 2020 or int(currDict.get("eyr")) > 2030 or len(str(currDict.get("eyr"))) != 4:
            print("Bad eyr! It is currently" + currDict.get("eyr"))
            # badCount+=1
            badFlag = True    
    else:
        badFlag = True   
        print("eyr not found")
    if "hgt" in currDict:
        height = str(currDict.get("hgt"))
        print(height)
        if(height[-2:] == "in"):
            if int(height[:len(height)-2]) > 76 or int(height[:len(height)-2]) < 59:
                print("Bad hgt! It is currently " + currDict.get("hgt"))
                badFlag = True
        elif(height[-2:] == "cm"):
            if int(height[:len(height)-2]) > 193 or int(height[:len(height)-2]) < 150:
                print("Bad hgt! It is currently " + currDict.get("hgt"))
                badFlag = True
        else:
            print("Bad hgt! It is currently " + currDict.get("hgt"))
            badFlag = True
    else:
        print("hgt not found")
        badFlag = True
    if "ecl" in currDict:
        print(currDict.get("ecl"))
        if currDict.get("ecl") not in eyeColor:
            print("Bad ecl! It is currently" + currDict.get("ecl"))
            badFlag = True
    else:
        print("ecl not found")
        badFlag = True


    if "hcl" in currDict:
        print(currDict.get("hcl"))
        hairColor = str(currDict.get("hcl"))
        flagger = False
        hclreg = re.compile("#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]")

        if not hclreg.fullmatch(str(currDict.get("hcl"))):
            print("Bad hcl! It is currently" + currDict.get("hcl"))
            badFlag = True
    else:
        print("hcl not found")
        badFlag = True
    if "pid" in currDict:
        print(currDict.get("pid"))
        reg = re.compile("[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]")
        if not reg.fullmatch(str(currDict.get("pid"))) and len(str(currDict.get("pid"))) != 9:
            print("Bad pid! It is currently" + currDict.get("pid"))
            badFlag = True
    else:
        print("pid not found")
        badFlag = True
    if badFlag:
        badCount+=1
    



    
print(len(data)-badCount)