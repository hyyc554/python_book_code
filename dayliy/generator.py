def mygenerator():
    i = 0
    while True:
        print('i',i)
        n = yield i
        print('n',n)
        i +=1

b = mygenerator()
b.send(None)
b.send(1)