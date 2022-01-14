from collections import deque

def virus_pos(graph):
    virus_dic = {}
    for i, row in enumerate(graph):
        for j in row:
            if j != 0:
                x = row.index(j)
                virus_dic[j] = [i, x]
    return virus_dic

def virus(graph, s, x_1, y_1):
    queue = deque()
    # 좌 우 상 하
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(s):
        virus_info = virus_pos(graph)
        virus_info = dict(sorted(virus_info.items()))
        for value, (x, y) in virus_info.items():
            queue.append((x, y))
            while queue:
                a, b = queue.popleft()
                for d in range(4):
                    na = a + dx[d]
                    nb = b + dy[d]
                    if (na < 0) or (nb < 0) or (na >= n) or (nb >= n):
                        continue
                    elif graph[na][nb] != 0:
                        continue
                    elif graph[na][nb] == 0:
                        graph[na][nb] = graph[na][nb] + value
                        queue.append((a, b))
                        continue

    print("Final map : {}".format(graph))

    return graph[x_1-1][y_1-1]

if __name__ == "__main__":

    n, k = map(int, input().split())

    graph = []

    for i in range(n):
        graph.append(list(map(int, input().split())))

    s, x, y = map(int, input().split())

    print(n)
    print(type(n))
    # n, k, s, x, y = 3, 3, 1, 2, 2
    #
    # graph = [[1, 0, 2], [0, 0, 0], [3, 0, 0]]
    print("Output : {}".format(virus(graph, s, x, y)))