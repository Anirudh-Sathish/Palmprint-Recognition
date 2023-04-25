# Anirudh Sathish 


# Code to Take the existing Birtland University Palmprint Database 
# and split into training and testing sample 
import os
import shutil


base_dir = "basedata"
# check if it exists 
if not os.path.exists(base_dir):
    # then make the dir 
    os.makedirs(base_dir)

# Make training and testing Folders 
training = "training"
training_path = os.path.join(base_dir,training)
testing = "testing"
testing_path = os.path.join(base_dir,testing)
validation = "validation"
validation_path = os.path.join(base_dir,validation)

# Check if exists , else create training
if not os.path.exists(training_path):
    # print(f"Creating directory : {training_path}")
    os.makedirs(training_path)

# Check if exists , else create testing
if not os.path.exists(testing_path):
    # print(f'Creating directory : {testing_path}')
    os.makedirs(testing_path)

# Check if exists , else create validation 
if not os.path.exists(validation_path):
    # print(f'Creating directory : {validation_path}')
    os.makedirs(validation_path)


# Split the BMPD_db database to test and train 
# For ease of use , from each person folder let us take the first two to test 
# Rest to train 

source_dir = "BMPD_db"
if os.path.exists(source_dir):
    # Get the list of dirs in source_dir
    subdirs = os.listdir(source_dir)

    # Now for each of this subdirs 
    # create palmLabels.txt in base_dir
    for dir in subdirs:
        # explore this inside dir 
        dir_path = os.path.join(source_dir,dir)
        files = os.listdir(dir_path)

        # Now 20 % Test , 10 % Validation , 70 % train
        test_len = (len(files)*20)/100
        validation_len = (len(files)*10)/100
        train_len = len(files) - (test_len + validation_len)


        # Making the split 
        test_files = files[:test_len]
        validation_files = files[test_len:test_len+validation_len]
        train_files = files[test_len+validation_len:len(files)]


        # Since we are sure that the destination folder is there , due to our
        # intial part in the code , let us not check for it again 

        # Now let us move the test 
        for test_file in test_files:
            # set the source path 
            source_file_path = os.path.join(dir_path,test_file)
            
            # set desitnation dir 
            destination_dir = os.path.join(testing_path,dir)
            # if not exists , create it 
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            
            # set path in destination dir 
            destination_file_path = os.path.join(destination_dir,test_file)

            # copy to test file
            if not os.path.exists(destination_file_path): 
                shutil.copy(source_file_path,destination_file_path)
        

        # For validation
        for validation_file in validation_files:
            # set the source path 
            source_file_path = os.path.join(dir_path,validation_file)
            
            # set desitnation dir 
            destination_dir = os.path.join(validation_path,dir)
            # if not exists , create it 
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            
            # set path in destination dir 
            destination_file_path = os.path.join(destination_dir,validation_file)

            # copy to file
            if not os.path.exists(destination_file_path): 
                shutil.copy(source_file_path,destination_file_path) 
        
        # For training 
        for train_file in train_files:
            # set the source path 
            source_file_path = os.path.join(dir_path,train_file)
            
            # set desitnation dir 
            destination_dir = os.path.join(training_path,dir)
            # if not exists , create it 
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            
            # set path in destination dir 
            destination_file_path = os.path.join(destination_dir,train_file)

            # copy to test file
            if not os.path.exists(destination_file_path): 
                shutil.copy(source_file_path,destination_file_path)

print("Completed Moving data into test train and validation into the folder basedata")


"""
Additional Information : 
1. Make Sure to have the BMPD_db in your directory 
2. Over here I have not shuffled the dataset 
3. Shuffling is a good practice and if time is present shuffle it 
"""

        

