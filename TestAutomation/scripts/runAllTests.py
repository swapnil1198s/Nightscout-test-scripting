import os, subprocess

filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'reports', 'testReport.html')

casepath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testCases')

outpath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testCasesExecutables')

try: os.remove(filename)
except: print('No File to delete!')

print(filename, os.path.exists(filename))

def exeGen(file, outfilepath):
        print('exegen', file, outfilepath)

        # remove old executables
        # for file in outfilepath:
        #         os.remove(file)

        # generate new executable
        # do stuff here

with open(filename, "w+") as htmlfile:
        htmlfile.write('''<!DOCTYPE html>\n
        <html lang="en-US" style="height: 100%;">\n
        <head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>My List HTML Output</title>\n''')

        for file in os.listdir(casepath):
                print(file, outpath)

                # generate executable based on line
                exeGen(file, outpath)

                # run NPM test and catch output
                line = subprocess.check_output('echo 1', shell=True).decode('utf-8')

                # write output to htmlfile
                print(line)
                htmlfile.write('<p style="margin-left: 0px">'+file+': '+str(line) +'</p>\n')
        print("done")

        htmlfile.write('''</head>''')

try: subprocess.call(['xdg-open', filename])
except: os.startfile(filename)

# delete old html, generate new empty one

# For each File in Test Cases
#     delete all executables
#     generate executable from file
        # import from script
#     subprocess.execute('NPM TEST')
#     pipe output to resutls.hmtl
        # import from script

# open 'finished' html file