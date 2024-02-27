#excercise 1 
Numbertest = range(1,1000)


for cubednumbers in Numbertest:
        if cubednumbers ** 3 >= 1000:
            break
        print(cubednumbers ** 3)


#execise 2
n = range(1,100)











#excecise 3
age = int(input("How old are you?:"))

if age < 18:
    print('kids')
elif 18 <= age <= 65:
    print('adults')
else:
    print('seniors')