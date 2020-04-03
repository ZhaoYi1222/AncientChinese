import os
import shutil
path='./续藏经/'
for i in os.listdir(path):
    if(os.path.isfile(path+i)):
        pass
    else:
        level_1 = path+i+'/'
        for j in os.listdir(level_1):
            book_path = level_1+j
            if(os.path.exists(path+j)):
                os.remove(book_path)
            else:
                shutil.move(book_path, path)  
        os.rmdir(level_1)









