import animals
menu = {
    "1" : "1.- snake",
    "2" : "2.- cat",
    "3": "3.- Trex",
    "0": "0.- Exit",
}
print("Please select an animal",animals.Saludo)
for o in menu.values():
   print(o)
while True:
    x = input('Please enter an option: ')
    if x == '0' :
        print('Thanks!!! See you')
        break      
    elif x == '1':
        print(animals.snake)
    elif x == '2' :
        print(animals.cat)
    elif x == '3' :
        print(animals.Trex)
    else:
        print('Unavailable Selection')
    



