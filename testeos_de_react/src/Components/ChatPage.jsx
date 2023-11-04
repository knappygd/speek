import data_messages from "../Data/data_messages";
import data_user_chat from "../Data/data_user_chat";
import Message from "./Message";
import React, { useState } from "react";


export default function Chatpage({ user_id, mostrarCaja }) {
  let displaynone = {
    display: "none"
  };

  if (user_id !== null) {
    displaynone = {};
  }

  let chat_id = 1000;
  for (const chat of data_user_chat) {
    if (chat.user_id === user_id) {
      chat_id = chat.chat_id;
    }
  };

  let message_list = [];
  for (const message of data_messages) {
    if (message.chat_id === chat_id) {
      message_list.push(message);
    }
  };

  let messages = message_list.map(i => {
    return <Message
      sender={i.sender}
      content={i.content} />
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
                // Aquí puedes acceder al valor de inputValue y usarlo para enviar el mensaje
                //const messageToSend = inputValue;
                // Luego puedes hacer lo que necesites con el messageToSend
                // Además, puedes limpiar el input después de presionar "Enter"
                console.log(inputValue);
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