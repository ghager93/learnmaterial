import { useState, useEffect } from "react";

import { Grid } from "@mui/material";

import Video from "./Video";

const VideosPage = () => {
  const videoCode = ['Tn6-PIqc4UM', 'SykxWpFwMGs', 'QO_Jlz1qpDw', 'N4mEzFDjqtA', 'WPvGqX-TXP0', 'Rub-JsjMhWY', '7TF00hJI78Y', '3FkWddODLno']; 

  const getVideos = async () => {
    const videos = await fetch('/api/videos')
      .then(resp => resp.json())
      .then(payload => payload['data']['items'])

    return videos;
  }

  const [videos, setVideos] = useState([]);

  useEffect(() => {
    fetch('/api/videos')
      .then(resp => resp.json())
      .then(payload => setVideos(payload['data']['items']));
  }, [])

  return (
    <Grid container spacing={2}>
      {[...Array(videos.length)].map((_, i) => (
        <Grid item xs={3}>
          <Video data={videos[i]} />
        </Grid>
      ))}
    </Grid>
  );
};

export default VideosPage;
