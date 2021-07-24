#read_file
f = open('inputFile.txt','r')
#write_into_file
write_file = open('copyPass.txt','w')
#fail_file
fail_file = open('failFile.txt','w')
# print(f.read())
for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        write_file.write(line)
    else:
        fail_file.write(line)
f.close()


