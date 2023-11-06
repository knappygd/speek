import React from "react";
import Card from './Card';
import data_users from "../Data/data_users";

export default function Friends({ onCardClick, busqueda2 = "" }) {

  const handleCardClick = (id) => {
    onCardClick(id);
  };

  const filteredUsers = data_users.filter((i) =>
    busqueda2 ? i.name.startsWith(busqueda2) : true
  );

  const users_list = filteredUsers.map((i) => {
    return <Card
      title={i.name}
      description={i.description}
      user_id={i.id}
      onCardClick={handleCardClick}
    />
  })

  return (
    <div id="left-friends">
      <div id='temporary_chats'>
        <div id="people">
          <div id="randomchatbutton">
            <button id="randomchat">Random Chat</button>
            <div id="stick">
              <select name="languages" id="languageRCB">
                <option value="eng" id="options">ENG</option>
                <option value="esp" id="options">ESP</option>
              </select>
            </div>
          </div>
        </div>
      </div>
      <div id='cont-all'>
        <div id='friendsplus'>
          <div>
            Friends
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