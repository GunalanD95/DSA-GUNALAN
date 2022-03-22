# Implementation of Hash Table


class HashTable():

    def __init__(self,size):
        self.size = size
        self.hashmap = [[] for _ in range(0,self.size)]
        print(self.hashmap)


    def _hash_(self,key):
        hashed_key = hash(key) % self.size
        return hashed_key

    def set(self,key,value):
        hash_key = self._hash_(key)
        key_exists = False
        slot = self.hashmap[hash_key]
        for i , kv in enumerate(slot):
            k , v = kv
            if key == k:
                key_exists = True      
                break

        if key_exists:
            slot[i] = (key,value)

        else:
            slot.append((key,value))


    def get(self,key):
        hash_key = self._hash_(key)
        slot = self.hashmap[hash_key]
        for kv in slot:
            k , v = kv
            if key == k:
                return v
            else:
                raise KeyError("Key not found")
        return None


    def delete(self, key):
        hash_key = self._hash_(key)
        key_exists = False
        slot = self.hashmap[hash_key]
        for i , kv in enumerate(slot):
            k, v = kv 
            if key == k:
                key_exists = True 
                break
        if key_exists:
            del slot[i]
            print ('Key {} deleted'.format(key))
        else:
            print ('Key {} not found'.format(key))


    def __setitem__(self,key,value):
        self.set(key,value)

    def __getitem__(self,key):
        return self.get(key)

a = HashTable(5)
a.set("key-1","value-1")
a.set("key-2","value-2")
a.set("key-3","value-3")
a.set("key-4","value-4")
a.set("key-34","value-34")
print(a.hashmap)
a.delete("key-34")
print(a.get("key-1"))
print(a.hashmap)