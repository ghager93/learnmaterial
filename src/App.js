import * as React from "react";

import {
  AppBar,
  Button,
  Container,
  CssBaseline,
  Divider,
  Drawer,
  Grid,
  IconButton,
  List,
  Paper,
  Toolbar,
  Typography,
} from "@mui/material";

import Header from "./components/Header";
import Sidebar from "./components/Sidebar";
import RightSideBar from "./components/RightSideBar";
import ArticlesPage from "./components/ArticlesPage";

import "./App.css";
import CodeSnippetsPage from "./components/CodesSnippetsPage";

function App() {
  return (
    <React.Fragment>
      <CssBaseline />
      <div className="App">
        <Grid container>
          <Grid item xs="2">
            <Sidebar />
          </Grid>
          <Grid item xs="7">
            <Header />
            <main>
              {/* <ArticlesPage /> */}
              <CodeSnippetsPage />
            </main>
          </Grid>
          <Grid item xs="3">
            <RightSideBar />
          </Grid>
        </Grid>
      </div>
    </React.Fragment>
  );
}

export default App;
