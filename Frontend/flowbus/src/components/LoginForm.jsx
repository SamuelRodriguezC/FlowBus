import React, { useState } from 'react'
import axios from 'axios'
import { registerUser, loginUser } from '../services/authService'


const LoginForm = () => {
    const [form, setForm] = useState({
        username: '', 
        password:'',
    })

    const [message, setMessage] = useState('')

    const handleChange = (e) => {
        setForm({...form, [e.target.name]: e.target.value})
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        try {
            const response = await loginUser(form)
            setMessage('Login Exitoso')
        } catch (error) {
            setMessage('Error en el Login')
        }
    }
  return (
    <div>
      <form onSubmit={handleSubmit}>
        <div className="">

            {/* NOMBRE DE USUARIO */}
            <label htmlFor="">Username</label>
            <input type="text" name='username' value={form.username} onChange={handleChange}/><br/>

            {/* CONTRASEÑA */}
            <label htmlFor="">Password</label>
            <input type="password" name='password' value={form.password} onChange={handleChange}/><br/>

            <button type='submit'>Registrarme</button>
            {message && <p>{message}</p>}
        </div>
      </form>
    </div>
    
  )
}

export default LoginForm
