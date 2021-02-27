from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)


  # 1Complete the create_arr method.

  # Each element of the hash table (arr) is a linked list.
  # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.

#Goal is to create the create_arr method. Each element of hash table arr is a linked list. 
#Method creates an array named list of a given size and populates each of its elements with a LinkedList object. 
  def create_arr(self, size):
    list_array = []
    
    for i in range(size): 
       #Using an iterative solution
        updated_linkedlist = LinkedList()
        list_array.append(updated_linkedlist)
    return list_array


    #Create your own hash function.
# Hash functions are a function that turns each of these keys into an index value that we can use to decide where in our list each key:value pair should be stored. 

  #Creating own Hash function method. Hash functions are functions that turn each of 
  #these keys into an index value that we can use to decide WHERE in our list each key:value pain
  #should be stored. Recall consolidation example
  def hash_func(self, key):
    #Should be similar to example Joi gave regarding the length of each word
    first_letter = key[0]
    distance_fron_letter_a = ord(first_letter) - ord('a')
    #ord must be one letter only or return error
    #Greater the distance, farther away
    index = distance_fron_letter_a % self.size 
    return index
  #Complete the insert method.

  # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

#Should insert a key value pair into the hash table where the key is the word 
#The value should be a counter for the number of times the word appears. 
#When inserting a new word in the hash table, should check if there is a Node with the same key in the table already

  def insert(self, key, value):
    hash_key = self.hash_func(key)
    #find the index of the key-value pair to place by finding key
    linked_list = self.arr[hash_key]
    linked_list_index = linked_list.find(key)
    #This finds the place in index of key-value pair and checks if the index is still available
    #If the item is not in our linked_list, we must create a tuple to append to our linked list
    #Use of Tuple taken from StackOverflow 
    our_tuple = (key, value)
    if linked_list.find(key) == -1:
      linked_list.append(our_tuple)
    else: 
      linked_list.update(our_tuple)

  # Complete the print_key_values method.

  # Traverse through the every Linked List in the table and print the key value pairs.

  # For example: 
  # a: 1
  # again: 1
  # and: 1
  # blooms: 1
  # erase: 2

  def print_key_values(self):
    for i in self.arr:
      i.print_nodes()




