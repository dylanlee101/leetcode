'''
哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。像句子"I reset the computer. It still didn’t boot!"已经变成了"iresetthecomputeritstilldidntboot"。在处理标点符号和大小写之前，你得先把它断成词语。当然了，你有一本厚厚的词典dictionary，不过，有些词没在词典里。假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。

注意：本题相对原题稍作改动，只需返回未识别的字符数

 

示例：

输入：
dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
输出： 7
解释： 断句后为"jess looked just like tim her brother"，共7个未识别字符。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/re-space-lcci
'''
class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        dictionary = {w for w in dictionary if sentence.find(w) != -1}
        lens = list({len(w) for w in dictionary})
        lens.sort(reverse=True)
        N,res,i = len(sentence),0,0
        @functools.lru_cache(maxsize=1000)
        def sol(i):
            if i >= N : return 0
            tails = []
            tails = [sol(i+l) for l in lens if i+l <=N and sentence[i:i+l] in dictionary]
            tails += [1 + sol(i + 1)]
            return (min(tails) if tails else 0)
        return sol(0)