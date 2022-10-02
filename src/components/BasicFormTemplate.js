import { useState } from "react";

const BasicFormTemplate = (fields) => {
    const [formReturn, setFormReturn] = useState(null);
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(name + " " + email);
    }

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Name:
                <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
            </label>
            <label>
                Email:
                <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
            </label>
            <input type="submit" value="Submit" />
        </form>
    )
}

export default BasicFormTemplate;
