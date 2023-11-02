import React, { useState } from 'react';

import data_users from "../Data/data_users";
import "../CSS/TopCard.css";


export default function Topright({ user_id }) {

  let title = "Choose a chat to talk";
  for (const user of data_users) {
    if (user.id === user_id) {
      title = user.name;
    }
  };


  const [mostrarCaja, setMostrarCaja] = useState(false);

  const mostrarOcultarCaja = () => {
    setMostrarCaja(!mostrarCaja);
  };

  return (
    <div id="Topright">
      <button onClick={mostrarOcultarCaja}><h1> {title} </h1></button>
      {mostrarCaja && <div className="caja0"></div>}
    </div>
  )
}
// Friends.Card.toggleContenido