
import React, {Component} from 'react';
import 'fontsource-roboto';
import { BrowserRouter, Route, Switch} from 'react-router-dom';
import About from './About';
import Board from './Board';

export default class App extends Component {
  constructor(props) {
    super(props);
    this.addTask = this.addTask.bind(this);
    this.moveTaskLeft = this.moveTaskLeft.bind(this);
    this.moveTaskRight = this.moveTaskRight.bind(this);
    this.toggleTaskCompleted = this.toggleTaskCompleted.bind(this);
    this.archiveTask = this.archiveTask.bind(this);
  }
  state = {
    tasks: [],
    isAuthenticated: false,
  }
  addTask(task) {
    this.setState((state, props) => ({
      tasks: [...state.tasks, task]
    }));
  }
  updateTask(task) {
    fetch(`http://localhost:5000/api/v1/tasks/${task.id}`, {
      method: 'PUT',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({data: task})
    })
    .catch(console.log);
  }
  toggleTaskCompleted(taskId) {
    this.setState((state, props) => {
      let updatedTasks = [...state.tasks];
      const taskIndex = this.state.tasks.findIndex(element => element.id === taskId )
      let task = {...updatedTasks[taskIndex]}
      task.completed = !task.completed;
      updatedTasks[taskIndex] = task;
      this.updateTask(task);
      return {tasks: updatedTasks};
    });
  }
  moveTaskLeft(taskId) {
    this.setState((state, props) => {
      let updatedTasks = [...state.tasks];
      const taskIndex = this.state.tasks.findIndex(element => element.id === taskId )
      let task = {...updatedTasks[taskIndex]}
      task.weekday = task.weekday > 0 ? task.weekday - 1 : task.weekday;
      updatedTasks[taskIndex] = task;
      this.updateTask(task);
      return {tasks: updatedTasks};
    });
  }
  moveTaskRight(taskId) {
    this.setState((state, props) => {
      let updatedTasks = [...state.tasks];
      const taskIndex = this.state.tasks.findIndex(element => element.id === taskId )
      let task = {...updatedTasks[taskIndex]}
      task.weekday = task.weekday < 7 ? task.weekday + 1 : task.weekday;
      updatedTasks[taskIndex] = task;
      this.updateTask(task);
      return {tasks: updatedTasks};
    });
  }
  archiveTask(taskId) {
    this.setState((state, props) => {
      let updatedTasks = [...state.tasks];
      const taskIndex = this.state.tasks.findIndex(element => element.id === taskId )
      let task = {...updatedTasks[taskIndex]}
      task.archived = true;
      updatedTasks[taskIndex] = task;
      this.updateTask(task);
      return {tasks: updatedTasks};
    });
  }
  componentDidMount(){
    fetch('http://localhost:5000/api/v1/tasks/')
    .then(res => res.json())
    .then((data) => {
      let tasks = data.data;
      this.setState({ tasks: tasks});
    })
    .catch(console.log);
  }
  render() {
    return (
      <BrowserRouter>
        <Switch>
          <Route exact path='/'>
            <Board addTask={this.addTask} 
              title={"kanweek"} 
              archiveTask={this.archiveTask} 
              toggleCheck={this.toggleTaskCompleted} 
              moveTaskLeft={this.moveTaskLeft} 
              moveTaskRight={this.moveTaskRight} 
              tasks={this.state.tasks}
              isAuthenticated={this.state.isAuthenticated}
              setAuthenticated={(authStatus) => this.setState((state) =>  { return {isAuthenticated: authStatus}})}
                />
          </Route>
          <Route exact path='/about'>
            <About />
          </Route>

        </Switch>
      </BrowserRouter>
    )
  }
};

