# Program to show various ways to read and
# write data in a file.
file1 = open("myfile.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"]

# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")
file1.writelines(L)
file1.close() #to change file access modes



# string to search in file
with open(r'myfile.txt', 'r') as fp:
	# read all lines using readline()
	lines = fp.readlines()
	for row in lines:
		# check if string present on a current line
		word = ','
#		 print(row.find(word))
		# find() method returns -1 if the value is not found,
		# if found it return 0
		if row.find(word) == 0:
			print('string exists in file')
			print('line Number:', lines.index(line))
