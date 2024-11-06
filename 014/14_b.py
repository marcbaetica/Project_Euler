# The following iterative sequence is defined for the set of positive integers:
# n -> n/2 (n is even)
# n -> 3n+1 (is odd)
# 
# Using the rule above and starting with 19, we generate the following sequence:
# 13 -> 40 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1.
# 
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.



seq_counter = dict({1: 1})
for start in range(2, 10**6):
    count = 1
    curr = start
    while curr != 1:
        if int(curr) in seq_counter.keys():
            # -1 because it was already added at computation time.
            count += seq_counter[int(curr)] - 1     
            break
        if curr%2 == 0:
            curr = curr/2
        else:
            curr = 3 * curr + 1
        count += 1
    seq_counter[start] = count


print(max(seq_counter, key=seq_counter.get))

