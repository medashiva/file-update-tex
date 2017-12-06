with open('test.xml', 'r+') as f:
    lines = f.readlines()
    f.seek(0)
    f.truncate()
    for line in lines:
        if '<heading>' or '</heading>' in line :
                line = line.replace('<heading>', '<-- <heading>').replace('</heading>', '</heading> -->')
        f.write(line)
