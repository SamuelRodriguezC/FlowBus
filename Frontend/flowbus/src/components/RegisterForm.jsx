import React, { useState } from 'react'
import axios from 'axios'
import { registerUser } from '../services/authService'

const RegisterForm = () => {
    const [form, setForm] = useState({
        username: '', 
        email:'',
        password:'',
    })

    const [message, setMessage] = useState('')

    const handleChange = (e) => {
        setForm({...form, [e.target.name]: e.target.value})
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        try {
            const response = await registerUser(form)
            setMessage('Registro Exitoso')
        } catch (error) {
            setMessage('Error en el registro', + (error.response?.data?.username || error.message))
        }
    }
  return (
    <div>
      <form onSubmit={handleSubmit}>
        <div className="">

            {/* NOMBRE DE USUARIO */}
            <label htmlFor="">Username</label>
            <input type="text" name='username' value={form.username} onChange={handleChange}/><br/>

            {/* EMAIL */}
            <label htmlFor="">Email</label>
            <input type="email" name='email' value={form.email} onChange={handleChange}/><br/>

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

export default RegisterForm
