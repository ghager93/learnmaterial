import { Link } from 'react-router-dom';

import {
  Divider,
  Drawer,
  List,
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Toolbar,
} from "@mui/material";

import ArticleIcon from '@mui/icons-material/Article';
import CodeIcon from '@mui/icons-material/Code';
import GifIcon from '@mui/icons-material/Gif';
import RedditIcon from '@mui/icons-material/Reddit';
import YouTubeIcon from "@mui/icons-material/YouTube";
import LightbulbIcon from '@mui/icons-material/Lightbulb';

const drawerWidth = 240;

const sideBarItems = [
  {
    to: '/Articles',
    text: 'Articles',
    icon: <ArticleIcon />
  },
  {
    to: '/CodeSnippets',
    text: 'Code Snippets',
    icon: <CodeIcon />
  },
  {
    to: '/Gifs',
    text: 'GIFs',
    icon: <GifIcon />
  },
  {
    to: '/Reddit',
    text: 'Reddit',
    icon: <RedditIcon />
  },
  {
    to: '/Videos',
    text: 'Videos',
    icon: <YouTubeIcon />
  },
  {
    to: '/ProjectIdeas',
    text: 'Project Ideas',
    icon: <LightbulbIcon />
  }
]

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
        {sideBarItems.map(({ to, text, icon }) => (
          <ListItem button key={text} disablePadding to={to} component={Link}>
            <ListItemButton>
              <ListItemIcon>
                {icon}
              </ListItemIcon>
              <ListItemText primary={text} />
            </ListItemButton>
          </ListItem>          
        ))}
      </List>
      <Divider />
    </Drawer>
  );
}

export default Sidebar;