# For a given number find the next power of 2
# examples: 4->8, 6->8, 9->16, 1->2

# approach-> floor(log(num)+1) gives a power to which you should power your 2
import math
def next_power_2(n):
	return pow(2, math.floor(math.log2(n)+1))

# approach -> find the most significant set bit and make the next left bit 1 and rest all 0
# example: 00101 -> 01000

def next_power_22(n):
	cnt = 0
	while(n!=0):
		n = n>>1
		cnt+=1
	return 1<<cnt

print(next_power_2(4))
print(next_power_2(6))
print(next_power_2(9))
print(next_power_2(1))

print('\n')

print(next_power_22(4))
print(next_power_22(6))
print(next_power_22(9))
print(next_power_22(1))