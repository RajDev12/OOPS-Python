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
f=open("sample.txt", 'w')
f.write('Hello World')
f.write('Stop the writing and close')
f.close()
# f.write("cant Write into file after closing the file")
#write multiples line =if the file is NOT present
f=open("sample1.txt", 'w')
f.write('Hi how are you?')   #15=RETURNS THE NUMBER OF CHARACTER INSERTED
f.write('\nWhere you from?')   #16
f.close()

#IF THE FILE IS PRESENT
f=open("sample.txt",'w')
f.write('Replaced Old content')
f.close()