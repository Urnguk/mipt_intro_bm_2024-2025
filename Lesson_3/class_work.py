# N, M = [int(x) for x in input().split()]
# edge_list = []
# for i in range(M):
#     s, f = [int(x) for x in input().split()]
#     edge_list.append((s, f))
#
# adj_matrix = [[0 for j in range(N)] for i in range(N)]
# for edge in edge_list:
#     s, f = edge
#     adj_matrix[s][f] = 1
#     adj_matrix[f][s] = 1
#
# adj_list = [[] for i in range(N)]
# for edge in edge_list:
#     s, f = edge
#     adj_list[s].append(f)
#     adj_list[f].append(s)

A = [
    [1, 2, 3],
    [2, 7, 8],
    [0, 0, 0]
]

for line in A:
    print(*line)
