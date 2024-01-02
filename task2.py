text = open("task2.txt",'r')
files = text.read()
print(files)

input = files.lower()

for alphabet in input:
    if(alphabet.isalpha()):
        result=input.count(alphabet)
        print(f"{alphabet}:{result}")
        
        
target_word = "python"
target = input.split().count(target_word.lower())
print(f"Target word repeated:{target}")