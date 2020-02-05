# p47.py
class Node:
    data = None
    nextnode = None
    prenode = None

    def __init__(self, data):
        self.data = data


class PersonChan:
    size = 0
    head = None
    tail = None
    sign = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.sign = None
        self.size = 0

    # 增加节点
    # 在查找到的a后面增加节点
    def ins_node(self, b):
        newnode = Node(b)
        global cursor

        if cursor is None and cursor == self.head:
            self.head = newnode
            self.tail = newnode
        elif cursor == self.tail and self.tail is not None:
            self.tail.nextnode = newnode
            self.tail = newnode
            self.tail.prenode = cursor
            self.tail.nextnode = None
        elif cursor == self.sign:
            newnode.nextnode = self.head
            self.head.prenode = newnode
            self.head = newnode
        else:
            newnode.prenode = cursor
            newnode.nextnode = cursor.nextnode
            cursor.nextnode.prenode = newnode
            cursor.nextnode = newnode
        cursor = newnode
        self.size = self.size + 1

    # 删除节点
    def del_node(self, node):
        global cursor
        if self.head != self.tail:
            if node == self.head:
                self.head = node.nextnode
                cursor = self.sign
            elif node == self.tail:
                self.tail = node.prenode
                node.prenode.nextnode = None
                cursor = node.prenode
            else:
                node.prenode.nextnode = node.nextnode
                node.nextnode.prenode = node.prenode
                cursor = node.prenode
        else:
            self.head = self.tail = None
            cursor = self.head
        self.size = self.size - 1


str1 = input().strip()
str1 = list(str1)

str2 = PersonChan()
cursor = str2.head
for i in str1:
    if i == '[':
        cursor = str2.sign
    elif i == ']':
        cursor = str2.tail
    elif i == '<':
        if cursor != str2.head and cursor != str2.sign:
            cursor = cursor.prenode
        elif cursor == str2.head:
            cursor = str2.sign
    elif i == '>':
        if cursor != str2.tail and cursor != str2.sign:
            cursor = cursor.nextnode
        elif cursor == str2.sign:
            cursor = str2.head
    elif i == '-':
        if (str2.head != str2.tail and cursor != str2.sign) or (
                str2.head == str2.tail and cursor != str2.sign and str2.head is not None):
            str2.del_node(cursor)
    else:
        str2.ins_node(i)

if str2.head is None:
    print('?')
else:
    t = str2.head
    while t is not None:
        print(t.data, end='')
        t = t.nextnode
