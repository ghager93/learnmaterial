import Typography from '@mui/material/Typography';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardActionArea from '@mui/material/CardActionArea';
import CardMedia from '@mui/material/CardMedia'

import logo from '../logo.svg';
import testGif from '../tooncasm-test-copy.gif'

const Gif = () => {
  return (
    <CardActionArea >
      <Card variant="outlined" align="center" sx={{ padding: 0, display: "flex", flexDirection: "column" }}>
        <CardMedia 
          component="img"
          image={testGif}
          alt="gif"
          sx={{ 
            flex: "5",
            minHeight: "100px",
            maxHeight: "450px",
            minWidth: "100px"
          }}
        />
        <CardContent sx={{ flex: "1", padding: 1 }}>
          <Typography variant="body1" align='left'>
            #GIF #Tag #Here
          </Typography>
        </CardContent>
      </Card>
    </CardActionArea>
  )
}

export default Gif;