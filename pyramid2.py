
arry = [1]
row_count = 10
for i in range(0,row_count-1):
    row_count -=1
    for j in range(1,row_count+1):
        print(' ' , end = ' ')
    
    for content in reversed(arry[1:]):
        print(content, end=' ')
    
    for content in arry:
        print(content , end = ' ')
    for k in range(1,row_count+1):
        print(' ', end = ' ')
        
    print()
    arry.append(arry[-1] + 1)

