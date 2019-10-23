var unit = require('../project/src/units');
var expect = require('chai').expect;

describe('units.js mmolToMgdl', function() {
    context('input 1; expected output 18', function(){
        it('testing if converts correctly', function(){
            expect(unit.mmolToMgdl(1)).to.equal(18)
        })
    })
})