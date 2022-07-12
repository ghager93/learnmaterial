import * as React from "react";

import {
  AppBar,
  Button,
  Container,
  CssBaseline,
  Divider,
  Drawer,
  IconButton,
  List,
  Paper,
  Stack,
  Toolbar,
  Typography,
} from "@mui/material";

import MenuIcon from "@mui/icons-material/Menu";
import ChevronLeftIcon from "@mui/icons-material/ChevronLeft";

import logo from "./logo.svg";
import "./App.css";

function App() {
  return (
    <React.Fragment>
      <CssBaseline />
      <div className="App">
        <Container maxWidth="lg">
          <AppBar position="sticky">
            <Toolbar>
              <IconButton color="inherit">
                <MenuIcon />
              </IconButton>
              <Typography
                component="h1"
                variant="h4"
                align="center"
                noWrap
                sx={{ flex: 1 }}
              >
                Made With Material.
              </Typography>
              <Button color="inherit">Sign Up</Button>
              <Button color="inherit">Sign In</Button>
            </Toolbar>
          </AppBar>
          <Drawer variant="permanent" open={true}>
            <Toolbar
              sx={{
                display: "flex",
                alignItems: "center",
                justifyContent: "flex-end",
                px: [1],
              }}
            >
              <IconButton>
                <ChevronLeftIcon />
              </IconButton>
            </Toolbar>
            <Divider />
            <List component="nav">
              <Typography>Articles</Typography>
              <Divider sx={{ my: 1 }} />
              <Typography>Projects</Typography>
              <Divider sx={{ my: 1 }} />
              <Typography>Content</Typography>
              <Divider sx={{ my: 1 }} />
            </List>
          </Drawer>
        </Container>
        <Container>
          <List component="nav">
              <Paper>Articles</Paper>
              <Divider sx={{ my: 1 }} />
              <Paper>Projects</Paper>
              <Divider sx={{ my: 1 }} />
              <Paper>Content</Paper>
              <Divider sx={{ my: 1 }} />
            </List>
        </Container>
      </div>
    </React.Fragment>
  );
}

export default App;
