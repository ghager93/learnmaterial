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

import Header from './components/Header';
import Article from './components/Article';
import Sidebar from './components/Sidebar';
import RightSideBar from "./components/RightSideBar";

import "./App.css";

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
              <List>
                {[...Array(8)].map(() => <Article />)}
              </List>
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
