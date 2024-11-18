file_read = open('Codingal.txt', 'r')
print("Fileinread mode -")
print(file_read.read())
file_read.close

file_write = open('Codingal.txt', 'w')
file_write.write("File in writting mode")
file_write.write("hi! i am penguin and i am 1 yr old")
file_write.close()

file_append = open('Codingal.txt', 'a')
file_append.write("\n File in append mode")
file_append.write("hi! iam penguin and i am 1 yr old")
file_append.close()

