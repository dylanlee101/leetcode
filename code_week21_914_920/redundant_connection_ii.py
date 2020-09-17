'''
在本问题中，有根树指满足以下条件的有向图。该树只有一个根节点，所有其他节点都是该根节点的后继。每一个节点只有一个父节点，除了根节点没有父节点。

输入一个有向图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。

结果图是一个以边组成的二维数组。 每一个边 的元素是一对 [u, v]，用以表示有向图中连接顶点 u 和顶点 v 的边，其中 u 是 v 的一个父节点。

返回一条能删除的边，使得剩下的图是有N个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。

示例 1:

输入: [[1,2], [1,3], [2,3]]
输出: [2,3]
解释: 给定的有向图如下:
  1
 / \
v   v
2-->3
示例 2:

输入: [[1,2], [2,3], [3,4], [4,1], [1,5]]
输出: [4,1]
解释: 给定的有向图如下:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3
注意:

二维数组大小的在3到1000范围内。
二维数组中的每个整数在1到N之间，其中 N 是二维数组的大小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/redundant-connection-ii
'''


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        cnt = set()
        for i in range(len(edges)):
            for j in range(len(edges[0])):
                cnt.add(edges[i][j])
        N = len(cnt)
        parent = [i + 1 for i in range(N)]
        indegree = [0] * N  # 记录每个节点的入度
        for x, y in edges:
            indegree[y - 1] += 1

        def find(parent, x):
            if parent[x - 1] == x:
                return x
            return find(parent, parent[x - 1])

        def union(parent, x, y):
            x_root = find(parent, x)
            y_root = find(parent, y)
            if x_root == y_root:
                return [x, y]
            elif x_root != y_root:
                parent[y_root - 1] = x_root  # 这里与`冗余连接I`有一点区别

        if 2 in indegree:  # 情况1
            dual_node = indegree.index(2) + 1
            dual_edge = []
            for x, y in edges:  # 找到入度为2的节点对应的两条边
                if y == dual_node:
                    dual_edge.append([x, y])

            for edge in dual_edge[::-1]:  # 为了满足题意，从后面往前删除
                flag = 0  # 判断删除后是否还有环，有flag=1，否则flag=0
                for e in edges:
                    if e != edge:
                        if union(parent, e[0], e[1]):
                            flag = 1
                if flag == 1:  # 如果存在环，那么冗余的就是另一条边
                    return dual_edge[0]
                else:  # 如果不存在环，那么冗余的就是这条边
                    return edge
        else:  # 情况2
            for x, y in edges:
                if union(parent, x, y):
                    return union(parent, x, y)

