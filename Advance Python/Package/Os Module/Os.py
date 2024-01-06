import os 
#Current woring directory
print(os.getcwd())

#Create new working directory(Folder)
# os.mkdir('mydir')

#Child directory here parent already created
# os.mkdir('mydir/childdir')

#create parent also child also parent created
# os.makedirs("mydir/childdir/grandchild")

#changing directory
# print(os.getcwd())
# os.chdir('mydir')
# print(os.getcwd())

# Change directory name
# os.rename('mydir','Mydirectory')

#remove directory but firstly child one by one dir delete
# os.rmdir('Mydirectory\childdir/grandchild')


# Remove all parent and child dir
# os.removedirs('Mydirectory\childdir')

#List all dir inside parent dir

# print("Files and Directories:", files_and_directories)
# files_and_directories = os.listdir(r"C:\Users\nitrsh\Documents\PythonAllInOne\Advance Python")
# print(files_and_directories)

print()
#print all file inside any dir
import os

def filename(dir_name):
    with os.scandir(dir_name) as f:
        for i in f:
            if i.is_file():
                print(i.name)
            elif i.is_dir():
                    filename(i.path)
dir_name=r"C:\Users\nitrsh\Documents\PythonAllInOne\Advance Python"
filename(dir_name)

