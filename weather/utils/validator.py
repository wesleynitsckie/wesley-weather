import datetime

#Validate the incoming parameters and other data
class Validator:
    
    def isValid(self, data):
        if('location' not in data):
            return False
        if('toDate' not in data):
            return False
        if('fromDate' not in data):
            return False
        return True
    
    def isValidDate(self, datestr):
        try :
            year,month,day = datestr.split('-')
            datetime.datetime(int(year),int(month),int(day))
            return True
        except ValueError  as e:
            print (e)
            return  False
            