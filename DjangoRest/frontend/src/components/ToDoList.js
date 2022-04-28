import React from 'react'

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

const ToDoList = ({items}) => {
    return (
        <table>
            <tr>
                <th>USER</th>
                <th>PROJECT</th>
                <th>DESCRIPTION</th>
                <th>STATUS</th>
            </tr>
            {items.map((item) => <ToDo item={item} />)}
        </table>
    )
}
export default ToDoList