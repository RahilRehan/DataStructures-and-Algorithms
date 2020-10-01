# xor logic, 1^1=>0(changed from 1->0) and 0^1=>1(changed from 0->1)
#logic is to xor with 1 at kth bit

def toggle_kth_bit(n, k):
	x = 1<<k
	return n ^ x

n = int(input("Enter a number: "))
k = int(input("Enter kth bit: "))

print(toggle_kth_bit(n, k))