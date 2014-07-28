#! /bin/bash

# 
# generate a statistic file for the segmentations

WD='./wacom_data.txt'
TD='./tablet_data.txt'
WSTAT='wacom_statistics.md'
counter=0

# delete the previous data sheet
if [ -f ./$WSTAT ]
then
	rm $WSTAT
fi

# Wacom data statistics
echo '! Generating statistics from Wacom data sheet !'
writers=`cat $WD | cut -d' ' -f3 | uniq`
for writer in $writers
do
	if [ $counter -gt 0 ];then
		echo ''>>$WSTAT
		echo '---'>>$WSTAT
	fi
	available_data=`cat $WD | cut -d' ' -f3 | uniq -c | grep $writer | sed 's/[^0-9]//g'`
	echo -e '#' $writer":\t"$available_data>>$WSTAT
	echo ''>>$WSTAT
	all_words=`cat $WD | grep $writer | cut -d' ' -f4 | sort`
	words_list=`cat $WD | grep $writer | cut -d' ' -f4 | sort | uniq`
	for word in $words_list
		do
			num=`cat $WD | grep $writer | cut -d ' ' -f4 | grep $word | uniq -c | sed 's/[^0-9]//g'`
			echo -e "\t"'|--'$word"\t"$num>>$WSTAT
		done
		let counter+=1
done

# finish
echo '√ Complete! ./'$WSTAT' is gererated. √'

