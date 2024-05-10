number = [n for n in range(1,5)]
print(number)

double_number = [n*2 for n in number]
print(double_number)

name = "keerthivasan"
name_letter = [letter for letter in name]
print(name_letter)

#using condition in list comprehension

name_list=["Alex","Charlie","Phil","Arun","Mike","Keerthivasan"]
short_name = [name for name in name_list if len(name)<5]
print(short_name)

uppercaseLongName_nameList = [name.upper() for name in name_list if len(name)>5]
print(uppercaseLongName_nameList)
