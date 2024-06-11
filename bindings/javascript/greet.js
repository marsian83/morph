const ffi = require("ffi-napi");
const ref = require("ref-napi");
const path = require("path");

const greet = ffi.Library("shared/greet.so", {
  greet: [ref.types.CString, [ref.types.CString]],
});

module.exports = { greet: greet.greet };
