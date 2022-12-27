import jieba
s='bewjbhew，。；/？！、\n啊u音乐会本地'
chars = ';,.。，/：；、？！\n'
for char in chars:
    s=s.replace(char,' ')
print(s)