import React from "react";
import Card from './Card';
import CardRandom from "./CardRandom";
import { useEffect, useState } from 'react';
import axios from 'axios';

export default function Friends({ onCardClick, busqueda2 = "", personal_id }) {

  const handleCardClick = (personal_id) => {
    onCardClick(personal_id);
  };

  const baseURL = 'http://127.0.0.1:5000';

  const [data, setData] = useState([]);
  useEffect(() => {
    if (personal_id !== "") {
      axios.get(`${baseURL}/api/v1/get_users`)
        .then(response => {
          setData(response.data);
        })
        .catch(error => {
          console.error(error);
        });
    }
  }, [personal_id]);


  const [friends, setFriends] = useState([]);
  useEffect(() => {
    if (personal_id !== "") {
      axios.get(`${baseURL}/api/v1/list_friends/${personal_id}`)
        .then(response => {
          setFriends(response.data);
        })
        .catch(error => {
          console.error(error);
        });
    }
  }, [personal_id]);


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

  const [random_id, setRandom] = useState("");
  const handleRandom = () => {
    axios.get(`${baseURL}/api/v1/get_random_chat`)
      .then(response => {
        setRandom(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  };
  const [random_list, setRandomList] = useState("");
  useEffect(() => {
    if (personal_id !== "") {
      axios.get(`${baseURL}/api/v1/list_random/${personal_id}`)
        .then(response => {
          setRandomList(response.data);
        })
        .catch(error => {
          console.error(error);
        });
    }
  }, [personal_id]);

  const user_random = [];
  for (const user of data) {
    for (const random of random_list)
      if (user.id === random) {
        user_random.push(user);
      }
  };
  const list_random = user_random.map(i => {
    return <CardRandom
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
            <button id="randomchat" onClick={handleRandom}>Random Chat</button>
            <div id="stick">
              <select name="languages" id="languageRCB">
                <option value="eng" id="options">ENG</option>
                <option value="esp" id="options">ESP</option>
              </select>
            </div>
          </div>
          {list_random}
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