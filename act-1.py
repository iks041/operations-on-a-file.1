file = open('Codingal.txt', 'r')
print(file.read())
file.close()

file = open('Codingal.txt', 'r')
print("\n Read ìn parts \n")
print(file.read(8))
file.close

file = open('Codingal.txt', 'a')
file.write("hi! i am peguine, i am 1 years old")
file.close
