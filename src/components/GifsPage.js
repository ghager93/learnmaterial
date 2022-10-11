import { Grid } from "@mui/material";

import Gif from "./Gif";

const GifsPage = () => {
  return (
    <Grid container spacing={2}>
      {[...Array(8)].map(() => (
        <Grid item xs={3}>
          <Gif />
        </Grid>
      ))}
    </Grid>
  );
};

export default GifsPage;
