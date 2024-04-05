#Types of data used in I/O
    # 1.Text= "1234" as a sequence of unicode character
    # 2.Binary= "1234" as a sequence in bits

#hence to deal with Two types of files
# 1.Text File    2.Binary File(img,music ,vedio etc)

#  3 steps done in File handling
#   (1). Open a file 
#   (2). Read/write in the FileExistsError
#   (3). Close the file

# 1. Writing to a Text File
# CAse 1= if the file is not created
# f=open("sample.txt", 'w')
# f.write('Hello World')
# f.write('Stop the writing and close')
# f.close()
# # f.write("cant Write into file after closing the file")
# #write multiples line =if the file is NOT present
# f=open("sample1.txt", 'w')
# f.write('Hi how are you?')   #15=RETURNS THE NUMBER OF CHARACTER INSERTED
# f.write('\nWhere you from?')   #16
# f.close()

# #IF THE FILE IS PRESENT
# f=open("sample.txt",'w')
# f.write('Replaced Old content') 
# f.close()

#With open() command python interpreter moves the file from ROM to Ram in  Buffer format
#Buffer is a way of reading each character one oy one to perform read and write operation
#With close() file puts back to the ROM


#Introducing append mode to not erase old content from the file
# f=open("File-Handling\sample1.txt", 'a')
# f.write('Use append to insert at the end of old content')
# f.close()


##Passing  a multiple lines inside a list
L=['hi\n','how are you\n','what the hell']
# f=open('File-Handling\sample.txt','w')
# f.writelines(L)
# f.close()


##Reading from a file
# f=open('File-Handling\sample.txt', 'r')
# s=f.read()
# print(s)
# f.close()

##Readin upto n characters from a file
# f=open('File-Handling\sample.txt', 'r')
# s=f.read(10)
# print(s)
# print(f.read(5)) ##it will start reading from 11th character as char till 10 already read
# f.close()

##Reading one by one line using readline()
# f=open('File-Handling\sample.txt','r')
# print(f.readline(),end="    ") ##end content will show after each line is printed
# print(f.readline(),end='    ')
# f.close()

##Reading  whole file using readline()
f=open('C:\\Users\Dev_nath\OneDrive\Desktop\PROJECTS\OOPS-Python\File-Handling\sample.txt','r')
while True:
    data=f.readline()
    if data==' ':
        break
    else:
        print(data,end=' ')
    f.close()






