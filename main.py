from art import logo
#add
def add(n1, n2):
  return n1 + n2

#subtract
def subtract(n1, n2):
  return n1 - n2

#multiply
def multiply(n1, n2):
  return n1 * n2

#divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator(operation, n1, n2):
  return operations[operation](n1, n2)

def program():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True

  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))

    calc_result = calculator(operation_symbol, num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {calc_result}")

    choice = input(f"Type 'y' to continue calculating with {calc_result}, or type 'n' to start a new calculation, or type 'e' to exit: ")

    if choice == "y":
      num1 = calc_result;
    elif choice == "n":
      should_continue = False
      program()
    elif choice == "e":
      should_continue = False
      print("Goodbye")

program()