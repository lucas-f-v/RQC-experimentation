import logging

# Configure logging
#dddd
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        logging.error("Attempted division by zero.")
        return "Error! Division by zero."
    return x / y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            logging.warning("Invalid input. Please enter a valid number.")
            print("Invalid input. Please enter a valid number.")

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice(1/2/3/4): ").strip()

        if choice in ['1', '2', '3', '4']:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == '1':
                result = add(num1, num2)
                operation = "addition"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "subtraction"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "multiplication"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "division"

            logging.info(f"Performed {operation} on {num1} and {num2}: Result = {result}")
            print(f"Result: {result}")
            
            next_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if next_calculation != 'yes':
                break
        else:
            logging.warning("Invalid choice. Please select a valid operation.")
            print("Invalid Input")

if __name__ == "__main__":
    calculator()