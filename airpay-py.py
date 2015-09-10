import webapp2
import os
from api import LocalbitcoinsAPI

api = LocalbitcoinsAPI()

class Self(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		response = api.make_request('GET', '/api/myself/')
		self.response.write(response.data)

class Balance(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		response = api.make_request('GET', '/api/wallet-balance/')
		self.response.write(response.data['data']['total']['balance'])


class Send(webapp2.RequestHandler):
	def post(self):
		self.response.headers['Content-Type'] = 'text/plain'
		
		response = api.make_request('POST', '/api/wallet-send/')
		self.response.write(response.data['data']['total']['balance'])

app = webapp2.WSGIApplication([
	('/self', Self),
	('/wallet/balance', Balance),
	('/wallet/send', Send),
], debug=True)

