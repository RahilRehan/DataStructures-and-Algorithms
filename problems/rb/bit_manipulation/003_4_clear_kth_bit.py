def clear_bit(n, k):
	x = 1<<k
	return n&(~x)


n = int(input("Enter number: "))
k = int(input("Enter kth bit: "))

n = clear_bit(n, k)
print(n)