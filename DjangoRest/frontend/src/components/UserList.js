import React from 'react'
import { Link } from 'react-router-dom'

const UserItem = ({user}) => {
    return (
        <tr>
            <td>
                <Link to={`/user/${user.id}`}>{user.id}</Link>
            </td>
            <td>
                {user.username}
            </td>
            <td>
                {user.first_name}
            </td>
            <td>
                {user.last_name}
            </td>
            <td>
                {user.email}
            </td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table>
            <th>
                id
            </th>
            <th>
                Username
            </th>
            <th>
                Firstname
            </th>
            <th>
                Lastname
            </th>
            <th>
                email
            </th>
            {users.map((user) => <UserItem user={user} />)}
        </table>
        )
    }
    export default UserList