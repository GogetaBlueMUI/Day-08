def greet(str):
    if str=='en':
        print("Hello!")
    elif str=='es':
        print("Hola!")
    elif str=='fr':
        print("Bonjour!")
str=input("Enter en or es or fr: ")
greet(str)