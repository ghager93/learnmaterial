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
import NewVideo from "./components/NewVideo";
import UserForm from "./components/UserForm";
import LoginForm from "./components/LoginForm";

export const userContext = React.createContext("");

const currentUser = () => {
  return localStorage.getItem("user") || "No one";
}

const [user, setUser] = React.useState("");

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
  },
  {
    path: '/NewUser',
    component: UserForm
  },
  {
    path: '/NewVideo',
    component: NewVideo
  },
  {
    path: '/signin',
    component: LoginForm
  }
]

function App() {
  return (
    <Router>
      <CssBaseline />
      <userContext.Provider value={{user, setUser}} >
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
      </userContext.Provider>
    </Router>
  );
}

export default App;
