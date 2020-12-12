import React from 'react';
import { Button } from '@material-ui/core';
import TextField from '@material-ui/core/TextField';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';

export default class TaskForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {open: this.props.open, title: '', description: '', weekday: 0}
  }
  handleChange = (event) => {
    this.setState({[event.target.name]: event.target.value});
  }
  
  handleSubmit = (event) => {
    try {
      fetch('http://localhost:5000/api/v1/tasks/', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({data: this.state})
      })
      .then(res => res.json())
      .then(data => this.props.addTask(data.data))
      this.setState({title: '', description: ''});
      this.props.handleClose();
    } catch (error) {
      throw error;
    }  
    event.preventDefault();
  };
  render = () => {
    return (
      <div>
        <Dialog open={this.props.open} onClose={this.props.handleClose} aria-labelledby="form-dialog-title">
          <DialogTitle id="form-dialog-title">Add Task</DialogTitle>
          <DialogContent>
            <DialogContentText></DialogContentText>
              <form autoComplete="off" onChange={this.handleChange}>
              <div>
                  <TextField name="title" required label="Task Title" placeholder="Clean home..." />
              </div>
              <div>
                  <TextField
                      multiline
                      name="description"
                      label="Task"
                      rows={5}
                      placeholder="Hoover the kitchen!"
                      />
              </div>
          </form>
          </DialogContent>
          <DialogActions>
            <Button onClick={this.props.handleClose} color="primary">
              Cancel
            </Button>
            <Button onClick={this.handleSubmit} type="submit" variant="contained" color="primary">
              Add
            </Button>
          </DialogActions>
        </Dialog>
      </div>
    );
  } 
}
        