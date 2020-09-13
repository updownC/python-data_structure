# table = [0 for i in range(10)]
# print(table)

# def hash_function(key):
#   return key % 10

# def storage_data(key,value):
#   hash_key = ord(key[0])
#   address = hash_function(hash_key)
#   table[address] = value

# def get_data(key):
#   hash_key = ord(key[0])
#   address = hash_function(hash_key)
#   return table[address]

# storage_data('sangha',102234)
# storage_data('eunjeong',1023334234)
# storage_data('juwon',102664)

# print(get_data("juwon"))

table = [0 for i in range(8)]

def get_hash_key(key):
  return hash(key)

def hash_function(key):
  return key % 8

def save_data(key, value):
  address = hash_function(get_hash_key(key))
  table[address] = value

def get_data(key):
  address = hash_function(get_hash_key(key))
  return table[address]

save_data('sangha',1111111)
save_data('juwon',2222222)
save_data('jihwan',333333)

print(table)