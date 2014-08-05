#! /bin/bash

# 
# generate a statistic file for the segmentations

WD='./wacom_data.txt'
TD='./tablet_data.txt'
WSTAT='wacom_statistics.md'
W_WORD_STAT='wacom_word_statistics.md'

# delete the previous statistics
if [ -f ./$WSTAT ]
then
	rm $WSTAT
fi

# Wacom data statistics
echo '! Generating statistics from Wacom data sheet !'
counter=0
writers=`cat $WD | cut -d' ' -f3 | uniq`
for writer in $writers
do
	if [ $counter -gt 0 ];then
		echo ''>>$WSTAT
		echo '---'>>$WSTAT
	fi
	available_data=`cat $WD | cut -d' ' -f3 | sort | uniq -c | grep ' '$writer' ' | sed 's/[^0-9]//g'`
	echo -e '#' $writer":\t"$available_data>>$WSTAT
	echo ''>>$WSTAT
	all_words=`cat $WD | grep $writer | cut -d' ' -f4 | sort`
	words_list=`cat $WD | grep $writer | cut -d' ' -f4 | sort | uniq`
	for word in $words_list
	do
			num=`cat $WD | grep $writer | cut -d' ' -f4 | grep $word | uniq -c | sed 's/[^0-9]//g'`
			echo -e "\t"'|--'$word"\t"$num>>$WSTAT
		done
		let counter+=1
done

# delete the previous data statistics
if [ -f ./$W_WORD_STAT ]
then
	rm $W_WORD_STAT
fi

# Wacom words data statistics
counter=0
words=`cat $WD | cut -d' ' -f4 | sort | uniq`
for word in $words
do
	if [ $counter -gt 0 ]; then
		echo ''>>$W_WORD_STAT
		echo '---'>>$W_WORD_STAT
	fi
	available_data=`cat $WD | cut -d' ' -f4 | sort | uniq -c | grep ' '$word'$' | sed 's/[^0-9]//g'`
	echo -e '#' $word":\t"$available_data>>$W_WORD_STAT
	echo ''>>$W_WORD_STAT
	all_writers=`cat $WD | grep ' '$word'$' | cut -d' ' -f3 | sort`
	writers_list=`cat $WD | grep ' '$word'$' | cut -d' ' -f3 | sort | uniq`
	for writer in $writers_list
	do
			num=`cat $WD | grep ' '$word'$' | cut -d' ' -f3 | grep $writer | uniq -c | sed 's/[^0-9]//g'`
			echo -e "\t"'|--'$writer"\t"$num>>$W_WORD_STAT
		done
		let counter+=1
done

# finish
echo '√ Complete! '$WSTAT' and '$W_WORD_STAT' is gererated. √'










