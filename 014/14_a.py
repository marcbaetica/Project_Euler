# The following iterative sequence is defined for the set of positive integers: n -> n/2 (n is even) n -> 3n+1 (is odd)
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



def compute_sequence_len(start):
    count = 1
    # print(f'Number: {start}')
    while start != 1:
        if start%2 == 0:
            start = start/2
        else:
            start = 3 * start + 1
        count += 1
    # print(count)
    return count


fat_seq_start = 0
fat = 0
for i in range(10**6, 8, -1):
    count = compute_sequence_len(i)
    if count > fat:
        fat = count
        fat_seq_start = i
        # print(f'New fat is {fat}. Start sequence was {i}, while the length was {count}.')
print(fat_seq_start)


# TODO: Too much redundant processing. much faster to store start with seq count and leverage the data struct.

