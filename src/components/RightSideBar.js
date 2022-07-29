import SearchBar from "material-ui-search-bar";
import { Button, Container } from "@mui/material";

const RightSideBar = () => {
    return (
        <Container sx={{ flex: 1, margin: 0, padding: 5 }}>
          <SearchBar />   
          <Button color="inherit">Sign Up</Button>
          <Button color="inherit">Sign In</Button>
        </Container>
    )
}

export default RightSideBar;