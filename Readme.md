# awk example
awk command to print all hostsnames with word "google"

```bash
awk '/google/{print $2}' hosts-sample.txt

google.com
myapp.google.com
test.google.com

```
# grep example

```bash

grep "google" hosts-sample.txt | awk '{print $2}'

google.com
myapp.google.com
test.google.com

```
# test-bash.sh script to achieve the same result

```bash
#!/bin/bash
while read -r line; do
  if [[ $line == *"google"* ]]; then
    echo $line | awk '{print $2}'
  fi
done < hosts-sample.txt

chmod +x test-bash.sh
./test-bash.sh 

google.com
myapp.google.com
test.google.com

```
# Python Test 

```bash

python --version
Python 3.11.2
❯ python test-python.py
google.com
myapp.google.com
test.google.com

```