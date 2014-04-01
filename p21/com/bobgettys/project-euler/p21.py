'''
Created on Mar 9, 2014

@author: rgettys
'''

'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

from functools import reduce

edivisors = {}
divisorSums = {}

'''
def sumList(l): 
    sum = 0
    for i in l:
        sum += i
    return sum
'''

maxRange = 10000
def findDivisors(n):
    list = []
    for i in range(1, n):
        if n / i == n // i:        
            list.append(i)
    return list

divisorSums[1] = 1
for i in range(2, maxRange):
    divisorSums[i] = reduce(lambda x, y: x + y, findDivisors(i))
    #print(str(i) + " " + str(divisorSums[i]))
amicables = {}
for i in range(1,maxRange):
    partner = divisorSums[i]
    if partner != i and partner <= maxRange and divisorSums[partner] == i:
        amicables[i] = partner
        print(str(i) + " and " + str(partner) + " are amicable")
        
print(reduce(lambda x, y: x + y, amicables.keys()))


if __name__ == '__main__':
    pass