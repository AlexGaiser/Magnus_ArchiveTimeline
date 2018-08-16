#! file maker

#this is a module which makes a file at the path location with the desired name and file type
import os
def filemaker(title, filetype, headers):
    filename = str(title + filetype)
    cwd = (os.getcwd())
    csvfilepath =  (cwd+ '\\'+'\\' + filename)
    
    print(filename)
    if not os.path.isfile(filename):#creates a csv with headers if doesn't exist in current directory
    	f = open(filename,"w")
    	f.write(headers)
    	print('File Created')
    else:
    	print("file already made")
    
  