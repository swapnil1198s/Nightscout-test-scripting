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
module.exports = configure, mmolToMgdl, mgdlToMMOL;