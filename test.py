

with open("test.txt",'w') as file:
    ch = input("enter file contents")
    while ch!="":
        ch =  input()
        file.write(ch + "\n")
file.close()     



# f.write("this is a test file")
# f.write("this is ")