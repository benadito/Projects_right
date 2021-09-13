import  reducer  from './reducers'
import { numberAdd2} from './actions/number'


export const initialState = {
    other: [],
    products: [],
    user: null,
    // foco será nesse atributo...
    number: 0
}

export {
    reducer,
    numberAdd2
}