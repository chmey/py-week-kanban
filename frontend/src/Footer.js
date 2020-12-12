import React from 'react';
import { InlineIcon } from '@iconify/react';
import coffee from '@iconify/icons-jam/coffee';
import heart from '@iconify/icons-jam/heart';
import Typography from '@material-ui/core/Typography';
export default function Footer() {
    return (
      <Typography variant="body2" color="textSecondary" align="center">
        {'Made with '}
        <InlineIcon icon={heart} />
        {' + '}
        <InlineIcon icon={coffee} />
        {' in '}
        {new Date().getFullYear()}
        {'.'}
      </Typography>
    );
  }