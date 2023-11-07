#https://www.youtube.com/watch?v=0fJNVerQaNI
stringS  = ("timon vermeersch magda oudenaarde")

words = stringS.split()
def printWords():
    for i in range(0,len(words)):
        print(words[i][0:2])

rat = print(words[0][0:2]+words[1][0:2]+words[2][-2:]+words[3][0:2])

"""
x (Start index): This is the index of the element where the slice begins. It's inclusive, which means the element at this index is included in the slice.

y (Stop index): This is the index of the element where the slice ends. It's exclusive, which means the element at this index is not included in the slice. The slice goes up to, but does not include, the element at this index.

z (Step or Stride): This is an optional part of the slice. It specifies how many elements to skip between the included elements. If you omit z, it defaults to 1, which means that every element in the specified range will be included. If you provide a positive number for z, it means you are skipping elements in a forward direction, and if you provide a negative number, you are skipping elements in a backward direction.

Here are some examples to illustrate how slicing works:

string[1:4] slices the string from index 1 (inclusive) to index 4 (exclusive), so it includes characters at indices 1, 2, and 3.

string[:3] slices the string from the beginning (index 0) up to index 3 (exclusive), so it includes characters at indices 0, 1, and 2.

string[2:] slices the string from index 2 (inclusive) to the end of the string, so it includes characters starting from index 2 to the end.

string[1:7:2] slices the string starting at index 1 and ending at index 7 (exclusive) with a step of 2, so it includes characters at indices 1, 3, and 5.

string[::-1] slices the string with a negative step of -1, which means it reverses the string.
"""
