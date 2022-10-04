from datetime import date
class Date:
	def __init__(self,month=0,day=0,year=0):
		if month==0:
			month=int(str(date.today()).split('-')[1])
		if day==0:
			day=int(str(date.today()).split('-')[2])
		if year==0:
			year=int(str(date.today()).split('-')[0])
		self._julianDay=0
		assert self._isValidGregorian(month,day,year),"Invalid Gregorian Date."
		tmp=0
		if month<3:
			tmp=-1
		self._julianDay=day-32075+(1461*(year+4800+tmp)//4)+(367*(month-2-tmp*12)//12)-(3*((year+4900+tmp)//100)//4)
	def month(self):
		return (self._toGregorian())[0]
	def day(self):
		return (self._toGregorian())[1]
	def year(self):
		return (self._toGregorian())[2]
	def dayOfWeek(self):
		month,day,year=self._toGregorian()
		if month<3:
			month=month+12
			year=year-1
		return ((13*month+3)//5+day+year+year//4-year//100+year//400)%7
	def __str__(self):
		month,day,year=self._toGregorian()
		return "%02d/%02d/%04d"%(month,day,year)
	def __eq__(self,otherDate):
		return self._julianDay==otherDate._julianDay
	def __lt__(self,otherDate):
		return self._julianDay<otherDate._julianDay
	def __le__(self,otherDate):
		return self._julianDay<=otherDate._julianDay
	def monthName(self):
		months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
		k = self.month()
		return months[k-1]
	def isLeapYear(self,y=0):
		if y==0:
			year = self.year()
		else:
			year = y
		if year%100==0:
			if year%400==0:
				return True
		else:
			if year%4==0:
				return True
		return False
	def numDays(self):
		days = [31,[28,29],31,30,31,30,31,31,30,31,30,31]
		if self.month()==2:
			j = days[1]
			if self.isLeapYear():
				return j[1]
			else:
				return j[0]
		else:
			k = self.month()
			return days[k-1]
	def advanceBy(self,days):
		self._julianDay += days
		return
	def _isValidGregorian(self,month,day,year):
		thirty = [1,3,5,7,8,10,12]
		thirty1 = [4,6,9,11]
		if month<1 or month>12:
			return False
		if month in thirty:
			if day>30 or day<1:
				return False
		elif month in thirty1:
			if day>31 or day<1:
				return False
		else:
			if not self.isLeapYear(year):
				if day>28:
					return False
			else:
				if day>29:
					return False
		return True
	def dayOfWeekName(self):
		days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
		return days[self.dayOfWeek()]
	def dayOfYear(self):
		days = [31,[28,29],31,30,31,30,31,31,30,31,30,31]
		Days = self.day()
		for i in range(1,self.month()):
			if i==2:
				k = days[1]
				if self.isLeapYear():
					Days += k[1]
				else:
					Days += k[0]
			else:
				Days += days[i-1]
		return Days
	def isWeekDay(self):
		if self.dayOfWeek() in range(0,5):
			return True
		else:
			return False
	def isEquinox(self):
		if self.month==3:
			if self.day==20:
				return True
		if self.month==9:
			if self.day==22:
				return True
		return False
	def isSolstice(self):
		if self.month()==6 or self.month()==12:
			if self.day()==21:
				return True
		return False
	def asGregorian(self,divchar='/'):
		month,day,year=self._toGregorian()
		return "%02d%c%02d%c%04d"%(month,divchar,day,divchar,year)
	def printCalender(self):
		d = Date(self.month(),1,self.year())
		td = d.numDays()
		title = "%7s %04d"%(d.monthName(),d.year())
		print(title.center(20," "))
		print("Su Mo Tu We Th Fr Sa")
		i = d.dayOfWeek()
		if d.dayOfWeek()!=6:
			while i>=0:
				print("  ",end=" ")
				i -= 1
		while td>0:
			print("%02d"%(d.day()),end=" ")
			d.advanceBy(1)
			if d.dayOfWeek() == 6:
				print()
			td -= 1
		print()
		print()

	def _toGregorian(self):
		A=self._julianDay+68569
		B=4*A//146097
		A=A-(146097*B+3)//4
		year=4000*(A+1)//1461001
		A=A-(1461*year//4)+31
		month=80*A//2447
		day=A-(2447*month//80)
		A=month//11
		month=month+2-(12*A)
		year=100*(B-49)+year+A
		return month,day,year


	# def printJulianDays(self):
	# 	start = Date(1,1,2000)
	# 	while start.month()==1:
	# 		print(start._julianDay)
	# 		start.advanceBy(1)
# for i in range(1,13):
# 	d = Date(i,1,2019+i)
# 	d.printCalender(d)
for i in range(1,13):
	w = Date(i,10,2022)
	w.printCalender()