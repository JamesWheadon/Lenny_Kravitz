import React, { useState } from 'react';
import axios from 'axios'

function SignUp({subscribe}) {

    const [email, setEmail] = useState("")

    const handleSubmit = async (e) => {
        e.preventDefault();
        await axios.post('http://localhost:5000/users', {email: email})
        setEmail("")
        subscribe(true)
    }

    const updateEmail = e => {
        const input = e.target.value
        setEmail(input)
    }

    return (
        <form className="room-form" onSubmit={handleSubmit} role="form">
            <label>Email
                <input type="text" value={email} onChange={updateEmail} />
            </label>
            <button type="submit">Join Mailing List</button>
        </form>
    );
};

export default SignUp;
