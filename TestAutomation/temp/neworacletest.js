srcname = %
funcname = %
inval = %

pathval = "../project/src/" +srcname

var src = require(pathval)

function runtest(inval){
    return src.funcname(inval)
}