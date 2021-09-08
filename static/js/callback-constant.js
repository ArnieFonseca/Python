/**
 * Defines Constants
 */
class Constant {
 
    static HTMLElement = class _ {
        static get cboOperation() { return document.querySelector('#cboOperation'); }
        static get btn() { return document.querySelector('#btn'); }
        static get first() { return document.querySelector('#first'); }
        static get second() { return document.querySelector('#second'); }
        static get result() { return document.querySelector('#result'); }
        static get imgLoader() { return document.querySelector('#imgLoader'); }
    }
    static Value = class _ {
        static get HIDDEN() { return 'hidden'; }
        static get VISIBLE() { return 'visible'; }
        static get ASYNC_DELAY() { return 5000; }
        static get TEN() { return 10;}
        static get KEY_CODE_ZERO() { return 48;}
        static get OPERATION() { return 'operation'; }
        static get NUMERIC_INPUT() {return [...NAVIGATION_CODE_LIST, ...NUMERIC_CODE_LIST]}
    }
}

/**
 * Array of the navigation keys : DEL Left-Arrow, Right-Arrow, HOME, END, and Back-Space
 */
const NAVIGATION_CODE_LIST = [8, 35, 36, 37, 39, 46];

/**
 * Numeric Codes : 48 to 59  1,2,3,...9
 */
const NUMERIC_CODE_LIST = [...Array(Constant.Value.TEN)].map((_, index) => Constant.Value.KEY_CODE_ZERO + index);
