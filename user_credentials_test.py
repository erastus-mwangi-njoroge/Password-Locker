import unittest
import pyperclip
from user_credentials import User, Credential


class TestUser(unittest.TestCase):
	def setUp(self):
		
		self.new_user = User('Erastus','Nj\'oro\'ge','uthiru10')
    
	def test_init_(self):
		
		self.assertEqual(self.new_user.first_name,'Erastus')
		self.assertEqual(self.new_user.last_name,'Nj\'oro\'ge')
		self.assertEqual(self.new_user.password,'uthiru10')

    def test_save_user(self):
		
		self.new_user.save_user()
		self.assertEqual(len(User.users_list),1)
    

