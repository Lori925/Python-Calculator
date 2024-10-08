def get_valid_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def choose_operation():
    valid_operations = {'+': 'Addition', '-': 'Subtraction', '*': 'Multiplication', '/': 'Division'}
    while True:
        operation = input("Choose operation (+, -, *, /): ")
        if operation in valid_operations:
            return operation
        print("Invalid operation. Please choose +, -, *, or /.")

def calculate(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

def main():
    print("Welcome to the Calculator!")
    
    while True:
        # Input A
        a = get_valid_input("Enter the first number (A): ")
        
        # Choose Operation
        operation = choose_operation()
        
        # Input B
        b = get_valid_input("Enter the second number (B): ")
        
        # Calculate Result
        try:
            result = calculate(a, b, operation)
            print(f"Result: {a} {operation} {b} = {result}")
        except ValueError as e:
            print(f"Error: {e}")
        
        # Ask if the user wants to perform another calculation
        if input("Do you want to perform another calculation? (y/n): ").lower() != 'y':
            break
    
    print("Thank you for using the Calculator!")

if __name__ == "__main__":
    main()
