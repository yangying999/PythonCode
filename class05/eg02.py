import jieba
# 写入文件
# --1--
# s='lddjfjjvngqwertyuioplkjhgfdsamnbvcxz啦啦啦啦啦啦啦啦啦'
# fp = open('./my.txt','w',encoding='utf-8')
# fp.write(s)
# fp.close()
# --2--
# with open('./my.txt','w',encoding='utf-8') as fp:
#     fp.write(s)

# 读文件
# with open('./西游记.txt','r',encoding='utf-8') as fp:
#     txt = fp.read()
#     print(txt)

#
# s='''
# 东胜神洲傲来国海边有一花果山，山顶一石，受日月精华，产下一个石猴。
# '''
# words=jieba.lcut(s)
# print(words)

#
txt = open('./西游记.txt','r',encoding='utf-8').read()
chars = ',.?!;:，。？；：！、\n""的你我他是到了在又有去与来不这被为之请如其后“”原得至'
for char in chars:
    txt=txt.replace(char,' ')
words = jieba.lcut(txt)

count = {}

for word in words:
    count[word] = count.get(word,0) + 1

items = list(count.items())
items.sort(key=lambda x: x[1],reverse=True)
print(items[1:40])

# for i in range(11):
#     word,count = items[i]
#     print("{0:<5}".format(word,count))