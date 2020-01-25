from __future__ import print_function, unicode_literals
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt, Separator
from examples import custom_style_2
import re
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError
from PyInquirer import style_from_dict, Token, prompt, print_json
from tabulate import tabulate
import mysql.connector 
#################################################################################
mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd="{password}",
database="Flight_Management"
)
cursor = mydb.cursor()
##################################################################################


if __name__ == "__main__":
	
	class AdminidValidator(Validator):
		def validate(self,document):
			pattern=r'[a-zA-z]+$'
			ok=re.match(pattern,document.text)
			if not ok:
				raise ValidationError(
					message='ENTER A VALID NAME',
					cursor_position=len(str(document))
					)
			else:
				query="SELECT Name FROM ADMINISTRATOR WHERE Name= %s"
				cursor.execute(query,(document.text,))
				ok=cursor.fetchall()
				if not ok:
					raise ValidationError(
					message="Account DOESN'T EXISTS !! ",
					cursor_position=len(str(document))
					)
	class RecepidValidator(Validator):
		def validate(self,document):
			pattern=r'[a-zA-z]+$'
			ok=re.match(pattern,document.text)
			if not ok:
				raise ValidationError(
					message='ENTER A VALID NAME',
					cursor_position=len(str(document))
					)
			else:
				query="SELECT Name FROM RECEPTIONIST WHERE Name= %s"
				cursor.execute(query,(document.text,))
				ok=cursor.fetchall()
				if not ok:
					raise ValidationError(
					message="Account DOESN'T EXISTS !! ",
					cursor_position=len(str(document))
					)



	class AdminpassValidator(Validator):
		def validate(self,document):
			pattern=r'\d{13}$'	
			ok=re.match(pattern,document.text)
			if not ok:
				raise ValidationError(
				message="ENTER A VALID PASSWORD ",
				cursor_position=len(str(document))
				)
			else:
				query="SELECT CNIC from ADMINISTRATOR WHERE CNIC = %s"
				cursor.execute(query,(document.text,))
				ok=cursor.fetchall()
				
				if not ok:
					raise ValidationError(
					message="NO ADMIN ACCOUNT WITH THESE CREDENTIALS",
					cursor_position=len(str(document))
					)
	class ReceppassValidator(Validator):
		def validate(self,document):
			pattern=r'\d{13}$'
			ok=re.match(pattern,document.text)
			if not ok:
				raise ValidationError(
				message="ENTER A VALID PASSWORD ",
				cursor_position=len(str(document))
				)
			else:
				query="SELECT CNIC from RECEPTIONIST WHERE CNIC = %s"
				cursor.execute(query,(document.text,))
				ok=cursor.fetchall()
				
				if not ok:
					raise ValidationError(
					message="NO RECEPTIONIST ACCOUNT WITH THESE CREDENTIALS",
					cursor_position=len(str(document))
					)
	class NameValidator(Validator):
		def validate(self,document):
			pattern=r'\w{3}-\d{3}$'
			ok=re.match(pattern,document.text)
			if not ok:
				raise ValidationError(
				message='ENTER A VALID PLANE NAME',
				cursor_position=len(str(document))
				)
			else:
				query="SELECT * FROM PLANE WHERE Plane_Name = %s"
				cursor.execute(query,(document.text,))
				ok=cursor.fetchall()
				if not ok:
					query="INSERT INTO PLANE (Plane_Name) VALUES (%s)"
					cursor.execute(query,(document.text,))
					mydb.commit()
	class CityValidator(Validator):
		def validate(self,document):
			pattern=r'[a-zA-Z]{3}$'
			ok=re.match(pattern,document.text)
			
			if not ok:
				raise ValidationError(
				message='ENTER A VALID CITY NAME',
				cursor_position=len(str(document))
				)
	class DateValidator(Validator):
		def validate(self,document):
			pattern=r'[0-9]{4}-[0-9]{2}-[0-9]{2}$'
			ok=re.match(pattern,document.text)
			
			if not ok:
				raise ValidationError(
				message='ENTER A VALID DATE ',
				cursor_position=len(str(document))
				)
	class TimeValidator(Validator):
		def validate(self,document):
			pattern=r'[0-9]{2}:[0-9]{2}:[0-9]{2}$'
			ok=re.match(pattern,document.text)
			
			if not ok:
				raise ValidationError(
				message='ENTER A VALID TIME',
				cursor_position=len(str(document))
				)

	class PriceValidator(Validator):
		def validate(self,document):
			pattern=r'[0-9]+$'
			ok=re.match(pattern,document.text)
			
			if not ok:
				raise ValidationError(
				message='ENTER A VALID PRICE',
				cursor_position=len(str(document))
				)
	class DeleteValidator(Validator):
		def validate(self,document):
			pattern=r'\d'
			ok=re.match(pattern,document.text)
			if not ok:
				raise ValidationError(
				message="ENTER VALID FLIGHT ID",
				cursor_position=len(str(document))
				)
			query="SELECT * FROM FLIGHTS WHERE Flight_ID= %s"
			cursor.execute(query,(document.text,))
			ok=cursor.fetchall()
			if not ok:
				raise ValidationError(
				message="ENTER VALID FLIGHT ID",
				cursor_position=len(str(document))
				)
	class DeleteIDValidator(Validator):
		def validate(self,document):
			pattern=r'\d'
			ok=re.match(pattern,document.text)
			if not ok:
				raise ValidationError(
				message="ENTER VALID PASSENGER ID",
				cursor_position=len(str(document))
				)
			query="SELECT * FROM PASSENGER WHERE Pass_ID= %s"
			cursor.execute(query,(document.text,))
			ok=cursor.fetchall()
			if not ok:
				raise ValidationError(
				message="ENTER VALID PASSENGER ID",
				cursor_position=len(str(document))
				)


	class PnameValidator(Validator):
		def validate(self,document):
			pattern=r'^\w+$'
			ok=re.match(pattern,document.text)
			if not ok:
				raise ValidationError(
				message="ENTER VALID NAME",
				cursor_position=len(str(document))

				)
	class CNICValidator(Validator):
		def validate(self,document):
			pattern=r'^[0-9]{13}$'
			ok=re.match(pattern,document.text)
			if not ok:
				raise ValidationError(
				message="ENTER VALID CNIC",
				cursor_position=len(str(document))
				)
			
			query="SELECT * from PASSENGER WHERE Pass_CNIC = %s"
			cursor.execute(query,(document.text,))
			ok=cursor.fetchall()
			if ok:
				raise ValidationError(
				message="PASSENGER WITH CNIC ALREADY EXISTS",
				cursor_position=len(str(document))
				)
	class NationValidator(Validator):
		def validate(self,document):
			pattern=r'^[a-zA-z]+$'
			ok=re.match(pattern,document.text)
			if not ok:
				raise ValidationError(
				message="ENTER VALID NATIONALITY",
				cursor_position=len(str(document))
				)
	class PhoneValidator(Validator):
		def validate(self,document):
			pattern=r'^[0-9]{11}$'
			ok=re.match(pattern,document.text)
			if not ok:
				raise ValidationError(
				message="ENTER VALID NATIONALITY",
				cursor_position=len(str(document))
				)



	def admin_menu():
		menu={

			'type':'list',
			'name':'admin_menu',
			'message':"CHOOSE AN OPTION !",
			'choices':[
				'ADD A NEW FLIGHT RECORD ',
				Separator(),
				'UPDATE FLIGHT DETAILS ',
				Separator(),
				'CANCEL A FLIGHT',
				Separator(),
				'VIEW FLIGHTS FOR A CITY',
				Separator(),
				'VIEW TABLES '
			]

		},
		x=prompt(menu,style=custom_style_2)
		return x
	def recep_menu():
		menu={
			'type':'list',
			'name':'recep_menu',
			'message':"CHOOSE AN OPTION !",
			'choices':[
				'ADD A NEW PASSENGER',
				Separator(),
				'UPDATE PASSENGER DETAILS',
				Separator(),
				'VIEW AVAILABLE FLIGHTS IN A TIME PERIOD',
				Separator(),
				'GENERATE TICKET RECORD FOR A PARTICULAR PASSENGER AND FLIGHT',
				Separator(),
				'VIEW CHEAPEST FLIGHTS',
				Separator(),
				'VIEW PASSENGER HISTORY',
				Separator(),
				'CANCEL A PARTICULAR RECORD'
			]
		}
		x=prompt(menu,style=custom_style_2)
		return x
	
	def add_flight():
		details=[
		{
			'type':'input',
			'name':'plane_name',
			'message':'PLANE NAME ',
			'validate': NameValidator,
			
		},
		{
			'type':'input',
			'name':'dep_city',
			'message':'DEPARTURE CITY ',
			'validate': CityValidator,
			
		},
		{
			'type':'input',
			'name':'arr_city',
			'message':'Arrival CITY ',
			'validate': CityValidator,
			
		},
		{
			'type' : 'input',
			'name' : 'date',
			'message': 'FLIGHT DATE ',
			'validate': DateValidator,
			

		},
		{
			'type':'input',
			'name':'dep_time',
			'message':'DEPARTURE TIME',
			'validate':TimeValidator,
			
		},
		{
			'type':'input',
			'name':'arr_time',
			'message':'ARRIVAL TIME',	
			'validate': TimeValidator,
			
		},
		{
			'type':'input',
			'name':'price',
			'message':'PRICE',
			'validate':PriceValidator,
			
		}
		]
		x=prompt(details,style=custom_style_2)
		return x
	def view_flight():
		choice={
			'type':'input',
			'name':'city',
			'message':'ENTER CITY ',
			'validate': CityValidator,
		}
		x=prompt(choice,style=custom_style_2)
		return x
	
	def add_passenger():
		choice=[
			{'type':'input',
			'name':'pass_name',
			'message':'ENTER Name ',
			'validate': PnameValidator,
			},
			{
			'type':'input',
			'name':'CNIC',
			'message':'ENTER CNIC ',
			'validate': CNICValidator,
			},
			{
			'type':'input',
			'name':'nation',
			'message':'ENTER NATIONALITY ',
			'validate': NationValidator,
			},
			{
			'type':'input',
			'name':'address',
			'message':'ENTER ADDRESS ',
			
			},
			{
			'type':'input',
			'name':'phone',
			'message':'ENTER PHONE NO ',
			'validate': PhoneValidator,
			}

		]
		x=prompt(choice,style=custom_style_2)
		return x

	def pass_updater(choices):
		for i in choices['fields']:
			if 'NAME' == i:
				choice={
				'type':'input',
				'name':'pass_name',
				'message':'ENTER Name ',
				'validate': PnameValidator,
				}
				x=prompt(choice,style=custom_style_2)
				query="UPDATE PASSENGER SET Name = %s WHERE Pass_ID = %s "
				cursor.execute(query,(x['pass_name'],choices['id']))
				mydb.commit()
			if 'CNIC' == i:
				choice={
					'type':'input',
					'name':'CNIC',
					'message':'ENTER CNIC ',
					'validate': CNICValidator,
					}
				x=prompt(choice,style=custom_style_2)
				query="UPDATE PASSENGER SET Pass_CNIC = %s WHERE Pass_ID = %s "
				cursor.execute(query,(x['CNIC'],choices['id']))
				mydb.commit()
			if "ADDRESS" == i:
				choice={
					'type':'input',
					'name':'address',
					'message':'ENTER ADDRESS ',
					}
				x=prompt(choice,style=custom_style_2)
				query="UPDATE PASSENGER SET Address = %s WHERE Pass_ID = %s "
				cursor.execute(query,(x['address'],choices['id']))
				mydb.commit()
			if "NATIONALITY" == i:
				choice={
					'type':'input',
					'name':'nation',
					'message':'ENTER NATIONALITY ',
					'validate': NationValidator,
				}
				x=prompt(choice,style=custom_style_2)
				query="UPDATE PASSENGER SET Nationality = %s WHERE Pass_ID = %s "
				cursor.execute(query,(x['nation'],choices['id']))
				mydb.commit()
			if "Phone" == i:
				choice={
					'type':'input',
					'name':'phone',
					'message':'ENTER PHONE NO ',
					'validate': PhoneValidator,
				}
				x=prompt(choice,style=custom_style_2)
				query="UPDATE PASSENGER SET Phone_no = %s WHERE Pass_ID = %s "
				cursor.execute(query,(x['phone'],choices['id']))
				mydb.commit()

	def update_flight():
		choice =[
				{
				'type':'input',
				'name':'id',
				'message':'ENTER FLIGHT ID ',
				'validate':DeleteValidator,
				},
				{
				'type':'checkbox',
				'name':'fields',
				'message': 'CHOOSE FIELDS TO UPDATE',
				'choices':[
					{'name':'PLANE NAME'},
					Separator(),
					{'name':'DEPARTURE CITY'},
					Separator(),
					{'name':'ARRIVAL CITY'},
					Separator(),
					{'name':'FLIGHT DATE'},
					Separator(),
					{'name':'DEPARTURE TIME'},
					Separator(),
					{'name':'ARRIVAL TIME'},
					Separator(),
					{'name':'PRICE'}
				]
			}
		]
		
		x=prompt(choice,style=custom_style_2)
		return x
	
	questions= [
		{
			'type': 'list',
			'name': 'login',
			'message': 'CHOOSE AN OPTION !! ',
			'choices': [
				'LOGIN AS ADMIN',
				Separator(),
				'LOGIN AS RECEPTIONIST',
				Separator(),
				'EXIT'

			]
		},
			
		{
					'type':'input',
					'name':'admin_name',
					'message':'ENTER Name',
					'validate': AdminidValidator,
					'when'   : lambda ans: (ans['login']=='LOGIN AS ADMIN')

		},
		{
					'type':'password',
					'name':'admin_pass',
					'message':'ENTER PASS',
					'validate': AdminpassValidator,
					'when'   :lambda ans: (ans['login']=='LOGIN AS ADMIN') 


		},
		{
					'type':'input',
					'name':'recep_name',
					'message':'ENTER Name',
					'validate': RecepidValidator,
					'when'   : lambda ans: (ans['login']=='LOGIN AS RECEPTIONIST')

		},
		{
					'type':'password',
					'name':'recep_pass',
					'message':'ENTER PASS',
					'validate': ReceppassValidator,
					'when'   :lambda ans: (ans['login']=='LOGIN AS RECEPTIONIST') 


		},
	]
	def deleter():
		question={
			'type':'input',
			'name':'id',
			'message':'ENTER FLIGHT ID TO DELETE',
			'validate':DeleteValidator
			
		}
		x=prompt(question,style=custom_style_2)
		return x
	
	def updater(fields):
		for i in fields["fields"]:
			if "PLANE NAME" == i:
				question={
						
				'type':'input',
				'name':'plane_name',
				'message':'PLANE NAME ',
				'validate': NameValidator,
				}
				x=prompt(question,style=custom_style_2)
				query="UPDATE FLIGHTS SET Plane_Name = %s WHERE Flight_ID = %s"
				cursor.execute(query,(x['plane_name'],fields['id']))
				mydb.commit()

			if "DEPARTURE CITY" == i:
				question={
				'type':'input',
				'name':'dep_city',
				'message':'DEPARTURE CITY ',
				'validate': CityValidator,
				}
				x=prompt(question,style=custom_style_2)
				query="UPDATE FLIGHTS SET Departure_City = %s WHERE Flight_ID = %s"
				cursor.execute(query,(x['dep_city'],fields['id']))
				mydb.commit()
			if "ARRIVAL CITY" == i:
				question={
				'type':'input',
				'name':'arr_city',
				'message':'ARRIVAL CITY ',
				'validate': CityValidator,
				}
				x=prompt(question,style=custom_style_2)
				query="UPDATE FLIGHTS SET Arrival_City = %s WHERE Flight_ID = %s"
				cursor.execute(query,(x['arr_city'],fields['id']))
				mydb.commit()
			if "FLIGHT DATE" == i:
				question={
					'type' : 'input',
					'name' : 'date',
					'message': 'FLIGHT DATE ',
					'validate': DateValidator,
					}
				x=prompt(question,style=custom_style_2)
				query="UPDATE FLIGHTS SET Flight_date = %s WHERE Flight_ID = %s"
				cursor.execute(query,(x['date'],fields['id']))
				mydb.commit()
			if "DEPARTURE TIME" == i:
				question={
				'type':'input',
				'name':'dep_time',
				'message':'DEPARTURE TIME',
				'validate':TimeValidator,
				}
				x=prompt(question,style=custom_style_2)
				query="UPDATE FLIGHTS SET Departure_time = %s WHERE Flight_ID = %s"
				cursor.execute(query,(x['dep_time'],fields['id']))
				mydb.commit()
			if "ARRIVAL TIME" == i:
				question={
				'type':'input',
				'name':'arr_time',
				'message':'ARRIVAL TIME',
				'validate':TimeValidator,
				}
				x=prompt(question,style=custom_style_2)
				query="UPDATE FLIGHTS SET Arrival_time = %s WHERE Flight_ID = %s"
				cursor.execute(query,(x['arr_time'],fields['id']))
				mydb.commit()
			if "PRICE" == i:
				question={'type':'input',
				'name':'price',
				'message':'PRICE',
				'validate':PriceValidator,
				}
				x=prompt(question,style=custom_style_2)
				query="UPDATE FLIGHTS SET Price = %s WHERE Flight_ID = %s"
				cursor.execute(query,(x['price'],fields['id']))
				mydb.commit()
	def update_passenger():
		choice =[
				{
				'type':'input',
				'name':'id',
				'message':'ENTER PASSENGER ID ',
				'validate':DeleteIDValidator,
				},
				{
				'type':'checkbox',
				'name':'fields',
				'message': 'CHOOSE FIELDS TO UPDATE',
				'choices':[
					{'name':'NAME'},
					Separator(),
					{'name':'CNIC'},
					Separator(),
					{'name':'ADDRESS'},
					Separator(),
					{'name':'NATIONALITY'},
					Separator(),
					{'name':'Phone'},
					
				]
			}
		]
		
		x=prompt(choice,style=custom_style_2)
		return x
	def time_choices():
		questions=[
			{
			'type':'input',
			'name':'dep_city',
			'message':'DEPARTURE CITY ',
			'validate': CityValidator,
			},
			{
			'type':'input',
			'name':'arr_city',
			'message':'ARRIVAL CITY ',
			'validate': CityValidator,
			},
			{
			'type' : 'input',
			'name' : 'date',
			'message': 'FLIGHT DATE ',
			'validate': DateValidator,
			},
			{
			'type':'input',
			'name':'dep_time',
			'message':'DEPARTURE TIME',
			'validate':TimeValidator,
			},
			{
			'type':'input',
			'name':'arr_time',
			'message':'ARRIVAL TIME',	
			'validate': TimeValidator,	
			},
			]
		x=prompt(questions,style=custom_style_2)
		return x;

	login_options=prompt(questions,style=custom_style_2)
	
	if "ADMIN" in login_options['login']:
		print('WELCOME <{}>'.format(login_options['admin_name']))
		while True:
			menu=admin_menu()
			if 'NEW FLIGHT' in menu['admin_menu']:
				details=add_flight()
				add_query="INSERT INTO FLIGHTS (Plane_Name,Departure_City,Arrival_City,Flight_date,Departure_time,Arrival_time,Price) VALUES (%s,%s,%s,%s,%s,%s,%s)"
				f_data=(details['plane_name'],details['dep_city'],details['arr_city'],details['date'],details['dep_time'],details['arr_time'],details['price']) 
				cursor.execute(add_query,f_data)
				mydb.commit()
				print("ALL DONE ")

			elif 'UPDATE' in menu['admin_menu']:
				cursor.execute("SELECT * FROM FLIGHTS")
				table=[]
				y=cursor.fetchall()
				for i in y:
					ans1=[]
					for k in i:
						ans1.append(k)
					table.append(ans1)
				headers=["FLIGHT_ID","DEPARTURE_CITY","ARRIVAL_CITY","DEPARTURE TIME","ARRIVAL_TIME","PRICE","PLANE_NAME","FLIGHT_DATE"]
				print(tabulate(table,headers,tablefmt="grid"))
				fields=update_flight()
				pprint(fields["fields"])
				updater(fields)
				print("ALL DONE ")

			elif 'CANCEL' in menu['admin_menu']:
				cursor.execute("SELECT * FROM FLIGHTS")
				table=[]
				y=cursor.fetchall()
				for i in y:
					ans1=[]
					for k in i:
						ans1.append(k)
					table.append(ans1)
				headers=["FLIGHT_ID","DEPARTURE_CITY","ARRIVAL_CITY","DEPARTURE TIME","ARRIVAL_TIME","PRICE","PLANE_NAME","FLIGHT_DATE"]
				print(tabulate(table,headers,tablefmt="grid"))
				x=deleter()
				query="DELETE FROM FLIGHTS WHERE Flight_ID= %s"
				cursor.execute(query,(x['id'],))
				mydb.commit()
				print("ALL DONE ")
			
			elif 'VIEW FLIGHTS' in menu["admin_menu"]:
				x=view_flight()
				query="SELECT * FROM FLIGHTS WHERE Departure_City = %s OR Arrival_City= %s"
				cursor.execute(query,(x['city'],x['city']))
				y=cursor.fetchall()
				table=[]
				for i in y:
					ans1=[]
					for k in i:
						ans1.append(k)
					table.append(ans1)
				headers=["FLIGHT_ID","DEPARTURE_CITY","ARRIVAL_CITY","DEPARTURE TIME","ARRIVAL_TIME","PRICE","PLANE_NAME","FLIGHT_DATE"]
				print(tabulate(table,headers,tablefmt="grid"))
			
			elif 'VIEW TABLES':
				query="SELECT * FROM ADMINISTRATOR"
				cursor.execute(query)
				y=cursor.fetchall()
				table=[]
				for i in y:
					ans1=[]
					for k in i:
						ans1.append(k)
					table.append(ans1)
				headers=["ADMIN_ID","NAME","CNIC","PHONE_NO"]
				print(tabulate(table,headers,tablefmt="grid"))
				query="SELECT * FROM RECEPTIONIST"
				cursor.execute(query)
				y=cursor.fetchall()
				table=[]
				for i in y:
					ans1=[]
					for k in i:
						ans1.append(k)
					table.append(ans1)
				headers=["RECEPTIONIST_ID","CNIC","NAME","PHONE_NO"]
				print(tabulate(table,headers,tablefmt="grid"))

				query="SELECT * FROM PLANE"
				cursor.execute(query)
				y=cursor.fetchall()
				table=[]
				for i in y:
					ans1=[]
					for k in i:
						ans1.append(k)
					table.append(ans1)
				headers=["PLANE_NAME"]
				print(tabulate(table,headers,tablefmt="grid"))
				query="SELECT * FROM FLIGHTS"
				cursor.execute(query)
				y=cursor.fetchall()
				table=[]
				for i in y:
					ans1=[]
					for k in i:
						ans1.append(k)
					table.append(ans1)
				headers=["FLIGHT_ID","DEPARTURE_CITY","ARRIVAL_CITY","DEPARTURE TIME","ARRIVAL_TIME","PRICE","PLANE_NAME","FLIGHT_DATE"]
				print(tabulate(table,headers,tablefmt="grid"))
				query="SELECT * FROM PASSENGER"
				cursor.execute(query)
				y=cursor.fetchall()
				table=[]
				for i in y:
					ans1=[]
					for k in i:
						ans1.append(k)
					table.append(ans1)
				headers=["PASSENGER_ID","PASSENGER_CNIC","NAME","NATIONALITY","ADDRESS","PHONE_NO"]
				print(tabulate(table,headers,tablefmt="grid"))
	if 'RECEPTIONIST' in login_options['login']:
		print('WELCOME <{}>'.format(login_options['recep_name']))
		while True:
			menu=recep_menu()
			if 'ADD A NEW PASSENGER' in menu['recep_menu']:
				details=add_passenger()
				query ="INSERT INTO PASSENGER (Name,Pass_CNIC,Nationality,Address,Phone_no) VALUES(%s,%s,%s,%s,%s)"
				data=(details['pass_name'],details['CNIC'],details['nation'],details['address'],details['phone'])
				cursor.execute(query,data)
				mydb.commit()
				print("ALL DONE ")

			if 'UPDATE PASSENGER DETAILS' in menu['recep_menu']:
				cursor.execute("SELECT * FROM PASSENGER")
				table=[]
				y=cursor.fetchall()
				for i in y:
					ans1=[]
					for k in i:
						ans1.append(k)
					table.append(ans1)
				headers=["PASS_ID","PASS_CNIC","NAME","NATIONALITY","ADDRESS","PHONE_NO"]
				print(tabulate(table,headers,tablefmt="grid"))
				choices=update_passenger()
				pass_updater(choices)
				print("ALL DONE ")
			if 'VIEW AVAILABLE FLIGHTS IN A TIME PERIOD' in menu['recep_menu']:
				query="SELECT * FROM FLIGHTS"
				cursor.execute(query)
				y=cursor.fetchall()
				table=[]
				for i in y:
					ans1=[]
					for k in i:
						ans1.append(k)
					table.append(ans1)
				headers=["FLIGHT_ID","DEPARTURE_CITY","ARRIVAL_CITY","DEPARTURE TIME","ARRIVAL_TIME","PRICE","PLANE_NAME","FLIGHT_DATE"]
				print(tabulate(table,headers,tablefmt="grid"))
				x=time_choices()
				query="SELECT * FROM FLIGHTS WHERE Departure_City = %s AND Arrival_City = %s AND Flight_date = %s AND Departure_time = %s AND Arrival_time= %s"
				data=(x['dep_city'],x['arr_city'],x['date'],x['dep_time'],x['arr_time'])
				cursor.execute(query,data)
				y=cursor.fetchall()
				table=[]
				for i in y:
					ans1=[]
					for k in i:
						ans1.append(k)
					table.append(ans1)
				headers=["FLIGHT_ID","DEPARTURE_CITY","ARRIVAL_CITY","DEPARTURE TIME","ARRIVAL_TIME","PRICE","PLANE_NAME","FLIGHT_DATE"]
				print(tabulate(table,headers,tablefmt="grid"))
			if 'GENERATE TICKET' in menu['recep_menu']:
				query="SELECT * FROM FLIGHTS"
				cursor.execute(query)
				y=cursor.fetchall()
				table=[]
				for i in y:
					ans1=[]
					for k in i:
						ans1.append(k)
					table.append(ans1)
				headers=["FLIGHT_ID","DEPARTURE_CITY","ARRIVAL_CITY","DEPARTURE TIME","ARRIVAL_TIME","PRICE","PLANE_NAME","FLIGHT_DATE"]
				print(tabulate(table,headers,tablefmt="grid"))
				query="SELECT * FROM PASSENGER"
				cursor.execute(query)
				y=cursor.fetchall()
				table=[]
				for i in y:
					ans1=[]
					for k in i:
						ans1.append(k)
					table.append(ans1)
				headers=["PASSENGER_ID","PASSENGER_CNIC","NAME","NATIONALITY","ADDRESS","PHONE_NO"]
				print(tabulate(table,headers,tablefmt="grid"))
				questions=[{
				'type':'input',
				'name':'flight_id',
				'message':'ENTER FLIGHT ID ',
				'validate':DeleteValidator,
				},
				{
				'type':'input',
				'name':'pass_id',
				'message':'ENTER PASSENGER ID ',
				'validate':DeleteIDValidator,
				}
				]
				x=prompt(questions,style=custom_style_2)
				query="INSERT INTO HISTORY (Flight_id,Pass_id) VALUES (%s,%s)"
				data=(x['flight_id'],x['pass_id'])
				cursor.execute(query,data)
				mydb.commit()
				query="SELECT * FROM HISTORY"
				cursor.execute(query)
				y=cursor.fetchall()
				table=[]
				for i in y:
					ans1=[]
					for k in i:
						ans1.append(k)
					table.append(ans1)
				headers=["NO","Flight_ID","PASSENGER_ID"]
				print(tabulate(table,headers,tablefmt="grid"))

			if 'VIEW CHEAPEST' in menu['recep_menu']:
				query="SELECT * FROM FLIGHTS"
				cursor.execute(query)
				y=cursor.fetchall()
				table=[]
				for i in y:
					ans1=[]
					for k in i:
						ans1.append(k)
					table.append(ans1)
				headers=["FLIGHT_ID","DEPARTURE_CITY","ARRIVAL_CITY","DEPARTURE TIME","ARRIVAL_TIME","PRICE","PLANE_NAME","FLIGHT_DATE"]
				print(tabulate(table,headers,tablefmt="grid"))
				questions=[{
					'type':'input',
					'name':'dep_city',
					'message':'DEPARTURE CITY ',
					'validate': CityValidator,
					},
					{
					'type':'input',
					'name':'arr_city',
					'message':'ARRIVAl CITY ',
					'validate': CityValidator,
					}]
				x=prompt(questions,style=custom_style_2)
				query="SELECT Price FROM FLIGHTS WHERE Departure_City= %s AND Arrival_City = %s "
				cursor.execute(query,(x['dep_city'],x['arr_city']))
				arr=[]
				y=cursor.fetchall()
				for i in y:
					j,=i
					arr.append(j)
				mini=min(arr)
				query="SELECT * FROM FLIGHTS WHERE Price = %s"
				cursor.execute(query,(mini,))
				y=cursor.fetchall()
				table=[]
				for i in y:
					ans1=[]
					for k in i:
						ans1.append(k)
					table.append(ans1)
				headers=["FLIGHT_ID","DEPARTURE_CITY","ARRIVAL_CITY","DEPARTURE TIME","ARRIVAL_TIME","PRICE","PLANE_NAME","FLIGHT_DATE"]
				print(tabulate(table,headers,tablefmt="grid"))
			if 'VIEW PASSENGER HISTORY' in menu['recep_menu']:
				question={
				'type':'input',
				'name':'pass_id',
				'message':'ENTER PASSENGER ID ',
				'validate':DeleteIDValidator,
				}
				x=prompt(question,style=custom_style_2)
				query="SELECT Flight_id FROM HISTORY WHERE Pass_id = %s "
				cursor.execute(query,(x['pass_id'],))
				y=cursor.fetchall()
				table=[]
				for i in y:
					j,=i
					query="SELECT * FROM FLIGHTS WHERE Flight_ID = %s"
					cursor.execute(query,(j,))
					k=cursor.fetchall()
					for l in k:
						ans1=[]
						for u in k:
							ans1.append(u)
						table.append(ans1)
				headers=["FLIGHT_ID","DEPARTURE_CITY","ARRIVAL_CITY","DEPARTURE TIME","ARRIVAL_TIME","PRICE","PLANE_NAME","FLIGHT_DATE"]
				print(tabulate(table,headers,tablefmt="grid"))

			if 'CANCEL A PARTICULAR RECORD' in menu['recep_menu']:
				query="SELECT * FROM FLIGHTS"
				cursor.execute(query)
				y=cursor.fetchall()
				table=[]
				for i in y:
					ans1=[]
					for k in i:
						ans1.append(k)
					table.append(ans1)
				headers=["FLIGHT_ID","DEPARTURE_CITY","ARRIVAL_CITY","DEPARTURE TIME","ARRIVAL_TIME","PRICE","PLANE_NAME","FLIGHT_DATE"]
				print(tabulate(table,headers,tablefmt="grid"))
				query="SELECT * FROM PASSENGER"
				cursor.execute(query)
				y=cursor.fetchall()
				table=[]
				for i in y:
					ans1=[]
					for k in i:
						ans1.append(k)
					table.append(ans1)
				headers=["PASSENGER_ID","PASSENGER_CNIC","NAME","NATIONALITY","ADDRESS","PHONE_NO"]
				print(tabulate(table,headers,tablefmt="grid"))
				query="SELECT * FROM HISTORY"
				cursor.execute(query)
				y=cursor.fetchall()
				table=[]
				for i in y:
					ans1=[]
					for k in i:
						ans1.append(k)
					table.append(ans1)
				headers=["NO","Flight_ID","PASSENGER_ID"]
				print(tabulate(table,headers,tablefmt="grid"))
				questions=[{
				'type':'input',
				'name':'flight_id',
				'message':'ENTER FLIGHT ID ',
				'validate':DeleteValidator,
				},
				{
				'type':'input',
				'name':'pass_id',
				'message':'ENTER PASSENGER ID ',
				'validate':DeleteIDValidator,
				}
				]
				x=prompt(questions,style=custom_style_2)
				query="DELETE FROM HISTORY WHERE Flight_id = %s AND Pass_id = %s"
				cursor.execute(query,(x['flight_id'],x['pass_id']))
				mydb.commit()
				query="SELECT * FROM HISTORY"
				cursor.execute(query)
				y=cursor.fetchall()
				table=[]
				for i in y:
					ans1=[]
					for k in i:
						ans1.append(k)
					table.append(ans1)
				headers=["NO","Flight_ID","PASSENGER_ID"]
				print(tabulate(table,headers,tablefmt="grid"))


				
				

			




				

				





			

				


			



				



		

			
				













				
					
				




	
				
	
	
	


