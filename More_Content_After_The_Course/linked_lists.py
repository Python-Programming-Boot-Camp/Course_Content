class node:
	def __init__(self,data=None):
		self.data=data
		self.next=None

class linked_list:
	def __init__(self):
		self.head=node()

	def append(self,data):
		new_node=node(data)
		current=self.head
		while current.next!=None:
			current=current.next
		current.next=new_node

	def length(self):
		current=self.head
		total=0
		while current.next!=None:
			total+=1
			current=current.next
		return total 

	def display(self):
		elems=[]
		current_node=self.head
		while current_node.next!=None:
			current_node=current_node.next
			elems.append(current_node.data)
		print(elems)

	def get(self,index):
		if index>=self.length() or index<0:
			print("ERROR: 'Get' Index out of range!")
			return None
		cur_idx=0
		cur_node=self.head
		while True:
			cur_node=cur_node.next
			if cur_idx==index: return cur_node.data
			cur_idx+=1

	def remove(self,index):
		if index>=self.length() or index<0:
			print("ERROR: 'Erase' Index out of range!")
			return 
		current_index=0
		current_node=self.head
		while True:
			last_node=current_node
			current_node=current_node.next
			if current_index==index:
				last_node.next=current_node.next
				return
			current_index+=1

	def __getitem__(self,index):
		return self.get(index)

my_list = linked_list()
my_list.append(1)
my_list.append(2)
my_list.display()
my_list.remove(1)
my_list.display()
my_list.append(1)
my_list.display()
my_list.get(1)
my_list.get(2)