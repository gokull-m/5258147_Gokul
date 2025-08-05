# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
# Print the decimal value of each fraction on a new line with  places after the decimal.
def plusMinus(arr):
    tot=len(arr)
    pos =0
    neg =0
    zer=0
    for x in arr:
        if x>0:
            pos +=1
        elif x<0:
            neg +=1
        else:
            zer +=1
            
    p=pos/tot
    n=neg/tot
    z=zer/tot
    
    print (f"{p:.6f}")
    print (f"{n:.6f}")
    print (f"{z:.6f}")
             