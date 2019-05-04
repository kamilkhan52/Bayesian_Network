read_lines = [line.rstrip('\n') for line in open('network.txt')]
lines_list = [i.split() for i in read_lines]
n = int(lines_list[0][0])
# create variables
variables = [i for i in range(1, n + 1)]  # n+1?

# read parents
parents_dict = dict.fromkeys(variables)

cond_prob_table = {}

k = 0
while k < len(lines_list) - 1:
    index = k
    num_parents = int(lines_list[index + 1][0])
    # print("num_parents = " + str(num_parents))
    k = index + 2 ** int(num_parents) + 1
    child_id = int(lines_list[index + 1][1])
    if num_parents != 0:
        parents_dict[child_id] = lines_list[index + 1][2:]
        # read the condition probabilities
        prob_table = lines_list[index + 2:k + 1]
        # print("prob_table = " + str(prob_table))
        for row in prob_table:  # write each row into cond_prob_table
            all_parents = '_'.join(parents_dict[child_id])
            truth_table = '_'.join(row[:len(row) - 1])
            entry = str(child_id) + "_" + str(all_parents) + "_" + str(truth_table)
            prob = float(row[-1])
            cond_prob_table[entry] = prob
            entry_false = str(child_id) + "_F_" + str(all_parents) + "_" + str(truth_table)
            cond_prob_table[entry_false] = 1 - prob
    else:
        parents_dict[child_id] = 0
        prob = float(lines_list[index + 2][0])
        entry = str(child_id) + "_T"
        entry_false = str(child_id) + "_F"
        cond_prob_table[entry] = prob
        cond_prob_table[entry_false] = 1 - prob

# calculate query joint probability
read_query = [line.rstrip('\n') for line in open('query.txt')]
query_list = read_query[0].split()
joint_prob = 1

for i in range(0, len(query_list)):
    cond = query_list[i]
    if cond == 'T':
        key = str(i + 1) + "_T"
        if parents_dict[i + 1] == 0:
            # print("Multiplying joint_prob = " + str(joint_prob) + " by cond_prob_table[key] =" + str(
            #     cond_prob_table[key]))
            joint_prob = joint_prob * cond_prob_table[key]
            # print("New joint_prob = " + str(joint_prob))
        elif len(parents_dict[i + 1]) > 0:
            # print("parents count = " + str(len(parents_dict[i + 1])))
            child = i + 1
            parents = '_'.join(parents_dict[child])
            conditions = ""
            for parent in parents_dict[child]:
                conditions = conditions + "_" + str(query_list[int(parent) - 1])
            read_key = str(child) + "_" + str(parents) + str(conditions)
            # print("Multiplying joint_prob = " + str(joint_prob) + " by cond_prob_table[read_key] =" + str(
            #     cond_prob_table[read_key]))
            joint_prob = joint_prob * cond_prob_table[read_key]
            # print("New joint_prob = " + str(joint_prob))

        else:
            print("Unknown number of parents for this child" + str(i + 1))
    else:
        key = str(i + 1) + "_F"

        if parents_dict[i + 1] == 0:
            # print("Multiplying joint_prob = " + str(joint_prob) + " by cond_prob_table[key] =" + str(
            #     cond_prob_table[key]))
            joint_prob = joint_prob * cond_prob_table[key]
            # print("New joint_prob = " + str(joint_prob))
        elif len(parents_dict[i + 1]) > 0:
            # print("parents count = " + str(len(parents_dict[i + 1])))
            child = i + 1
            parents = '_'.join(parents_dict[child])
            conditions = ""
            for parent in parents_dict[child]:
                conditions = conditions + "_" + str(query_list[int(parent) - 1])
            read_key = str(child) + "_F_" + str(parents) + str(conditions)
            # print("Multiplying joint_prob = " + str(joint_prob) + " by cond_prob_table[read_key] =" + str(
            #     cond_prob_table[read_key]))
            joint_prob = joint_prob * cond_prob_table[read_key]

            # print("New joint_prob = " + str(joint_prob))
        else:
            print("Unknown number of parents for this child" + str(i + 1))

print("{:.6f}".format(joint_prob))
