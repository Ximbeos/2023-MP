import datetime 
#1
my_data = ("Сафонов Илья Сереич",28,2,2004)

attestate ={
            "физра": 2,
            "География": 6,
            "инфа": 3,
            }
family_names =['Антон','Тихон','Прохор','Матвей']
kiwi_name ='Фибоначчиева куча' 

for element in attestate:
    print(element)  

mark_average =sum(attestate.values())/len(attestate)
print(mark_average) 


#2
unique_names=[]
for name in family_names:
    if name in unique_names:
        continue
    unique_names.append(name)
print(unique_names)
print(*set(family_names))

#5

print(bin(ord(kiwi_name[0])))

#7

today = datetime.datetime.today()
my_bday = datetime.datetime(day =my_data[1],year =my_data[3],month=my_data[2])
print((today-my_bday).days) 

