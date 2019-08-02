import sys, os
myPath = os.path.abspath(__file__)[0:len(os.path.abspath(__file__))-22] + 'interviewIterations/'
print(myPath)
sys.path.insert(1, myPath)

import interview3


def test_type():
    assert type (interview3.interview('./testFileStructure')) is list
    assert type (interview3.interview('./testFileStructure')[0]) is list
    assert type (interview3.interview('./testFileStructure')[0][0]) is str



def test_contents():
    assert interview3.interview('./testFileStructure') == [
        ['./testFileStructure/file0.txt', './testFileStructure/folder2/file4.txt', './testFileStructure/folder0/file2.txt', './testFileStructure/folder0/file1.txt', './testFileStructure/folder0/folder1/file3.txt'],
        ['', 'Contents of File 4\nAdditional folder and file to test the "unusual bug"', 'Contents of File 2\nTesting that function will read *multiple* files within a directory', 'Contents of File 1\nTesting that function will read file within a directory', 'Contents of File 3\nTesting that function will read file within a directory two levels from the original'] 
    ]
    assert interview3.interview('./testFileStructure/folderEmpty') == [[],[]]

# Tests re: the "Usual Bug" prompt
def test_bug():
    interview3.interview(os.path.expanduser('./testFileStructure/folder0'))
    interview3.interview(os.path.expanduser('./testFileStructure/folder2'))