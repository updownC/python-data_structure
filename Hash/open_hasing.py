import hashlib

# hash table and utils
table = [0 for i in range(8)]


def get_key(data):
    byte_data = data.encode()
    hash_object = hashlib.sha256()
    hash_object.update(byte_data)
    hex_dig = hash_object.hexdigest()

    return int(hex_dig, 16)


def hash_function(key):
    return key % 8

# Collision handling by open hasing with list type

# def save_data(key,value):
#   hash_key = get_key(key)
#   address = hash_function(hash_key)

#   if table[address] == 0 :
#     table[address] = [[key,value]]
#   else:
#     for index in range(len(table[address])):
#       if table[address][index][0] == key:
#         table[address][index][1] == value
#         return
#     table[address].append([key,value])

# def get_data(key):
#   hash_key = get_key(key)
#   address = hash_function(hash_key)

#   if table[address] == 0:
#     return print('EMPTY SLOT : no data exist')
#   else :
#     for index in range(len(table[address])):
#       if table[address][index][0] == key:
#         return table[address][index][1]
#     return 'Data not found'


# Collision handling by open hashing with linked list

class Node(object):
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


def save_data(key, value):
    hash_key = get_key(key)
    address = hash_function(hash_key)
    # slot이 비어 있는 경우, 최초입력
    if table[address] == 0:
        table[address] = Node(hash_key, value)
    # 이미 node가 저장된 경우
    else:
        node = table[address]
        # linked list 순회
        while node.next:
            # 현재 존재하는 key값이면 value update
            if node.key == hash_key:
                node.value = value
                return
            else:
                node = node.next
        # 마지막 node에 존재하는 경우,value update
        if node.key == hash_key:
            node.value = value
            return
        # 현재 node에 이어서 새로운 node 등록
        node.next = Node(hash_key, value)


def get_data(key):
    hash_key = get_key(key)
    address = hash_function(hash_key)

    if table[address] == 0:
        return "Data not found : Empty Slot"

    node = table[address]

    while node.next:
        if node.key == hash_key:
            return node.value
        else:
            node = node.next

    if node.key == hash_key:
        return node.value

    return "Data not found : 해당 key가 존재하지 않습니다."


save_data('sangha', 111)
save_data('sooo', 222)
save_data('fooo', 333)
save_data('bar', 444)
save_data('baz', 555)
save_data('ant', 666)
save_data('mike', 777)
save_data('kim', 888)
save_data('brand', 999)

print(get_data('sangha'))
print(get_data('mike'))
