import abc

class Heap:
	__metaclass__ = abc.ABCMeta
	@abc.abstractmethod
	def _is_lower_than(self, item1, item2):
		"""
		Return True if item1 should be
		positioned lower than item2 on the heap.
		Else return False
		"""
	def __init__(self, heap_data=None):
		if heap_data is None:
			self.items = []
		else:
			self.items = list(heap_data)


	def __get_lchild_index(self, parent_index):
		return parent_index * 2 + 1

	def __get_rchild_index(self, parent_index):
		return parent_index * 2 + 2

	def __get_parent_index(self, child_index):
		return (child_index - 1) / 2


	def __has_lchild(self, parent_index):
		return self.__get_lchild_index(parent_index) < len(self.items)

	def __has_rchild(self, parent_index):
		return self.__get_rchild_index(parent_index) < len(self.items)

	def __has_parent(self, index):
		return index > 0


	def __get_lchild(self, parent_index):
		return self.items[self.__get_lchild_index(parent_index)]

	def __get_rchild(self, parent_index):
		return self.items[self.__get_rchild_index(parent_index)]

	def __get_parent(self, child_index):
		return self.items[self.__get_parent_index(child_index)]


	def peek(self):
		if len(self.items) == 0:
			raise IndexError("peek from an empty Heap")
		return self.items[0]


	def poll(self):
		if len(self.items) == 0:
			raise IndexError("poll from an empty Heap")
		item = self.items[0]
		self.items[0] = self.items[-1]
		del self.items[-1]
		self.heapify_down()
		return item

	def add(self, item):
		self.items.append(item)
		self.heapify_up()

	def heapify_down(self):
		index = 0
		while self.__has_lchild(index):
			lowest_child_index = self.__get_lchild_index(index)
			if self.__has_rchild(index) and \
			   self._is_lower_than(self.__get_lchild(index), self.__get_rchild(index)):
				lowest_child_index = self.__get_rchild_index(index)
			if self._is_lower_than(self.items[index], self.items[lowest_child_index]):
				self.items[lowest_child_index], self.items[index] = self.items[index], self.items[lowest_child_index]
				index = lowest_child_index
			else:
				break


	def heapify_up(self):
		index = len(self.items) - 1
		while self.__has_parent(index) and \
		      self._is_lower_than(self.__get_parent(index), self.items[index]):
			parent_index = self.__get_parent_index(index)
			self.items[index] , self.items[parent_index] = self.items[parent_index], self.items[index]
			index = parent_index

class MinHeap(Heap):
    def _is_lower_than(self, item1, item2):
        return item1 > item2

class MaxHeap(Heap):
    def _is_lower_than(self, item1, item2):
        return item1 < item2
