print("###### todo basic file handling īn python ######")
with open("readme.txt", "r") as variable:
    content=variable.read() # reads all of the file readme.txt and stores as a string in content
    word_set=set(content.split()) # stores the entire string in sets, and break the strings. such that "varad hey there!" becomes {"varad","hey","there"}
    print("Unique words:",len(word_set)) #since set clears dupes by itself, using the length will now give the length of all uniques

with open("readme.txt","r") as r:
    buffer=r.read()
    for reader in buffer:
        print(reader,end="")


# to count the number of occurences of letter a the for loop by degfault checks char by char and not word by word
count=0
count_b=0
with open("text.txt","r") as r:
        buffer=r.read()
        for c in buffer:
             if(c=='a'): count+=1
             elif(c=='b'): count_b+=1

        print(f'\ncount of the letter a is {count} count of letter b is {count_b}')

# looping word by word
counter_and=0 
counter_rest=0
with open("sample.txt","r")as r:
     reader=r.read().lower().split() # use lower to handle AND & and
     #now reader has control over the entire message 
     for x in reader:
          if(x=="and"): counter_and+=1
          else: counter_rest+=1 
     print(f"the string sample.txt had {counter_and} ands and other than and there were {counter_rest} words")
     # use of lower ofc, also alters the original text 
     #for y in reader:
      #    print(y,end=" ")