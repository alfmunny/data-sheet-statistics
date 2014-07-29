#! /bin/bash

#
# Generate the full information for the segmentations of vibewrite
# 
# NOTE: Only for the Wacom recordings 
#

# the resource folder in git master branch
# please give the master branch as the first argument
SRC=$1
WACOM_SRC=$SRC/WacomRecordings
LABELS='*_labels.json'
LETTERS='*_letters.json'
PEN='*_pen.json'
INFO='wacom_data.txt'

# delete the previous data sheet
if [ -f ./$INFO ]
then
	rm $INFO
fi


# the info for wacom and tablet are gererated seperately

all_letters=`(cd $WACOM_SRC; find . -name $LETTERS)`
all_labels=`(cd $WACOM_SRC; find . -name $LABELS)`
all_pen=`(cd $WACOM_SRC; find . -name $PEN)`

# collect all the segmentations, which have labels letters and pen' data all three provided
echo '! Generating data sheet, please do not interupt !'
for lable in $all_labels
	do
		writer=`echo $lable | cut -d'/' -f2` 
		word=`cat $WACOM_SRC/$lable`
		flag=`echo $word | wc -c`
		# except the data form Yuanchen, because they are sentences
		# and check if the word is valid
		if [[ "$writer" != "Yuanchen" && $flag -gt 1 ]];then
		name=`basename $lable`
		num_labels=`echo $name | cut -d_ -f1`
		find $WACOM_SRC -name $num_labels*letters.json | grep letters>/dev/null
			if [ $? -eq 0 ];then
				find $WACOM_SRC -name $num_labels*pen.json | grep pen>/dev/null
				if [ $? -eq 0 ];then
					echo Wacom $num_labels $writer $word>>$INFO
				fi
			fi
		fi
	done

# finish
echo '√ Complete! '$INFO' is gererated. √'
