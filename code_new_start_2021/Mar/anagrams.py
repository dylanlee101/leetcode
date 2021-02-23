'''
输入：le chien marche vers sa niche et trouve une limace dee chine nue pleine de malice qui lui fait du charme
输出：{une,nue},{marche charme},{chien chine,niche},{malice,limace}
'''


def anagrams(w):
    w = list(set(w.split(" ")))
    d = {}
    for i in range(len(w)):
        s = ''.join(sorted(w[i]))
        if s in d:
            d[s].append(i)
        else:
            d[s] = [i]

    reponse = []
    for s in d:
        if len(d[s]) > 1:
            reponse.append([w[i] for i in d[s]])
    return reponse

if __name__ == '__main__':
    w = "le chien marche vers sa niche et trouve une limace dee chine nue pleine de malice qui lui fait du charme"
    print(anagrams(w))
