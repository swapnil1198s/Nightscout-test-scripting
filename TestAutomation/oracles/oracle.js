'use strict';

var tst = require("../testCasesExecutables/test")

var [expectval, returnval] = tst()

if (expectval === returnval){
    console.log('Pass')
}
else if (isNaN(expectval) && isNaN(returnval)){
    console.log('Pass')
}
else{
    console.log('Fail')
}