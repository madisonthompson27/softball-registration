#class document for softball_tryouts_app

#import for determining recruit age elibgility
import datetime

#importing for writing to pdf file
import PyPDF2

#START CLASS DECLARATION FOR AGILITY#

#takes in a total of four values, and if one is below par an error ensues
    #par determined in applcation, this is simply a class declaration
class AgilityBelowPar(Exception):
    def __init__(self):
        super.__init__("One or more agility metrics below par.")

#END#

#START CLASS DECLARATION FOR SPORSTMANSHIP#

#takes in values relating to a coach's judgement of character and outputs if a player in unacceptable
class UnsportsmanlikeConduct(Exception):
    def __init__(self):
        super.__init__("One or more behaviors unacceptable.")

#END#

#START CLASS DECLARATION FOR BATTING#
class BattingBelowPar(Exception):
    def __init__(self):
        super.__init__("One more more batting metrics below par.")

#END#

#START CLASS DECLARATION FOR FIELDING#
class FieldingBelowPar(Exception):
    def __init__(self):
        super.__init__("One more more fielding metrics below par. ")

#END#

#START CLASS DECLARATION FOR PITCHING#
class PitchingBelowPar(Exception):
    def __init__(self):
        super.__init__("One or more pitching metrics below par.")

#END#

#START CLASS DELCARATION FOR CATCHING#
class CatchingBelowPar(Exception):
    def __init__(self):
        super.__init__("One or more catching metrics below par.")

#END#

#START CLASS DECLARTION FOR BASIC RECRUIT INFO ERRORS#

#will be raised if a recruit is too old or too young, not trying out for enough positions, or not trying out for the needed postions
class BasicInfoError(Exception):
    def __init__(self):
        super.__init__("Recruit is ineligable by one or more criteria.")

#END#

#START CLASS DECLARATION FOR BASIC RECRUIT INFO#
class RecruitInfo():
    
    #instanchiating reference variables for the class
    
    #used in getRecruitName()
    name = ""
    
    #used in getRecruitPhone()
    recruitPhone = ""
    
    #used in getRecruitEmail()
    recruitEmail = ""    
    
    #used in getRecruitAge()
    age = 0
    dateOfBirth = ""
    athleticAge = 0
    yearsUntilIneligable = 0
    yearIneligable = 0
    
    #used in getRecruitGradYear()
    gradYear = 0

    #used in getRecruitPositions()
    position1 = ""
    position2 = ""
    position3 = ""
    
    #used in getRecruitYearsPlayed()
    yearsPlayed = 0
    yearsPlayedPrimary = 0
    
    #used in getRecruitSchool()
    recruitSchool = ""

    #used in getRecruitIntendedTeam()
    intendedTeam = ""
    
    #used in getRecruitIntendedMajor()
    intendedMajor = ""
    
    #used in getRecruitCollegeAthleticInfo()
    playInCollege = ""
    
    #used in getRecruitIntendedCollege()
    intendedCollege = ""
    
    #file declarations for coach's view and recruit's view. coach will see more info. 
    pdf = PyPDF2.PdfFileWriter
    
    #file for recruit
    #recruitProfile = open("recruitprofile.pdf", "a")
    #pdf.write(recruitProfile)
    
    #file for coach
    #coachProfile = open("coachProfile.pdf", "w")
    #pdf.write(coachProfile)
    
    #display welcome message for recruit
    def __init__(self):
        print("Welcome Recruit! Please fill out the information below to get registered.")

    #series of modifiers to create recruit profile
    
    #collects and sets the name of the recruit
    def getRecruitName(self):
        
        #while loop to ensure that at least two names are inputted before progressing
        while True:
            self.name = str(input("Recruit first and last name: ")).title()
        
            #in case names were split in a weird way, it ensures that the code does not break  
            try: 
                  
                #attempts to split names by space 
                splitNames = self.name.split(" ")
            
            except Exception: 
                print(f'Invalid input: {self.name}. Be sure to enter at least two names, seperated by a space. Ex: Madison Thompson.')                
                
            #checks to see if splitNames successfully created a list with at least two parameters
            if len(splitNames) >= 2:
                break
            
            else:
                print(f'Invalid input: {self.name}. Be sure to enter a first and last name, seperated by a space.')
            
        return self.name
    
    #collects and sets the phone number of the recruit
    def getRecruitPhone(self):
        
        #uses a while loop to ensure the desired input is achieved
        while True:
            self.recruitPhone = str(input("Enter recruit phone number as 10 digits: "))
            
            #validates that the input is all digits and that it is the correct length
            if len(self.recruitPhone) != 10 or int(self.recruitPhone.isalnum() == False):
                    print(f'Invalid value: {self.recruitPhone}. Pleas try again, in the format 1234567890.')

            #loop will not reach this point until the desired input format is reached
            else:
                
                #formatting recruit phone number
                areaCode = self.recruitPhone[0:3]
                firstThree = self.recruitPhone[3:6]
                lastFour = self.recruitPhone[6:10]
            
                self.recruitPhone = f'({areaCode})-{firstThree}-{lastFour}'
                break
        
        #returns following break of while loop        
        return self.recruitPhone
        
    #retrieving the recruits email
    def getRecruitEmail(self):
        self.recruitEmail = str(input("Enter recruit email: ")).lower() #.lower() for uniformity
        return self.recruitEmail    
    
    #collects and sets the recruits DOB, DOB as of Jan 1, age, grad year, years until ineligable, year ineligable
    def getRecruitAge(self):
        
        #while loop instead of try/except to ensure that message is repeated until desired input is acquired
        while True:
            
            #reading the date of birth of the recruit as a str input (split by -) to determine age and age as of jan 1. 
            self.dateOfBirth = str(input("Enter date of birth as MM-DD-YYYY: "))
            if len(self.dateOfBirth) != 10 or (self.dateOfBirth[2] != "-") or (self.dateOfBirth[5] != "-"):
                print(f'Invalid value: {self.dateOfBirth}. Please try again, in the format MM-DD-YYYY.')
                
            #writing function to output current age and athletic age (for eligibility purposes)
            else:
                splitDateOfBirth = self.dateOfBirth.split("-")
        
                #type conversions must be done to allow for comparison in if statements 
                yearBorn = int(splitDateOfBirth[2])
                dayBorn = int(splitDateOfBirth[1])
                monthBorn = int(splitDateOfBirth[0])
        
                #finding the recruit's current age and athletic age
                todaysDate = datetime.date.today()
        
                #if the month is greater than their birth month, their birthday has passed
                if todaysDate.month > monthBorn:
                    self.age = todaysDate.year - yearBorn
            
                #if birth month == todays month, check to make sure bday is today or has passed
                elif todaysDate.month == monthBorn:
                    if todaysDate.day >= dayBorn:
                        self.age = todaysDate.year - yearBorn
                
                    #if birthday is yet to occur, the age does not increase
                    else:
                        self.age = todaysDate.year - (yearBorn + 1)
        
                #if the birth month has yet to occur, the age does not increase
                else:
                    self.age = todaysDate.year - (yearBorn + 1)
            
                #does not return yet to allow athletic age to be found

                #finding athletic age (for elgibility)
                self.athleticAge = todaysDate.year - yearBorn
        
                #finding the year that an athlete becomes ineligable
                self.yearsUntilIneligable = 19 - self.age
                self.yearIneligable = todaysDate.year + self.yearsUntilIneligable
                
                #making sure to exit while loop
                break
        
        return self.dateOfBirth, self.age, self.athleticAge, self.yearsUntilIneligable, self.yearIneligable, todaysDate.year
        
    #asking for users grad year
    def getRecruitGradYear(self):
            while True: 
                #exception handling to ensure input is proper
                try:
                    self.gradYear = int(input("Enter high school graduation year: "))
                
                    #limits range of grad years to graduated two years ago or in sixth grade
                    if self.gradYear not in range (datetime.date.today().year - 2, datetime.date.today().year + 6):
                        print(f'Please enter the recruit\'s high school graduation year. For example: {datetime.date.today().year}.')
                
                    #else statement only reached if executed properly    
                    else:
                        break
                
                #exception to prevent code breaking, int conversions can be moody
                except Exception:
                    print(f'Please enter a numeric value with no spaces, such as {datetime.date.today().year}.')
                
            #returning value (outside of while loop)
            return self.gradYear
    
    
#testing effective as of 11/9/2022
#x = RecruitInfo()
#y = x.getRecruitName()
#print(y)
#z = x.getRecruitAge()
#print(z)

    #collects top three positions, stores as dict that can be output for coaches. third position optional. 
    #does not need to call itself
    def getRecruitPositions(self):
    
        #allowing the user to enter their prefered positions
        self.position1 = str(input("Enter primary position: ")).title()
        self.position2 = str(input("Enter secondary position: ")).title()
        
        #giving the option to enter a third option, in another while loop to ensure input validation doesn't repeat pos1, pos2
        while True:
            potentialPosition = str(input("Do you have a third position? Enter Y for yes or N for no: ")).upper()

            #input validation
            if potentialPosition != "Y" and potentialPosition != "N":
                print("Please try again, and be sure to only enter Y or N.")
                
            #progression to next portion if input is validated, otherwise it will repeat the prompt    
            elif potentialPosition == "Y":
                self.position3 = str(input("Enter tertiary position: ")).title()
                
                #else statement could be unreachable, so two break calls are needed. 
                break
                
            else:
                self.position3 = "None"
                break
        
        #returns once inputs are validated and loop is broken
        return self.position1, self.position2, self.position3

#testing effective as of 11/9/2022
#x = getRecruitPositions()
#print(x)

    #collects high school or middle school, current school, years played, years played primary position, intended team, intended major
    def getRecruitSchool(self):
    
        #determining recruit elgibility through tiered while loops. 
        while True:

            self.highOrMid = str(input("Are you in high school or middle school? Enter H or M: ")).upper()

            #input validation
            if self.highOrMid != "H" and self.highOrMid != "M":
                print(f'Invalid value: {self.highOrMid}. Be sure to only enter H or M.')
        
            #under else statement, program will execute normally until a value is not correct. will be skipped if caught in if statement.
            elif self.highOrMid == "H":
                self.recruitSchool = str(input("Enter name of high school: "))
                break
            
            else:
                self.recruitSchool = str(input("Enter name of middle school: "))
                break
        
        #reutrning values outside of while loop            
        return self.highOrMid, self.recruitSchool
    
    #finding the number of years that a recruit has played the sport and their primary. secondary while loop until desired input reached. 
    def getRecruitYearsPlayed(self):
        
        while True:
            
            #while loop one determines how long the athlete has played softball    
            while True:
                
                #try except block needed to prevent break in case input is not an int
                try:
                    #since codes would be the exact same and values could be easily confused, they're combined into one function
                    self.yearsPlayed = int(input("Enter number of years played: "))

                except Exception: 
                    #prints error message and then loop will reinterate, secondary validations are yet to occur
                    print(f'Invalid value: {self.yearsPlayed}. Be sure to only enter a number. Ex: 13.')
             
                else:
                    break
            
            #while loop 2 determines how long the athlete has played their primary position
            while True:
                
                #try except block prevents any code breaks due to int classification
                try:
                    self.yearsPlayedPrimary = int(input("Enter number of years you've played your primary position: "))

                except Exception: 
                    #prints error message and then loop will reinterate, secondary validations are yet to occur
                    print(f'Invalid value: {self.yearsPlayed}. Be sure to only enter a number. Ex: 13.')
             
                else:
                    #another layer of validation to ensure that the years played primary aren't greater than
                    if self.yearsPlayedPrimary <= self.yearsPlayed:
                        break
                    
                    else:
                        print("Years played primary cannot exceed years played. Please try again.")
            
            #following loops, secondary validation ensures that values are within a reasonable range   
            if self.yearsPlayed not in range(0, 100):
                print(f'Invalid value: {self.yearsPlayed}. Please try again.')
                    
            elif self.yearsPlayedPrimary not in range(0, 100):
                print(f'Invalid value: {self.yearsPlayedPrimary}. Please try again.')
            
            #prevents return values from executing main until loop has completely iterated        
            else:
                break
        
        #returns correct values after while loop is broken out of     
        return self.yearsPlayed, self.yearsPlayedPrimary
    
    #accepting recruit intended team
    def getRecruitIntendedTeam(self):
        self.intendedTeam = str(input("Enter the name, coach, and age of the team you're trying out for. Ex: NTR McCollum 06: "))
        
        return self.intendedTeam

    #finding academic information
    def getRecruitIntendedMajor(self):
        #finding intended team and intended major
        self.intendedMajor = str(input("Enter your intended major: ")).title()
        
        return self.intendedMajor
    
    #collects info on whether the recruit wishes to play in college and where they are in the recruitment process
    def getRecruitCollegeAthelticInfo(self):
        
        #finding out if recruit is interested in playing in college
        while True: 
            
            self.playInCollege = str(input("Do you intend on playing in college? Type Y for yes and N for no: ")).upper()
            
            if self.playInCollege != "Y" and self.playInCollege != "N":
                print(f'Invalid value: {self.playInCollege}. Be sure to only enter Y or N.')

            else:
                break
            
        return self.playInCollege
    
    def getRecruitIntendedCollege(self):
        
        #initializing local reference variables
        targetSchool = ""
        
        #allowing a user to enter their intended college athletics
        if self.playInCollege == "Y":
            
            #ensures clarity for user when reviewing application in RecruitInfoConfirmation()
            self.playInCollege = "Yes"
                        
            #collecting information to determine stage in recruiting process
            targetSchool = str(input("Do you have an target school, or have you been recruited? Enter Y for yes or N for no: ")).upper()
                        
            #if a school is in mind, further information is collected. 
            if targetSchool == "Y":
                self.intendedCollege = str(input("Enter potential colleges, seperated by commas.\nIndicate interest with an (I), recruitment with an (R), and commitmnet with a (C): ")).title()
            else:
                self.intendedCollege = "Non-athletic"
        else:
            
            #ensures clarity for user when reviewing application in RecruitInfoConfirmation()
            self.playInCollege = "No"
            
        return self.playInCollege, self.intendedCollege
    
    
    #allows the recruit to confirm their information before being fully registered, items in order of global instantchiation 
    def RecruitInfoConfirmation(self):
        print()
        print("Please confirm the following is correct to finish your registration.")
        
        #spacing
        print()
        print()
        print("Basic Information:")
        print(f'1. Name: {self.name}')
        print(f'2. Phone number {self.recruitPhone}')
        print(f'3. Email: {self.recruitEmail}')
        print(f'4. DOB: {self.dateOfBirth}')
        print(f'5. HS graduation year: {self.gradYear}')

        
        #spacing
        print()
        print()
        print("Athletic Information:")
        print(f'6. Primary position: {self.position1}')
        print(f'7. Secondary position: {self.position2}')
        print(f'8. Tertiary position: {self.position3}')
        print(f'9. Years played: {self.yearsPlayed}')
        print(f'10. Years played primary: {self.yearsPlayedPrimary}')
        print(f'11. Current school: {self.recruitSchool}')
        print(f'12. Intended team: {self.intendedTeam}')
        print(f'13. Intended major: {self.intendedMajor}')
        print(f'14. Plans to play in college: {self.playInCollege}')
        
        #only prints if the user has stated they intend to participate in college athletics
        if self.playInCollege == "Yes":
            print(f'15. Target school: {self.intendedCollege}')
        
        
        #while loop to allow the user to edit any incorrect information
        while True:
            infoModification = str(input("Type C to confirm or the number of the incorrect item: "))
            
            #checking to see if loop should break
            if infoModification.upper() == "C": 
                break
            
            #allowing user to edit their selection menu option (since no break occurred)
            if infoModification == "1":
                self.getRecruitName()
            
            #all use the same function (have dependencies)
            elif infoModification == "2":
                self.getRecruitPhone()
            
            elif infoModification == "3":
                self.getRecruitEmail()
                
            elif infoModification == "4":
                self.getRecruitAge()
            
            elif infoModification == "5":
                self.getRecruitGradYear()
            
            #grouped together due to potential repetitive changes that would need to be made for each (like switching primary/secondary)
            elif infoModification == "6" or infoModification == "7" or infoModification == "8":
                self.getRecruitPositions()
            
            #grouped together due to potential repetitive changes (reducing by one year, accidentally flipped them, etc.)    
            elif infoModification == "9" or infoModification == "10":
                self.getRecruitYearsPlayed()
            
            elif infoModification == "11":
                self.getRecruitSchool()
            
            elif infoModification == "12":
                self.getRecruitIntendedTeam()
                
            elif infoModification == "13":
                self.getRecruitIntendedMajor()
                
            elif infoModification == "14":
                self.getRecruitCollegeAthelticInfo()
            
            elif infoModification == "15":
                self.getRecruitIntendedCollege()
            
            #will iterate again until sentinel value obtained    
            else: 
                print("Invalid option")
        
        self.RecruitInfoConfirmation()
        
        #after all values are updated a global pdf will be started for the coach's reference and for the recruit's 
        #self.recruitProfile.write("")
        #FIXME write code to print menu to file
                
    #allows the coach to set parameters for the tryout
    def TryoutParameters(self):
        pass

    #prints a report for coaches to view the recruit's basic info
    def CoachBasicReport(self):
        pass
    
    #prints a final report for the recruit, states pass or fail for all parameters and suggests whether recruit should make team
    def CoachFinalReport(self):
        pass
    
    ##NOTES##
    #FIXME parts of above 3 methods might be better written as the program in softball_tryouts_app, practice importing the class
    #FIXME should the if statements display "previous value: "