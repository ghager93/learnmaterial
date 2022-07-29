import Typography from '@mui/material/Typography';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardActionArea from '@mui/material/CardActionArea';

import CodeBlock from '@tenon-io/tenon-codeblock';


const CodeSnippet = () => {
  return (
    <CardActionArea sx={{ marginBottom: 2}}>
      <Card variant="outlined" sx={{ display: "flex" }}>
        <CardContent sx={{ flex: "1" }}>
          <Typography variant="h5" align='left'>
            An Article Title
          </Typography>
          <CodeBlock 
            codeString="This is some code."
          />
        </CardContent>
      </Card>
    </CardActionArea>
  )
}

export default CodeSnippet;