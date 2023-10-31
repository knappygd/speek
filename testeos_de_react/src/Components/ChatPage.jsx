import data_chat from "../Data/data_chat";
import data_messages from "../Data/data_messages";
import data_user_chat from "../Data/data_user_chat";
import data_user_messages from "../Data/data_user_messages";
import Message from "./Message";


export default function Chatpage({ user_id, onCardClick }) {

  const handleCardClick = (id) => {
    onCardClick(id);
  };

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
      content={i.content}
      onCardClick={handleCardClick} />
  });


  return (
    <div id="right-chat" style={{
      backgroundImage: `url(/background-mainpage.png)`,
      backgroundRepeat: 'no-repeat',
      backgroundPosition: 'center',
      backgroundSize: 'cover'
    }}>
      <div id="cont-chat">
      <div id="chat">
        {messages}
      </div>
      </div>
      <div id="contenedor-de-la-barra">
        <form id="cont-barra">
          <input type="text" placeholder="Type a message..." id="barra"></input>
          <input type="submit" id="enviar-mensaje"></input>
        </form>
      </div>
    </div>
  )
}