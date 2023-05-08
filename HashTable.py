from LinkedList import LinkedList


class HashTable(object):

    def __init__(self, num_buckets=8):
        """Initialize this hash table with the given initial size."""
        self.buckets = [LinkedList() for i in range(num_buckets)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    def load_factor(self):
        """Return the load factor, the ratio of number of entries to buckets.a"""
        # count number of entries
        num_entries = 0
        for bucket in self.buckets:
          num_entries += bucket.length()
        
        # Calculate load factor
        load_factor = num_entries / len(self.buckets)
        return load_factor
        

    def items(self):
        """Return a list of all entries (key-value pairs) in this hash table."""
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Best case running time: ??? under what conditions? [TODO]
        - Best case is when the key-value pair we are looking for is the first element

        Worst case running time: ??? under what conditions? [TODO]
        - Worst case is when the linked list in the bucket has 'n' elements and the key we are looking for is at the end or not in the list
        """
        
        # get the hash value for the given key
        hash_value = self._bucket_index(key)
        
        # Find the bucket the given key belongs in
        bucket_index = hash_value % len(self.buckets)
    
        # Find the entry with the given key in that bucket, if one exists
        current_node = self.buckets[bucket_index]
        while current_node is not None:
          if current_node.data[0] == key:
            return current_node.data[1]
          
          current_node = current_node.next

        raise KeyError(str(key))


    def set(self, key, value):
        """Insert the given key with its associated value.
        Best case running time: ??? under what conditions? [TODO]
        - best case is when the key already exists in the hash table and set() can update the value without having to iterate through the linkedlist for the corresponding bucket

        Worst case running time: ??? under what conditions? [TODO]
        - worst case is when the key does not exist in the hash table and the set() method has to iterate through whole list of corresponding bucket to find the correct location
        """ 
        
        # Find the bucket the given key belongs in
        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]

        # check if the key already exists in the bucket
        current_node = bucket.head
        while current_node is not None:
          if current_node.data[0] == key:
            # if key already exists, update the value
            current_node.data = (key, value)
            return

          current_node = current_node.next

        # if key doesnt exist, insert the new key-value entry in to the bucket's linkedlist
        bucket.append((key, value))
        
        #Check if the load factor exceeds a threshold such as 0.75
        if self.load_factor() > 0.75:
          #If so, automatically resize to reduce the load factor
          self._resize()


    def delete(self, key):
      #THIS IS STRETCH WILL NEED TO IMPLEMENT DELETE IN LL
        """Delete the given key and its associated value, or raise KeyError.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Find the bucket the given key belongs in
        
        # Find the entry with the given key in that bucket, if one exists
        pass


    def _resize(self, new_size=None):
        """Resize this hash table's buckets and rehash all key-value entries.
        Should be called automatically when load factor exceeds a threshold
        such as 0.75 after an insertion (when set is called with a new key)."""

        # determine new size if not given, double it by default
        if new_size is None:
          new_size = len(self.buckets) * 2

        #store items into a temporary list
        old_items = []
        for key, value in self.items():
          old_items.append((key, value))

        #create new list of buckets with new size
        self.buckets = [LinkedList() for _ in range(new_size)]
        
        #rehash old items into new buckets
        for key, value in old_items:
          bucket_index = self._bucket_index(key)
          self.buckets[bucket_index].append((key, value))
        


def test_hash_table():
    ht = HashTable(4)
    print('HashTable: ' + str(ht))

    print('Setting entries:')
    ht.set('I', 1)
    print('set(I, 1): ' + str(ht))
    ht.set('V', 5)
    print('set(V, 5): ' + str(ht))
 
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))
    ht.set('X', 10)
    print('set(X, 10): ' + str(ht))
    ht.set('L', 50)  # Should trigger resize
    print('set(L, 50): ' + str(ht))
  
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))

    print('Getting entries:')
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('get(L): ' + str(ht.get('L')))
    

    print('Deleting entries:')
    ht.delete('I')
    print('delete(I): ' + str(ht))
    ht.delete('V')
    print('delete(V): ' + str(ht))
    ht.delete('X')
    print('delete(X): ' + str(ht))
    ht.delete('L')
    print('delete(L): ' + str(ht))
   
 
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))

