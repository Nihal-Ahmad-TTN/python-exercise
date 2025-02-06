#importing datetime module
import datetime as dt

#defining the datecount function
def datecount(start, step):
	#ignoring the case by converting into lowercase
	step=step.lower()

	while True:
		yield start
		#applying condition on the step variable
		if step=="daily":
			start+=dt.timedelta(days=1)
		elif step=="alternative":
			start+=dt.timedelta(days=2)
		elif step=="weekly":
			start+=dt.timedelta(days=7)
		elif step=="monthly":
			start+=dt.timedelta(days=30)
		elif step=="quarterly":
			start+=dt.timedelta(days=90)
		elif step=="yearly":
			start+=dt.timedelta(days=365)
		else:
			print("Invalid input")

#main driver code

#taking input from user
step= input("Enter the duration in daily, alternative, weekly, monthly, quarterly, yearly : ")

#initialising the date as current date
start= dt.date.today()

#calling the datecount function
result= datecount(start,step)

#printing output
for dates in range(10):
	print(next(result))
