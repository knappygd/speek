import Message from "./Message";
import React, { useEffect, useState } from "react";
import axios from 'axios';


export default function Chatpage({ user_id, mostrarCaja }) {
  const baseURL = 'http://127.0.0.1:5000';

  const [user, setId] = useState("a89136d5-9fee-465e-af62-8b7c49c197ff");
  const [chat, setChat] = useState("0");
  const [messageList, setMessage] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response1 = await axios.get(`${baseURL}/test_api/get_id`);
        setId(response1.data);

        const response2 = await axios.get(`${baseURL}/test_api/search_chat/${user}/${user_id}`);
        setChat(response2.data);

        const response3 = await axios.get(`${baseURL}/test_api/list_message/${chat}`);
        setMessage(response3.data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchData();
  }, [user_id, user, user_id, chat]);

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
      user_id={user} />
  });

  const [inputValue, setInputValue] = useState("");

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
                  const response4 = axios.post(`${baseURL}/test_api/send_message/${inputValue}/${user_id}/${chat}`);
                } catch (error) {
                  console.error(error);
                }
                setInputValue("");
              }
            }}
          ></input>
          <input type="submit" id="enviar-mensaje"></input>
        </div>
      </div>
    </div>
  )
}