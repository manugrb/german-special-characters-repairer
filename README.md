# german-special-characters-repairer

Having special characters like spaces, 'ä', 'ö' or 'ü' in a file or folder name can lead to big problems, because these special characters get encoded in some apps. Those apps will then be unable to locate these files in the file system. To aviod this one should not use these speacial characters.
This script will help you take care of the already existing special characters. It will detect the following characters: ' ', 'Ä', 'Ö', 'Ü', 'ä', 'ö', 'ü' and 'ß' and will replace it with Ae Oe and so on.

## How to use:
 1. Run `python repairFileNames.py` in the directory with all of the files you want to rename.
 2. The program will detect all files, folders, and files and folders in those folders with special characters. You can have an unlimited amount of nested folders. The program will check them recursively.
 3. The program will list every file and folder that it will rename and what it will change
 4. If you are happy with the displayed changes press enter. If you are not happy with the changes interrupt the script (CTRL + C)
 5. The program will make all of the announced changes
 6. To complete the execution just press enter once more.
