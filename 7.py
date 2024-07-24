def is_integer(stri):
    try:
        int(stri)
        return True
    except:
        return False
str="123"
str1="Hello"
print("Convertion Status For 123: ", is_integer(str))
print("Convertion Status For Hello: ", is_integer(str1))
