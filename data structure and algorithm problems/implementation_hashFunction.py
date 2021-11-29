# ========================================== implementation a hash function ================================

def hashFunction(key: str|int, dictionarySize: int):
    if type(key) is str:
        arrayIndexKey= key.__hash__() % dictionarySize
        return arrayIndexKey

    elif type(key) is int:
        arrayIndexKey= key % dictionarySize
        return arrayIndexKey

    raise KeyError("the entered key must be an integer key or a string key")

print(hashFunction("123478-A", 100))
print(hashFunction(12, 100))
print(hashFunction(128123798, 100))
# print(hashFunction([], 100))
