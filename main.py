import os, argparse

parser = argparse.ArgumentParser(description='Take Eventbrite CSV and turn it into YAML for OpenShifter')
#need two args - one for the infile and one for the password
parser.add_argument('infile', help='the full path of the file to be processed. Outfile will have the same name '
                                              'with .yml on the end')
parser.add_argument('--password', help='Optional parameter to specify a password to be used with all accounts. If not '
                                       'present than email is used as password')

args = parser.parse_args()

infile = args.infile
password = args.password
file = open(infile, 'r', encoding='utf-8')
outfile = open(infile+'.yml', 'w')

#skip the first line which is the headers
file.readline()
for line in file:
    last_comma = line.rfind(',')
    email = line[last_comma+1:].rstrip()
    outfile.writelines('  - username: ' + email  +'\n')
    if (not password):
        outfile.writelines('    password: ' + email + '\n')
    else:
        outfile.writelines('    password: ' + password + '\n')
print('done')
