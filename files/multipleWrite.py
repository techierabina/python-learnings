line=["\n First line","\n Second line","\n Third Line"]
with open("test_append.txt","a") as file:
    file.writelines(line)