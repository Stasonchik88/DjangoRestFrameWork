import React from 'react'
import {useParams} from 'react-router-dom'

const ToDo = ({item}) => {
    return (
    <tr>
        <td>{item.user}</td>
        <td>{item.project}</td>
        <td>{item.description}</td>
        <td>{item.status}</td>
    </tr>
    )
}

const UserToDoList = ({items}) => {
    var {id} = useParams()
    var filtered_items = items.filter((item) => item.user.includes(parseInt(id)))

    return (
        <table>
            <tr>
                <th>USER</th>
                <th>PROJECT</th>
                <th>DESCRIPTION</th>
                <th>STATUS</th>
            </tr>
            {filtered_items.map((item) => <ToDo item={item} />)}
        </table>
    )
}
export default UserToDoList