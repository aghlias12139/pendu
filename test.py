import os
print(os.getcwd())
os.chdir(r"C:/Users/anis/OneDrive/Documents/test")
print(os.getcwd())
my_file = open("test","r")
contenu = my_file.read()
print("oui ", contenu, )
print(type(my_file))

