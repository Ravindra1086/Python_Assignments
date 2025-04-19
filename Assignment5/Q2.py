import os
list = []
for i in range(1,11):
    list.append(i)

print("Original list: ",list)

extractedList = list[:5]
reversedExtractedList = extractedList[::-1]
print("Extracted first five elements: ",extractedList)
print("Reversed extracted elements: ",reversedExtractedList)