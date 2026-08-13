import collections

class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.prev = prev
        self.next = next


class LinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)

        self.left.next = self.right
        self.right.prev = self.left

        self.map = {}

    def length(self):
        return len(self.map)

    def pushRight(self, val):
        node = ListNode(
            val,
            self.right,
            self.right.prev
        )

        self.map[val] = node

        node.prev.next = node
        self.right.prev = node

    def pop(self, val):
        if val in self.map:
            node = self.map[val]

            next_node = node.next
            prev_node = node.prev

            next_node.prev = prev_node
            prev_node.next = next_node

            self.map.pop(val, None)

    def popLeft(self):
        res = self.left.next.val
        self.pop(res)
        return res


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.minFreq = 0
        self.valMap = {}
        self.countMap = collections.defaultdict(int)
        # frequency -> LinkedList of keys
        self.listMap = collections.defaultdict(LinkedList)

    def length(self):
        return len(self.valMap)

    def counter(self, key):
        cnt = self.countMap[key]
        self.countMap[key] += 1
        self.listMap[cnt].pop(key)

        self.listMap[cnt + 1].pushRight(key)

        if cnt == self.minFreq and self.listMap[cnt].length() == 0:
            self.minFreq += 1

    def get(self, key: int) -> int:
        if key not in self.valMap:
            return -1

        self.counter(key)

        return self.valMap[key]

    def put(self, key: int, value: int) -> None:

        if self.cap == 0:
            return

        if key in self.valMap:
            self.valMap[key] = value
            self.counter(key)
            return

        if len(self.valMap) == self.cap:
            res = self.listMap[self.minFreq].popLeft()

            self.valMap.pop(res)
            self.countMap.pop(res)

        self.valMap[key] = value
        self.countMap[key] = 1
        self.minFreq = 1
        self.listMap[1].pushRight(key)