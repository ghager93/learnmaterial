
import SearchBar from "material-ui-search-bar";
import { Button, Container, IconButton } from "@mui/material";

import SettingsIcon from "@mui/icons-material/Settings";
import AddBoxIcon from "@mui/icons-material/AddBox";

import { userContext } from "../App";

const getCurrentUser = () => {
  return localStorage.getItem("user") || "no user";
}

const CurrentUser = () => {
  return (
    <p>Hello {getCurrentUser() || "No-one"}</p>
  );
}

const RightSideBar = () => {
    return (
        <Container sx={{ flex: 1, margin: 0, padding: 5 }}>
          <userContext.Consumer>
            {
              ({user, setUser}) => <p>Hello {user}</p>
            }
          </userContext.Consumer>
          <SearchBar />   
          <Button color="inherit" href={"/NewUser"}>Sign Up</Button>
          <Button color="inherit" href={"/signin"}>Sign In</Button>
          <IconButton color="inherit">
            <SettingsIcon />
          </IconButton>
          <IconButton color="inherit" href={"/NewVideo"}>
            <AddBoxIcon />
          </IconButton>
        </Container>
    )
}

export default RightSideBar;