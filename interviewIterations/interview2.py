import os
from typing import *

def interview(sPath: str) -> str:

    content = []
    output = []

    def read_Files(sPath1: str) -> str:

        for sChild in os.listdir(sPath1):
            sChildPath = sPath1 + '/' + sChild

            if os.path.isdir(sChildPath): 
                read_Files(sChildPath)
            else:
                print('Path: ', sChildPath)
                output.append(sChildPath)
                try: 
                    f_content = open(sChildPath, 'r')
                    c = f_content.read()
                    print ('Contents: ', c, '\n')
                    content.append(c) 
                except UnicodeDecodeError:
                    pass
                finally: 
                    f_content.close()

    read_Files(sPath)
    print('Summary of files', output, '\n')
    return [output, content]


