class Date:
    @classmethod
    def toHHMMSS(cls,timeTup):
        return "%02d:%02d:%02d"%(timeTup[3],timeTup[4],timeTup[5])