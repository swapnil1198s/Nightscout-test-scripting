def exeGen(infilepath, outpath, exectemplatepath):
        print('exegen', infilepath, outpath)
        # infilepath == 'infilepath'

        # remove old executables
        # for file in outfilepath:
        #         os.remove(file)

        # generate new executable
        exeTemplate = open(exectemplatepath, "w+")
        testCase = open(infilepath, "r")
        inputs = testCase.readLines()
        for i in inputs:
                pass
        # do stuff here

        exeTemplate.close()
        testCase.close()