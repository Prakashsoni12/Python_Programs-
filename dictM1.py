numbers = [1,2,3,4,5]

dict_square = dict()
for num in numbers:
    dict_square[num] = num**2  
print(dict_square)
#doing same program in single line
square_dict = {num:num**2 for num in numbers}
print(square_dict)

old_price= {'milk':1.02, 'coffee':2.5,'bread':2.5}

new_price = {key:value*1.05 if value>2 else value for (key,value) in old_price.items()}
print(new_price)