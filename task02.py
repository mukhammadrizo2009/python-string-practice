import random


name = str(input("Ismingiz: "))
last_name = str(input("Familiyangiz: "))
raqam = random.randint(1, 100)
raqam2 = random.randint(1,100)


result = f"{name}_{last_name} \n {last_name}.{name} \n {name}{raqam} \n {last_name} {raqam2} "


print(result)