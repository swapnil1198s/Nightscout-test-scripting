srcname = "units.js"
funcname = "mmolToMgdl"
inval = '3'
expectval = TypeError()

pathval = "../project/src/" +srcname

var src = require(pathval)

function runtest(){
    return [expectval, src.funcname(inval)]
};
module.exports = runtest
