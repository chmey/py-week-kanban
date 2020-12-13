import React from 'react';
import { InlineIcon } from '@iconify/react';
import coffee from '@iconify/icons-jam/coffee';
import heart from '@iconify/icons-jam/heart';
import Typography from '@material-ui/core/Typography';
import { Link } from 'react-router-dom';
export default function Footer() {
    return (
      <div>
        <Typography variant="body2" color="textSecondary" align="center">
          {'Made with '}
          <InlineIcon icon={heart} />
          {' + '}
          <InlineIcon icon={coffee} />
          {' in '}
          {new Date().getFullYear()}
          {'.'}
        </Typography>
        <Typography component="div" variant="caption" color="textSecondary" align="center">
          <Link to="/about">About</Link>  
        </Typography>
      </div>
    );
  }