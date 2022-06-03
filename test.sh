#!/bin/bash
declare -a arr=("standard1"
                "standard2"
                "standard3"
                )
standard_files=$(echo standard_{1..3}.txt)
standard_big_files=$(echo standard_big_{1..3}.txt)
standard_huge_files=$(echo standard_huge_{1..3}.txt)
few_repeats_files=$(echo few_repeats_{1..3}.txt)
few_repeats_big_files=$(echo few_repeats_big_{1..3}.txt)
few_repeats_huge_files=$(echo few_repeats_huge_{1..3}.txt)
many_repeats_files=$(echo many_repeats_{1..3}.txt)
many_repeats_big_files=$(echo many_repeats_big_{1..3}.txt)
many_repeats_huge_files=$(echo many_repeats_huge_{1..3}.txt)

files="$standard_files $standard_big_files $standard_huge_files \
       $few_repeats_files $few_repeats_big_files $few_repeats_huge_files \
       $many_repeats_files $many_repeats_big_files $many_repeats_huge_files"

YELLOW='\033[0;33m'
BOLD_YELLOW='\033[1;33m'
NC='\033[0m'
for file in $files
do
    echo -n -e "$YELLOW Running with input $BOLD_YELLOW$file...${NC}"
    time python3 . < inputs/$file > /dev/null
done