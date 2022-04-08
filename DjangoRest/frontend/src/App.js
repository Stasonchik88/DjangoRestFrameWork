import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/UserList.js';
import axios from 'axios';

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': []
    }
  }
  
  componentDidMount() {
    axios
      .get('http://127.0.0.1:8000/api/users')
      .then(response => {
        let users = response.data
        this.setState({
            'users': users
        })
      })
      .catch(error => console.log(error))
  }
    
  render () {
    return (
      <html>
        <head>
          <title>Список пользователей</title>
        </head>
        <body>
          <div>
            <UserList users={this.state.users} />
          </div>
        </body>
        <footer>
          <b>Copyright 2022</b>
        </footer>
      </html>
    )
  }
}

export default App;
