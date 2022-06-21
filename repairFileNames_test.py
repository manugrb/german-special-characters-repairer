import os
import random

specChars = [['Ö', 'Oe'], ['Ä', 'Ae'], ['Ü', 'Ue'], ['ö', 'oe'], ['ä', 'ae'], ['ü', 'ue'], ['ß', 'ss'], [' ', '_']]
dir = os.path.dirname(os.path.abspath(__file__))

def createFiles():
	for i in range(150):
		name = 'file' + str(i)
		for j in range(random.randrange(0, 50)):
			name += specChars[random.randrange(0, len(specChars))][0]

		file = open(name + '.png', "w")
		file.write(str(i))
		file.close()


def checkForBadChars(targetDir):
	foundSomething = False
	for name in os.listdir(targetDir):
		if(os.path.isdir(targetDir + '\\' + name)):
			dirPath = os.path.relpath(targetDir + '\\' + name)
			if(checkForBadChars(targetDir=dirPath)):
				foundSomething = True

		for i in range(len(specChars)):
			if(name.find(specChars[i][0]) != -1):
				print('Sonderzeichen gefunden: ', specChars[i][0], '! sollte mit ', specChars[i][1], 'erstetz werden. Dateiname:', targetDir + name)
				foundSomething = True

	if(not foundSomething):
		print("test passed successfully")


	else:
		print("test Failed!!!")
	return foundSomething




def checkForBadCharsInCurrentAndSubdirectories():
	foundSomething = False

	for name in os.listdir(dir):
		if(not os.path.isdir(name)):
			continue
			
		dirPath = os.path.relpath(name)
		foundSomething = checkForBadChars(targetDir=dirPath)

	if(not foundSomething):
		return checkForBadChars(targetDir=dir)

	return True


def main():
	createFilesIn = input("create new files (y/n)")
	checkForBadSigns = input('check for bad chars? (y/n)')

	if(createFilesIn == "y"):
		createFiles()

	if(checkForBadSigns == "y"):
		if(not checkForBadCharsInCurrentAndSubdirectories()):

			print("all tests passed successfully...")

	input("press enter to continue...")

if __name__ == '__main__':
	main()