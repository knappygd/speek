import React from "react";
import Card from './Card';
import { useEffect, useState } from 'react';
import axios from 'axios';

export default function Friends({ onCardClick, busqueda2 = "" }) {

  const handleCardClick = (id) => {
    onCardClick(id);
  };

  const baseURL = 'http://127.0.0.1:5000';

  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get(`${baseURL}/test_api/get_users`)
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  // const filteredUsers = data_users.filter((i) =>
  //  busqueda2 ? i.name.startsWith(busqueda2) : true
  // );  Needs fix

  const users_list = data.map(i => {
    return <Card
      title={i.username}
      description={i.desc}
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