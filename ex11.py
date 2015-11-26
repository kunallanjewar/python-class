# Student: Kunal Lanjewar
# Programming Ex: 11

class Division(object):
    def __init__(self,dept, fullTime, partTime):
        self.dept=dept
        self.fullTime = fullTime
        self.partTime = partTime
        
    def getList(self):
        print ("The {0} department has {1} full-time and {2} part-time instructors.".format(self.dept, self.fullTime, self.partTime))

class Department(Division):
     pass
       
myDept = Department("CIS",12,27)
myDept.getList()