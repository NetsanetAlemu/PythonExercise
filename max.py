def max(*args):
    max = args[0]
    for i in args:
        if i >= max:
            max = i
    return max

def min(*args):
    min = args[0]
    for i in args:
        if i <= min:
            min = i
    return min


print("Minimum: " + str(min(3,2,4,5,6,7,8,9)))
print("Maximum: " + str(max(1,3,2,4,50,6,7,8,9)))
