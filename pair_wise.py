from allpairspy import AllPairs
import pandas as pd

parameters = [
    ["A1", "A2", "A3"],
    ["B1"],
    ["C1", "C2", "C3"],
    ["D1", "D2", "D3"],
    ["E1", "E2", "E3"],
]

for i, pairs in enumerate(AllPairs(parameters)):
    print("{:2d}: {}".format(i + 1, pairs))

i_list = list()
A_list = list()
B_list = list()
C_list = list()
D_list = list()
E_list = list()
# F_list = list()
# G_list = list()
for i, pairs in enumerate(AllPairs(parameters)):
    i_list.append(i + 1)
    A_list.append(pairs[0])
    B_list.append(pairs[1])
    C_list.append(pairs[2])
    D_list.append(pairs[3])
    E_list.append(pairs[4])
    # F_list.append(pairs[2])
    # G_list.append(pairs[2])

#
df = pd.DataFrame({
    'pair wise': i_list,
    'A': A_list,
    'B': B_list,
    'C': C_list,
    'D': D_list,
    'E': E_list,
    # 'F': C_list,
    # 'G': C_list,
})
#
df.to_csv('out.csv', index=False)
