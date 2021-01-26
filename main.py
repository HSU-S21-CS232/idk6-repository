print('Hello, World!')
name = 'Ian'

'''
multi-line comment
'''

'''
backup script that syncs files between locations
If file in destination is newer, don't copy and instead move new version
to source
'''

'''
function to create set number of files
'''



import random
import os


def create_random_files(directory_path, num_files):
    for i in range(num_files):

        file_name = str(random.randint(0, 1000)) + ".txt"
        file_path = os.path.join(directory_path, file_name)

        with open(file_path, "w") as random_file:
            print(random.randint(0, 999), file = random_file)

        

def clean_directory(directory_name):
    pass


create_random_files('folder1', 100)
print("done")