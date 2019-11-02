import json
from imager import Imager
from os import listdir, getcwd, walk
from os.path import isfile, join

inDir = input('Directories -\n{}\nInput directory: '.format(next(walk('.'))[1]))

myImager = Imager()
dataset = []

print('Processing data')
for picFile in [fileName if fileName.endswith('.jpg') else '' for fileName in listdir(getcwd() + '/' + inDir)]:
    rawImg = myImager.open_img(inDir + '/' + picFile)
    procdImg = myImager.process_img(rawImg)
    if procdImg is None: continue

    #myImager.show_img(procdImg)
    dataset.append([procdImg.tolist(),
                    int(picFile.split()[0].split('.')[0])]) #picFile.split()[0]])

print('Writing to dataset file')
with open(inDir + '-dataset.json', 'w') as dsFile:
    dsFile.write(json.dumps(dataset))
print('Sucessfully wrote data set to JSON file')
    
