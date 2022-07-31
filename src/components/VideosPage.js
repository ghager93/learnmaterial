import { Grid } from "@mui/material";

import Video from "./Video";

const VideosPage = () => {
  const videoCode = ['Tn6-PIqc4UM', 'SykxWpFwMGs', 'QO_Jlz1qpDw', 'N4mEzFDjqtA', 'WPvGqX-TXP0', 'Rub-JsjMhWY', '7TF00hJI78Y', '3FkWddODLno'] 
  return (
    <Grid container spacing={2}>
      {[...Array(videoCode.length)].map((_, i) => (
        <Grid item xs={3}>
          <Video id={videoCode[i]} />
        </Grid>
      ))}
    </Grid>
  );
};

export default VideosPage;
