import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

try:
    number = int(input("Enter an integer: "))
    result = proxy.factorial(number)
    print(f"Factorial of {number} is: {result}")
except ValueError:
    print("Please enter a valid integer.")
