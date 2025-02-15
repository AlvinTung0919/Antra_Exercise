common_words = ("the", "of", "and", "a", "to", \
    "in", "is", "you", "that", "it", "he", \
    "was", "for", "on", "are", "as", "with", "his", \
        "they", "I", "at", "be", "this", "have", "from")

#A: number of words
print(len(common_words))

#B - first 5 words
print(common_words[0:5])

#C - last 3 words
print(common_words[-3:])

#D - every 5th word
print(common_words[0:25:5])

#E - four-letter words
for i in common_words:
    if len(i)==4:
        print(i)

#F - Words starting with w
for i in common_words:
    if i.startswith('w'):
        print(i)
        
#G - words in order
result=[]
for i in common_words:
    result.append(i)

result.sort()
print(result)
    