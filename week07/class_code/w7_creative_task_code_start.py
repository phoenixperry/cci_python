infile = open("dracula.txt", "r")
filestring = infile.read()
infile.close()

# in words ==========================================
words = filestring.split()

#for word in words:
#    print(word)


# in sentences ==========================================
sentences = filestring.split(".")

# dark magicks!
#import re
#sentences2 = re.split(r' *[\.\?!][\'"\)\]]* *', filestring)


# in paragraphs ==========================================
paragraphs = filestring.split("\n\n") # depends on how your text is written!

#for paragraph in paragraphs:
#    print(paragraph)

