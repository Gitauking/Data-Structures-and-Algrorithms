
#create the array
fruits = ['apple', 'banana', 'mango']

#add a fruit
fruits.append('watermelon')
fruits.remove('apple')
#print all fruits

for fruit in fruits:
    print(fruit)

#find fruit
search = 'pinapple'
if search in fruits:
    print(f"{search} is in the list!")
else:
    print(f"{search} not found")

