# 模版

def slidingWindow(s,t):
    need = {}
    for c in t:
        need[c] += need.get(c,0) + 1
    left = 0
    right = 0
    valid = 0
    while right < len(s):
        # 移入窗口字符
        c = s[right]
        # 右移窗口
        right += 1

        # debug
        print("window: ",left,right)

        # 判断左侧窗口是否收缩
        while (window need shrink):
            # d是将移出窗口的字符
            d = s[left]
            # 左移窗口
            left += 1

