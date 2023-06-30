class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def add(data):
    node = head # node 라는 변수에 첫번째 노드를 넣어줘
    while node.next: # 노드의 포인터 값(다음 노드의 정보)가 있다면..
        node = node.next # node 라는 변수에 노드의 포인터 값(=다음 노드의 정보)을 넣어줘(변수 node 재정의)
    node.next = Node(data) # (노드의 포인터 값이 없다면) 노드의 포인터 값에 Node(data)를 넣어줘

# def get_data():
#     node = head
#     while node.next:
#         print(node.data)
#         node = node.next 
#     print(node.data)

                # 노드의 구조 : (데이터값, 포인터(주소값))
head = Node(1)  # 첫번째 노드 : (1, None)  # head = 첫번째 노드

add(2)
node = Node(1)
# while Node(1).next 가 값이 없어서, while문스킵
Node(1).next = Node(2) # 첫번째 노드 : (1, Node(2))
                       # 두번째 노드 : (2, None)

add(3)
node = Node(1)
while Node(1).next: # 이젠 Node(2)로 값이 생겨서, while문 실행
    node = Node(1).next = Node(2) # node 라는 변수에 Node(1).next, 즉 Node(2) 가 들어감
# while Node(2).next 가 값이 없어서, while문 스킵
Node(2).next = Node(3) # 두번째 노드 : (2, Node(3))
                       # 세번째 노드 : (3, None)

# for index in range(2, 10):
#     add(index)

# get_data()


# linke list 를 llist 로 굳이 표현해보자면..?
# [(1, Node(2)), (2, Node(3)), ~~ (9, None) ...] -> 사실 일렬로 있지 않지만, 편의상 한줄에 표현
#   첫번째노드     두번째노드       마지막노드  ㄴ 노드가 추가되면 자동으로 자리 생김


