from art import logo
def add(num1, num2):
  return num1+num2
def subtract(num1, num2):
  return num1-num2
def multiply(num1, num2):
  return num1*num2
def divide(num1, num2):
  return num1/num2
def exp(num1, num2):
  return num1**num2
def remainder(num1, num2):
  return num1%num2
  
operations={
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "^": exp,
  "%": remainder
}
second=True
first=True
while first:
  print(logo)
  n1=float(input("First number: "))
  for i in operations:
    print(i)
    second=True
    first=True
  while second:
    symbol=input("What operation would you like to use?: ")
    n2=float(input("Another number: "))
    result=operations[symbol]
    answer=result(n1,n2)
    print(f"{n1} {symbol} {n2} = {answer}")
    again=input("Would you like to keep calculating? yes or no: ")
    if again=="no":
      second=False
      first=False
      print("Thank you!")
    else:
      fresh=input("Fresh start? yes or no: ")
      if fresh=="yes":
        second=False
      else:
        n1=answer