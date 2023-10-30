import Card from './Card';
import data_users from "../Data/data_users";

export default function Friends() {
  const users_list = data_users.map(i => {
    return <Card title={i.name} description=
      {i.description} />
  })

  return (
    <div id="left-friends">
      <div id='temporary_chats'>
        <h1>ddsfs</h1>
      </div>
      <div id='cont-all'>
        <div id='friendsplus'>
          <div>
            friends
          </div>
        </div>
      <div id='cont'>
          <div id="friends_chats">
            {users_list}
          </div>
        </div>
      </div>
    </div>
  )
}