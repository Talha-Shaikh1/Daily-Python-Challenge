'''
📢 Day 6 – Daily Python Challenge 🐍
🚀 Challenge:
Aisa Python program likhna hai jo user se ek integer number lega aur uska binary (0s aur 1s) me conversion karega, phir check karega ke ye palindrome hai ya nahi! 🔄✨

🔥 Example:
📌 Input: 9
📌 Binary: 1001
📌 Output: Palindrome ✅

📌 Input: 13
📌 Binary: 1101
📌 Output: Not a Palindrome ❌

'''

def is_binary_palindrome(n):
    binary_rep = bin(n)[2:]  # Convert number to binary and remove '0b' prefix
    return binary_rep == binary_rep[::-1]  # Check if binary is same as its reverse

num = int(input("Enter a number: "))

if is_binary_palindrome(num):
    print(f"{num} binary is ({bin(num)[2:]}) and it is palindrome")
    
else:
    print(f"{num} binary is ({bin(num)[2:]}) and it is not palindrome")