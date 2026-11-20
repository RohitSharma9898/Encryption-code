from cryptography.fernet import Fernet

# 1. Generate a secret key
key = Fernet.generate_key()

# 2. Create Fernet encryption object
cipher = Fernet(key)

# 3. Take student details from the user
name = input("Enter your name: ")
age = input("Enter your age: ")
course = input("Enter your course: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")

# 4. Combine all details into one message
student_details = f"""
Name: {name}
Age: {age}
Course: {course}
Email: {email}
Phone: {phone}
"""

# 5. Convert the message into bytes
student_details = student_details.encode()

# 6. Encrypt the student details
encrypted_data = cipher.encrypt(student_details)

# 7. Display encrypted data
print(encrypted_data)

# 8. Decrypt the data using the SAME secret key
decrypted_data = cipher.decrypt(encrypted_data)

# 9. Convert bytes back to normal text
decrypted_data = decrypted_data.decode()

# 10. Display decrypted details
print(decrypted_data)
