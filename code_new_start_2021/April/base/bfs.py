
visited = set()
def bfs(graph,start,end):
    queue = []
    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.pop()
        visited.add(node)
        process(node)

        nodes = generate_related_nodes(node)
        queue.push(nodes)


'''
binary-tree-level-order-traversal
minimum-genetic-mutation
generate-parentheses
find-largest-value-in-each-tree-row



word-ladder
word-ladder-ii
number-of-islands
minesweeper
'''