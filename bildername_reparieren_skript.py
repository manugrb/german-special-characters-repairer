import os

specChars = [['Ö', 'Oe'], ['Ä', 'Ae'], ['Ü', 'Ue'], ['ö', 'oe'], ['ä', 'ae'], ['ü', 'ue'], ['ß', 'ss'], [' ', '_']]
dir = os.path.dirname(os.path.abspath(__file__))


def repairNames(targetDir):
	for name in os.listdir(targetDir):
		if(os.path.isdir(targetDir + '\\' + name + '\\')):
			dirPath = targetDir + '\\' + name + '\\'
			success = repairNames(targetDir=dirPath)
			if(not success):
				return False
			
		repairedName = name

		for i in range(len(specChars)):
			if(repairedName.find(specChars[i][0]) != -1):
				print('Sonderzeichen gefunden: ', specChars[i][0], '! ersetze mit: ', specChars[i][1], ' im bild: ', targetDir + name)
				repairedName = repairedName.replace(specChars[i][0], specChars[i][1])

		try:
			os.rename(targetDir + name, targetDir + repairedName)
		except FileExistsError as e:
			input('Achtung: Die Datei ' + targetDir + repairedName + ' existiert bereits. Das skript muss unterbrochen werden. Bitte finde die Datei ' + targetDir + repairedName + ' und lösche sie, falls sie wirklich doppelt existiert. Führe dann das Skript nochmal aus.')
			return False
		except FileNotFoundError as e:
			print(e)
			continue
		except PermissionError as e:
			print(e)
			continue
	return True


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
	return foundSomething

def repairNamesInCurrentAndSubdirectories():

	return repairNames(targetDir=dir + '/')


def checkForBadCharsInCurrentAndSubdirectories():

	return checkForBadChars(targetDir=dir)



def main():

	input("dieses Skript kann die Sonderzeichen: Ä, Ö, Ü, ä, ö, ü, ß, und ẞ (großes schrafes S) in ihre normale Form zurückformatieren und in Ae etc. umwandeln.\nDrücke Enter um Fortzufahren.")
	foundSomething = checkForBadCharsInCurrentAndSubdirectories()

	if(foundSomething):
		goOn = input("\nBist du dir sicher, dass du alle gerade aufgelisteten Namen ändern möchtest?\nDrücke N und dann Enter um abzubrechen. Drücke nur Enter um Fortzufahren.")
		if(goOn == "n" or goOn == "N"):
			return

		success = repairNames(dir + '/')
		if(not success):
			return


		input("\nFertig! Alle Sonderzeichen sollten jetzt wieder in der richtigen Form sein. Drücke Enter um den Prozess zu beenden.")

	else:
		input("\nEs wurden keine Sonderzeichen gefunden! Bist du dir sicher, dass du das skript im richtigen Ordner ausgeführt hast? Wenn ja dann gibt es anscheinend keine Sonderzeichen...\n Drücke Enter um das Skript zu beenden.")

if __name__ == '__main__':
	main()