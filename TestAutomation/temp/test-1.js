var unit = require('../project/src/units');
var expect = require('chai').expect;

describe('mmolToMgdl(); return int', function() {
    context('with integer argument', function(){
        it('should convert 1 to 18', function(){
            expect(unit.mmolToMgdl(1)).to.equal(18)
        })
    })
})