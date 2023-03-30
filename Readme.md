# sample hosts file

```bash
#sample hosts file
127.0.0.1   localhost
192.168.0.1 router
192.168.0.2 google.com
10.0.0.1    myapp.google.com
10.28.100.1 test.google.com
```

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
# Python Test script test-python.py

```bash
#!/usr/bin/env python3
with open('hosts-sample.txt', 'r') as f:
    print('\n'.join([line.split()[1] for line in f if 'google' in line]))

```

```bash

python --version
Python 3.11.2
❯ python test-python.py
google.com
myapp.google.com
test.google.com

```