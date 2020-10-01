def kth_set(n, k):
	x = 1<<k
	print("Number to be anded with : ", bin(x).replace("0b", ""))
	return 0 if n&x==0 else 1


n = int(input("Enter a number: "))
k = int(input("Enter k 0th index: "))
print("Binary rep of number is: ", bin(n).replace("0b", ""))
print("Kth bit is set " if kth_set(n,k)==1 else "Kth bit is not set")