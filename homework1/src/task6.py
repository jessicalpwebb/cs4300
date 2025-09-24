#reading text file to count number of words
with open("/home/student/cs4300/homework1/src/task6_read_me.txt","r") as file:
    summary = file.read()
    
words = summary.split()
count = len(words)

print(count)