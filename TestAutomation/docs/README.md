# 2-2 Javascript Unit Testing Framework Project

Jack Fraser, Jesse Deacon, Swapnil Srivastava

1. To run the tests, first install nodejs.

This can be done with by following the instuctions here:
<https://tecadmin.net/install-latest-nodejs-npm-on-ubuntu/>

2. Ensure that nodejs is installed correctly; your computer may need to restart, ``sudo apt update`` or ``sudo apt upgrade -y``

3. Ensure that the file to be tested is a `javascript` file that is fully unit-testable, and that it is located in the `project/src` directory

4. Ensure that test cases exist for the tested file, are located in `testCases/`, and that they have been written according to the [Test Case Template](https://github.com/csci-362-02-2019/2-2/blob/master/TestAutomation/docs/testcaseTemplate).

3. cd into the TestAutomation subdirectory. The locations where you run the scripts from is important, and the assignment document states that they will be run from TestAutomation

4. execute the command ``python3 scripts/runAllTests.py``. This should run the tests, generate the report, and open it in your web browser. If it does not do so, please check for the html file in the reports subdirectory.