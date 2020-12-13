
import React from 'react';
import {TextField, Box, Link, Button, Dialog, DialogActions, DialogContent, DialogContentText, DialogTitle, Typography} from '@material-ui/core';
import MuiAlert from '@material-ui/lab/Alert';

function Alert(props) {
    return <MuiAlert elevation={5} variant="filled" {...props} />;
  }

export default function AuthModal(props) {
    const {isAuthenticated, setAuthenticated} = props;
    const [open, setOpen] = React.useState(!isAuthenticated);
    const [isSignUp, setSignUp] = React.useState(false);
    const [email, setEmail] = React.useState("");
    const [password, setPassword] = React.useState("");
    const [confirmPassword, setConfirmPassword] = React.useState("");
    const [formErrorMessage, setFormErrorMessage] = React.useState("");
    const handleClose = () => {
        setOpen(false);
    };
    const handleSubmit = (e) => {
        if(isSignUp){
            if (password !== confirmPassword)
            {
                setFormErrorMessage('The passwords did not match.')
            }
            try {
                fetch('http://localhost:5000/api/v1/users/', {
                  method: 'POST',
                  headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                  },
                  body: JSON.stringify({data: {email: email, password: password}})
                })
                .then(res => res.json())
                .then(d => console.log(d))
              } catch (error) {
                throw error;
              }  
        } else {
            try {
                fetch('http://localhost:5000/api/v1/auth/login', {
                  method: 'POST',
                  headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                  },
                  body: JSON.stringify({data: {email: email, password: password}})
                })
                .then(res => res.json())
                .then(d => {
                    if (!d.isAuthenticated)
                    {
                        setFormErrorMessage('Login failed.')
                    }
                    else {
                        handleClose();
                    }
                    setAuthenticated(d.data.isAuthenticated);
                    
                })
              } catch (error) {
                throw error;
              }  
        }
        e.preventDefault()
    }
    return (
        <React.Fragment>
            <Dialog open={open} aria-labelledby="auth-dialog-title">
                <DialogTitle id="auth-dialog-title">{isSignUp ? "Register" : "Login"}</DialogTitle>
                <DialogContent>
                    <DialogContentText>
                    <form autoComplete="off">
                    <div>
                        <TextField fullWidth={true} required onChange={e => setEmail(e.target.value)} label="Email Address" placeholder="you@example.com" />
                    </div>
                    <div>
                        <TextField fullWidth={true} type="password" onChange={e => setPassword(e.target.value)} required label="Password" placeholder="hunter2" />
                    </div>
                    {isSignUp ?
                    <div>
                        <TextField fullWidth={true} type="password" onChange={e => setConfirmPassword(e.target.value)} required label="Confirm password" placeholder="hunter2" />
                    </div>
                    : null
                    }
                    
                    </form>
                    { formErrorMessage
                    ? <Box style={{marginTop: "0.5em"}}><Alert severity="error">{formErrorMessage}</Alert></Box>
                    : null
                    }
                </DialogContentText>
                </DialogContent>
                <DialogActions>
                    {isSignUp ?
                    <React.Fragment>
                        <Typography variant="caption">
                            <Link href="#" onClick={() => {setSignUp(false); setFormErrorMessage("")}}>I have an account</Link>
                        </Typography>
                        <Button onClick={handleSubmit} type="submit" variant="contained" color="primary">
                        Register
                        </Button>
                    </React.Fragment>
                    : 
                    <React.Fragment>
                        <Typography variant="caption">
                            <Link href="#" onClick={() => {setSignUp(true); setFormErrorMessage("")}}>Create an account</Link>
                        </Typography>
                        <Button onClick={handleSubmit} type="submit" variant="contained" color="primary">
                        Login
                        </Button>
                    </React.Fragment>
                    }
                    
                </DialogActions>
            </Dialog>
        </React.Fragment>
    )
}