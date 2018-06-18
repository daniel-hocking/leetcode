# Written by Eric Martin for COMP9021


'''
A Binary Tree abstract data type
'''


class BinaryTree:
    def __init__(self, value = None):
        self.val = value
        if self.val is not None:
            self.left = BinaryTree()
            self.right = BinaryTree()
        else:
            self.left = None
            self.right = None

    def height(self):
        '''An empty tree is of height 0.
        The height of a nonempty tree is the length of its longest branch minus 1.
        So both an empty tree and a tree consisting of its root are of height 0.
        
        >>> t = BinaryTree()
        >>> t.height()
        0
        >>> t = BinaryTree(1)
        >>> t.height()
        0
        >>> t = BinaryTree(3); t_L = BinaryTree(2); t_LL = BinaryTree(1)
        >>> t_R = BinaryTree(5); t_RL = BinaryTree(4); t_RLR = BinaryTree(6); t_RR = BinaryTree(6)
        >>> t.left = t_L; t_L.left = t_LL
        >>> t.right = t_R; t_R.left = t_RL; t_RL.right = t_RLR ; t_R.right = t_RR
        >>> t.height()
        3
        '''
        if self.val is None:
            return 0
        return max(self.left._height(), self.right._height())

    def _height(self):
        if self.val is None:
            return 0
        return max(self.left._height(), self.right._height()) + 1

    def size(self):
        '''Returns the number of nodes.
        
        >>> t = BinaryTree()
        >>> t.size()
        0
        >>> t = BinaryTree(1)
        >>> t.size()
        1
        >>> t = BinaryTree(3); t_L = BinaryTree(2); t_LL = BinaryTree(1)
        >>> t_R = BinaryTree(5); t_RL = BinaryTree(4); t_RLR = BinaryTree(6); t_RR = BinaryTree(6)
        >>> t.left = t_L; t_L.left = t_LL
        >>> t.right = t_R; t_R.left = t_RL; t_RL.right = t_RLR ; t_R.right = t_RR
        >>> t.size()
        7
        '''
        if self.val is None:
            return 0
        return 1 + self.left.size() + self.right.size()

    def occurs_in_tree(self, value):
        '''
        >>> t = BinaryTree()
        >>> t.occurs_in_tree(0)
        False
        >>> t = BinaryTree(1)
        >>> t.occurs_in_tree(0)
        False
        >>> t.occurs_in_tree(1)
        True
        >>> t = BinaryTree(3); t_L = BinaryTree(2); t_LL = BinaryTree(1)
        >>> t_R = BinaryTree(5); t_RL = BinaryTree(4); t_RLR = BinaryTree(6); t_RR = BinaryTree(6)
        >>> t.left = t_L; t_L.left = t_LL
        >>> t.right = t_R; t_R.left = t_RL; t_RL.right = t_RLR ; t_R.right = t_RR
        >>> t.occurs_in_tree(0)
        False
        >>> t.occurs_in_tree(1), t.occurs_in_tree(2), t.occurs_in_tree(3)
        (True, True, True)
        >>> t.occurs_in_tree(4), t.occurs_in_tree(5), t.occurs_in_tree(6)
        (True, True, True)
        '''
        if self.val is None:
            return False
        if self.val == value:
            return True
        return self.left.occurs_in_tree(value) or self.right.occurs_in_tree(value)

    def occurs_in_bst(self, value):
        '''
        >>> t = BinaryTree()
        >>> t.occurs_in_bst(0)
        False
        >>> t = BinaryTree(1)
        >>> t.occurs_in_bst(0)
        False
        >>> t.occurs_in_bst(1)
        True
        >>> t = BinaryTree(4); t_L = BinaryTree(2); t_LL = BinaryTree(1); t_LR = BinaryTree(3)
        >>> t_R = BinaryTree(5); t_RR = BinaryTree(7); t_RRL = BinaryTree(6)
        >>> t.left = t_L; t_L.left = t_LL; t_L.right = t_LR
        >>> t.right = t_R; t_R.right = t_RR; t_RR.left = t_RRL
        >>> t.occurs_in_bst(0)
        False
        >>> t.occurs_in_bst(1), t.occurs_in_bst(2), t.occurs_in_bst(3)
        (True, True, True)
        >>> t.occurs_in_bst(4), t.occurs_in_bst(5), t.occurs_in_bst(6), t.occurs_in_bst(7)
        (True, True, True, True)
        '''
        if self.val is None:
            return False
        if self.val == value:
            return True
        if value < self.val:
            return self.left.occurs_in_bst(value)
        return self.right.occurs_in_bst(value)

    def is_bst(self):
        '''
        >>> t = BinaryTree()
        >>> t.is_bst()
        True
        >>> t = BinaryTree(1)
        >>> t.is_bst()
        True
        >>> t = BinaryTree(3); t_L = BinaryTree(2); t_LL = BinaryTree(1)
        >>> t_R = BinaryTree(5); t_RL = BinaryTree(4); t_RLR = BinaryTree(6); t_RR = BinaryTree(6)
        >>> t.left = t_L; t_L.left = t_LL
        >>> t.right = t_R; t_R.left = t_RL; t_RL.right = t_RLR ; t_R.right = t_RR
        >>> t.is_bst()
        False
        >>> t = BinaryTree(4); t_L = BinaryTree(2); t_LL = BinaryTree(1); t_LR = BinaryTree(3)
        >>> t_R = BinaryTree(5); t_RR = BinaryTree(7); t_RRL = BinaryTree(6)
        >>> t.left = t_L; t_L.left = t_LL; t_L.right = t_LR
        >>> t.right = t_R; t_R.right = t_RR; t_RR.left = t_RRL
        >>> t.is_bst()
        True
        '''
        if self.val is None:
            return True
        node = self.left
        if node.value is not None:
            while node.right.value is not None:
                node = node.right
            if self.val <= node.value:
                return False
        node = self.right
        if node.value is not None:
            while node.left.value is not None:
                node = node.left
        if node.value is not None and self.val >= node.value:
            return False
        return self.left.is_bst() and self.right.is_bst()

    def insert_in_bst(self, value):
        '''
        >>> t = BinaryTree()
        >>> t.insert_in_bst(4)
        True
        >>> t.print_binary_tree()
        4
        >>> t.insert_in_bst(2)
        True
        >>> t.print_binary_tree()
              2
        4
        <BLANKLINE>
        >>> t.insert_in_bst(1)
        True
        >>> t.print_binary_tree()
                    1
              2
        <BLANKLINE>
        4
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        >>> t.insert_in_bst(5)
        True
        >>> t.print_binary_tree()
                    1
              2
        <BLANKLINE>
        4
        <BLANKLINE>
              5
        <BLANKLINE>
        >>> t.insert_in_bst(3)
        True
        >>> t.print_binary_tree()
                    1
              2
                    3
        4
        <BLANKLINE>
              5
        <BLANKLINE>
        >>> t.insert_in_bst(6)
        True
        >>> t.print_binary_tree()
                    1
              2
                    3
        4
        <BLANKLINE>
              5
                    6
        >>> t.insert_in_bst(7)
        True
        >>> t.print_binary_tree()
        <BLANKLINE>
                    1
        <BLANKLINE>
              2
        <BLANKLINE>
                    3
        <BLANKLINE>
        4
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
              5
        <BLANKLINE>
                    6
                          7
        >>> t.insert_in_bst(1), t.insert_in_bst(2), t.insert_in_bst(3)
        (False, False, False)
        >>> t.insert_in_bst(4), t.insert_in_bst(5), t.insert_in_bst(6), t.insert_in_bst(7)
        (False, False, False, False)
        '''
        if self.val is None:
            self.val = value
            self.left = BinaryTree()
            self.right = BinaryTree()
            return True
        if self.val == value:
            return False
        if value < self.val:
            return self.left.insert_in_bst(value)
        return self.right.insert_in_bst(value)


    def delete_in_bst(self, value):
        '''
        >>> t = BinaryTree(4); t_L = BinaryTree(2); t_LL = BinaryTree(1); t_LR = BinaryTree(3)
        >>> t_R = BinaryTree(5); t_RR = BinaryTree(6); t_RRR = BinaryTree(7)
        >>> t.left = t_L; t_L.left = t_LL; t_L.right = t_LR
        >>> t.right = t_R; t_R.right = t_RR; t_RR.right = t_RRR
        >>> t.print_binary_tree()
        <BLANKLINE>
                    1
        <BLANKLINE>
              2
        <BLANKLINE>
                    3
        <BLANKLINE>
        4
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
              5
        <BLANKLINE>
                    6
                          7
        >>> t.delete_in_bst(0.5), t.delete_in_bst(1.5), t.delete_in_bst(2.5), t.delete_in_bst(3.5)
        (False, False, False, False)
        >>> t.delete_in_bst(4.5), t.delete_in_bst(5.5), t.delete_in_bst(6.5), t.delete_in_bst(7.5)
        (False, False, False, False)
        >>> t.delete_in_bst(5)
        True
        >>> t.print_binary_tree()
                    1
              2
                    3
        4
        <BLANKLINE>
              6
                    7
        >>> t.delete_in_bst(7)
        True
        >>> t.print_binary_tree()
                    1
              2
                    3
        4
        <BLANKLINE>
              6
        <BLANKLINE>
        >>> t.delete_in_bst(2)
        True
        >>> t.print_binary_tree()
        <BLANKLINE>
              1
                    3
        4
        <BLANKLINE>
              6
        <BLANKLINE>
        >>> t.delete_in_bst(4)
        True
        >>> t.print_binary_tree()
              1
        3
              6
        >>> t.delete_in_bst(1)
        True
        >>> t.print_binary_tree()
        <BLANKLINE>
        3
              6
        >>> t.delete_in_bst(6)
        True
        >>> t.print_binary_tree()
        3
        >>> t.delete_in_bst(3)
        True
        >>> t.print_binary_tree()
        '''
        return self._delete_in_bst(value, self, '')

    def _delete_in_bst(self, value, parent, link):
        if self.val is None:
            return False
        if value < self.val:
            return self.left._delete_in_bst(value, self, 'L')
        if value > self.val:
            return self.right._delete_in_bst(value, self, 'R')
        if self.left.value is None:
            new_tree = self.right
        elif self.right.value is None:
            new_tree = self.left
        elif self.left.right.value is None:
            new_tree = self.left
            new_tree.right = self.right
        else:
            # Looking for the node containing the largest value
            # smaller than the value to delete.
            # That node will be node_2 and its parent node_1
            node_1 = self.left
            node_2 = node_1.right
            while node_2.right.value is not None:
                node_1 = node_2
                node_2 = node_2.right
            # The value stored in node_2 is meant to replace
            # the value to delete.
            # The replacement will only happen in case the value
            # being deleted is stored in the root; otherwise,
            # node_2 will be connected to the parent
            # of the node storing the value to delete.
            new_tree = node_2
            # Values larger than the value to delete
            # are larger than the replacing value.
            new_tree.right = self.right
            # Values between the value to delete
            # and the value stored in the parent P
            # of the node N storing that value 
            # are larger than the replacing value
            # and can be linked to P since N is going away.
            node_1.right = node_2.left
            # The replacing value is larger than
            # all other values stored on the left
            # of the node N containing the value to delete,
            # and can be linked to the node containing that value
            # since N is going.
            new_tree.left = self.left      
        if link == '':
            self.val = new_tree.value
            self.left = new_tree.left
            self.right = new_tree.right
        elif link == 'L':
            parent.left = new_tree
        else:
            parent.right = new_tree
        return True
    
    def print_binary_tree(self):
        '''
        >>> t = BinaryTree()
        >>> t.print_binary_tree()
        >>> t = BinaryTree(1)
        >>> t.print_binary_tree()
        1
        >>> t = BinaryTree(3); t_L = BinaryTree(2); t_LL = BinaryTree(1)
        >>> t_R = BinaryTree(5); t_RL = BinaryTree(4); t_RLR = BinaryTree(6); t_RR = BinaryTree(6)
        >>> t.left = t_L; t_L.left = t_LL
        >>> t.right = t_R; t_R.left = t_RL; t_RL.right = t_RLR ; t_R.right = t_RR
        >>> t.print_binary_tree()
        <BLANKLINE>
                    1
        <BLANKLINE>
              2
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        3
        <BLANKLINE>
                    4
                          6
              5
        <BLANKLINE>
                    6
        <BLANKLINE>
        '''
        if self.val is None:
            return
        self._print_binary_tree(0, self.height())

    def _print_binary_tree(self, n, height):
        if n > height:
            return
        if self.val is None:
            print('\n' * (2 ** (height - n + 1) - 1), end = '')
        else:
            self.left._print_binary_tree(n + 1, height)
            print('      ' * n, self.val, sep = '')
            self.right._print_binary_tree(n + 1, height)
            
    def pre_order_traversal(self):
        '''
        >>> t = BinaryTree()
        >>> t.pre_order_traversal()
        []
        >>> t = BinaryTree(1)
        >>> t.pre_order_traversal()
        [1]
        >>> t = BinaryTree(3); t_L = BinaryTree(2); t_LL = BinaryTree(1)
        >>> t_R = BinaryTree(5); t_RL = BinaryTree(4); t_RLR = BinaryTree(6); t_RR = BinaryTree(6)
        >>> t.left = t_L; t_L.left = t_LL
        >>> t.right = t_R; t_R.left = t_RL; t_RL.right = t_RLR ; t_R.right = t_RR
        >>> t.pre_order_traversal()
        [3, 2, 1, 5, 4, 6, 6]
        '''
        if self.val is None:
            return []
        values = [self.val]
        values.extend(self.left.pre_order_traversal())
        values.extend(self.right.pre_order_traversal())
        return values

    def in_order_traversal(self):
        '''
        >>> t = BinaryTree()
        >>> t.in_order_traversal()
        []
        >>> t = BinaryTree(1)
        >>> t.in_order_traversal()
        [1]
        >>> t = BinaryTree(3); t_L = BinaryTree(2); t_LL = BinaryTree(1)
        >>> t_R = BinaryTree(5); t_RL = BinaryTree(4); t_RLR = BinaryTree(6); t_RR = BinaryTree(6)
        >>> t.left = t_L; t_L.left = t_LL
        >>> t.right = t_R; t_R.left = t_RL; t_RL.right = t_RLR ; t_R.right = t_RR
        >>> t.in_order_traversal()
        [1, 2, 3, 4, 6, 5, 6]
        '''
        if self.val is None:
            return []
        values = self.left.in_order_traversal()
        values.append(self.val)
        values.extend(self.right.in_order_traversal())
        return values

    def post_order_traversal(self):
        '''
        >>> t = BinaryTree()
        >>> t.post_order_traversal()
        []
        >>> t = BinaryTree(1)
        >>> t.post_order_traversal()
        [1]
        >>> t = BinaryTree(3); t_L = BinaryTree(2); t_LL = BinaryTree(1)
        >>> t_R = BinaryTree(5); t_RL = BinaryTree(4); t_RLR = BinaryTree(6); t_RR = BinaryTree(6)
        >>> t.left = t_L; t_L.left = t_LL
        >>> t.right = t_R; t_R.left = t_RL; t_RL.right = t_RLR ; t_R.right = t_RR
        >>> t.post_order_traversal()
        [1, 2, 6, 4, 6, 5, 3]
        '''
        if self.val is None:
            return []
        values = self.left.post_order_traversal()
        values.extend(self.right.post_order_traversal())
        values.append(self.val)
        return values

           
if __name__ == '__main__':
    import doctest
    doctest.testmod()    

    
