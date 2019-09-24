'use strict';

function mgdlToMMOL(mgdl) {
  return (Math.round((mgdl / 18) * 10) / 10).toFixed(1);
}

function mmolToMgdl(mgdl) {
  return Math.round(mgdl * 18);
}

function configure() {
  return {
    mgdlToMMOL: mgdlToMMOL
    , mmolToMgdl: mmolToMgdl
  };
}

// modified to export functions
// module.exports = configure;
// https://stackoverflow.com/questions/16631064/declare-multiple-module-exports-in-node-js/16631079

// original export
// module.exports = configure;

// modified export
module.exports = {
  ToMMOL: function mgdlToMMOL() {},
  ToMgdl: function mmolToMgdl() {}
}