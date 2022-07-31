import * as React from "react";

// import axios from "axios";

import Typography from '@mui/material/Typography';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardActionArea from '@mui/material/CardActionArea';
import CardMedia from '@mui/material/CardMedia'


const axios = require('axios').default;

const Video = ({ id }) => {
  // const id = "D7eFpRf4tac";
  const apikey = "AIzaSyAIfz7XZvmZSmrVqn1X0gb5B2Dhe8hCXoM";
  const apiurl = "https://www.googleapis.com/youtube/v3/videos?id=" + id + "&key=" + apikey + "&part=snippet,contentDetails,statistics,status" ;

  const [title, setTitle] = React.useState([]);

  React.useEffect(() => {
    const fetchData = async () => {
      const response = await axios.get(apiurl);
      setTitle(response.data.items[0].snippet.title);
      console.log(response);
    }

    fetchData();
  }, [apiurl]);

  return (
    <CardActionArea>
      <Card
        variant="outlined"
        align="center"
        sx={{ padding: 0, display: "flex", flexDirection: "column" }}
      >
        <CardMedia
          component="img"
          image={"https://img.youtube.com/vi/" + id + "/mqdefault.jpg"}
          alt="gif"
          sx={{
            flex: "5",
            minHeight: "100px",
            maxHeight: "450px",
            minWidth: "100px",
          }}
        />
        <CardContent sx={{ flex: "1", padding: 1 }}>
          <Typography variant="h5" align="left">
            {title}
          </Typography>
          <Typography variant="body1" align="left">
            #GIF #Tag #Here
          </Typography>
        </CardContent>
      </Card>
    </CardActionArea>
  );
};

export default Video;
