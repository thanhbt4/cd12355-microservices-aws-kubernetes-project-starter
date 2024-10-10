import os

os.environ['DB_USERNAME'] = 'thanhbt4'
os.environ['DB_PASSWORD'] = 'thanhbt4'
os.environ['DB_HOST'] = '127.0.0.1'
os.environ['DB_PORT'] = '5433'
os.environ['DB_NAME'] = 'coworking'

# Replace 'KEY' with the name of your environment variable
key_value = os.environ.get('DB_USERNAME')

if key_value:
    print(f"The value of 'DB_USERNAME' is: {key_value}")
else:
    print("Environment variable 'DB_USERNAME' is not set.")