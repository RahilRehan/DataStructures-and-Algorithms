# 4^0 -> 1
# 4^1 -> 100
# 4^2 -> 10000
# 4^3 -> 1000000
# 4^4 -> 100000000

# has even 0 after 1

def check_pow_4(n):
	cnt=0
	while(n!=0):
		if n&1: # if last bit is 1, check if cnt is even
			if cnt%2==0 and (n>>1)==0: # if cnt is even and rest number is 0
				return 1
			else: return 0
		else:  # if last bit is 0 shift and increment cnt
			n=n>>1
			cnt+=1

def check_pow_42(n):
	while(n%4==0):
		n = n/4
	return 1 if n==1 else 0


print(check_pow_4(1))
print(check_pow_4(4))
print(check_pow_4(16))
print(check_pow_4(64))

print(check_pow_4(11))
print(check_pow_4(42))
print(check_pow_4(167))
print(check_pow_4(643))

print("\n")

print(check_pow_42(1))
print(check_pow_42(4))
print(check_pow_42(16))
print(check_pow_42(64))

print(check_pow_42(11))
print(check_pow_42(42))
print(check_pow_42(167))
print(check_pow_42(643))



