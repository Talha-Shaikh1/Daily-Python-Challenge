def is_prime(number):
    # Numbers less than or equal to 1 are not prime
    if number <= 1:
        return False
    
    # Check from 2 to square root of the number
    # If any number divides evenly, it's not prime
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    return True

def main():
    try:
        # Get input from user
        num = int(input("Please enter a number: "))
        
        # Check if the number is prime
        if is_prime(num):
            print(f"{num} is a prime number!")
        else:
            print(f"{num} is not a prime number.")
            
    except ValueError:
        print("Please enter numbers only!")

if __name__ == "__main__":
    main() 