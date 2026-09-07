prices = [1,3,4,2,6,1,7]

dp = [[i - j for i in prices] for j in prices]

print(dp)