"""
Write a series of custom exceptions to deem whether a player trying out for a softball team should make the cut. 
    Reference agility, sportsmanship, batting, and fielding. Pitchers and catchers will have their own categories. 
    Player profile: 
    Agility: home to first, around the diamond, squat, benchpress
    Sportsmanship: attitude, likeability, team, communication
    Batting: base hit percentage, fly out, can bunt, baserunning
    Fielding: throwing velocity, throwing accuracy, fielding percentage, field awareness 
    Pitching: velocity, number of pitches, consistency, multiple positions, leadership
    Catching: throwdown velocity, throwdown consistency, framing, pop time, multiple positions, leadership
"""

#importing all class declarations as ERR for when exceptions are raised
import softball_tryouts_classes as ERR

#collecting basic recruit info

y = ERR.RecruitInfo()
y.getRecruitName()
print()
y.getRecruitPhone()
print()
y.getRecruitEmail()
print()
y.getRecruitAge()
print()
y.getRecruitGradYear()
print()
y.getRecruitPositions()
print()
y.getRecruitYearsPlayed()
print()
y.getRecruitSchool()
print()
y.getRecruitIntendedTeam()
print()
y.getRecruitIntendedMajor()
print()
y.getRecruitCollegeAthelticInfo()
print()
y.getRecruitIntendedCollege()
print()
y.RecruitInfoConfirmation()
print()
