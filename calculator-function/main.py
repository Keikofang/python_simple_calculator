#from matematika import *
#from matematika import add, subtract, multiply, divide
import matematika as mtk
print("select operation.")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")
print("5. factorial")
print("6. fibonacci")
print("7. hcf")
while True:
  choice = input("Enter choice(1/2/3/4/5/6/7): ")

  if choice in ('1', '2', '3', '4', '7'):
    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))

    if choice == '1':
      print(num1, "+", num2, "=", mtk.add(num1, num2))
  
    elif choice == '2':
      print(num1, "-", num2, "=", mtk.subtract(num1, num2))
    
    elif choice == '3':
      print(num1, "*", num2, "=", mtk.multiply(num1, num2))
  
    elif choice == '4':
      print(num1, "/", num2, "=", mtk.divide(num1, num2))
      
    elif choice == '7':
      print("the HCF of", num1, "and", num2, "is", mtk.hcf(int(num1),int(num2)))
    break

  elif choice in ('5','6'):
    num = int (input("enter the number: "))
    if choice == '5' :
      print("factorial of", num, "is", mtk.recur_factorial(num))
    elif choice == '6':
      if num <= 0:
        print("fibonacci number should be positive")
      else:
        print("fibonacci sequence:")
        for i in range(num):
          print(mtk.recur_fibo(i))
      
  else:
    print("Invalid Input")