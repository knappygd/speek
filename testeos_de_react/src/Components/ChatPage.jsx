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

  return (
    <div id="right-chat" style={{
      backgroundImage: `url(/background-mainpage.svg)`,
      backgroundRepeat: 'no-repeat',
      backgroundPosition: 'center',
      backgroundSize: 'cover'
    }}>
      {mostrarCaja && <div id="perfilebox">
        <div className="topPerfilebox">
          <p> {user_id} </p>
        </div>

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
            value={inputValue} // Establece el valor del input en el estado
            onChange={(e) => setInputValue(e.target.value)} // Manejador de eventos para el cambio del input
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
                const response4 = await axios.post(`${baseURL}/api/v1/send_message/Lets going to talk about ${topic}/${user_id}/${chat}`);
              } catch (error) {
                console.error(error);
              }
            }
            fetchData();
          }}
          >Topic</button>
        </div>
      </div>
    </div>
  )
}