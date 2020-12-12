import {
    Card,
    CardContent,
    CardHeader,
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
  import archive from '@iconify/icons-jam/archive';
  import { withStyles } from '@material-ui/core/styles';
  import React, { Component } from 'react';
  import { format, parseISO } from 'date-fns';

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
        this.archiveTask = this.archiveTask.bind(this);
    }
    printDueDate() {
        return 'Due: ' + format(parseISO(this.props.dateDue), 'dd MMMM yyyy, HH:mm');
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
    archiveTask(e) {
        this.props.archiveTask(this.props.id);
        e.preventDefault();
    }    
    render() {
        var middleActionButton;
        if (this.props.completed) {
            middleActionButton = (
                <IconButton color={'secondary'} onClick={this.toggleCheck} aria-label="uncheck task">
                    <Icon icon={close} />
               </IconButton>
            );
        } else {
            middleActionButton = (
                <IconButton color={'primary'} onClick={this.toggleCheck} aria-label="check task">
                    <Icon icon={check} />
                </IconButton>
            );
        }
        return (
            <GridFlexGrow1 item>
                <CardTask style={{textDecoration : this.props.completed ? 'line-through' : 'none' }} variant="outlined"> 
                    <CardHeader 
                        action={
                            this.props.completed ?
                            <IconButton size={'small'} color={'secondary'} onClick={this.archiveTask} aria-label="archive task">
                                <Icon icon={archive} />
                            </IconButton>
                            : undefined
                        }
                        title={this.props.title}
                        titleTypographyProps={{'variant': 'body1'}}
                        subheader={
                            this.props.dateDue ?
                            this.printDueDate()
                            : undefined
                        }
                        subheaderTypographyProps={{'variant': 'caption'}}
                    >
                    </CardHeader>
                    { 
                    this.props.description ?
                    <CardContent>
                        <Typography variant="caption" component="p">
                        {this.props.description}
                        </Typography>
                    </CardContent>
                    : undefined
                    }
                    <CardActionAreaJustified component={"div"}>
                        <IconButton color={'primary'} onClick={this.moveLeft} aria-label="move left">
                            <Icon icon={arrowleft} />
                        </IconButton>
                        {middleActionButton}
                        <IconButton color={'primary'} onClick={this.moveRight} aria-label="move right">
                            <Icon icon={arrowright} />
                        </IconButton>
                    </CardActionAreaJustified>
                </CardTask>
            </GridFlexGrow1>
        )
    }
}