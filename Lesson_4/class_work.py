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


def acyclic(curr_node, adj_list, grey=None, black=None, stack=None):
    if grey is None:
        grey = set()
    if black is None:
        black = set()
    if stack is None:
        stack = []
    grey.add(curr_node)
    for adj_node in adj_list[curr_node]:
        if adj_node in grey:
            return False
        if adj_node not in black:
            if not acyclic(adj_node, adj_list, grey, black, stack):
                return False
    grey.discard(curr_node)
    black.add(curr_node)
    stack.append(curr_node)
    return True

def solve():
    N, M = [int(x) for x in input().split()]
    adj_list = [[] for i in range(N)]
    for i in range(M):
        s, f = [int(x) for x in input().split()]
        adj_list[s].append(f)
\
    grey = set()
    black = set()
    stack = []
    for i in range(N):
        if i not in black:
            flag = acyclic(i, adj_list, grey, black, stack)
            if not flag:
                print("NO")
                return
    print(*stack[::-1])

solve()




