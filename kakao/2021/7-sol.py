# dfs

def solution(sales, links):
    def dfs(node, d):
        if tree[node]:
            s_c = 0
            flag = False
            min_d = 1e9
            for ele in tree[node]:
                dfs(ele, d)
                s_c += min(d[ele][0], d[ele][1])
                if d[ele][0] > d[ele][1]:
                    flag = True
                if (d[ele][1] - d[ele][0]) < min_d:
                    min_d = d[ele][1] - d[ele][0]
            d[node][1] = sales[node - 1] + s_c
            if flag:
                d[node][0] = s_c
            else:
                d[node][0] = s_c + min_d
        else:
            d[node][1] = sales[node - 1]
    tree = [[] for _ in range(len(sales) + 1)]
    for link in links:
        tree[link[0]].append(link[1])
    d = [[0, 0] for _ in range(len(sales) + 1)]
    dfs(1, d)
    return min(d[1][0], d[1][1])




sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
print(solution(sales, links))