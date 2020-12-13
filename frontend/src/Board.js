import React from 'react';
import { Container, Box } from '@material-ui/core';
import TaskList from './TaskList';
import Footer from './Footer';
import Header from './Header';
import mockData from './mockData';
import AuthModal from './AuthModal';
export default function Board(props) {
    const { setAuthenticated, isAuthenticated, addTask, archiveTask, toggleCheck, moveTaskLeft, moveTaskRight, tasks} = props;
    return (
          <React.Fragment>
            <Container style={{height: "inherit"}} maxWidth={false}>
              <Header addTask={addTask} isAuthenticated={isAuthenticated} title="kanweek" />
              {
                isAuthenticated
                ? <main><TaskList archiveTask={archiveTask} toggleCheck={toggleCheck} moveTaskLeft={moveTaskLeft} moveTaskRight={moveTaskRight} tasks={tasks}/></main>
                : <main style={{filter: "blur(0.5em)"}}><TaskList tasks={mockData} archiveTask={null} toggleCheck={null} moveTaskLeft={null} moveTaskRight={null}/></main>
              }
              
            </Container>
            <Box width={1} style={{paddingBottom: "0.5em"}}>
                <Footer/>
            </Box>
            <AuthModal setAuthenticated={setAuthenticated} isAuthenticated={isAuthenticated}></AuthModal>
          </React.Fragment>
    )
}