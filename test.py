#!/usr/bin/python

## This is to test python class

from __future__ import print_function
import sys

##catching the argument


if len(sys.argv) != 2:
	print("Usage: " + sys.argv[0] + " person's name")
	exit()

person_of_interest = sys.argv[1]

# if type(person_of_interest) != "<type 'str'>":
# 	print('Name should be string: ', type(person_of_interest))
# 	exit()


if person_of_interest != 'a_person':
	print('You are not authorised!!')
	exit()



##Class defination.


class Account(object):

	account_origin = 'online'

	def __init__(self,account_type,account_number,account_holder_name):

		self.account_type = account_type
		self.account_number = account_number
		self.account_holder_name = account_holder_name


	def account_summery(self,main_balance,amount_not_paid = 0):

		self.main_balance = main_balance
		self.amount_not_paid = amount_not_paid
		return self.main_balance


	def get_status(self,status = 'OK'):
		self.status = status
		return self.status

		


##object initialization

person_of_interest = Account(account_type = 'checking', account_number = 123456, account_holder_name = 'samy')
a_person_main_bal = person_of_interest.account_summery(main_balance = 1500, amount_not_paid = 100)


## Outputs

print('----------------------------')
print('      Account Story:')
print('----------------------------')
print('Account Type: {X}'.format(X=person_of_interest.account_type))
print('Account Number: {Y}'.format(Y=person_of_interest.account_number))
print('Account Holder Name: {Z}'.format(Z=person_of_interest.account_holder_name.upper()))
print('Main Balance: {A}'.format(A=a_person_main_bal))
print('Not paid Amount: {B}'.format(B=person_of_interest.amount_not_paid))
print('Account Status: {C}'.format(C=person_of_interest.get_status()))
