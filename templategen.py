import os
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
         
         
         


line=raw_input('enter template:')
words=lines.split(' ')
blockstack=Stack()
curblock={};
for word in words:
	parentblock=blockstack.peek()

	if word=="{":
		forbl
		prevtoken.clear()
	elif word=="}":

	elif word=="in":
		inputdic=dic(type="in",vars=prevtokens)
		parentblock.childs.append(inputdic)
	elif word=="":
		pass
	else:
		prevtoken.append(word)
 
print output











