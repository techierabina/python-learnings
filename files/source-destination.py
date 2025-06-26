#important concept read from one file and copy the content in another file
with open('example.txt','r') as source_file:
   content=source_file.read()

with open('destination.txt','w') as destination_file:
   destination_file.write(content)