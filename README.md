cracks/
Directory with files containing cracked hashes. The naming convention will follow: <name_of_your_python_script>.cracks
So when you call john, do so like the following:

$:_> john --wordlist=<name_of_your_python_script>.dict shadow-lab.txt > <name_of_your_python_script>.cracks
-----------------------------------------------------------------------------------------------------------------------

dictionaries/
Directory with files containing useful guesses for john. Each member will alter the original dictionary,
dictionaries/animals.txt, with their respective python script.

$:_> python <name_of_your_python_script>.py > <name_of_your_python_script>.dict
-----------------------------------------------------------------------------------------------------------------------
hashes/
Directory with hashes to crack.

-----------------------------------------------------------------------------------------------------------------------
new_scripts/
Revised or refactored python scripts. Each member will author their own.

Every python script will have a header like the following:
'''
Author:  <team member name>
Date:    <date originally written>
Contact: <email>
'''

How you run your script is completely up to you, however this format is simple and common:
$:_> python replace.py animals.txt e 3
argv[0] is used to name my output as:               open(argv[0][:-3] + ".dict", "w") # Remove ".py" from file name
argv[1] is used to read in the original dictionary: open(argv[1], "r")
argv[2], argv[3], etc...any other required command line arguments for your script

-----------------------------------------------------------------------------------------------------------------------
old_scripts/
The original python scripts written in class.
