#! /bin/bash

# Generate the full information for the segmentations of vibewrite

# 
# Note: Only for tablet recordings of Alex's corrected data.
# 

# the resource folder in git master branch
# please give the master branch as the first argument
SRC=$1
TABLET_SRC=$SRC/TabletRecordings/O2Collection
SUB_SRC=Alex-May-21/delay_corrected
LABELS='*_labels.json'
LETTERS='*_letters.json'
PEN='*_pen.json'
INFO='tablet_data.txt'

# delete the previous data sheet
if [ -f ./$INFO ]
then
	rm $INFO
fi

# the info for wacom and tablet are gererated seperately

all_letters=`(cd $TABLET_SRC; ls $SUB_SRC/$LETTERS)`
all_labels=`(cd $TABLET_SRC; ls $SUB_SRC/$LABELS)`
all_pen=`(cd $TABLET_SRC; ls $SUB_SRC/$PEN)`

# collect all the segmentations, which have labels letters and pen' data all three provided
echo '! Generating data sheet, please do not interupt !'
for lable in $all_labels
	do
		#echo $lable # for test

		writer=`echo $lable | cut -d'/' -f1 | cut -d'-' -f1` 
		# except the data form Yuanchen, because they are sentences
		word=`cat $TABLET_SRC/$lable`
		flag=`echo $word | wc -c`
		name=`basename $lable`
		num_labels=`echo $name | cut -d_ -f1`
		ls $TABLET_SRC/$SUB_SRC/$num_labels*letters.json | grep letters>/dev/null &&	\
			ls $TABLET_SRC/$SUB_SRC/$num_lables*pen.json | grep pen>/dev/null
			if [[ $? -eq 0 && $flag -gt 1 ]];then
				echo Tablet $num_labels $writer $word>>$INFO
			fi
	done

# finish
echo '√ Complete! '$INFO' is gererated. √'
