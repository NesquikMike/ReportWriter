# Report Writer
This markdown file is an instructional guide on how to install and use the Report Writer.

## Installing 

#### 1. Setting up the folder
  
  1. Press the magnifying glass icon in the top right hand corner of the screen and type in `terminal` and press Enter. 
   
  2. Your Terminal should now be open. It should have written on the last line something along the lines of: 
  `Honigs-MacBook-Air:~ honigschnitzel$` Don't worry if it does not have exactly this written on it. The important thing 
  is that it has `~` (This is your current directory, which is your home directory, i.e. where you start when you first
  open a Terminal) and `$` (This is the symbol that usually precedes an instruction to the computer) in the right places.
   Let's go ahead and pin the Terminal to your dock so that you don't have to keep searching for it to open it. 
  Right click on your open Terminal in the dock and go to `Options` and click `Keep in Dock` like in the image below: 
  ![alt text](https://cms-assets.tutsplus.com/uploads/users/53/posts/23318/image/pinterminaltodock.png
   "Adding Terminal to the Dock")
  
  3. Let's now check that we are in the right place. Into your terminal let's type in `pwd` (which stands for "present 
  working directory") after the dollar sign and 
  press Enter. You should get something that looks like this:

        ```bash
        Honigs-MacBook-Air:~ honigschnitzel$ pwd
        /Users/honigschnitzel
        ```
     For future reference from here on in I will write all of the code that you should enter into the terminal after a 
     dollar sign and the expected result on the line below, if the line below starts with a `$` then that is a new 
     instruction for the computer once you have entered the previous line, it also implies that there will probably be 
     no output. Thus, the previous instruction and result would appear like this:
     
        ```bash
        $ pwd
        /Users/honigschnitzel
        ```
      But there is no need to type the dollar sign, it merely signifies code to type in. :)
      
  4. Now let's move into the right place to make these folders. Let's first check that the folders are structured as 
  expected. Do `$ ls` (Remember there is no need to type the dollar sign, it should already be on the last line of 
  your terminal!) such that you can get a list of files and 
  folders in your home directory, like so:
        ```bash
        $ ls
        Applications		Public			projects
        Desktop			i<3HonigSchnitzel.docx  server.R
        Documents		bash_profile		testGame1.R
        Downloads		go			testGame2.R
        IdeaProjects		hello.py		ui.R
        Library			mpsGame1.R		venv
        Movies			my_oauth		xkcd.ttf
        Music			placeNamesFilter.csv
        Pictures		probRetention.R
        ```
        
     No doubt your list of folders and files will look different to this but it should look similar. Now we should be 
     ready to move to where we need to be. Move into documents by doing `$ cd Documents` you should have no output 
     such that the computer is now ready to accept a new instruction:
     
        ```bash
        Honigs-MacBook-Air:~ honigschnitzel$ cd Documents
        Honigs-MacBook-Air:Documents honigschnitzel$
        ```
      Notice that the `~` has been replaced by `Documents`. This is because you are no longer in your Home directory 
      (a directory is a folder), but you are now in Documents. Whatever follows the colon is always the name of 
      your current folder in the Terminal.
      
  5. Let's now download the program and simultaneously create the folder that will store the program. It will also 
  store the master file that the program will read to make the file for each student, and the files for each student. 
  Do `$ git clone https://github.com/NesquikMike/ReportWriter.git` to do both these steps at once. It might ask you 
  for your Github Username and Password in which case you can use my Username which is `NesquikMike` and I will 
  text you the password! Your terminal should output the following upon running this:
        ```bash
        $ git clone https://github.com/NesquikMike/ReportWriter.git
        Cloning into 'ReportWriter'...
        remote: Counting objects: 42, done.
        remote: Compressing objects: 100% (23/23), done.
        remote: Total 42 (delta 16), reused 42 (delta 16), pack-reused 0
        Unpacking objects: 100% (42/42), done.
        ```
      In the event that we uncover a bug and the program needs to be updated, you can download the updated version by 
      going into the `ReportWriter` folder using `$ cd ReportWriter` from the `Documents` folder and then running 
      `$ git pull` 
      let's go ahead and do that now, just to practice. So one more time, from Documents, you have to do:
        ```bash
        $ cd ReportWriter
        $ git pull
        Already up-to-date.
        ```
      If there is a change that has been downloaded doing the above will yield an output similar to the following 
      instead:
        ```bash
        $ cd ReportWriter
        $ git pull
        remote: Counting objects: 3, done.
        remote: Compressing objects: 100% (3/3), done.
        remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
        Unpacking objects: 100% (3/3), done.
        From https://github.com/NesquikMike/ReportWriter
           18c38b4..a763eb3  master     -> origin/master
        Updating 18c38b4..a763eb3
        Fast-forward
         README.md | 44 +++++++++++++++++++++++++++++++++++++++++++-
         1 file changed, 43 insertions(+), 1 deletion(-)
        ```
  6. We've been doing some pretty new and advanced things here so let's do something a bit easier now and move the 
  master report word document into the ReportWriter folder. I could have put the master document on the Github 
  repository, but I was a little worried that that would violate your school's data policy, so I have emailed it to 
  your gmail account instead, you can find it there. Download it and copy and paste it into the ReportWriter folder 
  in your Documents folder, as you would in the normal way, no need for the terminal for this. Make sure that once 
  it is in the ReportWriter folder it is named `master` not `master(1)` or anything like that, this is very important. 
  You can check that you have done this right by going back into your terminal and from within the ReportWriter 
  folder doing `$ ls` which should give you the following output (the order of the files may differ) if we have done 
  everything correctly up to here: 
        ```bash
        $ ls
        README.md		reportWriter.py
        master.docx		reportWriterPROTO.py
        ```
     If this is the case the file structure is all completely set up and we can now move on to setting up python 
     correctly!
     
#### 2. Configuring Python

  1. This bit might be finnicky so feel free to phone me if something goes wrong! Firstly I remember you mentioning 
  that you might update your computer in which case it might have updated 
  Python 3 for you. Let's check this. Exit your current Terminal and open a new one, then do `$ python3 --version` 
  if you get an output along the lines of:
        ```bash
        $ python3 --version
        Python 3.6.1
        ```
      then we can skip to the next step! If instead it says something along the lines of `Python 2.7` or something 
      else completely different then we need to install Python 3! You can do this by following the instructions in 
      this video: [How to Install Python 3 on Mac](https://www.youtube.com/watch?v=0hGzGdRQeak)
      
  2. Now that Python 3 is installed. We are going to install a package that will allow Python to use 
  Microsoft Word documents. To do this run 
        ```
        $ sudo pip3 install python-docx
        ``` 
     in your terminal, which might ask for a password in which 
     case you should enter the password that you use for your user account on your MacBook Air, and press Enter. Don't 
     worry that it does not look like you are typing in your password, they do that deliberately. If this has been done 
     correctly you should have an output in your terminal that finishes like so:
        ```
        Collecting python-docx
          Downloading https://files.pythonhosted.org/packages/2e/07/6a89e91c4fa32f074b77a05564e926420b28e5966ee0fc2a1983805acb3c/python-docx-0.8.6.tar.gz (5.3MB)
            100% |████████████████████████████████| 5.3MB 436kB/s 
        Requirement already satisfied: lxml>=2.3.2 in /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages (from python-docx) (4.2.1)
        Installing collected packages: python-docx
          Running setup.py install for python-docx ... done
        Successfully installed python-docx-0.8.6
        ``` 
     Finally close your terminal window. Now that that is all done we should be ready to get reporting! The next section details how to use the 
     Report Writer.
     
 ## Using the Report Writer
 
   1. Open your Terminal and move into your Documents folder by doing:
        ```bash
        $ cd Documents
        ```
      If you need to, you can check that the ReportWriter folder is in here by doing `$ ls`, which will list all 
      the files and folders in your Documents folder. `ReportWriter` should be listed among them.
   2. Move into the ReportWriter folder by doing:
        ```bash
        $ cd ReportWriter
        ```
   3. Now we can produce a report. To do so enter the following into the terminal:
        ```bash
        $ python3 reportWriter.py [First Name] [Last Name] [Gender] [Religious Education] [English] [Phonics] [Maths] [Science] [OtherSubjects] [Behaviour]
        ```
      Where the place holder in each of the square brackets represents what you're inputting for said student. To 
      give an example of an outstanding student:
        ```
        $ python3 reportWriter.py Angela Merkel f 3 3 3 3 3 3 3
                
        RELIGIOUS STUDIES: 
        Angela has done brilliantly in Religious Studies. 
        
        ENGLISH: 
        Angela has made excellent progress during English this year. She is a confident writer and displays a sound understanding of a variety of sentence structures. She consistently uses a range of time connectives to formulate well-structured recounts and has a good comprehension of the way in which adjectives and descriptive language can be used to enhance a piece of writing. Her use and comprehension of full stops and capital letters is excellent, and she is starting to use other punctuation, such as speech marks, exclamation marks and possessive apostrophes in her writing. 
        
        Angela's knowledge of phonics sounds is excellent. She is able to decode and blend a range of words carefully and accurately and can confidently read and transcribe all of the 40+ phonemes. Angela has shown a considerable interest in reading for pleasure, and I have been very impressed by her readiness to share her reading experiences and favourite books with the rest of the class. Her thoughtful contributions to discussions during whole-class reading sessions have been very much appreciated. 
        
        MATHS: 
        Angela has made excellent progress this academic year, her has made fantastic progress in Phonics especially. 
        
        SCIENCE: 
        Angela has done brilliantly in Science. 
        
        GENERAL COMMENTS: 
        Angela has done well in her other subjects. Angela is delightful to work with and always gives 100%. 
        ``` 
      Last Names can be entered in using speech marks if they have multiple names, for instance:
        ```bash
        $ python3 reportWriter.py Willy "Von Gammler" m 3 2 3 1 1 1 2
        ```
      Gender can be entered as `f` for female and `m` for male. Subjects are ordered as they will be in the report,
      like so: Religious Education, English, Phonics, Maths, Science and Other Subjects. Finally, goes a score for 
      behaviour. The scores range from one to three, the higher the better. So inputting a 3 for Science 
      will give the student a Science report that reflects the fact that they are "above year group expectations". 
      It will also give them an "Ab" for their achievement in that subject. Running this command will output a 
      Microsoft Word docx file of a school report for said student. This report can be found in the normal way by 
      going into your Documents folder and then into the ReportWriter folder, no need for the Terminal. 
      From there you can do as you please 
      with the reports. It will also print the reports for each subject in the Terminal so that it is clear the 
      program has run successfully. Once you have run it, you can run it again if you are not happy with that 
      specific report and would prefer a different randomised report. An easy shortcut so that you don't have to 
      retype into the terminal is just to press the up button on the keyboard in the terminal which will paste 
      the previous command that was executed by the terminal without yet executing it, so you can also edit it if 
      you would prefer to change something like their name or their rating in a specific subject. You can also just 
      keep using the up button and changing the inputs for each student so that you don't have to keep typing 
      `python3 reportWriter.py` each time you want to generate a report for a new student. If you spot any bugs text 
      me and I will fix them ASAP, and update the code on Github so that you use the `$ git pull` command, as 
      discussed in section 1.5 of the installation guide, to download the fixed code. Happy reporting! :) 

  
 


