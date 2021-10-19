exports.id = 32;
exports.ids = [32];
exports.modules = {

/***/ 8891:
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Z": () => (/* binding */ Layout)
/* harmony export */ });
/* harmony import */ var next_link__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(1664);
/* harmony import */ var _styles_Layout_module_css__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(5803);
/* harmony import */ var _styles_Layout_module_css__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_styles_Layout_module_css__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(5282);
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_1__);




function Layout(props) {
  var _props$titulo;

  return /*#__PURE__*/(0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_1__.jsxs)("div", {
    className: (_styles_Layout_module_css__WEBPACK_IMPORTED_MODULE_2___default().layout),
    children: [/*#__PURE__*/(0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_1__.jsxs)("div", {
      className: (_styles_Layout_module_css__WEBPACK_IMPORTED_MODULE_2___default().cabecalho),
      children: [/*#__PURE__*/react_jsx_runtime__WEBPACK_IMPORTED_MODULE_1__.jsx("h1", {
        children: (_props$titulo = props.titulo) !== null && _props$titulo !== void 0 ? _props$titulo : 'Mais um exemplo'
      }), /*#__PURE__*/react_jsx_runtime__WEBPACK_IMPORTED_MODULE_1__.jsx(next_link__WEBPACK_IMPORTED_MODULE_0__.default, {
        href: "/",
        children: " Voltar "
      })]
    }), /*#__PURE__*/react_jsx_runtime__WEBPACK_IMPORTED_MODULE_1__.jsx("div", {
      className: (_styles_Layout_module_css__WEBPACK_IMPORTED_MODULE_2___default().conteudo),
      children: props.children
    })]
  });
}

/***/ }),

/***/ 5803:
/***/ ((module) => {

// Exports
module.exports = {
	"layout": "Layout_layout__3byAJ",
	"cabecalho": "Layout_cabecalho__2UOBy",
	"conteudo": "Layout_conteudo__2xisD"
};


/***/ }),

/***/ 2431:
/***/ (() => {

/* (ignored) */

/***/ })

};
;