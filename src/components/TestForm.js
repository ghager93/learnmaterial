import { useState } from "react";

const TestForm = () => {
    const handleSubmit = (e) => {
        alert('A name was submitted: ' + value);
        e.preventDefault();
    };

    const handleChange = (e) => {
        setValue(e.target.value);
    };

    const [value, setValue] = useState("");

    return (
        <form onSubmit={handleSubmit}>
            <label>
            Name:
            <input type="text" value={value} onChange={handleChange} />
            </label>
            <input type="submit" value="Submit" />
        </form>
    )
}

export default TestForm;