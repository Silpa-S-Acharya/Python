# Python program to check
# if two lists have at-least
# one element common
# using traversal of list

def common_data(list1, list2):
	result = False

	# traverse in the 1st list
	for x in list1:

		# traverse in the 2nd list
		for y in list2:
	
			# if one common
			if x == y:
				result = True
				print("c.Same value occur in both list",x)
				print("\t",result)
				
				
	return result
def length(list1,list2):
    print("a.Length of list 1\t",len(list1))
    print("\tLength of list 2\t",len(list2))
    if len(list1)==len(list2):
        print("\tBoth list have same size")
def sumoflist(list1,list2):
    total=0
    su=0
    for ele in range(0, len(list1)):
        total = total + list1[ele]
    for ele in range(0, len(list2)):
        su = su + list1[ele]
    ts=total+su
    if ts==len(list1)and su==len(list2):
        print("b.List sums to same values")

    else:
        print("b.List sums not to same values")


    
    
# driver code
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
length(a, b)
sumoflist(a,b)
print(common_data(a, b))



