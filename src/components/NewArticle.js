import { useState } from "react";
import { useNavigate } from "react-router-dom";

const NewVideo = () => {
    const [name, setName] = useState("");
    const [youtubeId, setYoutubeId] = useState("");

    const url = "https://www.youtube.com/watch?v=" + youtubeId;

    const navigate = useNavigate();

    const handleSubmit = (e) => {
        e.preventDefault();

        const requestOptions = {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                'username': 'username',
                'name': name,
                'youtube_id': youtubeId,
                'url': url
            })
        }

        fetch('api/videos', requestOptions)
            .then(response => response.json())
            .then(out => console.log(out));
        navigate('/Videos');
    }

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Name:
                <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
            </label>
            <br></br>
            <label>
                Youtube ID:
                <input type="text" value={youtubeId} onChange={(e) => setYoutubeId(e.target.value)} />
            </label>
            <br></br>
            <input type="submit" value="Submit" />
        </form>
    )
}

export default NewVideo;
