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
    <AppBar position="sticky" sx={{ zIndex: (theme) => theme.zIndex.drawer + 1, color: "inherit"}}>
      <Toolbar>
        <Typography
          component="h1"
          variant="h4"
          align="center"
          sx={{ flex: "2", color: "white" }}
        >
          Made With Material.
        </Typography>
      </Toolbar>
    </AppBar>
  );
};

export default Header;
