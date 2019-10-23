var unit = require('../project/src/units');
var expect = require('chai').expect;

describe('round trip conversion mgdl->MMOL->mgdl', function(){
    context('with integer values', function(){
        it('should convert 36 to 2.0 to 36', function(){
            expect(unit.mmolToMgdl(unit.mgdlToMMOL(36))).to.equal(36)
        })
    })
})
