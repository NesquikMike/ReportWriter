# Report Writer
This markdown file is an instructional guide on how to install and use the Report Writer.

## Installing 

#### 1. Creating the right folders
  
  1. Press the magnifying glass icon in the top right hand corner of the screen and type in `terminal` and press Enter. 
   
  2. Your Terminal should now be open. And should have written on the last line something along the lines of: 
  `Honigs-MacBook-Air:~ honigschnitzel$` Don't worry if it does not have exactly this written on it. The important thing 
  is that it has `~` (This is your current directory, which is your home directory, i.e. where you start when you first
  open a Terminal) and `$` (This is the symbol that usually precedes an instruction to the computer)in the right places.
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
     dollar sign and the expected result on the line below. Thus, the previous instruction and result would appear like this:
     
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
  Do `$ git clone https://github.com/NesquikMike/ReportWriter.git` to do both these steps at once, your terminal 
  output the following upon running this:
        ```bash
        $ git clone https://github.com/NesquikMike/ReportWriter.git
        Cloning into 'ReportWriter'...
        remote: Counting objects: 42, done.
        remote: Compressing objects: 100% (23/23), done.
        remote: Total 42 (delta 16), reused 42 (delta 16), pack-reused 0
        Unpacking objects: 100% (42/42), done.
        ```
      In the event that we uncover a bug and the program needs to be updated 
  6. 
  
Download Python 3.6


