#!/bin/bash

# Określenie zakresu dat
start_date=$(date -d "2022-10-22" +%s)
end_date=$(date -d "2022-12-22" +%s)
current_date=$start_date

# Pętla while iterująca po każdym dniu w zakresie dat
while [ $current_date -le $end_date ]
do
    next_date=$(date -d "@$current_date" +%Y-%m-%d)

    snscrape --jsonl --max-results 100 twitter-search "#Brexit until:$next_date since:$current_date" >> "../data/twitter23.jsonl"

    current_date=$(date -d "$next_date + 1 day" +%s)
done
