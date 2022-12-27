p1 = {
    "name":"高小一",
    "age":18,
    "salay":30000
}
p2 = {
    "name":"高小二",
    "age":19,
    "salay":20000
}
p3 = {
    "name":"高小五",
    "age":20,
    "salay":10000
}
p = [p1,p2,p3]
# print(p)
for x in p:
    if x.get('salay')>15000:
        print(x)
