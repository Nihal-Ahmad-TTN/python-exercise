'''
Question:
Programing: From a multi-words and multi-line string, display list of words and word's length with occurrence more than 1 in sorted order
'''

str='''Python Multiline String Using Triple Quotes Using the triple quotes style is one of the easiest and most common ways to split a large string into a multiline Python string. Triple quotes can be used to create a multiline string. It allows you to format text over many lines and include line breaks. Put two triple quotes around the multiline Python string, one at the start and one at the end, to define it.'''

word_count={}
str=str.split(" ")
for words in str:
    if words in word_count:
        word_count[words]+=1
    else:
        word_count[words]=1

print("Word \t Length \t Occurence")
for key, value in word_count.items():
	if value>1:
		print(key,"\t", len(key), "\t", value)