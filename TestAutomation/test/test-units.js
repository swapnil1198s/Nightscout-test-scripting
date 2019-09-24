/* test/test-units.js */

// requires exporting of private functions
// https://stackoverflow.com/questions/22097603/unit-testing-of-private-functions-with-mocha-and-node-js

var unit = require('../project/src/units');
var expect = require('chai').expect;

describe('mmolToMgdl(); return int', function() {
    context('with invalid argument type', function(){
        it('should throw error', function(){
            expect(function() {
                unit.mmolToMgdl('3')
              }).to.throw(new TypeError())
        })
    })

    context('with integer argument', function(){
        it('should conver 1 to 18', function(){
            expect(unit.mmolToMgdl(1)).to.equal(18)
        })
        it('should convert 2 to 36', function(){
            expect(unit.mmolToMgdl(2)).to.equal(36)
        })
    })

    context('with float argument', function(){
        it('should convert 2.5 to 45', function(){
            expect(unit.mmolToMgdl(2.5)).to.equal(45)
        })
        it('should convert 1.145 to 21', function(){
            expect(unit.mmolToMgdl(1.145)).to.equal(21)
        })
        it('should counvert 1.06 to 19', function(){
            expect(unit.mmolToMgdl(1.06)).to.equal(19)
        })
    })
})


describe('mgdlToMMOL(); return .1 decimal', function() {
    context('with invalid argument type', function(){
        it('should throw TypeError', function(){
            expect(function() {
                unit.mgdlToMMOL('3')
              }).to.throw(new TypeError())
        })
    })

    context('with integer argument', function(){
        it('should conver 18 to \'1.0\'', function(){
            expect(unit.mgdlToMMOL(18)).to.equal('1.0')
        })
        it('should convert 36 to \'1.7\'', function(){
            expect(unit.mgdlToMMOL(135)).to.equal('7.5')
        })
    })

    context('with float argument', function(){
        it('should convert 21.3 to \'1.2\'', function(){
            expect(unit.mgdlToMMOL(21.3)).to.equal('1.2')
        })
        it('should convert 30.01 to \'1.7\'', function(){
            expect(unit.mgdlToMMOL(30.01)).to.equal('1.7')
        })
        it('should counvert 1.06 to \'0.1\'', function(){
            expect(unit.mgdlToMMOL(1.06)).to.equal('0.1')
        })
    })
})
