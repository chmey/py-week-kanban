import {Typography } from '@material-ui/core';
import Grid from '@material-ui/core/Grid';
import TaskItem from './TaskItem';
import { withStyles } from '@material-ui/core/styles';
export default function TaskList(props) {
    const { tasks, moveTaskLeft, moveTaskRight, toggleCheck } = props;
    const GridWeek = withStyles({
        root: {

        }
    })(Grid);
    const GridDay = withStyles({
        root: {
          borderRadius: 3,
          color: 'white',
          justifyContent: "center",
        }
      })(Grid);
      const GridTaskList = withStyles({
        root: {
            justifyContent: "center",
          }
      })(Grid);
      const GridHeader = withStyles({
        root: {
            justifyContent: "center",
          }
      })(Grid);
    return (
        <GridWeek alignItems="flex-start" wrap="nowrap" container spacing={0}>
            {
                [...Array(8)].map((e, i) => (
                    <GridDay key={i} container item>
                        <GridHeader item>
                            <Typography color={"textPrimary"} variant={"h5"} component={"h5"}>{weekdays[i]}</Typography>
                        </GridHeader>
                        <GridTaskList container item>
                            {tasks
                            .filter(task => task.weekday === i)
                            .map((task) => {
                                return <TaskItem toggleCheck={toggleCheck} moveTaskLeft={moveTaskLeft} moveTaskRight={moveTaskRight} key={task.id} {...task} />
                            })}
                        </GridTaskList>
                    </GridDay>
                ))
            }
        </GridWeek>
    )
}

const weekdays = ['Open', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];