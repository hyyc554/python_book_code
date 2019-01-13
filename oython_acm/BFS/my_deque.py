from collections import deque


graph={}


def person_is_seller(name):
    """
    判断一个人是不是芒果经销商，如果名字以“m”结尾就认为他是
    """
    return name[-1]=='m'
def serach_mango(name):
    search_queue = deque()    # 创建一个队列
    search_queue+=graph[name]  # 将你的邻居都加入到这个搜索队列中
    serached = []
    while search_queue:
        person = search_queue.popleft
        if person not in serached:
            if person_is_seller(person):
                print(person+"is a mango seller")
                return True
            else:
                search_queue+=graph[person]
                serached.append(person)
    return False