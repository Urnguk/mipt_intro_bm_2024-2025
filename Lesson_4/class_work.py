def DFS(curr_node, adj_list, visited=None):
    if visited is None:
        visited = set()
    visited.add(curr_node)
    for adj_node in adj_list[curr_node]:
        if adj_node not in visited:
            DFS(adj_node, adj_list, visited)
    return visited


def count_comp(adj_list):
    res = 0
    visited = set()
    for i in range(len(adj_list)):
        if i not in visited:
            DFS(i, adj_list, visited)
            res += 1
    return res


def acyclic(curr_node, adj_list, grey=None, black=None):
    if grey is None:
        grey = set()
    if black is None:
        black = set()
    grey.add(curr_node)
    for adj_node in adj_list[curr_node]:
        if adj_node in grey:
            return False
        if adj_node not in black:
            if not acyclic(adj_node, adj_list, grey, black):
                return False
    grey.discard(curr_node)
    black.add(curr_node)
    return True


S1 = set([2, 4, 5])
S2 = set([5, 6, 4])
print(S1 & S2)



