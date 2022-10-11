import SearchBar from "material-ui-search-bar";
import { Button, Container, IconButton } from "@mui/material";

import SettingsIcon from "@mui/icons-material/Settings";
import AddBoxIcon from "@mui/icons-material/AddBox";

const RightSideBar = () => {
    return (
        <Container sx={{ flex: 1, margin: 0, padding: 5 }}>
          <SearchBar />   
          <Button color="inherit" href={"/NewUser"}>Sign Up</Button>
          <Button color="inherit">Sign In</Button>
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