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
fullName = firstName + " " + lastName
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
    print("ERROR: Please insert a valid value for Religious Study Attainment - where 1 is bad, 2 is ok,"
          " 3 is good Attainment.")
    exit()

otherSubjects = int(sys.argv[9])
behaviour = int(sys.argv[10])
nominalPronoun = "she"
possessivePronoun = "her"
nominalPronounCapitalised = "She"
possessivePronounCapitalised = "Her"
report = ""
religStudyReport = ""
englishReport = ""
mathsReport = ""
scienceReport = ""
generalReport = ""

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

okEnglishProgress = (
    "{0} has made steady progress in English this academic year. ",
    "",
    "{0} has progressed well in English this year. "
)

okEnglishPunctuation = (
    "{3} shows an understanding of the importance of finger spaces as a means to demarcate words in sentences and"
    " {2} use of full stops and capital letters is increasingly accurate and consistent. ",
    "{4} use of finger spaces, capital letters and full stops has improved and {1} shows a good understanding of"
    " the way in which full stops help to demarcate sentences. {0} consistently and accurately distinguishes between"
    " upper and lower case letters, and {2} handwriting is increasingly clear and neat. ",
    "{3} has a sound understanding of capital letters and full stops and uses these in {2} work with increasing"
    " accuracy and consistency. {0} uses finger spaces in order to improve the clarity of {2} writing and {2}"
    " distinction between upper and lower case letters in {2} handwriting has improved considerably. "
)

okEnglishSpelling = (
    "{0} is a confident and imaginative writer and has written a number of creative character descriptions and"
    " stories over the course of the year. {0} is beginning to use time connectives to structure a recount and"
    " {2} correct spelling of high frequency and tricky words has improved considerably since the start of the year. ",
    "{4} accurate spelling of high frequency and tricky words is steadily improving, and {0} should continue to"
    " apply {2} knowledge of phonemes when sounding out and spelling words. {0} is developing {2} knowledge and use of"
    " adjectives, and I have seen {2} use a range of time connectives to write a well-structured recount. ",
    "{0} has a sound knowledge of phase 3 and 4 high frequency words and I would like to see {2} develop more"
    " confidence with spelling phase 5 tricky words. {0} is a confident and imaginative writer and has developed"
    " {2} knowledge of a range of adjectives to enhance {2} writing. "
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

okPhonicsProgress = (
    "{0} has a good knowledge of phonics sounds and can confidently and consistently recognise the majority of"
    " the 40+ phonemes. {4} ability to accurately decode and blend a range of words has improved over the course"
    " of the year, and I would like to see {0} continue to practise sounding out words before writing them down, in"
    " order to improve the accuracy of {2} spelling. ",
    "I am very pleased with {0}'s progress in phonics this year. {3} sounds out and blends a range of words with"
    " increasing confidence and now has a good understanding of a majority of the 40+ phonemes. I would now like"
    " to see {0} develop {2} knowledge of alternative spellings for various sounds. ",
    "{0} is an accurate and confident decoder and blender of words and sounds and I have been pleased with {2}"
    " progress in phonics this year. {3} can consistently identify the majority of the 40+ phonemes and can apply"
    " these sounds well in the majority of cases when spelling words. I would like {0} to take {2} time when"
    " sounding out words for spellings, in order to ensure that {2} spellings are consistently accurate and plausible. "
)

okPhonicsLastSentence = (
    "{0} has become an increasingly confident and accurate reader and I have been impressed by {0}'s readiness"
    " to share {2} ideas about {2} favourite books with the class. ",
    "{0} shows an enthusiasm for reading, and it is a delight to see {0} so engaged during whole-class"
    " reading sessions. {3} makes several insightful and thoughtful contributions to discussions and is frequently"
    " willing to share and discuss {2} favourite books during show and tell. ",
    "{0} is a confident reader, and I am pleased by {2} increasing fluency when reading to an adult. {0} is"
    " frequently keen to share {2} ideas about books with the rest of the class and {1} demonstrates a clear"
    " understanding of the features of a story, such as character and setting. "
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
    religStudyReport += badReligStudy[x]
elif religStudy == 2:
    x = random.randint(0, len(okReligStudy) - 1)
    religStudyReport += okReligStudy[x]
else:
    x = random.randint(0, len(goodReligStudy) - 1)
    religStudyReport += goodReligStudy[x]

report += religStudyReport
report += "\n"

report += "\nENGLISH: \n"
if english == 1:
    x = random.randint(0, len(badEnglish) - 1)
    englishReport += badEnglish[x]
elif english == 2:
    x = random.randint(0, len(okEnglishProgress) - 1)
    englishReport += okEnglishProgress[x]
    x = random.randint(0, len(okEnglishPunctuation) - 1)
    englishReport += okEnglishPunctuation[x]
    x = random.randint(0, len(okEnglishSpelling) - 1)
    englishReport += okEnglishSpelling[x]
else:
    x = random.randint(0, len(goodEnglishOverall) - 1)
    englishReport += goodEnglishOverall[x]
    x = random.randint(0, len(goodEnglishSentenceStructure) - 1)
    englishReport += goodEnglishSentenceStructure[x]
    x = random.randint(0, len(goodEnglishPunctuation) - 1)
    englishReport += goodEnglishPunctuation[x]

englishReport += "\n\n"

if phonics == 1:
    x = random.randint(0, len(badPhonics) - 1)
    englishReport += badPhonics[x]
elif phonics == 2:
    x = random.randint(0, len(okPhonicsProgress) - 1)
    englishReport += okPhonicsProgress[x]
    x = random.randint(0, len(okPhonicsLastSentence) - 1)
    englishReport += okPhonicsLastSentence[x]
else:
    x = random.randint(0, len(goodPhonicsOverall) - 1)
    englishReport += goodPhonicsOverall[x]
    x = random.randint(0, len(goodPhonicsSounds) - 1)
    englishReport += goodPhonicsSounds[x]
    x = random.randint(0, len(goodPhonicsReading) - 1)
    englishReport += goodPhonicsReading[x]

report += englishReport
report += "\n"

report += "\nMATHS: \n"
if maths == 1:
    x = random.randint(0, len(badMaths) - 1)
    mathsReport += badMaths[x]
elif maths == 2:
    x = random.randint(0, len(okMaths) - 1)
    mathsReport += okMaths[x]
else:
    x = random.randint(0, len(goodMaths) - 1)
    mathsReport += goodMaths[x]

report += mathsReport
report += "\n"

report += "\nSCIENCE: \n"
if science == 1:
    x = random.randint(0, len(badScience) - 1)
    scienceReport += badScience[x]
elif science == 2:
    x = random.randint(0, len(okScience) - 1)
    scienceReport += okScience[x]
else:
    x = random.randint(0, len(goodScience) - 1)
    scienceReport += goodScience[x]

report += scienceReport
report += "\n"

report += "\nGENERAL COMMENTS: \n"
if otherSubjects == 1:
    x = random.randint(0, len(badOtherSubjects) - 1)
    generalReport += badOtherSubjects[x]
elif otherSubjects == 2:
    x = random.randint(0, len(okOtherSubjects) - 1)
    generalReport += okOtherSubjects[x]
else:
    x = random.randint(0, len(goodOtherSubjects) - 1)
    generalReport += goodOtherSubjects[x]

if behaviour == 1:
    x = random.randint(0, len(badBehaviour) - 1)
    generalReport += badBehaviour[x]
elif behaviour == 2:
    x = random.randint(0, len(okBehaviour) - 1)
    generalReport += okBehaviour[x]
else:
    x = random.randint(0, len(goodBehaviour) - 1)
    generalReport += goodBehaviour[x]

report += generalReport
report += "\n"

religStudyReport = religStudyReport.format(firstName,
                       nominalPronoun,
                       possessivePronoun,
                       nominalPronounCapitalised,
                       possessivePronounCapitalised)
englishReport = englishReport.format(firstName,
                       nominalPronoun,
                       possessivePronoun,
                       nominalPronounCapitalised,
                       possessivePronounCapitalised)
mathsReport = mathsReport.format(firstName,
                       nominalPronoun,
                       possessivePronoun,
                       nominalPronounCapitalised,
                       possessivePronounCapitalised)
scienceReport = scienceReport.format(firstName,
                       nominalPronoun,
                       possessivePronoun,
                       nominalPronounCapitalised,
                       possessivePronounCapitalised)
generalReport = generalReport.format(firstName,
                       nominalPronoun,
                       possessivePronoun,
                       nominalPronounCapitalised,
                       possessivePronounCapitalised)
report = report.format(firstName,
                       nominalPronoun,
                       possessivePronoun,
                       nominalPronounCapitalised,
                       possessivePronounCapitalised)

def delete_paragraph(paragraph):
    p = paragraph._element
    p.getparent().remove(p)
    p._p = p._element = None

def addRating(rating):
    if rating == 1:
        return "WT"
    elif rating == 2:
        return "At"
    else:
        return "Ab"

def addDetails():
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    if 'Pupil:' in paragraph.text:
                        paragraph.add_run(" " + fullName)
                    if 'Class:' in paragraph.text:
                        paragraph.add_run(" Year 1")
                    if 'Teacher:' in paragraph.text:
                        paragraph.add_run(" Miss B. Archibald")
                        return

def addSubjectAttainment(subject, subjectAttainment):
    for table in document.tables:
        lstRow = iter(table.rows)
        for row in lstRow:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    if subject in paragraph.text:
                        for rowExtra in lstRow:
                            for cellExtra in rowExtra.cells:
                                for paraExtra in cellExtra.paragraphs:
                                    if 'Achievement' in paraExtra.text:
                                        for rowExtraExtra in lstRow:
                                            for cellExtraExtra in rowExtraExtra.cells:
                                                for paraExtraExtra in cellExtraExtra.paragraphs:
                                                    if paraExtraExtra.text == "":
                                                        paraExtraExtra.add_run(addRating(subjectAttainment))
                                                        return


def addSubjectReportText(subject, subjectReport):
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                lst = iter(cell.paragraphs)
                for paragraph in lst:
                    if subject in paragraph.text:
                        paragraph.add_run("\n" + subjectReport)
                        for para in lst:
                            delete_paragraph(para)
                        return

def addSubjectReport(subject, subjectReport, subjectAttainment):
    addSubjectReportText(subject, subjectReport)
    addSubjectAttainment(subject, subjectAttainment)
    return

addDetails()
addSubjectReport('Religious Education', religStudyReport, religStudy)
addSubjectReport('English', englishReport, (english + phonics) // 2)
addSubjectReport('Mathematics', mathsReport, maths)
addSubjectReport('Science', scienceReport, science)

documentName = firstName + lastName + '.docx'
document.save(documentName)

print(report)
