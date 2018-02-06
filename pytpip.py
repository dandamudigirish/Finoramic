import pip
import re

def inst_pkg(req_file):
    b = []
    with open(req_file,'r') as f:
        for line in f:
            if '==' in line:
                line = re.sub(',', '', line)
                try:
                    abc = pip.main(["install", line])
                    if abc == 2 :
                        b.append(line)
                except Exception as e:
                    pass

    if(len(b) == 0):
        print "Success"
    else:
        print"Failed"
        for i in b:
            print i

inst_pkg("req.txt")