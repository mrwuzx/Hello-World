name = ''
while not name or name.isspace():
    name = input("Please enter your name: ")
print('Hello, %s!' % name)
