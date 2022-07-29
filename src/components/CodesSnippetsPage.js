import { List } from "@mui/material";

import CodeSnippet from "./CodeSnippet";

const CodeSnippetsPage = () => {
  return (
    <List>
      {[...Array(8)].map(() => (
        <CodeSnippet />
      ))}
    </List>
  );
};

export default CodeSnippetsPage;
