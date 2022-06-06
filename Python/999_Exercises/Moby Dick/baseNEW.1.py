#sentence = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"
times = 0
#for i in range(0, len(sentence)):
    #if(sentence[i:i+5] == "whale"):
#        times = times + 1
#print("The number of times whale appears in this sentence: ")
#print(times)





with open('moby.txt') as f:
   for line in f:
       sentence = line.strip()
       for i in range(0,len(sentence)):
            s = sentence[i:i+5]
            if(s == "whale" or s == "Whale" or s == "WHALE" or s == "WHale" or s == "WhAle" or s == "WHALe"):
                times = times + 1
print("The number of times whale appears in Moby Dick: ")
print(times)

f.close()
