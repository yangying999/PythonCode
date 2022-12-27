# s="A123x456 17960? 309yhu5876"
# i = 0
# a = []
# while i<len(s):
#     sub=''
#     while s[i] in '0123456789':
#         sub = sub + s[i]
#         i+=1
#         if i==len(s):
#             break
#
#     if len(sub)>0:
#         a.append(sub)
#     i+=1
# print(a)

#
s="A123x456 17960? 309yhu5876"
sub = ''
a=[]
for i in range(len(s)):
    if s[i] in '0123456789':
        sub+=s[i]
        if i==len(s)-1:
            a.append(sub)
    else:
        if len(sub)>0:
            a.append(sub)
        sub=''
print(a)