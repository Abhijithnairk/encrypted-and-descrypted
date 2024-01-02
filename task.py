import string
task=open("task.txt",'r')
files=task.read()
#print(files)

encrypted=""
input=files.lower()

for alphabets in input:
    if alphabets.isalpha():
        number=ord(alphabets)-96
        encrypted+=str(number) + ' '
    
print(encrypted)

value = encrypted.split()
descrypted = ""

for i in value:
    char_value=chr(int(i)+96)
    descrypted+=char_value + ' '
    
    
print(f"Descrypted value :{descrypted}")