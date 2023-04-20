import React, { useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { login } from '../redux/actions/authActions'
import { useHistory } from 'react-router-dom'
import { Alert } from 'react-bootstrap'

const Login = () => {
    const dispatch = useDispatch()
    const history = useHistory()
    const [formData, setFormData] = useState({
        email: '',
        password: '',
    })
    const isAuthenticated = useSelector((state) => state.auth.isAuthenticated)
    const msg = useSelector((state) => state.auth.msg)

    const { email, password } = formData

    const handleChange = (e) =>
        setFormData({ ...formData, [e.target.name]: e.target.value })

    const handleSubmit = (e) => {
        e.preventDefault()
        dispatch(login(email, password))
    }

    if (isAuthenticated) {
        history.push('/')
    }

    return (
        <div className="row mt-5">
            <div className="col-md-6 m-auto">
                <div className="card card-body">
                    <h1 className="text-center mb-3">
                        <i className="fas fa-sign-in-alt"></i> Login
                    </h1>
                    {msg ? <Alert variant="danger">{msg}</Alert> : null}
                    <form onSubmit={handleSubmit}>
                        <div className="form-group">
                            <label htmlFor="email">Email</label>
                            <input
                                type="email"
                                id="email"
                                name="email"
                                className="form-control"
                                placeholder="Enter Email"
                                value={email}
                                onChange={handleChange}
                                required
                            />
                        </div>
                        <div className="form-group">
                            <label htmlFor="password">Password</label>
                            <input
                                type="password"
                                id="password"
                                name="password"
                                className="form-control"
                                placeholder="Enter Password"
                                value={password}
                                onChange={handleChange}
                                required
                            />
                        </div>
                        <button
                            type="submit"
                            className="btn btn-primary btn-block"
                        >
                            Login
                        </button>
                    </form>
                </div>
            </div>
        </div>
    )
}

export default Login
