import { List } from "@mui/material";

import Article from "./Article";

const ArticlesPage = () => {
  return (
    <List>
      {[...Array(8)].map(() => (
        <Article />
      ))}
    </List>
  );
};

export default ArticlesPage;
