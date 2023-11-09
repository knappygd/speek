import React from "react";
import Card from './Card';
import { useEffect, useState } from 'react';
import axios from 'axios';

export default function Friends({ onCardClick, busqueda2 = "", personal_id }) {

  const handleCardClick = (personal_id) => {
    onCardClick(personal_id);
  };

  const baseURL = 'http://127.0.0.1:5000';

  const [data, setData] = useState([]);
  useEffect(() => {
    // Verifica si personal_id no es una cadena vacía antes de hacer la llamada a la API
    if (personal_id !== "") {
      axios.get(`${baseURL}/api/v1/get_users`)
        .then(response => {
          setData(response.data);
        })
        .catch(error => {
          console.error(error);
        });
    }
  }, [personal_id]);  // Asegúrate de que el efecto se ejecute nuevamente cuando personal_id cambie


  const [friends, setFriends] = useState([]);
  useEffect(() => {
    // Verifica si personal_id no es una cadena vacía antes de hacer la llamada a la API
    if (personal_id !== "") {
      axios.get(`${baseURL}/api/v1/list_friends/${personal_id}`)
        .then(response => {
          setFriends(response.data);
        })
        .catch(error => {
          console.error(error);
        });
    }
  }, [personal_id]);  // Asegúrate de que el efecto se ejecute nuevamente cuando personal_id cambie



  const user_friends = [];
  for (const user of data) {
    for (const friend_id of friends)
      if (user.id === friend_id) {
        user_friends.push(user);
      }
  };


  // const filteredUsers = data_users.filter((i) =>
  //  busqueda2 ? i.name.startsWith(busqueda2) : true
  // );  Needs fix

  const users_list = user_friends.map(i => {
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