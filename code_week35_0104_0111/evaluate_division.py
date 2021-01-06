'''
给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。

另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。

返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。

 

注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。

 

示例 1：

输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
解释：
条件：a / b = 2.0, b / c = 3.0
问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]
示例 2：

输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
输出：[3.75000,0.40000,5.00000,0.20000]
示例 3：

输入：equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
输出：[0.50000,2.00000,-1.00000,-1.00000]
 

提示：

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj 由小写英文字母与数字组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/evaluate-division
'''


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict
        # 先创建图
        graph = defaultdict(dict)
        for (x, y), val in zip(equations, values):
            '''
            if x in graph:
                graph[x][y] = val
            else:
                graph[x] = {y:val}
            if y in graph:
                graph[y][x] = 1/val
            else:
                graph[y] = {x:1/val}
            '''
            # 借助defaultdict可以用以下两句话代替上述讨论
            graph[x][y] = val
            graph[y][x] = 1 / val

        res = []
        for s, e in queries:
            visited = set()
            res.append(self.dfs(s, e, visited, graph))
        return res

    # dfs实现
    def dfs(self, start, end, visited, graph):
        visited.add(start)  # 第一个点先加进visited，如果不加对结果没影响因为a/b * b/a = 1 但是别的题会错
        if start not in graph: return -1
        if start == end: return 1
        for w in graph[start]:
            if w == end:
                return graph[start][w]
            elif w not in visited:
                visited.add(w)
                v = self.dfs(w, end, visited,
                             graph)  # dfs就是每次只做分内事，剩下的交给recursion来跑，但这题应该是‘如果跑出不是-1的就进行计算’，而不是‘跑出-1就说这个值计算不了’。
                # print(v)
                if v != -1:
                    # print(v)
                    return graph[start][w] * v
                else:
                    # print(v)
                    # return -1
                    pass  # 这里不能return -1 因为会‘死路’但实际上走别的节点可以‘出路’，不能走一条死路就判断整体不存在
        return -1  # 都失败了才是-1

