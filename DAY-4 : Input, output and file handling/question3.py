"""
Question:
Without using Python CSV module write a "csvlook` command csvlook should have following features:
 * [-d DELIMITER] if -`d` option not paased script should be able to guess a seperator 
 * [-q QUOTECHAR] used to parsed colum value parenthesised within QUOTECHAR, 
 if the value not passed should assume default value dboult quote 
 `csvlook` should display data nicely on console in uniform width To project the data `csvlook` 
 script should accept comma seprated colum numbers, e.g -f 3,5,7 should print only column 3, 5 7 
 --skip-row N to skil first N rows 
 --head N to display only first N rows 
 --tail N to display last N rows
"""


#Taking command line input from user
command=input("Enter the command : ")

#initialising default arguments
delimiter='\t'
quotation='"'
skip=0
head=0
tail=0
unique=set()

#splitiing the command 
command=command.split(' ')

# checking if it starts with csvlook or not
if command[0]=='csvlook':

    #extracting the filepath/filename
    file_path=command[-1]

    # overriding the arguments based on the inputs from commands
    if "-d" in command:
        delimiter= command[command.index("-d")+1]

    if "-q" in command:
        quotation= command[command.index("-q")+1]

    if "-f" in command:
        number= command[command.index("-f")+1]
        number=number.split(",")
        for num in number:
            unique.add(int(num))

    if "--skip-row" in command:
        skip= command[command.index("--skip-row")+1]
        if skip.startswith("-") or '.' in skip:
            skip=0
        else:
            skip=int(skip)
        

    if "--head" in command:
        head= command[command.index("--head")+1]
        if head.startswith("-") or '.' in head:
            head=5
        else:
            head=int(head)
        

    if "--tail" in command:
        tail= command[command.index("--tail")+1]
        if tail.startswith("-") or '.' in tail:
            tail=5
        else:
            tail=int(tail)
    
    #initialising an empty list to store the content of file
    lines=[]

    #opening the file and extracting its content and appending it into the list
    with open(file_path,'r') as file:
        for line in file:
            lines.append(line)
    
    #initialising the start and stop parameters for efficient working of loop
    start=0
    stop=len(lines)

    # adjusting values of start and stop according to the arguments
    if skip>0:
        start+=skip
    if head>0:
        stop=head+1
    if tail>0:
        start= stop - tail

    #iterating the content of lines
    for content in range(start,stop):

        # preprocessing the data 
        result=lines[content].strip().split(",")

        #checking if we need to display specific columns
        if len(unique)!=0:
            for words in unique:
                print(quotation+"".join(result[words])+quotation, end=f'{delimiter}')
        
        #iterating on all values 
        else:
            for words in result:
                print(quotation+"".join(words)+quotation, end=f'{delimiter}')
        print()
