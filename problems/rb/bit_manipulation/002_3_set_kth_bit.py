def set_kth(n,k):
	x = 1<<k
	n = n|x
	return n



n = int(input("Enter a number: "))
k = int(input("Enter k 0th index: "))
n = set_kth(n,k)
print("After setting: ", n)
