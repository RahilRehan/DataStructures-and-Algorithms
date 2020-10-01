# aproach 1: 2^1->0010   2^2->0100  2^3->1000
#therefore number only contains one set bit, thrfr check if number has only one set bit

# aproach 2: n -> 8(1000) and n-1 -> 0111
# therefore bitwise (and n & n-1)
# exception is number 0

def check_power_2(n):
	if n==0:
		return 0
	return not (n&n-1)

print(check_power_2(4))
print(check_power_2(8))
print(check_power_2(3))
print(check_power_2(9))
