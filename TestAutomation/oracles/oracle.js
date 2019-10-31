'use strict'

import { runtest } from "./testCasesExecutables/test.js"

console.log('here1')

var res = runtest()
var expectval = res[0]
var returnval = res[1]

console.log('here2')

if (expectval === returnval){
    // return 'Pass'
    console.log('Pass')
}
else if (isNaN(expectval) && isNaN(outval)){
    // return 'Pass'
    console.log('Pass')
}
else{
    // return 'Fail'
    console.log('Fail')
}