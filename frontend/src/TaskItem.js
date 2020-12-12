import {
    Card,
    CardContent,
    CardActionArea,
    Typography,
    IconButton
  } from '@material-ui/core';
  import Grid from '@material-ui/core/Grid';
  import { Icon } from '@iconify/react';
  import arrowleft from '@iconify/icons-jam/arrow-left';
  import arrowright from '@iconify/icons-jam/arrow-right';
  import check from '@iconify/icons-jam/check';
  import close from '@iconify/icons-jam/close';
  import { withStyles } from '@material-ui/core/styles';
  import React from 'react';

  const CardTask = withStyles({
    root: {

    }
  })(Card);
  const GridFlexGrow1 = withStyles({
    root: {
        flexGrow: 1,
        "&:nth-child(1)": {
            marginTop: "1em"
        }
    },
  })(Grid);
  
  const CardActionAreaJustified = withStyles({
    root: {
      justifyContent: "space-between",
      display: "flex",
    },
  })(CardActionArea);
  export default class Toggle extends React.Component {
    constructor(props) {
        super(props);
        this.moveLeft = this.moveLeft.bind(this);
        this.moveRight = this.moveRight.bind(this);
        this.toggleCheck = this.toggleCheck.bind(this);
    }

    moveLeft(e) {
        this.props.moveTaskLeft(this.props.id);
        e.preventDefault();
    }
    moveRight(e) {
        this.props.moveTaskRight(this.props.id);
        e.preventDefault();
    }
    toggleCheck(e) {
        this.props.toggleCheck(this.props.id);
        e.preventDefault();
    }    
    render() {
        var middleActionButton;
        if (this.props.completed) {
            middleActionButton = (
                <IconButton onClick={this.toggleCheck} aria-label="move left">
                    <Icon icon={close} />
               </IconButton>
            );
        } else {
            middleActionButton = (
                <IconButton onClick={this.toggleCheck} aria-label="move left">
                    <Icon icon={check} />
                </IconButton>
            );
        }
        return (
            <GridFlexGrow1 item>
                <CardTask style={{textDecoration : this.props.completed ? 'line-through' : 'none' }} variant="outlined"> 
                    <CardContent>
                        {/* <Typography color="textSecondary" variant="subtitle2">
                        {new Date(this.props.dateCreated).toLocaleString()}
                        </Typography> */}
                        <Typography variant="body1">
                        {this.props.title}
                        </Typography>
                        <Typography variant="caption" component="p">
                        {this.props.description}
                        </Typography>
                    </CardContent>
                    <CardActionAreaJustified component={"div"}>
                        <IconButton onClick={this.moveLeft} aria-label="move left">
                            <Icon icon={arrowleft} />
                        </IconButton>
                        {middleActionButton}
                        <IconButton onClick={this.moveRight} aria-label="move right">
                            <Icon icon={arrowright} />
                        </IconButton>
                    </CardActionAreaJustified>
                </CardTask>
            </GridFlexGrow1>
        )
    }
}