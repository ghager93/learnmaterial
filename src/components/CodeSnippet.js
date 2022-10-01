import Typography from '@mui/material/Typography';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardActionArea from '@mui/material/CardActionArea';

import CodeBlock from '@tenon-io/tenon-codeblock';


const CodeSnippet = () => {
  const helloString = `const HelloWorld = () => {
  console.log('Hello World!')
  
  return true;
}`

  return (
    <CardActionArea sx={{ marginBottom: 2}}>
      <Card variant="outlined" sx={{ display: "flex" }}>
        <CardContent sx={{ flex: "1" }}>
          <Typography variant="h5" align='left'>
            A Code Snippet Title
          </Typography>
          <CodeBlock 
            codeString={helloString}
          />
        </CardContent>
      </Card>
    </CardActionArea>
  )
}

export default CodeSnippet;