import { List } from "@mui/material";

import Article from "./Article";
import TestForm from "./TestForm";

const ArticlesPage = () => {
  return (
    <List>
      {[...Array(8)].map(() => (
        <TestForm />
      ))}
    </List>
  );
};

export default ArticlesPage;
