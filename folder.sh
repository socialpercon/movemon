FOLDER_PATH=$1
for j in `find $FOLDER_PATH -maxdepth 1 -type d`
do
	echo $j
	#al=`basename $j`
	#echo  $al
	#cd $j
	#command="$al"
	#command="convert *.jpg $al"
	#echo $command

done
