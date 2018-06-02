import sys
import random
from docx import Document

document = Document('master.docx')

if len(sys.argv) < 11:
    print("ERROR: Not enough information. Please provide First Name, Last Name, Gender - f for female, m for male,"
          " RE, English, Phonics, Maths, Science, Other Subjects and Behaviour "
          "- where 1 is bad, 2 is ok, 3 is good attainment or behaviour.")
    exit()

firstName = sys.argv[1]
lastName = sys.argv[2]
gender = sys.argv[3]

maths = int(sys.argv[4])

if maths < 1 or maths > 3:
    print("ERROR: Please insert a valid value for Maths Attainment - where 1 is bad, 2 is ok, 3 is good Attainment.")
    exit()
        
english = int(sys.argv[5])
    
if english < 1 or english > 3:
    print("ERROR: Please insert a valid value for English Attainment - where 1 is bad, 2 is ok, 3 is good Attainment.")
    exit()
    
phonics = int(sys.argv[6])
    
if phonics < 1 or phonics > 3:
    print("ERROR: Please insert a valid value for Phonics Attainment - where 1 is bad, 2 is ok, 3 is good Attainment.")
    exit()
    
science = int(sys.argv[7])
    
if science < 1 or science > 3:
    print("ERROR: Please insert a valid value for Science Attainment - where 1 is bad, 2 is ok, 3 is good Attainment.")
    exit()
    
religStudy = int(sys.argv[8])
    
if religStudy < 1 or religStudy > 3:
    print("ERROR: Please insert a valid value for Religious Study Attainment - where 1 is bad, 2 is ok, 3 is good Attainment.")
    exit()

otherSubjects = int(sys.argv[9])
behaviour = int(sys.argv[10])
nominalPronoun = "she"
possessivePronoun = "her"
nominalPronounCapitalised = "She"
possessivePronounCapitalised = "Her"
report = ""

if gender != "m" and gender != "f":
    print("Sorry, this gender is not yet supported. Please enter f for female or m for male")
    exit()
elif gender == "m":
    nominalPronoun = "he"
    possessivePronoun = 'his'
    nominalPronounCapitalised = "He"
    possessivePronounCapitalised = "His"

if behaviour < 1 or behaviour > 3:
    print("Please insert a valid value for Behaviour - where 1 is bad, 2 is ok, 3 is good Behaviour.")
    exit()

goodMaths = (
    "{0} has made excellent progress this academic year, {2} has made fantastic progress in Phonics especially. ",
    "{0} has done very well this year, {2} has shown fantastic ability in Maths. ",
    "{0} has shown fantastic ability this year, {1} has made progress in all of"
    " {2} subjects and is in a great place to move into Year 2. "
)

okMaths = (
    "{0} has made reasonable progress this academic year, {2} has made the most progress in Science. ",
    "{0} has done well this year, {2} should focus on {2} phonics where more improvement is needed. ",
    "{0} has shown good ability this year, {2} should practice Maths more"
    " in order to be best placed to move into Year 2. "
)

badMaths = (
    "{0} has not made enough progress this academic year, {2} needs to improve in English to be ready for the"
    " jump to Year 2. ",
    "{0} has not done well enough this year, {2} has shown glimmers of ability in Maths,"
    " but needs to improve in Phonics. ",
    "{0} has not shown enough ability this year, {2} has not made progress in all of"
    " {2} subjects and should be worried about moving into Year 2. "
)

goodEnglishOverall = (
    "{0} has made excellent progress during English this year. ",
    "{0} has progressed well in English this year. "
)

goodEnglishSentenceStructure = (
    "{3} demonstrates a sound knowledge of a range of sentence structures and can consistently and confidently use "
    "time connectives to write a well structured recount. ",
    "{3} is a confident writer and displays a sound understanding of a variety of sentence structures. "
    "{3} consistently uses a range of time connectives to formulate well-structured recounts and has a good"
    " comprehension of the way in which adjectives and descriptive language can be used to enhance a piece of writing. "
)

goodEnglishPunctuation = (
    "{4} use and comprehension of full stops and capital letters is excellent, and {1} is starting to use other"
    " punctuation, such as speech marks, exclamation marks and possessive apostrophes in {2} writing. ",
    "{4} use of capital letters and full stops is very consistent. "
)

okEnglish = (
    "{0} has done ok in English. ",
)

badEnglish = (
    "{0} has done badly in English. ",
)

goodPhonicsOverall = (
    "{0}'s knowledge of phonics sounds is excellent. ",
)

goodPhonicsSounds = (
    "{3} is able to decode and blend a range of words carefully and accurately and can confidently read and transcribe"
    " all of the 40+ phonemes. ",
)

goodPhonicsReading = (
    "{0} shows an enthusiasm for reading and I have been very impressed by {2} insightful and thoughtful"
    " contributions to discussions during  whole-class reading sessions. "
    "{3} demonstrates a good understanding of story features and makes erudite inferences about characters and"
    " events. ",
    "{0} has shown a considerable interest in reading for pleasure, and I have been very impressed by {2} readiness to"
    " share {2} reading experiences and favourite books with the rest of the class. {4} thoughtful contributions to "
    "discussions during whole-class reading sessions have been very much appreciated. "
)

okPhonics = (
    "{0} has done ok in Phonics. ",
)

badPhonics = (
    "{0} has done badly in Phonics. ",
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

goodReligStudy = (
    "{0} has done brilliantly in Religious Studies. ",
)

okReligStudy = (
    "{0} has done ok in Religious Studies. ",
)

badReligStudy = (
    "{0} has done badly in Religious Studies. ",
)

goodOtherSubjects = (
    "{0} has done well in {2} other subjects. ",
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

report += "\n"

report += "\nENGLISH: \n"
if english == 1:
    x = random.randint(0, len(badEnglish) - 1)
    report += badEnglish[x]
elif english == 2:
    x = random.randint(0, len(okEnglish) - 1)
    report += okEnglish[x]
else:
    x = random.randint(0, len(goodEnglishOverall) - 1)
    report += goodEnglishOverall[x]
    x = random.randint(0, len(goodEnglishSentenceStructure) - 1)
    report += goodEnglishSentenceStructure[x]
    x = random.randint(0, len(goodEnglishPunctuation) - 1)
    report += goodEnglishPunctuation[x]

report += "\n\n"

if phonics == 1:
    x = random.randint(0, len(badPhonics) - 1)
    report += badPhonics[x]
elif phonics == 2:
    x = random.randint(0, len(okPhonics) - 1)
    report += okPhonics[x]
else:
    x = random.randint(0, len(goodPhonicsOverall) - 1)
    report += goodPhonicsOverall[x]
    x = random.randint(0, len(goodPhonicsSounds) - 1)
    report += goodPhonicsSounds[x]
    x = random.randint(0, len(goodPhonicsReading) - 1)
    report += goodPhonicsReading[x]

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

report = report.format(firstName,
                       nominalPronoun,
                       possessivePronoun,
                       nominalPronounCapitalised,
                       possessivePronounCapitalised)
print(report)
