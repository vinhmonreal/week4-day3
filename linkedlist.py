class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class LinkedList:
    
    def __init__(self):
        self.head = None

    def add_node(self, value):
        node = Node(value)
        if not self.head:
          self.head = node
        else:
          current_node = self.head
          while current_node.right:
              previous_node = current_node
              current_node = current_node.right
              current_node.left = previous_node
          current_node.right = node

    def __iter__(self):
       current_node = self.head
       while current_node:
          yield current_node
          current_node = current_node.right

    def __repr__(self):
      return ' -> '.join(node.value for node in self)
      # nodes = []
      # for node in self:
      #   nodes.append(node.value)
      # return ' -> '.join(nodes)

    def insert_node(self, target, value):
       new_node = Node(value)
       if self.head:
          for node in self:
             if node.value == target:
                right_node = node.right
                node.right = new_node
                new_node.right = right_node
       else:
          print('Empty List')

    def remove_node(self, value):
        if value == self.head.value:
           self.head = self.head.right
        else:
           for node in self:
              if node.right:
                if node.right.value == value:
                  node.right = node.right.right
                  return
                
    def get_tail(self):
      #  for node in self:
      #     pass
      #  return node.value
      node = self.head
      while node.right:
         node = node.right
      return node.value

    def remove_tail(self):
      node = self.head
      if node.right:
        while node.right.right:
          node = node.right
        node.right = None
    
    def prepend(self, value):
        new_node = Node(value)
        new_node.right = self.head
        self.head = new_node
        
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.right
        return count

    def add_list_element(self, data_list):
        for i in data_list:
            self.add_node(i)
        
            
          
# linkedlist = LinkedList()
# linkedlist.add_node('99')
# linkedlist.add_list_element(['green', 'yellow', 'orange'])
# linkedlist.prepend('red')
# print(linkedlist)