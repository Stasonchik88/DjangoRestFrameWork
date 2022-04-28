import React from 'react';
import axios from 'axios';
import UserList from './components/UserList.js';
import ProjectList from './components/ProjectList.js';
import ToDoList from './components/ToDoList.js';
import UserToDoList from './components/UserToDo.js';
import {BrowserRouter, Route, Routes, Link, useLocation} from 'react-router-dom'


const NotFound404 = () => {
  var location = useLocation()

  return (
    <div>
      <h1>Страница по адресу "{location.pathname}" не найдена!</h1>
    </div>
  )
}


class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': [],
      'projects': [],
      'todo': []
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
    axios
      .get('http://127.0.0.1:8000/api/projects')
      .then(response => {
        let projects = response.data
        this.setState({
            'projects': projects
        })
      })
      .catch(error => console.log(error))
    axios
      .get('http://127.0.0.1:8000/api/todo')
      .then(response => {
        let todo = response.data
        this.setState({
            'todo': todo
        })
      })
      .catch(error => console.log(error))
  }
    
  render () {
    return (
      <div className='App'>
        <BrowserRouter>
          <nav>
            <ul>
              <li>
                <Link to='/users'>Users</Link>
              </li>
              <li>
                <Link to='/projects'>Projects</Link>
              </li>
              <li>
                <Link to='/todo'>ToDo</Link>
              </li>
            </ul>
          </nav>
          <Routes>
            <Route exact path='/users' element={<UserList users={this.state.users}/>} />
            <Route exact path='/projects' element={<ProjectList items={this.state.projects}/>} />
            <Route exact path='/todo' element={<ToDoList items={this.state.todo}/>} />
            <Route exact path='/user/:id' element={<UserToDoList items={this.state.todo}/>}/>
            <Route path='*' element={<NotFound404/>} />
          </Routes>
        </BrowserRouter>
      </div>
    )
  }
}

export default App;
