import sys
import random
#from docx import Document

#document = Document()

if len(sys.argv) < 10:
    print("ERROR: Not enough information. Please provide First Name, Last Name, Gender - f for female, m for male,"
          " Attainment and Behaviour - where 1 is bad, 2 is ok, 3 is good attainment or behaviour.")
    exit()

firstName = sys.argv[1]
gender = sys.argv[2]

religStudyEffort = ""
englishEffort = ""
phonicsEffort = ""
mathsEffort = ""
scienceEffort = ""

if len(sys.argv[6]) == 2:
    maths = int(sys.argv[6][0])
    mathsEffort = int(sys.argv[6][1])
    if mathsEffort < 1 or mathsEffort > 3:
        print("ERROR: Please insert a valid value for Maths Effort - where 1 is bad, 2 is ok, 3 is good Effort.")
        exit()
else:
    maths = int(sys.argv[3][0])

if maths < 1 or maths > 3:
    print("ERROR: Please insert a valid value for Maths Attainment - where 1 is bad, 2 is ok, 3 is good Attainment.")
    exit()
        
if len(sys.argv[4]) == 2:
    english = int(sys.argv[4][0])
    englishEffort = int(sys.argv[4][1])
    if englishEffort < 1 or englishEffort > 3:
        print("ERROR: Please insert a valid value for English Effort - where 1 is bad, 2 is ok, 3 is good Effort.")
        exit()
else:
    english = int(sys.argv[4][0])
    
if english < 1 or english > 3:
    print("ERROR: Please insert a valid value for English Attainment - where 1 is bad, 2 is ok, 3 is good Attainment.")
    exit()
    
if len(sys.argv[5]) == 2:
    phonics = int(sys.argv[5][0])
    phonicsEffort = int(sys.argv[5][1])
    if phonicsEffort < 1 or phonicsEffort > 3:
        print("ERROR: Please insert a valid value for Phonics Effort - where 1 is bad, 2 is ok, 3 is good Effort.")
        exit()
else:
    phonics = int(sys.argv[5][0])
    
if phonics < 1 or phonics > 3:
    print("ERROR: Please insert a valid value for Phonics Attainment - where 1 is bad, 2 is ok, 3 is good Attainment.")
    exit()
    
if len(sys.argv[7]) == 2:
    science = int(sys.argv[7][0])
    scienceEffort = int(sys.argv[7][1])
    if scienceEffort < 1 or scienceEffort > 3:
        print("ERROR: Please insert a valid value for Science Effort - where 1 is bad, 2 is ok, 3 is good Effort.")
        exit()
else:
    science = int(sys.argv[6][0])
    
if science < 1 or science > 3:
    print("ERROR: Please insert a valid value for Science Attainment - where 1 is bad, 2 is ok, 3 is good Attainment.")
    exit()
    
if len(sys.argv[3]) == 2:
    religStudy = int(sys.argv[3][0])
    religStudyEffort = int(sys.argv[3][1])
    if religStudyEffort < 1 or religStudyEffort > 3:
        print("ERROR: Please insert a valid value for Religious Studies Effort - where 1 is bad, 2 is ok, 3 is good Effort.")
        exit()
else:
    religStudy = int(sys.argv[3][0])
    
if religStudy < 1 or religStudy > 3:
    print("ERROR: Please insert a valid value for Religious Study Attainment - where 1 is bad, 2 is ok, 3 is good Attainment.")
    exit()

otherSubjects = int(sys.argv[8])
behaviour = int(sys.argv[9])
nominalPronoun = "she"
possessivePronoun = "her"
report = ""

if gender != "m" and gender != "f":
    print("Sorry, this gender is not yet supported. Please enter f for female or m for male")
    exit()
elif gender == "m":
    nominalPronoun = "he"
    possessivePronoun = 'his'

if behaviour < 1 or behaviour > 3:
    print("Please insert a valid value for Behaviour - where 1 is bad, 2 is ok, 3 is good Behaviour.")
    exit()

goodMaths = (
    "{0} {1} has made excellent progress this academic year, {2} has made fantastic progress in Phonics especially. ",
    "{0} has done very well this year, {2} has shown fantastic ability in Maths. ",
    "{0} {1} has shown fantastic ability this year, {2} has made progress in all of"
    " {2} subjects and is in a great place to move into Year 2. "
)

okMaths = (
    "{0} {1} has made reasonable progress this academic year, {2} has made the most progress in Science. ",
    "{0} has done well this year, {2} should focus on {2} phonics where more improvement is needed. ",
    "{0} {1} has shown good ability this year, {2} should practice Maths more"
    " in order to be best placed to move into Year 2. "
)

badMaths = (
    "{0} {1} has not made enough progress this academic year, {2} needs to improve in English to be ready for the"
    " jump to Year 2. ",
    "{0} has not done well enough this year, {2} has shown glimmers of ability in Maths,"
    " but needs to improve in Phonics. ",
    "{0} {1} has not shown enough ability this year, {2} has not made progress in all of"
    " {2} subjects and should be worried about moving into Year 2. "
)

goodMathsEffort = (
    "{0} has made an excellent effort in Maths. ",
)

okMathsEffort = (
    "{0} has made a decent effort in Maths, although they could still improve. ",
)

badMathsEffort = (
    "{0} has made a poor effort in Maths. ",
)

goodEnglish = (
    "{0} has done brilliantly in English. ",
)

okEnglish = (
    "{0} has done ok in English. ",
)

badEnglish = (
    "{0} has done badly in English. ",
)

goodEnglishEffort = (
    "{0} has made an excellent effort in English. ",
)

okEnglishEffort = (
    "{0} has made a decent effort in English, although they could still improve. ",
)

badEnglishEffort = (
    "{0} has made a poor effort in English. ",
)

goodPhonics = (
    "{0} has done brilliantly in Phonics. ",
)

okPhonics = (
    "{0} has done ok in Phonics. ",
)

badPhonics = (
    "{0} has done badly in Phonics. ",
)

goodPhonicsEffort = (
    "{0} has made an excellent effort in Phonics. ",
)

okPhonicsEffort = (
    "{0} has made a decent effort in Phonics, although they could still improve. ",
)

badPhonicsEffort = (
    "{0} has made a poor effort in Phonics. ",
)

goodScience = (
    "{0} has done brilliantly in Science. ",
)

okScience = (
    "{0} has done ok in Science. ",
)

badScience = (
    "{0} has done badly in Science. ",
)

goodScienceEffort = (
    "{0} has made an excellent effort in Science. ",
)

okScienceEffort = (
    "{0} has made a decent effort in Science, although they could still improve. ",
)

badScienceEffort = (
    "{0} has made a poor effort in Science. ",
)

goodReligStudy = (
    "{0} has done brilliantly in Religious Studies. ",
)

okReligStudy = (
    "{0} has done ok in Religious Studies. ",
)

badReligStudy = (
    "{0} has done badly in Religious Studies. ",
)

goodReligStudyEffort = (
    "{0} has made an excellent effort in Religious Studies. ",
)

okReligStudyEffort = (
    "{0} has made a decent effort in Religious Studies, although they could still improve. ",
)

badReligStudyEffort = (
    "{0} has made a poor effort in Religious Studies. ",
)

goodOtherSubjects = (
    "{0} has done well in {2} other subjects"
)

okOtherSubjects = (
    "{0} has done ok in other subjects. ",
)

badOtherSubjects = (
    "{0} has done badly in other subjects. ",
)

goodBehaviour = (
    "{0} is very well behaved and sets a fantastic example to {2} peers. ",
    "{0} is always ready to learn and leads the classroom in behaviour. ",
    "{0} is delightful to work with and always gives 100%. "
)

okBehaviour = (
    "{0} generally behaves well, but is occasionally distracted by classmates. ",
    "{0} can be distracted by others, but generally is studious and applies a good work ethic. ",
    "{0}'s behaviour is inconsistent, {2} at times sets a fantastic example while at other times is very disruptive. "
)

badBehaviour = (
    "{0} is too chatty sometimes and would do well not to stay focused on {2} work instead of distracting others. ",
    "{0}'s energy needs to be applied more to studies and less to playing with classmates. ",
    "{0} is a disruptive influence in the class and would benefit from focusing more in lessons. "
)
praise = (
    "Great work {0}!",
    "Excellent {0}!",
    "Superb {0}!",
    "Keep up the excellent work {0}!"
)

decent = (
    "Keep it up {0}!",
    "Push it to next level {0}!",
    "Work harder to show more of your ability {0}!"
)

report += "\nRELIGIOUS STUDIES: \n"
if religStudy == 1:
    x = random.randint(0, len(badReligStudy) - 1)
    report += badReligStudy[x]
elif religStudy == 2:
    x = random.randint(0, len(okReligStudy) - 1)
    report += okReligStudy[x]
else:
    x = random.randint(0, len(goodReligStudy) - 1)
    report += goodReligStudy[x]
    
if religStudyEffort:
    if religStudyEffort == 1:
        x = random.randint(0, len(badReligStudyEffort) - 1)
        report += badReligStudyEffort[x]
    elif religStudyEffort == 2:
        x = random.randint(0, len(okReligStudyEffort) - 1)
        report += okReligStudyEffort[x]
    else:
        x = random.randint(0, len(goodReligStudyEffort) - 1)
        report += goodReligStudyEffort[x]

report += "\n"

report += "\nENGLISH: \n"
if english == 1:
    x = random.randint(0, len(badEnglish) - 1)
    report += badEnglish[x]
elif english == 2:
    x = random.randint(0, len(okEnglish) - 1)
    report += okEnglish[x]
else:
    x = random.randint(0, len(goodEnglish) - 1)
    report += goodEnglish[x]
    
if englishEffort:
    if englishEffort == 1:
        x = random.randint(0, len(badEnglishEffort) - 1)
        report += badEnglishEffort[x]
    elif englishEffort == 2:
        x = random.randint(0, len(okEnglishEffort) - 1)
        report += okEnglishEffort[x]
    else:
        x = random.randint(0, len(goodEnglishEffort) - 1)
        report += goodEnglishEffort[x]

if phonics == 1:
    x = random.randint(0, len(badPhonics) - 1)
    report += badPhonics[x]
elif phonics == 2:
    x = random.randint(0, len(okPhonics) - 1)
    report += okPhonics[x]
else:
    x = random.randint(0, len(goodPhonics) - 1)
    report += goodPhonics[x]

if phonicsEffort:
    if phonicsEffort == 1:
        x = random.randint(0, len(badPhonicsEffort) - 1)
        report += badPhonicsEffort[x]
    elif phonicsEffort == 2:
        x = random.randint(0, len(okPhonicsEffort) - 1)
        report += okPhonicsEffort[x]
    else:
        x = random.randint(0, len(goodPhonicsEffort) - 1)
        report += goodPhonicsEffort[x]

report += "\n"

report += "\nMATHS: \n"
if maths == 1:
    x = random.randint(0, len(badMaths) - 1)
    report += badMaths[x]
elif maths == 2:
    x = random.randint(0, len(okMaths) - 1)
    report += okMaths[x]
else:
    x = random.randint(0, len(goodMaths) - 1)
    report += goodMaths[x]
    
if mathsEffort:
    if mathsEffort == 1:
        x = random.randint(0, len(badMathsEffort) - 1)
        report += badMathsEffort[x]
    elif mathsEffort == 2:
        x = random.randint(0, len(okMathsEffort) - 1)
        report += okMathsEffort[x]
    else:
        x = random.randint(0, len(goodMathsEffort) - 1)
        report += goodMathsEffort[x]

report += "\n"

report += "\nSCIENCE: \n"
if science == 1:
    x = random.randint(0, len(badScience) - 1)
    report += badScience[x]
elif science == 2:
    x = random.randint(0, len(okScience) - 1)
    report += okScience[x]
else:
    x = random.randint(0, len(goodScience) - 1)
    report += goodScience[x]
    
if scienceEffort:
    if scienceEffort == 1:
        x = random.randint(0, len(badScienceEffort) - 1)
        report += badScienceEffort[x]
    elif scienceEffort == 2:
        x = random.randint(0, len(okScienceEffort) - 1)
        report += okScienceEffort[x]
    else:
        x = random.randint(0, len(goodScienceEffort) - 1)
        report += goodScienceEffort[x]

report += "\n"

report += "\nGENERAL COMMENTS: \n"
if otherSubjects == 1:
    x = random.randint(0, len(badOtherSubjects) - 1)
    report += badOtherSubjects[x]
elif otherSubjects == 2:
    x = random.randint(0, len(okOtherSubjects) - 1)
    report += okOtherSubjects[x]
else:
    x = random.randint(0, len(goodOtherSubjects) - 1)
    report += goodOtherSubjects[x]

if behaviour == 1:
    x = random.randint(0, len(badBehaviour) - 1)
    report += badBehaviour[x]
elif behaviour == 2:
    x = random.randint(0, len(okBehaviour) - 1)
    report += okBehaviour[x]
else:
    x = random.randint(0, len(goodBehaviour) - 1)
    report += goodBehaviour[x]

report += "\n"

# if (attainment + behaviour) > 4:
#     x = random.randint(0, len(praise) - 1)
#     report += praise[x]
# else:
#     x = random.randint(0, len(decent) - 1)
#     report += decent[x]

report = report.format(firstName, nominalPronoun, possessivePronoun)
print(report)
