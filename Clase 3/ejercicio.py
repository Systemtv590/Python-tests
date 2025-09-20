num = int(input("Ingrese un Numero:\n"))
num2 = int(input("Ingrese otro Numero:\n"))
if num%2==0 and num2%2==0:
   print("Ambos numeros son Par")
elif num%2==0 and num2%2!=0:
   print("El primer numero es Par")
   print("El segundo numero es Impar")
elif num%2!=0 and num2%2==0:
   print("El primer numero es Impar")
   print("El segundo numero es Par")
else:
   print("Ambos numeros son Impar")