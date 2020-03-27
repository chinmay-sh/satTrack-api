from flask import jsonify

class Satellite:
    
    def __init__(self,name,catNum,classification,launchYear,yearlyLaunchNum,inclination,periArg,dailyRevs,totalRevsTillEpoch):
        self.name = name
        self.catalogNum = catNum
        self.classification = classification
        self.launchYear = launchYear
        self.yearlyLaunchNum = yearlyLaunchNum
        self.inclination = inclination
        self.periArg = periArg
        self.dailyRevs = dailyRevs
        self.totalRevsTillEpoch = totalRevsTillEpoch


    def getSatData(self):
        response = {'name':self.name,'catalog_number':self.catalogNum,'classification':self.classification,'launch_year':self.launchYear,
            'launch_number_of_the_year':self.yearlyLaunchNum,'inclination(deg)':self.inclination,'argument_perigee':self.periArg,
            'daily_revolutions':self.dailyRevs,'total_revs_till_epoch':self.totalRevsTillEpoch
        }
        return response
"""
    def getSatDataText(self):
        response = {'name':self.name,'catalog_number':self.catalogNum,'classification':self.classification,'launch_year':self.launchYear,
            'launch_number_of_the_year':self.yearlyLaunchNum,'inclination(deg)':self.inclination,'argument_perigee':self.periArg,
            'daily_revolutions':self.dailyRevs,'total_revs_till_epoch':self.totalRevsTillEpoch
        }
        return response
        """