#!/bin/bash

# Add a line on user-home .bashrc file, setting umask to 002 which means 664 for file and 775 for folder
#
# Usage: ./umask_setting A B
#        where
#        A is the folder where the user-homes are, tipically is '/home'.
#        B is the first bunch of letter of the user-home you want to change.
#        you can omit this parameter if you want to change every user-home.
#
# Example: ./umask_setting.sh /home U
#          it will change every .bashrc found in user-home starting with U

if [[ -z $1 ]]; then echo Error: Folder needed; exit 1; fi

for folder in $(ls $1); do
	if [[ $folder =~ ^$2 ]]; then
		echo $folder changed
		cat << TheEnd | tee -a $1/$folder/.bashrc
umask 002
TheEnd
	fi
done
