'''
Source: 
https://www.hackerearth.com/practice/machine-learning/prerequisites-of-machine-learning/basic-probability-models-and-rules/tutorial/


Mike wants to go fishing this weekend to nearby lake. His neighbour 
Alice (is the one Mike was hoping to ask out since long time) is also 
planing to go to the same spot for fishing this weekend. 
The probability that it will rain this weekend is p_1. There are two 
possible ways to reach the fishing spot (bus or train). 

The probability that Mike will take the bus is p_mb and 
that Alice will take the bus is p_ab. 
Travel plans of both are independent of each other and rain.

What is the probability  that Mike and Alice meet each other only 
(should not meet in bus or train) in a romantic setup (on a lake in rain)?

Input constraints:
all probailities in [0,1] interval


Input format

FIrst line: p_mb
Second line: p_ab
Third line: p_1

Output format

p_rs, rounded up to six decimal places.
'''

# My Python code here

# convert input values into float type
p_mb = float(input())
p_ab = float(input())
p_1 = float(input())

# probability(Alice takes a bus and Mike takes a train) = p_ab*p_mt = p_ab*(1-p_mb)
# probability(Alice takes a train and Mike takes a bus) = p_at*p_mb = p_mb*(1-p_ab)
# P(they don't meet on the way to the spot) = 
#  = P(Alice takes a bus and Mike takes a train) + probability(Alice takes a train and Mike takes a bus)
# P(they meet on the spot in the rain) = P(rain)*P(they don't meet on the way to the spot)

p_rs = p_1*(p_ab*(1-p_mb) + p_mb*(1-p_ab))

# use format(p, '.6f') to make sure the output format is 6 decimal places

p_rs = format(p_rs, '.6f')
print(p_rs)



