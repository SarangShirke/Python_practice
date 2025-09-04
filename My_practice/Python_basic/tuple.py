rating = (10,20,30,40,50,1.23,4.5,5.6)
print(rating[0:3])
print(len(rating))
print(sorted(rating))
#rating[0] = 100 #tuple is immutable
#nesting tuple
my_tuple = (10,20,30,(40,50,60),(70,80,90))

print(my_tuple[3][1])
print(my_tuple[4][2])
