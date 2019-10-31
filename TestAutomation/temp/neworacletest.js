console.log('hi')

var src = require("../project/src/units.js")
function runtest(){
    var res = [NaN, src.mmolToMgdl('3')]
    console.log(res)
    return res
}
module.exports = runtest

// runtest()