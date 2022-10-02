import { List } from "@mui/material";

import Article from "./Article";
import BasicFormTemplate from "./BasicFormTemplate";
import TestForm from "./TestForm";

const ArticlesPage = () => {
  return (
    <List>
      {[...Array(8)].map(() => (
        <BasicFormTemplate />
      ))}
    </List>
  );
};

export default ArticlesPage;
