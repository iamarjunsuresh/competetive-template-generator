import json
from pprint import pprint

from string import Template


class template:
	self.template=[]
	def load(self,jsonfile):
		with open('jsonfile') as f:
			self.template = json.load(f)
	
	def render(self,block):
		return rendercontent(self,block)
	def rendercontent(self,block):
		
		output=""
		for b in block.childs:
			output+=generate(self,b)
		d=dict(block=output)
		return substi(template.file,d)
		
	def generate(self,block)
		instr=block.type
		output=""
		inner=""
		if instr=="for":
			
			for b in block.childs:
				inner+=generate(self,b)
				
			return subti(self,data["for"],{block:inner,i:block.i,start:block.start,end:block.end})
		elif instr=="out":
			
			for v in block.vars:
				output+=subti(self,data["out"],{var:v})
			return output	
		elif instr=="in":
			for v in block.vars:
				output+=subti(self,data["out"],{var:v})
			return output
		return output
	def subti(self,str,d):
		s = Template(str)
		return s.substitute(d)
		
