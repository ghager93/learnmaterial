import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import IconButton from "@mui/material/IconButton";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";
import SearchIcon from "@mui/icons-material/Search";
import SettingsIcon from "@mui/icons-material/Settings";
import { Container } from "@mui/system";

const Header = () => {
  return (
    <AppBar position="sticky" sx={{ zIndex: (theme) => theme.zIndex.drawer + 1}}>
      <Toolbar>
        <Typography
          component="h1"
          variant="h4"
          align="center"
          sx={{ flex: "2" }}
        >
          Made With Material.
        </Typography>
        <Container
          align="right"
          sx={{ flex: "1" }}
        >
          <IconButton color="inherit">
            <SettingsIcon />
          </IconButton>
          <Button color="inherit">Sign Up</Button>
          <Button color="inherit">Sign In</Button>
        </Container>
      </Toolbar>
    </AppBar>
  );
};

export default Header;
