'''
给定一个文件 file.txt，转置它的内容。

你可以假设每行列数相同，并且每个字段由 ' ' 分隔.

示例:

假设 file.txt 文件内容如下：

name age
alice 21
ryan 30
应当输出：

name alice ryan
age 21 30

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/transpose-file
'''

# Read from the file file.txt and print its transposed content to stdout.
python3 -c "
data = []
i = 0
j = 0
with open('file.txt') as f:
    for line in f:
        i = len(line.split())
        j += 1
        data.append(line.split())
res = [[] for _ in range(i)]

for a in range(j):
    for b in range(i):
        res[b].append(data[a][b])
st = ''
for item in res:
    st = st + ' '.join(item) + '\n'
print(st[:-1])
"