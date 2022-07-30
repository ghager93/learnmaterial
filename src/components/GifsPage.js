import { Grid } from "@mui/material";

import Gif from "./Gif";

const GifsPage = () => {
  return (
    <Grid container>
      {[...Array(8)].map(() => (
        <Grid item xs={3} >
          <Gif />
        </Grid>
      ))}
    </Grid>
  );
};

export default GifsPage;
