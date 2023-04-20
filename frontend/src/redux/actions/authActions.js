import axios from 'axios'
import { LOGIN_SUCCESS, LOGIN_FAIL, LOGOUT } from '../types'

export const login = (email, password) => async (dispatch) => {
    try {
        const res = await axios.post(
            'http://68.178.167.183/api/v1/user/login/',
            { email, password },
            {
                headers: {
                    clientid: 'IwVuiUsLcQmZ9eTpzf6RYgPCUDxWjdmDPTWMCMRH',
                },
            }
        )
        dispatch({
            type: LOGIN_SUCCESS,
            payload: res.data,
        })
    } catch (err) {
        dispatch({
            type: LOGIN_FAIL,
            payload: err.response.data.msg,
        })
    }
}

export const logout = () => (dispatch) => {
    dispatch({
        type: LOGOUT,
    })
}
