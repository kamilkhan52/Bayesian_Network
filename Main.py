read_lines = [line.rstrip('\n') for line in open('network.txt')]
print(read_lines)
lines_list = [i.split() for i in read_lines]
print(lines_list)
n = int(lines_list[0][0])
print(n)
# create variables
variables = [i for i in range(1, n + 1)]  # n+1?

print(str(variables))
# read parents

parents_dict = dict.fromkeys(variables)
print(parents_dict)
k = 0
while k < len(lines_list) - 1:  # minus ?
    index = k
    print("k = " + str(k))
    num_parents = int(lines_list[index + 1][0])
    print("num_parents = " + str(num_parents))
    k = index + 2 ** int(num_parents) + 1
    print("k = " + str(k))
    parent_id = int(lines_list[index + 1][1])
    if num_parents != 0:
        parents_dict[parent_id] = lines_list[index + 1][2:]
        # read the condition probabilities?
    else:
        parents_dict[parent_id] = 0
        pass
    print(parents_dict)

# generate conditional probabilities table


# calculate query joint probability
