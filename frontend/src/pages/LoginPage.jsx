import React, { useState } from 'react'
import axios from 'axios'

const API = import.meta.env.VITE_API_URL

export default function LoginPage({ setToken }) {
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")
  const [error, setError] = useState("")

  const handleLogin = async () => {
    try {
      const res = await axios.post(`${API}/login`, { username, password })
      localStorage.setItem("token", res.data.token)
      setToken(res.data.token)
    } catch (err) {
      setError("Login failed")
    }
  }

  return (
    <div className="h-screen flex items-center justify-center bg-gray-50">
      <div className="p-8 bg-white rounded shadow-md w-full max-w-md">
        <h2 className="text-2xl mb-4 font-bold">Login</h2>
        <input className="border p-2 w-full mb-4" placeholder="Username" value={username} onChange={e => setUsername(e.target.value)} />
        <input className="border p-2 w-full mb-4" placeholder="Password" type="password" value={password} onChange={e => setPassword(e.target.value)} />
        <button className="bg-blue-500 text-white px-4 py-2 w-full" onClick={handleLogin}>Login</button>
        {error && <p className="text-red-500 mt-2">{error}</p>}
      </div>
    </div>
  )
}
