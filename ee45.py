
filename = "ee45.txt"
data  = open(filename).read()
words = data.split()
#id = words.index('"utilize"')
id = [i for i, x in enumerate(words) if x == '"utilize"']

for i in range(0,len(id)):
    words[id[i]] = '"use"'

str1 = ' '.join(words)

print("The word use is used: ", len(id))
new_path = input("Name of output file: ")
new_file = open(new_path,'w')
new_file.write(str1)
new_file.close()


