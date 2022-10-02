import { useState } from "react";

const NewUser = (fields) => {
    const [name, setName] = useState("");
    const [password, setPassword] = useState("");
    const [passwordConfirm, setPasswordConfirm] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();

        if(password === passwordConfirm) {
            const requestOptions = {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    'username': name,
                    'email': 'test@email',
                    'password': password
                })
            }
            fetch('api/users', requestOptions)
                .then(response => response.json())
                .then(out => console.log(out))
        }
    }

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Name:
                <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
            </label>
            <br></br>
            <label>
                Password:
                <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
            </label>
            <br></br>
            <label>
                Confirm Password:
                <input type="password" value={passwordConfirm} onChange={(e) => setPasswordConfirm(e.target.value)} />
            </label>
            <input type="submit" value="Submit" />
        </form>
    )
}

export default NewUser;
