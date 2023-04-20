import { LOGIN_SUCCESS, LOGIN_FAIL, LOGOUT } from '../types'

const initialState = {
    isAuthenticated: false,
    user: null,
    token: localStorage.getItem('token'),
    msg: null,
}

const authReducer = (state = initialState, action) => {
    switch (action.type) {
        case LOGIN_SUCCESS:
            localStorage.setItem('token', action.payload.token)
            return {
                ...state,
                isAuthenticated: true,
                user: action.payload.user,
                token: action.payload.token,
                msg: null,
            }
        case LOGIN_FAIL:
            localStorage.removeItem('token')
            return {
                ...state,
                isAuthenticated: false,
                user: null,
                token: null,
                msg: action.payload,
            }
        case LOGOUT:
            localStorage.removeItem('token')
            return {
                ...state,
                isAuthenticated: false,
                user: null,
                token: null,
                msg: null,
            }
        default:
            return state
    }
}

export default authReducer
