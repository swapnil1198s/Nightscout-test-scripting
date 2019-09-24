/* test/test-units.js */

// requires exporting of private functions
// https://stackoverflow.com/questions/22097603/unit-testing-of-private-functions-with-mocha-and-node-js

var unit = require('../project/src/units');
var expect = require('chai').expect;

describe('#mmolToMgdl', function() {
    // context('without arguments', function(){
    //     it('should return 0', function(){
    //         expect(unit.mmolToMgdl().to.equal(0))
    //     })
    // })

    context('with integer argument', function(){
        it('should return .1 decimal conversion to and from', function(){
            expect(unit.mmolToMgdl(1)).to.equal(18)
            expect(unit.mmolToMgdl(2)).to.equal(36)
        })
    })

    // context('with float argument', function(){
    //     it('should return .1 decimal conversion to and from', function(){
    //         expect(unit.mmolToMgdl(2.5, 45).to.equal(45))
    //         expect(unit.mmolToMgdl(1.24765).to.equal(23.4))
    //     })
    // })
})
