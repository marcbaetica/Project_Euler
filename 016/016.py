# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 9 = 26.
# 
# What is the sum of the digits of the number 2^1000?



# pow = 15
pow = 1000

print(sum([int(char) for char in str(2**pow)]))

# OR:
print(sum(list(map(int, list(str(2**pow))))))

