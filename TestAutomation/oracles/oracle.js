'use strict';

var tst = require("../testCasesExecutables/test")

var [expectval, returnval] = tst()

console.log(expectval)
console.log(returnval)

if (expectval == returnval){
    console.log('Pass')
}
else if (Number.isNaN(expectval) && Number.isNaN(returnval)){
    console.log('Pass')
}
else{
    console.log('Fail')
}