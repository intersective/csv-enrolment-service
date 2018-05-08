import boto3
import sys

#replace with right bucket
bucket = 'uploads-rmitvn' 

# To run : "python script-filename.py enrolment-csv.csv"
# CSV file needs to be in the same place as the python script 

# method to upload file to s3
def upload():
    # validate file input
    if len(sys.argv) < 2:
        print('File input missing. check your CLI: \'python enrol.py csvfile.csv\'')
        return
    # get filename
    filename = sys.argv[1]    
    
    try:
        with open(filename, 'r') as myfile:
            data = myfile.read()

        session = boto3.session.Session(profile_name='rmitvn-s3-credentials')
        s3 = session.resource('s3')   
        s3.Bucket(bucket).put_object(Key=filename, Body=data)
        # Output
        print('File successfully uploaded to s3!')
    except:
        print('Oops..there is an error uploading the file.')

#call upload method
upload()