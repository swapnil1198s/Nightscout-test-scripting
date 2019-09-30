# 2-2

1. To run the tests, first install nodejs.

This can be done with by following the instuctions here:
<https://tecadmin.net/install-latest-nodejs-npm-on-ubuntu/>

2. cd into the TestAutomation subdirectory. The locations where you run the scripts from is important, and the assignment document states that they will be run from TestAutomation

3. execute the command ``./scripts/setup.sh``. If it does not work, please try ``sh ./scripts/setup.sh``. This will install the node-dependencies. If they fail, ensure that nodejs is installed correctly; your computer may need to restart, ``sudo apt update`` or ``sudo apt upgrade -y``

4. execute the command ``./scripts/runAllTests.sh`` or ``sh ./scripts/runAllTests.sh``. This should run the tests, generate the report, and open it in your web browser. If it does not do so, please check for the html file in the reports subdirectory.

5. if an error message occurs that states something like 'node did not recognize this command; did you mean to write 'test' or 'tst'?', there is likely an eol error in the .sh file. These are pernicious because my IDE seems to forget my EOL settings between sessions and overwrite them. It should be set to have no carriage return at EOL; changing it in a text editor will fix the error.