'''
Question:
Write a code to read a "Python_script.py" as inpit file and extract following information to prepare a JSON 
* all package name which the input Python script use 
* all function name which the input Python script define 
* all class name which the input Python script define 
* all the variable name which the input Python script define 
example output: 
{ "package": ["os", "itertools"], "funation": ["function1", "function2"], "class": ["classA", "classB"], "variable": ["num", "i", "j"] }

'''

#importing json module
import json

#opening the file sample2.txt to read its content
with open("python_script.py",'r') as file:

    #initalising a dictionary
    dictionary={
    "module":[],
    "function":[],
    "class":[],
    "variable":set()
    }

    #iterating the file to fetch its content
    for line in file:

        #Preprocessing: replacing colon with empty string, comma with space, stripping to remove the new line and split at spaces
        line=line.lower().replace(":",'').replace(",",' ').strip().split(" ")

        #logic to check for module name and inserting it into dictionary
        if line[0]=="import" or line[0]=="from":
            dictionary["module"].append(line[1])
        
        #logic to check for function name and inserting it into dictionary
        elif line[0]=="def":
            fun_name=''
            for char in line[1]:
                if char=="(":
                    break
                else:
                    fun_name+=char
            dictionary["function"].append(fun_name)

        #logic to check for class name and inserting it into dictionary
        elif line[0]=="class":
            dictionary["class"].append(line[1])
        
        #logic to check for variable name and inserting it into dictionary
        elif "=" in line:

            #iterating the list till we get the = operator 
            for words in range(line.index("=")):

                #checking for empty strings if exixts
                if line[words]=="":
                    continue
                
                #inserting the names of the variable in dictionary
                else:
                    dictionary["variable"].add(line[words])
    
    #type casting set into list to encounter any error in making json file
    dictionary["variable"]= list(dictionary["variable"])

#creating a new output.json file and printing its content
with open("output.json",'w') as json_file:
    result= json.dumps(dictionary, indent=4)
    print(result)


