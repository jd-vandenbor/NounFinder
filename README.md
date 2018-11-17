# NounFinder
this program concatenates files, and gets the wordcount for specific words. After that, for each occurence of one of the words, it finds the closest noun in the text and keeps track of it. Finally for each word, it outputs the most common "close noun".

to run the file simply run from the command line wordCount.py
- the first output will be the total wordcount of the document
- followed by the list of words and there total number of occurences
- then a bar graph will pop up and display the number of occurrences
- the Last output is each word and its associated "closest noun".

this program works by comparing words to a large database of words collected from the nltk.corpus. The downside of determining what is and isn't a noun from this, is some words have dual meanings, and worse yet homynyms exist, so a word like "annual" can sometimes refer to a type of flower, which makes it a noun, however in the context which it is most frequently brought up is in regards to time. This is indeed why annual is the closest noun to the word report, and is a flaw in the system.
