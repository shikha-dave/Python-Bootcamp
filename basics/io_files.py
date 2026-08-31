import os


with  open("test.txt", "r") as file:
    content = file.read()
print(content)
print("-----------------")
print(content)
print("The file has been read second time successfully.")
print("Current working directory:", os.getcwd())