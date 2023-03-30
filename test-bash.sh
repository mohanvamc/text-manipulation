#!/bin/bash
while read -r line; do
  if [[ $line == *"google"* ]]; then
    echo $line | awk '{print $2}'
  fi
done < hosts-sample.txt