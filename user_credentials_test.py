import unittest
import pyperclip
from user_credentials import User, Credential


class TestUser(unittest.TestCase):
	def setUp(self):
		
		self.new_user = User('Erastus','Nj\'oro\'ge','uthiru10')
    
