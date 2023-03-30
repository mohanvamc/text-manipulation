with open('hosts-sample.txt', 'r') as f:
    for line in f:
        if 'google' in line:
            fields = line.split()
            print(fields[1])