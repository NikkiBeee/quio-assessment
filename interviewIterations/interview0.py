
import os
from typing import *

def interview(sPath: str, output: List[str] = []) -> str:

    for sChild in os.listdir(sPath):
        sChildPath = sPath + '/' + sChild

        if os.path.isdir(sChildPath): 
            interview(sChildPath)
        else:
            print(sChildPath)
            try: 
                f_content = open(sChildPath, 'r+')
                while f_content.readline() != '':
                    c = f_content.readline()
                    print (c)
                output.append(sChildPath)
            except UnicodeDecodeError:
                pass

    print (output)
