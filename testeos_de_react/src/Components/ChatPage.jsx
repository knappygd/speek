import Message from "./Message";
import React, { useEffect, useState } from "react";
import axios from 'axios';


export default function Chatpage({ user_id, mostrarCaja, personal_id }) {
  const baseURL = 'http://127.0.0.1:5000';

  const [messageList, setMessage] = useState([]);
  const [chat, setChat] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response1 = await axios.get(`${baseURL}/api/v1/get_chat/${user_id}`);
        setMessage(response1.data);

        const response2 = await axios.get(`${baseURL}/api/v1/search_chat/${personal_id}/${user_id}`);
        setChat(response2.data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchData();
  }, [user_id, messageList, chat]);

  let displaynone = {
    display: "none"
  };

  if (user_id !== null) {
    displaynone = {};
  }

  let messages = messageList.map(i => {
    return <Message
      sender={i.sender}
      content={i.content}
      user_id={personal_id} />
  });

  const [inputValue, setInputValue] = useState("");

  const [topic, setTopic] = useState("");
  const handleFriend = () => {
    axios.post(`${baseURL}/api/v1/add_friend/${user_id}`)
      .catch(error => {
        console.error(error);
      });
  };

  return (
    <div id="right-chat" style={{
      backgroundImage: `url(/background-mainpage.svg)`,
      backgroundRepeat: 'no-repeat',
      backgroundPosition: 'center',
      backgroundSize: 'cover'
    }}>
      {mostrarCaja && <div id="perfilebox">
        <div className="topPerfilebox">
        </div>
        <div className="descriptionBox1">
          <p>Description</p>
        </div>
        <div className="descriptionBox2">
          <h4>I wanted to practice my English on this web page</h4>
        </div>
        <div className="descriptionBox3">
          <p class='lan'>Languages</p>
          <p>English</p>
          <p>Spanish</p>
        </div>
        <button className="friendRequestButton" onClick={handleFriend}>
          <h3>Send friend request</h3>
        </button>

      </div>}
      <div id="cont-chat">
        <div id="chat">
          {messages}
        </div>
      </div>
      <div id="contenedor-de-la-barra">
        <div id="cont-barra" style={displaynone}>
          <input
            type="text"
            placeholder="Type a message..."
            id="barra"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            onKeyPress={(e) => {
              if (e.key === "Enter") {
                try {
                  const response4 = axios.post(`${baseURL}/api/v1/send_message/${inputValue}/${user_id}/${chat}`);
                } catch (error) {
                  console.error(error);
                }
                setInputValue("");
              }
            }}
          ></input>
          <button type="submit" id="enviar-mensaje" onClick={(e) => {
            const fetchData = async () => {
              try {
                const response5 = await axios.get(`${baseURL}/api/v1/random_topic`);
                setTopic(response5.data);
                const response4 = await axios.post(`${baseURL}/api/v1/send_message/Lets talk about ${topic}/${user_id}/${chat}`);
              } catch (error) {
                console.error(error);
              }
            }
            fetchData();
          }}
          style={{
            backgroundImage: `url(/dados.svg)`,
            backgroundRepeat: 'no-repeat',
            backgroundSize: '40px 40px',
            userSelect: 'none',
            cursor: 'pointer',
            border: "none",
            padding: 0,
          }}
        >
          </button>
        </div>
      </div>
    </div>
  )
}