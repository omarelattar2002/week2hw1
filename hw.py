#excercise 1 
Numbertest = range(1,1000)


for cubednumbers in Numbertest:
        if cubednumbers ** 3 >= 1000:
            break
        print(cubednumbers ** 3)


#execise 2
# HINT::
# An else after an if runs if the if didn’t
# An else after a for runs if the for didn’t break



# Prime number - A number that is divisible by only 1 and itself

for n in range(1,100):
    for i in range(2,n):
        if n % i == 0:
            break
    else:
        print(n)












#excecise 3
age = int(input("How old are you?:"))

if age < 18:
    print('kids')
elif 18 <= age <= 65:
    print('adults')
else:
    print('seniors')