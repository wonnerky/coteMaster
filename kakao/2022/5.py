def solution(info, edges):
    result = []
    def dfs(s_w, node, visit):
        if visit[node] == 0:
            s_w[info[node]] += 1
            visit[node] = 1
        
        if info[node] == 1 or (info[node] == 0 and not edge_info[node]):
            dfs


        for edge in edge_info[node]:
            dfs(s_w, edge)


    edge_info = [[] for _ in range(len(info))]
    for edge in edges:
        edge_info[edge[0]].append(edge[1])
    s_w = [0, 0]
    node = 0
    visit = [0] * len(info)
    dfs(s_w, node, visit)
    answer = 0
    return answer




info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
print(solution(info, edges))