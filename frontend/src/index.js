<<<<<<< Updated upstream
import React from 'react'
import ReactDOM from 'react-dom'
import reportWebVitals from './reportWebVitals'

import App from './App'
import './index.css'

ReactDOM.render(<App />, document.getElementById('root'))
=======
import React from "react";
import ReactDOM from "react-dom/client";
import "bootstrap/dist/css/bootstrap.min.css";
import "./index.css";
import App from "./App";

import reportWebVitals from "./reportWebVitals";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
>>>>>>> Stashed changes

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
<<<<<<< Updated upstream
reportWebVitals()
=======
reportWebVitals();
>>>>>>> Stashed changes
