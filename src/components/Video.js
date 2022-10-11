import * as React from "react";

// import axios from "axios";

import Typography from '@mui/material/Typography';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardActionArea from '@mui/material/CardActionArea';
import CardMedia from '@mui/material/CardMedia'


const Video = ({ data }) => {
  return (
    <CardActionArea>
      <Card
        variant="outlined"
        align="center"
        sx={{ padding: 0, display: "flex", flexDirection: "column" }}
      >
        <CardMedia
          component="img"
          image={ data.thumbnail_link }
          alt={ data.youtube_id }
          sx={{
            flex: "5",
            minHeight: "100px",
            maxHeight: "450px",
            minWidth: "100px",
          }}
        />
        <CardContent sx={{ flex: "1", padding: 1 }}>
          <Typography variant="h5" align="left">
            { data.title }
          </Typography>
          <Typography variant="body1" align="left">
            { data.tags }
          </Typography>
        </CardContent>
      </Card>
    </CardActionArea>
  );
};

export default Video;
