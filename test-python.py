#!/usr/bin/env python3
with open('hosts-sample.txt', 'r') as f:
    print('\n'.join([line.split()[1] for line in f if 'google' in line]))