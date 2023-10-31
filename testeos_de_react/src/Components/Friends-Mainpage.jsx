import React from "react";
import Card from './Card';
import data_users from "../Data/data_users";

export default function Friends({ onCardClick }) {

  const handleCardClick = (title) => {
    onCardClick(title);
  };

  const users_list = data_users.map(i => {
    return <Card 
    title={i.name}
    description={i.description}
    onCardClick={handleCardClick} />
  })

  return (
    <div id="left-friends">
      <div id='temporary_chats'>
        <h1>Random Chats Box</h1>
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