def nsqrt(x): # do not change the heading of the function
    start = 1
    end = x
    current = (start+end) // 2
    while (True) :
        if current*current == x or (current*current<x and (current+1)*(current+1) > x):
            return current
        elif (current+1)*(current+1) < x:
            start = current
        elif current*current > x:
            end = current
        current = (start + end) // 2

print(nsqrt(11), nsqrt(1369))