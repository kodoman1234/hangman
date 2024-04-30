#!/usr/bin/env python3
#! x = y işlemi x ve y'yi eşitler ancak x == y işlemi x ve y 'nin eşitliğini sorgular.(true-false) x != y --> x eşit değildir y kontrolü
#* and or not operators
#! IF STATEMENTS
if 3 > 2:
    print ("3 is greater than 2")
x = 5
y = 5
if x > y:
    print("x is greater")
elif x == y:
    print("x and y are equal")
else:
    print("y is greater")
# my_superhero = input("ur fav superhero: ")
# if my_superhero == "Batman":
#     print("Batmaaaaaaaaan")
# elif my_superhero == "Superman":
#     print("Supermaaaannn")
# elif my_superhero == "Ironman":
#     print("Ironmannnnn")
# else:
#     print(":))))))))))")

isDead = False
if isDead == True:
    print("ur character is dead")
else:
    print("ur character is not dead")

if isDead:
    print("ur character is dead")
else:
    print("ur character is not dead")

if not isDead:
    print("ur character is dead")

my_dictionary = {"key1":20,"key2":50,"key3":60}
if 20 in my_dictionary.values():
    print("true")
else:
    print("false")

my_list = [1,2,3,4,5]
if 2 in my_list:
    print("evet o var.")
else:
    print("hayır o yok.")
#! FOR LOOP
my_number_list = [1,2,3,4,5,6,7,8,9,10]
for number in my_number_list:
    if number % 2 == 0:
        print(number)

my_string = "Shifaya Gunawan"
for letter in my_string:
    print(letter) #! yukarıdan aşağıya teker teker elemanları sıralar. 

my_new_list = [("a","b"),("c","d"),("e","f"),("g","h")]
for element in my_new_list:
    print(element)
for (x,y) in my_new_list:
    print (x)
    print (y)
my_dictionary = {"key1":100,"key2":200,"key3":300}
for (key,value) in my_dictionary.items():
    print(key)
#! BREAK CONTINUE PASS
my_list = [10,20,30,40,50,60,70]
for number in my_list:
    print(number * 5)
for num in my_list:
    if num == 30:
        break
    print(num)

for num in my_list:
    if num == 30:
        continue #! 30 u atla 10,20,40,50,60,70
    print(num) 
#! for'da elemanları tek tek ele alıyoruz. while'da ise koşul devam ettikçe şartı var.
a = 0
while a <= 5:
    print("hello")
    a += 1
my_list_2 = [1,2,3,4,5,6]
while 3 in my_list_2:
    print("3 in my list")
    my_list_2.pop()
number = 0
while number < 10:
    #! if number == 5:
    #!     break --> bu iki satır mantıklı değildir zaten number < 5 yapsam da aynı sonucu alacağım.
    print(number)
    number += 1
p = 0
while p < 20:
    #! print("value p: " + str(p))
    print(f"value p: {p}")
    p += 1    
#! SOME HELPFUL METHODS
#* RANGE
for number in list(range(20)):
    print(number * 5)
for num in list(range(5,21,2)):
    print(num * 5)
#!ENUMERATE
index = 1
for num in list(range(0,20,3)):
    print(f"number: {num} ix: {index} ")
    index += 1
#!üsttekini enumerate ile de yapabiliriz.
for element in enumerate(list(range(5,15))):
    print(element)

for (index,number) in enumerate(list(range(5,15))):
    print(index)
    print(number)
#! RANDOM rastgele sayı oluşturma
from random import randint
my_list = (randint(0,1000))
print(my_list)
my_list_3 = list(range(0,20))
print(my_list_3)
from random import shuffle
shuffle(my_list_3)
print(my_list_3)
#!ZIP --> ayrı ayrı listeleri birleştirmek
sport_list = ["run","swim","basketball"]
calories_list = [100,200,300]
day_list = ["monday","sunday","saturday"]
my_zip = list(zip(sport_list,calories_list,day_list)) #! must do zip
print(my_zip)
for element in my_zip:
    print(element)
#! LIST ADVANCED
new_list = []
my_string = "metallica"

for element in my_string:
    new_list.append(element)
print(new_list)
#! üstteki ile aynı işlemi element for element ile yapmak
new_list = [element for element in my_string]
print(new_list)

new_list_2 = [number**5 for number in list(range(0,10))]
print(new_list_2)
