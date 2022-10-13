import re

infile = open("arquivo_dados.txt", 'r')
data = infile.read()
infile.close()
virgula = re.sub(",", ";", data)

print(virgula)

file1 = open("arquivo_dados_novo.txt","w")
file1.write(virgula)
file1.close()


