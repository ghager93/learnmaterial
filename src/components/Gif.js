import Typography from '@mui/material/Typography';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardActionArea from '@mui/material/CardActionArea';
import CardMedia from '@mui/material/CardMedia'

import logo from '../logo.svg';
import testGif from '../tooncasm-test-copy.gif'

const Article = () => {
  return (
    <CardActionArea sx={{ marginBottom: 2}}>
      <Card variant="outlined" sx={{ }}>
        <CardMedia 
          component="img"
          image={testGif}
          alt="gif"
          sx={{ 
            minHeight: "100px",
            maxHeight: "150px",
            width: "100px"
          }}
        />
        <CardContent sx={{ }}>
          <Typography variant="body1" align='left'>
            #GIF #Tag #Here
          </Typography>
        </CardContent>
      </Card>
    </CardActionArea>
  )
}

export default Article;