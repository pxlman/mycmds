#!/bin/bash
# cmd setup blabla-1.2.tar.xz com.discord.bla
# cmd alias add com.discord.bla dicord
set -e
mkdir -p ~/.config/taller/
flatname=$3
if [[ ! (-e /tmp/archive) ]]; then
	mkdir /tmp/archive
fi
if [[ $1 == "setup" ]]; then
	# Extracting the tar in /tmp to be removed
	tar -xvf $2 -C /tmp/archive >/tmp/archive/o.txt
	# Program name by getting the folder name in the tar file
	name=$(cat /tmp/archive/o.txt | head -1 | awk -F'/' '{print $1}') # may be uppercase
	# The name in lowercase to be better sorted
	cmd=$(echo $name | tr '[:upper:]' '[:lower:]') # lowercase name
	# The extraction directory
	dir="/tmp/archive/$name"
	rm /tmp/archive/o.txt
	#
	# Case of the dir exists
	if [[ -e /opt/$cmd ]]; then
		echo "You want to replace|update /opt/$name with your new application? [y/N]"
		read ans
		if [[ ans != "y" ]]; then
			echo "That's not cool man"
			exit
		# Upgrading the app
		else

		fi
	fi
	#
	# Installing from scratch
	#
	# Removing the old version folder
	sudo rm -R /opt/$cmd
	# Making new directory
	sudo mkdir /opt/$cmd
	# Moving app directory to opt
	sudo mv $dir/* /opt/$cmd/ && dir=/opt/$cmd
	# Now $dir is the new app directory at /opt that will be used
	#
	#get the $app                ---------------------------------->?
	# Get the executable program in the dir
	echo "Please type the exec program in the tar.gz (case is sensitive): "
	read app
	#
	# Adding a symbolic lint in /sbin
	sudo ln --symbolic $dir/$app ~/.local/bin/$cmd
	# Making the desktop app
	# First we need to check if it was there in the tar so we use it
	if find $dir -maxdepth 1 -name "*.desktop"; then
		desk=$(find $dir -maxdepth 1 -name "*.desktop" | awk -F'/' '{print $NF}')
	fi
elif [[ $1 == "alias" ]]; then
	if [[ $2 == 'add' ]]; then
		aliased=$4
		aliasesFile=~/.config/taller/aliases.conf
		if [[ ! (-e ~/.config/taller/aliases.conf) ]]; then
			touch $aliasesFile
		fi
		# Test it's not there first             ------------------------->?
		# Done
		if grep " $aliased;" $aliasesFile; then
			if grep "$flatname " $aliasesFile; then
				echo "It's already there"
			else
				echo "It's used for $(
					awk \"/ $aliased
					/ {print $1}\" $aliasesFile
				)"
			fi
		else
			echo "$flatname $aliased;" >>$aliasesFile
		fi
	elif [[ $2 == 'remove' ]]; then
		if grep " $aliased;" $aliasesFile; then
			awk "!/ $aliased/ {print}" >$aliasesFile
		else
			echo "It's already not there"
		fi
	elif [[ $2 == 'list' ]]; then
		cat $aliasesFile | sed "s/;//g" | awk '{print $1 -> $2}'
	fi
fi
