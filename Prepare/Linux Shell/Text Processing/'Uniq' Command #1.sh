#!/bin/bash
rm file.txt > stdout.txt 2> stderr.txt
while IFS= read -r line || [ -n "$line" ]; do
  echo "$line" >> file.txt
done
uniq < file.txt
