#Activity-1--------------------------------------------------------------------------------
# file = open("tiger.txt")
# print(file.read())
# file.close()

#Activity-2--------------------------------------------------------------------------------
# file_read=open("tiger.txt","r")
# print(file_read.read())

# file_write=open("tiger.txt","w")
# file_write.write("This is a new line")

# file_append=open("tiger.txt","a")
# file_append.write("\nThis is an additional line")



#Activity-3--------------------------------------------------------------------------------
# file=open("tiger.txt","r")
# counter=0
# content=file.read()
# colist=content.split("\n")
# for i in colist:
#     if i:
#         counter+=1
        
# print(counter)



#Activity-4---------------------------------------------------------------------------------
file1="flower.txt"
file2="tiger.txt"

f1=open(file1, "r")
f2=open(file2, "r")

print(f1.read())
print(f2.read())

f1.close()
f2.close()

f1=open(file1, "a+")
f2=open(file2, "r")

f1.write(f1.read())
f1.seek(0)
f2.seek(0)

print("Content for first file after appending:",f1.read())
print("Content for seconf file after appending:",f2.read())

f1.close()
f2.close()
