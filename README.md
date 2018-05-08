CSV Enrolment Service
=======

Overview
-------------
With correct setup and preparations, by running this script along with 'valid' CSV enrolment files will add participants to Practera.


Prerequisite
-------
- **valid** _aws_access_key_id_ and _aws_secret_access_key_
- **python** and **pip** installed on the machine where the script will run. 
- **boto3** python library installed on the machine where the script will run (boto3 can be installed with command _pip install boto3_ assuming you have **pip** installed on your machine.)

Setup 
-------
1. Assuming valid aws keys are in possession and user is on MAC OSX, go to **~/.aws** in root path with command _cd ~/.aws_. IF, **.aws** do not exist, please create one with command _mkdir .aws_ 
2. When you are in **~/.aws** folder, see **credentials** file exist. 
3. IF **credentials** does not exist in the **~.aws**, please create one with command _touch credentials_ . IF the file exists, please skip this step.
4. Open **credentials** file with any text editor you like.
5. Update the file in the following format: 
	```
	[rmitvn-s3-credentials] 
	aws_access_key_id = XXXXXXXXXXXXXX
	aws_secret_access_key = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
	```
Now you are ready to run the script. 


Executing the script  
-------
1. On terminal, cd to the cloned repo that consist of the script. 
2. Move the **valid** CSV enrolment file to the cloned repo and **make sure** it is in the same folder with the script. 
3. If CSV file is in the same folder with the script, go to terminal and while still on the **cloned repo** folder, run the command in next stop. 
4. _python enrol.py your_file.csv_ 
5. If successful, you should see the 'success' message. 