import React, { useState, useEffect } from 'react'
import axios from 'axios'

const API = import.meta.env.VITE_API_URL

export default function Dashboard({ token, setToken }) {
  const [rows, setRows] = useState([])
  const [name, setName] = useState("")
  const [email, setEmail] = useState("")

  const fetchData = async () => {
    try {
      const res = await axios.get(`${API}/users`, {
        headers: { Authorization: "Bearer " + token }
      })
      setRows(res.data)
    } catch (err) {
      console.error(err)
    }
  }

  const handleInsert = async () => {
    try {
      await axios.post(`${API}/insert`, {
        name,
        email
      }, {
        headers: { Authorization: "Bearer " + token }
      })
      setName("")
      setEmail("")
      fetchData()
    } catch (err) {
      console.error(err)
    }
  }

  const handleDelete = async (id) => {
    try {
      await axios.delete(`${API}/delete?id=${id}`, {
        headers: { Authorization: "Bearer " + token }
      })
      fetchData()
    } catch (err) {
      console.error(err)
    }
  }

  const handleLogout = () => {
    localStorage.removeItem("token")
    setToken(null)
  }

  useEffect(() => { fetchData() }, [])

  return (
    <div className="p-4">
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-xl font-bold">Dashboard</h1>
        <button className="text-red-600" onClick={handleLogout}>Logout</button>
      </div>

      <div className="mb-6">
        <h2 className="font-semibold mb-2">Add New User</h2>
        <div className="flex gap-2">
          <input className="border p-2" placeholder="Name" value={name} onChange={e => setName(e.target.value)} />
          <input className="border p-2" placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} />
          <button className="bg-green-500 text-white px-4 py-2" onClick={handleInsert}>Add</button>
        </div>
      </div>

      <table className="w-full border">
        <thead>
          <tr className="bg-gray-200">
            <th className="p-2 border">ID</th>
            <th className="p-2 border">Name</th>
            <th className="p-2 border">Email</th>
            <th className="p-2 border">Actions</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((row, i) => (
            <tr key={i} className="border-t">
              <td className="p-2 border">{row[0]}</td>
              <td className="p-2 border">{row[1]}</td>
              <td className="p-2 border">{row[2]}</td>
              <td className="p-2 border">
                <button onClick={() => handleDelete(row[0])} className="text-sm text-red-500">Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
