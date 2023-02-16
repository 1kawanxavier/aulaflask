x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
z = int(input("Digite o terceiro número: "))

if x > y and x > z:
    result = "x é o maior numero"
elif y > x and y> z:
     result = "y é o maior numero"
elif z > x and z> y:
     result = "z é o maior numero"
else:
    result = "há numeros iguais"
    
print(result)