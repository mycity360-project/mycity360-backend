import React from 'react'
import { Button } from 'react-bootstrap'
import { useDispatch } from 'react-redux'
import { logout } from '../redux/actions/authActions'

const Home = () => {
    const dispatch = useDispatch()

    const handleLogout = () => {
        dispatch(logout())
    }

    return (
        <div className="container mt-5">
            <h2>Welcome to the Home screen!</h2>
            <Button variant="primary" onClick={handleLogout}>
                Logout
            </Button>
        </div>
    )
}

export default Home
