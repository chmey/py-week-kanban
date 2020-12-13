import React from 'react';
import PropTypes from 'prop-types';
import Toolbar from '@material-ui/core/Toolbar';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import TaskForm from './Form';


export default function Header(props) {
  const {addTask, title, isAuthenticated } = props;
  const [open, setOpen] = React.useState(false);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  return (
    <React.Fragment>
      <Toolbar>
        <Typography
          style={{marginRight: "1em"}}
          component="h2"
          variant="h4"
          align="center"
          noWrap
          >
          {title}
        </Typography>
        {
          isAuthenticated ?
            <Button  onClick={handleClickOpen} variant="contained" color="primary">
              Add Task
            </Button>
          : null
        }
      </Toolbar>
      <TaskForm handleClose={handleClose} open={open} addTask={addTask}/>
    </React.Fragment>
  );
}

Header.propTypes = {
  title: PropTypes.string,
};