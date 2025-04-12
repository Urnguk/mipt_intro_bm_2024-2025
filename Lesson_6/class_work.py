def Prim(adj_list):
    res = []
    visited = set()
    visited.add(0)
    edges = [(0, finish, weight) for finish, weight in adj_list[0]]
    while len(visited) < len(adj_list):
        edge = min(edges, key=lambda x: x[2])
        edges.remove(edge)
        dest = edge[1]
        if dest not in visited:
            visited.add(dest)
            edges += [(dest, finish, weight) for finish, weight in adj_list[dest]]
            res.append(edge)
    return res


def Kraskal(N, edge_list):
    edge_list = sorted(edge_list, key=lambda x: x[2])
    groups = [i for i in range(N)]
    groups_cnt = N
    res = []
    i = 0
    for i in range(len(edge_list)):
        v1, v2, w = edge_list[i]
        if groups[v1] != groups[v2]:
            res.append((v1, v2, w))
            groups_cnt -= 1
            el_tag = groups[v2]
            new_tag = groups[v1]
            for j in range(len(groups)):
                if groups[j] == el_tag:
                    groups[j] = new_tag
        if groups_cnt == 1:
            break
    return res














