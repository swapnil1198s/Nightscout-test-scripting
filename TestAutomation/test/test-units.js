/* test/test-units.js */

// requires exporting of private functions
// https://stackoverflow.com/questions/22097603/unit-testing-of-private-functions-with-mocha-and-node-js

var unit = require('../project/src/units');
var mgdlToMMOL = unit.ToMMOL;
var mmolToMgdl = unit.ToMgdl;
var expect = require('chai').expect;

describe('#mgdlToMMOL', function() {
    context('without arguments', function(){
        it('should return 0', function(){
            expect(mgdlToMMOL().to.equal(0))
        })
    })

    context('with integer argument', function(){
        it('should return .1 decimal conversion to and from', function(){
            expect(mgdlToMMOL(1)).to.equal({1:18, 18:1})
            expect(mgdlToMMOL(2)).to.equal({2:36, 36:2})
        })
    })

    context('with float argument', function(){
        it('should return .1 decimal conversion to and from', function(){
            expect(mgdlToMMOL(2.5).to.equal({2.5:45, 45:2.5}))
            expect(mgdlToMMOL(1.24765).to.equal({1.3:23.4, 23.4:1.3}))
        })
    })
})


describe('#mmolToMgdl', function() {
    context('without arguments', function(){
        it('should return 0', function(){
            expect(mmolToMgdl().to.equal(0))
        })
    })

    context('with integer argument', function(){
        it('should return .1 decimal conversion to and from', function(){
            expect(mmolToMgdl(1).to.equal({1:18, 18:1}))
            expect(mmolToMgdl(2).to.equal({2:36, 36:2}))
        })
    })

    context('with float argument', function(){
        it('should return .1 decimal conversion to and from', function(){
            expect(mmolToMgdl(2.5).to.equal({2.5:45, 45:2.5}))
            expect(mmolToMgdl(1.24765).to.equal({1.3:23.4, 23.4:1.3}))
        })
    })
})