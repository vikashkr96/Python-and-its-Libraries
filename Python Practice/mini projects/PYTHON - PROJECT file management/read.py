file = open('vikash.txt','r') # mode is r because we have to read the file 
content = file.read()
file.close()
print(f"content of 'vikash.txt':{content}") 