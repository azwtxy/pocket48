# -*- coding: utf-8 -*-
'''
@author: DipperStar
@mail: ssr@yinheng.xyz
'''
import pymongo
import traceback

class MongoDB:
	'''
	基于pymongo封装的CURD
	'''
	def __init__(self, db, collections):
		self.client = pymongo.MongoClient('localhost', 27017)
		self.db = self.client[db]
		self.post = self.db[collections]

	def insert(self, data):
		try:
			self.post.insert(data)
			return True
		except:
			return False
	
	def insert_many(self, data):
		try:
			self.post.insert_many(data)
			return True
		except:
			return False

	def remove(self, select):
		self.post.remove(select)

	def update(self, data, upsert = False, ):
		try:								
			if self.post.update(data, {'$set': data}, upsert)['updatedExisting']:
				return 'exists'
			else:
				return 'success'
		except:
			print(traceback.print_exc())
			return False

	def update_many(self, data, upsert = False):
		try:
			self.post.update_many(data, data, upsert)
			return True
		except:
			return False

	def find(self, select, limit = False):
		try:
			if limit:
				return self.post.find(select).limit(limit)
			else:
				return self.post.find(select)
		except:
			return False

	def distinct(self, label, select = None):
		try:
			return self.post.distinct(label, filter = select)
		except:
			return False




