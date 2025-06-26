#a program to read the lines, words and character in file
with open('example.txt','r') as file:
    content=file.readlines()
    line_count=len(content)
    print(line_count)
    word_count= sum(len(line.split()) for line in content)
    print(word_count)
    char_count=sum(len(line) for line in content)
    print(char_count)
