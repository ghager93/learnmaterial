import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardActionArea from '@mui/material/CardActionArea';
import CardMedia from '@mui/material/CardMedia'

import logo from '../logo.svg';

const Article = () => {
  return (
    <CardActionArea sx={{ marginBottom: 2}}>
      <Card variant="outlined" sx={{ display: "flex" }}>
        <CardContent sx={{ flex: "3" }}>
          <Typography variant="h5" align='left'>
            An Article Title
          </Typography>
          <Typography variant="subtitle1" align='left'>
            This is a short subtitle.
          </Typography>
        </CardContent>
        <CardMedia 
          component="img"
          image={logo}
          alt="react-logo"
          sx={{ 
            flex: "1",
            minHeight: "100px",
            maxHeight: "150px",
            width: "100px"
          }}
        />
      </Card>
    </CardActionArea>
  )
}

export default Article;