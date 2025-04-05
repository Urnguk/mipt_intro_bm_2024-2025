def read_adj_list():
    N, M = [int(x) for x in input().split()]
    res = [[] for i in range(N)]
    for i in range(M):
        x, y, w = [int(x) for x in input().split()]
        res[x].append((y, w))
        # res[y].append((x, w))


def dijkstra(adj_list, start_node):
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
            if dist[adj_node] > min_dist + weight:
                dist[adj_node] = min_dist + weight
    return res


                
    