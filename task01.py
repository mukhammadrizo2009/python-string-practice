number = str(input("telefon nomeringizni kiriting: "))

n = number[:2]
n2 = number[2:5]
n3 = number[5:7]
n4 = number[7:9]


result = f"Sizning nomeringiz: +998 {n} {n2} {n3} {n4}"

print(result)