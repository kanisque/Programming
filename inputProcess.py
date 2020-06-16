with open('input','r') as file:
    line = file.read()

lines = line.split('Add attachment')

for line in lines:
    listLine = str(line)
    listLine = listLine.replace('Description','')
    listLine = listLine.replace('New  ','')
    listLine = listLine.replace('Expense Type','')
    listLine = listLine.replace('American Express',' ')
    listLine = " ".join(listLine.split())
    print(listLine[3])

