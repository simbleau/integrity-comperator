from difflib import SequenceMatcher
import os

class Comparation:
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2
    
    def __hash__(self):
        return hash(self.file1) + hash(self.file2)

    def __eq__(self,other):
        if isinstance(other, self.__class__):
            return hash(self) == hash(other)
        else:
            return NotImplemented

    def __str__(self):
        return "{0}% | {1}, {2}".format(self.calc(), self.file1, self.file2)
    
    def calc(self):
        text1 = open(self.file1).read()
        text2 = open(self.file2).read()
        m = SequenceMatcher(None, text1, text2)
        return round(m.ratio()* 100, 2)
    


comparators = set()

## O(n^2) comparation
directory = r'submissions'
for filename in os.listdir(directory):
    file1 = os.path.join(directory, filename)
    for filename2 in os.listdir(directory):
        file2 = os.path.join(directory, filename2)
        if (file1 != file2):
            comparators.add(Comparation(file1, file2))


for comparation in comparators:
    print(comparation)
