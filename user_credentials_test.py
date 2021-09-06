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
    

class TestCredentials(unittest.TestCase):
	'''
	Test class that defines test cases for the credentials class behaviours.
	Args:
	    unittest.TestCase: helps in creating test cases
	'''
	def test_check_user(self):
		'''
		Function to test whether the login in function check_user works as expected
		'''
		self.new_user = User('Faith','Mb\'uth\'ia','pswd100')
		self.new_user.save_user()
		user2 = User('Ken','Mb\'uth\'ia','pswd100')
		user2.save_user()

		for user in User.users_list:
			if user.first_name == user2.first_name and user.password == user2.password:
				current_user = user.first_name
		return current_user
        
        self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))

	def setUp(self):
		
		self.new_credential = Credential('Charles','Facebook','charlesndugire','password100')

	def test_init_(self):
		
		self.assertEqual(self.new_credential.user_name,'Charles')
		self.assertEqual(self.new_credential.site_name,'Facebook')
		self.assertEqual(self.new_credential.account_name,'charlesndugire')
		self.assertEqual(self.new_credential.password,'password100')

	def test_save_credentials(self):
	
		self.new_credential.save_credentials()
		twitter = Credential('Jane','Twitter','maryjoe','pswd100')
		twitter.save_credentials()
		self.assertEqual(len(Credential.credentials_list),2)

	def tearDown(self):
		'''
		Function to clear the credentials list after every test
		'''
		Credential.credentials_list = []
		User.users_list = []

