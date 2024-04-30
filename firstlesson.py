2 ** 9
19 % 2
#! integer
3 * 5
#! float
0.4 * 1.2
#! Variables
x=3
y=5
x+y
x**y
#! built in = halıhazırda tanımlı fonksiyonlar (print(),input("r:"))
r = input("r:")
type(r)
r_int = int(r) 
type(r_int)
r_int * x
#! escape characters
print("hello \nworld")
print("hello \tpython")
#*INDEXING
my_string = "Hello world!"
my_string[9]
my_string[-1] #son harf
my_string_2 = "123456789"
my_string_2[0]
#! slicing
my_string_2[2:] #* 3.sıradan başlat. yani yazılanı dahil et
my_string_2[:2] #* 3.ve sonrasını kes. yazılanı dahil etme -stopping index-
my_string_2[2:4]
#! step size
my_string_2[::3] #* üçer üçer atla
my_string_2[2:4:2]
my_string_2[::-1] #* terse çevir.
#! STRING METHODS
my_name = "enes"
my_name_capitalized = my_name.capitalize() #* ilk harfini büyült.
my_name
my_name_capitalized
my_name_2 = "enes simsek"
my_name_2_split = my_name_2.split()
my_name_2_split
my_name_2_split[1]
my_number = 123 
#! stile göre method önerir.
my_name_2.upper()
"james" * 10 * 10 
"james" + "5" 
"james" * 3
#! LISTS
my_string_3 = "syifalakh"
my_string_3.capitalize()
my_string_3[0] = "g" #! strings her zaman immutable'dır.
my_list = [1234567]
type(my_list)
my_list.append(9) #! sonuna eleman olarak ekler.
my_list #! lists her zaman mutable'dır. 
my_list[0] = 2
#* bazı fonksiyonlar içinde işlem yapıyor bazıları döndürüyor. hattı bazıları ikisini aynı anda yapar.
my_mixed_list = [1,2,"a","bhf"]
my_mixed_list[::-1] #! tersten düze doğru
my_mixed_list[-1] #! son karakteri al
my_complicated_list = my_mixed_list + my_list
my_complicated_list
my_complicated_list * 3
my_complicated_list.reverse()
my_complicated_list
#! mested list (iç içe geçmiş liste)
new_list = [1,2,["a","b"]]
new_list[2][0]
#! DICTIONARY
my_dictionary = {"key":"value"}
my_dictionary["key"]
my_fitness_dictionary = {"swim":100,"run":300}
my_fitness_dictionary["swim"]
my_fitness_dictionary["run"]
my_dictionary_2 = {"key1":100,"key2":[1,2,3],"key3":{"a":2}}
my_dictionary_2["key3"]["a"]
my_dictionary_3 = {"key1":5,"key2":7} #* dictionary is muttable
my_dictionary_3["key2"] = 8
my_dictionary_3
my_dictionary_3["key3"] = 13 #! appending a new key
my_dictionary_3 
#! SET
my_set = [1,2,3,1]
my_set
my_set_2 = set(my_set)
my_set_2
type(my_set_2)
my_set_3 = {1,2,3,1,2}
my_set_3
my_set_4 = {}
type(my_set_4)
my_set_5 = set()
type(my_set_5)
my_set_6 = dict()
type(my_set_6)
my_set_7 = {}
type(my_set_7)
my_set_7 = {1,2,3,4}
type(my_set_7)
my_set_7["key2"] = 6
#! TUPLE (IMMUTABLE FUNCTION)
my_tuple = (1,2,3,4,5,6) #! its immutable
my_tuple.count(2)
my_tuple[2] = 3 #! we cant change like that 
#! BOOLEAN (TRUE AND FALSE OPTION)
x = 5
y = input("y: ")
type(y)
y_int = int(y)
type(y_int)
y_int > x 
my_list.