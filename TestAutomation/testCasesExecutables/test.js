var unit = require('../project/src/units');
var expect = require('chai').expect;

describe('round trip conversion MMOL->mgdl->MMOL', function(){
    context('with integer values', function(){
        it('should convert 1 to 18 to 1.0', function(){
            expect(unit.mgdlToMMOL(unit.mmolToMgdl(1))).to.equal('1.0')
        })
    })
})