import "../CSS/TopCard.css";
import { useEffect, useState } from 'react';
import axios from 'axios';

export default function Topright({ user_id, toggleCaja }) {

  const baseURL = 'http://127.0.0.1:5000';
  const [user, setUser] = useState([]);
  let title = "Choose a chat to talk";
  useEffect(() => {
    if (user_id !== null) {
      axios.get(`${baseURL}/api/v1/search_user/${user_id}`)
        .then(response => {
          setUser(response.data);
        })
        .catch(error => {
          console.error(error);
        });
    }
  }, [user_id]);
  title = user.username;

  const mostrarOcultarCaja = () => {
    toggleCaja();
  };

  return (
    <div id="Topright">
      <button onClick={mostrarOcultarCaja}><h1> {title} </h1></button>
    </div>
  );
}
