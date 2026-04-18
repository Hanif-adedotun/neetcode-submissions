class LNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self, r = None):
        self.root = r
        self.size = 0
    
    def get(self, index: int) -> int:
        curr_node = self.root
        i=0
        while curr_node:
            if i == index:
                return curr_node.val
            else:
                i+=1
                curr_node = curr_node.next
        return -1

    def insertHead(self, val: int) -> None:
        prev_root = self.root
        self.root = LNode(val)
        self.root.next = prev_root
        self.size +=1

    def insertTail(self, val: int) -> None:
        curr_node = self.root
        if not curr_node:
            self.root = LNode(val)
            self.size +=1
            return
        while curr_node:
            if curr_node.next == None:
                curr_node.next = LNode(val) 
                self.size +=1
                return
            else:
                curr_node = curr_node.next
        

    def remove(self, index: int) -> bool:
        curr_node = self.root
        prev = None
        i=0
        while curr_node:
            if i == index:
                if prev:
                    prev.next = curr_node.next
                else:
                    self.root = curr_node.next
                self.size-=1
                return True
            else:
                i+=1
                prev = curr_node
                curr_node = curr_node.next
        return False

    def getValues(self) -> List[int]:
        curr_node = self.root
        vals = []
        while curr_node:
            vals.append(curr_node.val)
            curr_node = curr_node.next
        return vals
        
