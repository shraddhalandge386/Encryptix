import random
import string

print("Password Generator")
print("----------------")

length = int(input("Enter the desired password length: "))

password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))

print(f"Generated Password: {password}")