str="hi this is very poor man please need to help"
upperletter=str.upper()
print(upperletter)

#first Letter of sentance to be capital
cammellteer=str.capitalize()
print(cammellteer)

#every word of first letter will be capital
everyfirstlettercapital=str.title()
print(everyfirstlettercapital)

#every space will remove from this sentance
removespace=str.replace(" ", "")
print(removespace)

#sentance have splited in words and convert it in list
sortingword= str.split()
print(sortingword)

#**********filter digit from sendtance or paragraph

Str1="Our country independence day is celebrated on 15 August , 26 January republicday, 1947 and 2014 is magic day"
digit=[]
alphalet=[]
for dig in Str1.split():
    if dig.isdigit():
        digit.append(dig)
    elif dig.isalpha():
        alphalet.append(dig)

print(digit)
print(alphalet)


#**********Count of lower length word or maximum lenghth
Str2="Our country independence day is celebrated on 15 August , 26 January republicday, 1947 and 2014 is magic day"
count=0
smallword=[]
for word in Str2.split():
    if len(word)<=2:
        smallword.append(word) #total smalest word list
        count=count+len(word) # total world count

print(smallword)
print(len(smallword))
print(count)

#**************Count of character***
char_count=Str2.count('a') # count() function provide similar type character count
print(char_count)

# ************Merge of two different list****

list1=[1,2,3,4,5]
list2=['apple', 'python', 'c', 'd', 'diction']
Dictionary=dict(zip(list1, list2))  # dict() function return dictionary where as zip() function return iterable of item.
print("after merge two list Dictionary: ", Dictionary)