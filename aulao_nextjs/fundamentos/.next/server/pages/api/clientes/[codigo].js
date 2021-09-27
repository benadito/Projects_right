"use strict";
/*
 * ATTENTION: An "eval-source-map" devtool has been used.
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file with attached SourceMaps in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(() => {
var exports = {};
exports.id = "pages/api/clientes/[codigo]";
exports.ids = ["pages/api/clientes/[codigo]"];
exports.modules = {

/***/ "./src/pages/api/clientes/[codigo].js":
/*!********************************************!*\
  !*** ./src/pages/api/clientes/[codigo].js ***!
  \********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (/* binding */ handler)\n/* harmony export */ });\nfunction handler(req, res) {\n  const codigo = req.query.codigo;\n  res.status(200).json({\n    id: codigo,\n    nome: `Maria ${codigo}`,\n    email: `mariamariamaria${codigo}@xcfmail.com`\n  });\n}//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvcGFnZXMvYXBpL2NsaWVudGVzL1tjb2RpZ29dLmpzLmpzIiwibWFwcGluZ3MiOiI7Ozs7QUFBZSxTQUFTQSxPQUFULENBQWlCQyxHQUFqQixFQUFzQkMsR0FBdEIsRUFBMEI7QUFDckMsUUFBTUMsTUFBTSxHQUFHRixHQUFHLENBQUNHLEtBQUosQ0FBVUQsTUFBekI7QUFDQUQsRUFBQUEsR0FBRyxDQUFDRyxNQUFKLENBQVcsR0FBWCxFQUFnQkMsSUFBaEIsQ0FBcUI7QUFDakJDLElBQUFBLEVBQUUsRUFBRUosTUFEYTtBQUVqQkssSUFBQUEsSUFBSSxFQUFHLFNBQVFMLE1BQU8sRUFGTDtBQUdqQk0sSUFBQUEsS0FBSyxFQUFHLGtCQUFpQk4sTUFBTztBQUhmLEdBQXJCO0FBS0giLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9mdW5kYW1lbnRvcy8uL3NyYy9wYWdlcy9hcGkvY2xpZW50ZXMvW2NvZGlnb10uanM/ZGMzNiJdLCJzb3VyY2VzQ29udGVudCI6WyJleHBvcnQgZGVmYXVsdCBmdW5jdGlvbiBoYW5kbGVyKHJlcSwgcmVzKXtcbiAgICBjb25zdCBjb2RpZ28gPSByZXEucXVlcnkuY29kaWdvXG4gICAgcmVzLnN0YXR1cygyMDApLmpzb24oe1xuICAgICAgICBpZDogY29kaWdvLFxuICAgICAgICBub21lOiBgTWFyaWEgJHtjb2RpZ299YCxcbiAgICAgICAgZW1haWw6IGBtYXJpYW1hcmlhbWFyaWEke2NvZGlnb31AeGNmbWFpbC5jb21gXG4gICAgfSlcbn0iXSwibmFtZXMiOlsiaGFuZGxlciIsInJlcSIsInJlcyIsImNvZGlnbyIsInF1ZXJ5Iiwic3RhdHVzIiwianNvbiIsImlkIiwibm9tZSIsImVtYWlsIl0sInNvdXJjZVJvb3QiOiIifQ==\n//# sourceURL=webpack-internal:///./src/pages/api/clientes/[codigo].js\n");

/***/ })

};
;

// load runtime
var __webpack_require__ = require("../../../webpack-runtime.js");
__webpack_require__.C(exports);
var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
var __webpack_exports__ = (__webpack_exec__("./src/pages/api/clientes/[codigo].js"));
module.exports = __webpack_exports__;

})();