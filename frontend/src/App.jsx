import React, { useState } from 'react'
import LoginPage from './pages/LoginPage'
import Dashboard from './pages/Dashboard'

export default function App() {
  const [token, setToken] = useState(localStorage.getItem("token"))

  return token ? <Dashboard token={token} setToken={setToken} /> : <LoginPage setToken={setToken} />
}
