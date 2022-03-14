# Big O(n^2) Quadrantic runtime

# Log all pairs of array

boxes = ['a','b','c','d']

# indx = 0
# for i in boxes:
#     print(i,boxes[indx])
#     indx += 1

def PrintAllPairs(ls):
    for i in ls:
        for j in range(0,len(ls)):
            print(i,boxes[j])

PrintAllPairs(boxes)


# When we have a function with nested loops we will use * 
# The Above Is O(n * n) = o (n ^2)