import itertools
import operator
import matplotlib.pyplot as plt
import numpy as np
from nltk.corpus import wordnet as wn


#define noun checking myFunction
def findNoun(i, nouns, words):
    previousNoun = ""
    prev = 0
    checker = False
    count = 0
    while(not checker):
        count += 1
        if ( words[i - count] in nouns and words[i - count] != "a"):
        #if ( words[i - count] in nouns):
            previousNoun = words[i - count]
            prev = count
            checker = True
    nextNoun = ""
    next = 0
    checker = False
    count = 0
    while(not checker):
        count += 1
        if ( words[i + count] in nouns and words[i - count] != "a"):
        #if ( words[i + count] in nouns):
            nextNoun = words[i + count]
            next = count
            checker = True
    if (prev < next):
        return previousNoun
    else:
        return nextNoun
#end of function

#find most common element of group
def most_common(L):
  groups = itertools.groupby(sorted(L))
  def _auxfun((item, iterable)):
    return len(list(iterable)), -L.index(item)
  return max(groups, key=_auxfun)[0]
#end



#concatenate the files
filenames = ['electricityAct.doc', 'educationAct.doc', 'AODA.doc', 'registryAct.doc', 'BuisnessCorperationsAct.doc']
#filenames = ['test.txt']
with open('/Users/joshvandenbor/repos/python/ministryInterview/outfile.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)


#perform wordcount on outfile
file=open("/Users/joshvandenbor/repos/python/ministryInterview/outfile.txt")
#wordcount = 0;
#for word in file.read().split():
#    wordcount = wordcount + 1
wordcount = len(file.read().split())
print ("total wordcount: " + str(wordcount))
file.close();

#perform wordcount for the given wordbank
file=open("/Users/joshvandenbor/repos/python/ministryInterview/outfile.txt")
wordbank={"report", "shall", "comply", "should"}
wordcount={}
for word in wordbank:
        wordcount[word] = 0
for word in file.read().split():
    if word in wordcount:
        wordcount[word] += 1
print (wordcount)
file.close();

#find closest noun
file=open("/Users/joshvandenbor/repos/python/ministryInterview/outfile.txt")
nouns = {x.name().split('.', 1)[0] for x in wn.all_synsets(wn.NOUN)}
words = file.read().split()
shallNouns = []
reportNouns = []
shouldNouns = []
complyNouns = []
for i in range(0, len(words)):
    if words[i] in wordcount and words[i] == "report":
        reportNouns.append(findNoun(i, nouns, words))
    if words[i] in wordcount and words[i] == "shall":
        shallNouns.append(findNoun(i, nouns, words))
    if words[i] in wordcount and words[i] == "comply":
        complyNouns.append(findNoun(i, nouns, words))
    if words[i] in wordcount and words[i] == "should":
        shouldNouns.append(findNoun(i, nouns, words))
print ("report's most common noun: " + most_common(reportNouns))
print ("shall's most common noun: " + most_common(shallNouns))
print ("comply's most common noun: " + most_common(complyNouns))
print (shouldNouns)
file.close();

label = []
counts = []
for word in wordcount:
    label.append(word)
    counts.append(wordcount[word])
# this is for plotting purpose
index = np.arange(len(label))
plt.bar(index, counts)
plt.xlabel('words', fontsize=15)
#plt.ylabel('No of Movies', fontsize=15)
plt.xticks(index, label, fontsize=15, rotation=30)
plt.title('Number of Occurences')
plt.show()
