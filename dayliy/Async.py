from time import sleep
class Potato:
    @classmethod
    def make(cls, num, *args, **kws):
        potatos = []
        for i in range(num):
            potatos.append(cls.__new__(cls, *args, **kws))
        return potatos

all_potatos = Potato.make(5)
print(all_potatos)
def take_potatos(num):
    count = 0
    while True:
        if len(all_potatos) == 0:
            sleep(.1)
        else:
            potato = all_potatos.pop()
            yield potato
            count += 1
            if count == num:
                break

def buy_potatos():
    bucket = []
    for p in take_potatos(3):
        bucket.append(p)
    return bucket

print(buy_potatos())