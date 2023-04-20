import React from 'react'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'
import Login from './components/Login'
import Home from './components/Home'
import PrivateRoute from './components/PrivateRoute'
import { useSelector } from 'react-redux'

const App = () => {
    const isAuthenticated = useSelector((state) => state.auth.isAuthenticated)

    return (
        <Router>
            <div className="container">
                <Switch>
                    <PrivateRoute
                        exact
                        path="/"
                        component={Home}
                        isAuthenticated={isAuthenticated}
                    />
                    <Route exact path="/login" component={Login} />
                </Switch>
            </div>
        </Router>
    )
}

export default App
