from sqlalchemy.exc import IntegrityError
from models import Session
from models import TblReqs
import os

## classes which helps to represent and use the object of Request 
class Core(object):
	def __init__(self):
		self.requests = {}
		self.load_requests()




	def add_request(self,time,req):
		try:
			session=Session()
			request=TblReqs(time=time,request=req)

			session.add(request)
			session.commit()


		except IntegrityError:
			session.rollback()
			raise ValueError("Fail to add")

		self.requests[request.id] =Reqs(request.time,request.request) 

	def load_requests(self):
		for c in Session().query(TblReqs).all():
			self.requests[c.id]=Reqs(c.request,c.time)






class Reqs(object):
	def __init__(self,req,time):
		self.request=req
		self.time=time

	def to_dict(self):
		return {'req':self.request, 'time':self.time}


