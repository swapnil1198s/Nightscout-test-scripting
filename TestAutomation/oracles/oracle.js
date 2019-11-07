'use strict';

var tst = require("../testCasesExecutables/test")

var [expectval, returnval] = tst()

// console.log('E:'+expectval)
// console.log('R:'+returnval)

if (expectval == returnval){
    console.log('Pass')
}
else if (expectval === returnval){
    console.log('Pass')
}
else{
    console.log('Fail')
}