# # first question
# n_students = int(input('please enter number of students'))
# weight_kg=[]
# for i in range(n_students):
#     weight= int(input('input the weight'))
#     x=weight*0.453592
#     weight_kg.append(x)
# print(weight_kg)

# second question
# def string_alternativ():
#     print(new[0::2])
# new = str(input('please enter you statment'))
# string_alternativ()

#third prog
infile = open("words.txt",'r')
words={}
count=2
line = infile.readline()
while line != "":
    for word in line.split(' '):
        word=word.strip()
        if word in words:
           words[word]=count
           count=count+1
        else:
            words[word]= 1
    line = infile.readline()
print(words)
f= open("words2.txt",'w')
for key, value in words.items():
    print(key, value)
    f.write('%s:%s\n' % (key, value))
f.close()