def bfs_tree(tree):
    stack = [tree]

    while stack:
        current = stack.pop(0)
        print(current[0])

        stack.extend([child for child in [current[1][0],current[1][1]] if child])

def bfs_trie(trie):
    stack = [trie]

    while stack:
        current = stack.pop(0)
        print(current[0])

        for letter in [character for character in trie[1] if character]:
            stack.extend([letter for letter in [character for character in current[1] if character]])

def bfs_adj_list(graph,visited):
    for vertex in graph:
        if vertex not in visited:
            stack = [vertex]

            while stack:
                current = stack.pop(0)
                if current not in visited:
                    visited[current] = True
                    print(current)

                    for node in graph[current]:
                        stack.append(node)

def bfs_adj_mat(graph, visited):
    for node in range(len(graph)):
        stack = [node]

        while stack:
            current = stack.pop(0)
            if current not in visited:
                visited[current] = True
                print(current)

                index = 0
                while index < len(graph[current]) and (graph[current][index] == 0 or index in visited):
                    index += 1
                if index < len(graph[current]):
                    stack.append(index)


if __name__ == '__main__':
    from DataStructures import quick_data_structures as qds

    bs = qds.tree(9)
    tr = qds.trie(["hippopotamus","hypothermia","hyperthermia"])
    al = qds.adj_list(7,15,directed=True,acyclic=False)
    am = qds.adj_mat(5,15,directed=True,acyclic=False,weighted=True)

    bfs_tree(bs)
    bfs_trie(tr)
    bfs_adj_list(al,{})
    bfs_adj_mat(am,{})

    print('\npass')