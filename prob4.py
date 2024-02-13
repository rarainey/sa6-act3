l1 = [0,1,2,3,4,5,6,7,8]
l2 = [0,1,2,8,9,10,11,4]

intersection = list(filter(lambda x: x in l2, l1))
print(intersection)