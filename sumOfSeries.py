## 1.D. Write a program to calculate sum of the following series: 1+2+3+...+n

n = int(input("Enter the value of n: "))
sum=0

for i in range(1, n+1):
	sum +=i

print(sum)
	