"use strict";
(() => {
var exports = {};
exports.id = 328;
exports.ids = [328];
exports.modules = {

/***/ 1782:
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (/* binding */ handler)
/* harmony export */ });
function handler(req, res) {
  if (req.method === "GET") {
    handleGet(req, res);
  } else {
    res.status(405).send();
  }
}

function handleGet(req, res) {
  res.status(200).json({
    id: 3,
    nome: 'Maria',
    email: 'mariamariamaria@xcfmail.com'
  });
}

/***/ })

};
;

// load runtime
var __webpack_require__ = require("../../webpack-runtime.js");
__webpack_require__.C(exports);
var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
var __webpack_exports__ = (__webpack_exec__(1782));
module.exports = __webpack_exports__;

})();