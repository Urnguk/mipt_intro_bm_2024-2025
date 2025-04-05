def read_adj_list():
    N, M = [int(x) for x in input().split()]
    res = [[] for i in range(N)]
    for i in range(M):
        x, y, w = [int(x) for x in input().split()]
        res[x].append((y, w))
        # res[y].append((x, w))


def Dijkstra(adj_list, start_node):
    dist = {i: float('inf') for i in range(len(adj_list))}
    dist[start_node] = 0
    res = {}
    
    while dist:
        min_dist = min(dist.values())
        min_node = 0
        for key in dist:
            if dist[key] == min_dist:
                min_node = key
                break
        res[min_node] = min_dist
        dist.pop(min_node)
        
        for adj_node, weight in adj_list[min_node]:
            if adj_node in dist:
                dist[adj_node] = min(min_dist + weight, dist[adj_node])

    return res


def FordBellman(edge_list, N, start_node):
    dist = [float("inf") for i in range(N)]
    dist[start_node] = 0
    correct = [True for i in range(N)]

    for i in range(2 * N - 1):
        for j in range(len(edge_list)):
            s, f, w = edge_list[j]
            if dist[f] > dist[s] + w:
                dist[f] = dist[s] + w
                if i >= N:
                    correct[f] = False

    return dist, correct


def FloydWarshall(adj_matrix):
    n = len(adj_matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                adj_matrix[i][j] = min(adj_matrix[i][k] + adj_matrix[k][j], adj_matrix[i][j])
    return adj_matrix
                
    