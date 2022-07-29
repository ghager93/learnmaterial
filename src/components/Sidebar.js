import {
  Divider,
  Drawer,
  List,
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Toolbar,
  Typography,
} from "@mui/material";

import InboxIcon from "@mui/icons-material/Inbox";
import MailIcon from "@mui/icons-material/Mail";
import ArticleIcon from '@mui/icons-material/Article';
import CodeIcon from '@mui/icons-material/Code';
import GifIcon from '@mui/icons-material/Gif';
import RedditIcon from '@mui/icons-material/Reddit';
import YouTubeIcon from "@mui/icons-material/YouTube";
import LightbulbIcon from '@mui/icons-material/Lightbulb';

const drawerWidth = 240;

const Sidebar = () => {
  return (
    <Drawer
            sx={{
              width: drawerWidth,
              flexShrink: 0,
              '& .MuiDrawer-paper': {
                width: drawerWidth,
                boxSizing: 'border-box',
              },
            }}
            variant="permanent"
            anchor="left"
          >
            <Toolbar />
            <Divider />
            <List>
              <ListItem key='Articles' disablePadding>
                <ListItemButton>
                  <ListItemIcon>
                    <ArticleIcon />
                  </ListItemIcon>
                  <ListItemText primary='Articles' />
                </ListItemButton>
              </ListItem>
              <ListItem key='Code Snippets' disablePadding>
                <ListItemButton>
                  <ListItemIcon>
                    <CodeIcon />
                  </ListItemIcon>
                  <ListItemText primary='Code Snippets' />
                </ListItemButton>
              </ListItem>  
              <ListItem key='GIFs' disablePadding>
                <ListItemButton>
                  <ListItemIcon>
                    <GifIcon />
                  </ListItemIcon>
                  <ListItemText primary='GIFs' />
                </ListItemButton>
              </ListItem>
              <ListItem key='Reddit' disablePadding>
                <ListItemButton>
                  <ListItemIcon>
                    <RedditIcon />
                  </ListItemIcon>
                  <ListItemText primary='Reddit' />
                </ListItemButton>
              </ListItem>
              <ListItem key='Videos' disablePadding>
                <ListItemButton>
                  <ListItemIcon>
                    <YouTubeIcon />
                  </ListItemIcon>
                  <ListItemText primary='Videos' />
                </ListItemButton>
              </ListItem>
              <ListItem key='Project Ideas' disablePadding>
                <ListItemButton>
                  <ListItemIcon>
                    <LightbulbIcon />
                  </ListItemIcon>
                  <ListItemText primary='Project Ideas' />
                </ListItemButton>
              </ListItem>
            </List>
            <Divider />
    </Drawer>
  );
}

export default Sidebar;