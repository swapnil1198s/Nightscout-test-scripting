var unit = require('../project/src/units');
var expect = require('chai').expect;

describe('mgdlToMMOL(); return .1 decimal', function() {
    context('with integer argument', function(){
        it('should convert 18 to \'1.0\'', function(){
            expect(unit.mgdlToMMOL(18)).to.equal('1.0')
        })
    })
})