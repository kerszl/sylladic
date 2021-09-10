#!/bin/bash

tmp4dictionary="tmp4dictionary"
TMP1="tmp1.txt"
FILE_IN_SJP="slowa.txt"
DIC_MAIN_NAME="dic.words.pl"
DIC_MAIN_NAME_NO_DIAC="dic.words.no.diactrics.pl"


make_and_clean_directory () {
cd ..
#make dictionary if doesn't exists    
if [ ! -d $tmp4dictionary ]; then
    mkdir $tmp4dictionary
else
cd $tmp4dictionary
rm -f sjp*.zip
rm -f "$DIC_MAIN_NAME"*.txt
cd ..
fi
}

go_to_directory () {
    cd $tmp4dictionary
}

dictionary_from_sjp () {

    SJP_SITE='https://sjp.pl/slownik/growy/'
    SJP_WER=$(curl -sk https://sjp.pl/slownik/growy/ | grep  -o '[a-z0-9-]*\.zip' | uniq)    
    SJP_WER_NO_ZIP=${SJP_WER/.zip/}
    
    echo "Downloading the latest version of the dictionary from:" $SJP_SITE
    curl -ks $SJP_SITE$SJP_WER --output $SJP_WER
    echo "Unpacking: " $SJP_SITE$SJP_WER
    unzip -o $SJP_WER $FILE_IN_SJP
    SJP_UNPACK_NAME="$DIC_MAIN_NAME""-""$SJP_WER_NO_ZIP"".txt"
    SJP_UNPACK_NO_DIACTRICS_NAME="$DIC_MAIN_NAME_NO_DIAC""-""$SJP_WER_NO_ZIP"".txt"    
    mv $FILE_IN_SJP $SJP_UNPACK_NAME
}

check_installed_programs ()
{
which iconv 1>/dev/null
if (($? != 0)); then
echo Install iconv
exit
fi
}

delete_diacritics () {
echo "Deleting diactricts"
cat $SJP_UNPACK_NAME | iconv -f=utf-8 -t=ascii//TRANSLIT > $TMP1
}

sort_and_delete_duplicates () {
echo "Sort and delete duplicates"

sort $TMP1 | uniq > $SJP_UNPACK_NO_DIACTRICS_NAME
rm $TMP1
}

mv_all () {
echo "Move all to : ../dict"
    mv *.txt ../dict
cd ..
}

if [[ $1 != run ]];then
echo "to run type ./makedictionary.sh run"
exit
fi


check_installed_programs
make_and_clean_directory 
go_to_directory
dictionary_from_sjp
delete_diacritics
sort_and_delete_duplicates
mv_all


