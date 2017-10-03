#!/bin/bash
inpFile=$1
confFile=$2
outFile=$3
outFileDir=`dirname $3`
outFileName=`basename $3`

mkdir -p $outFileDir
value=$(<$inpFile)
mapValues=$(<$confFile)

declare -A mapVals
preIFS=${IFS}
IFS="=" 

#read the input file. 
readarray inpArray < $inpFile

#read cong file
while IFS='=' read -r var val 
do
	mapVals["${var}"]="${val}"
done < "$confFile"

#check to print keys. 
for key in "${!mapVals[@]}"
do
	match=[\[][\[]$key]]
	let index=0
	for line in "${inpArray[@]}"
	do
		if [[ $line =~ $match ]];
		then
			newLine="${line/$match/${mapVals[$key]}}"
			inpArray[$index]="${newLine}" 
		fi 
		index=$(($index+1))
	done		
done

printf "%s" "${inpArray[@]}" >$outFile
echo File Written "$outFile"
IFS=${preIFS}





