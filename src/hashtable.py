# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        # return hash(key)
        return self._hash_djb2(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash = 5381
        for i in key:
            hash = ((hash << 5) + hash) + ord(i)
        return hash

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        # we get the new index by calling the hash fuction with the provided key
        index = self._hash_mod(key)

        # using the provided key and value, we generate a new key value pair by calling the LinkedPair function
        new_pair = LinkedPair(key, value)

        # we generate or make available a memory space for the next pair of key and value by storing the index in the next pair
        new_pair.next = self.storage[index]

        # with that, we can now store the new pair of key and value in the array using the index
        self.storage[index] = new_pair

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        # first we get our index
        index = self._hash_mod(key)

        # if index does not exit print error message
        if self.storage[index] is None:
            print("The key is not there")

        # else get the position of the index in our storage
        remove = self.storage[index]

        # since the next index position is none, we set the current position of our index to next
        self.storage[index] = remove.next

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        # get the current index
        index = self._hash_mod(key)

        # get the position of the current index
        current_pair = self.storage[index]

        while current_pair:
            # if the key at current positon is equal to key
            if current_pair.key == key:
                # return the key value pair
                return current_pair.value
            # else check the next by set the current podition to next, and repeat the loop
            current_pair = current_pair.next
        # else return none if not found on reaching the end of the list
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # we simple append a none after every index position in the list
        for _ in range(self.capacity):
            self.storage.append(None)


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
