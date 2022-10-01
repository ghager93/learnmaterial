import * as React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import {
  CssBaseline,
  Grid,
} from "@mui/material";

import Header from "./components/Header";
import Sidebar from "./components/Sidebar";
import RightSideBar from "./components/RightSideBar";

import "./App.css";
import ArticlesPage from "./components/ArticlesPage";
import CodeSnippetsPage from "./components/CodesSnippetsPage";
import GifsPage from "./components/GifsPage";
import VideosPage from "./components/VideosPage";


const routes = [
  {
    path: '/Articles',
    component: ArticlesPage
  },
  {
    path: '/CodeSnippets',
    component: CodeSnippetsPage
  },
  {
    path: '/Gifs',
    component: GifsPage
  },
  {
    path: '/Videos',
    component: VideosPage
  }
]

function App() {
  return (
    <Router>
      <CssBaseline />
      <div className="App">
        <Grid container>
          <Grid item xs="2">
            <Sidebar />
          </Grid>
          <Grid item xs="7">
            <Header />
            <main>
              <Routes>
                <Route path="/" element={<p>No page!</p>} />
                {routes.map(({path, component: C}) => (
                  <Route key={path} path={path} element={<C />} />
                ))}
              </Routes>
            </main>
          </Grid>
          <Grid item xs="3">
            <RightSideBar />
          </Grid>
        </Grid>
      </div>
    </Router>
  );
}

export default App;
