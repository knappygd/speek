import React, { useState } from "react";
import Friends from "./Friends-Mainpage"
import Chatpage from "./ChatPage"
import Topleft from "./Top-left"
import Topright from "./Top-right"
import SearchFriends from "./Search_friends"

export default function Mainpage1() {
  const [toprightTitle, setToprightTitle] = useState(null);
  const [mostrarCaja, setMostrarCaja] = useState(false);
  const [busqueda1, setBusqueda] = useState("");

  const handleCardClick = (user_id) => {
    setToprightTitle(user_id);
  };

  const toggleCaja = () => {
    setMostrarCaja(!mostrarCaja)
  };

  const handleBusquedaChange = (nuevaBusqueda) => {
    console.log("Búsqueda recibida en Mainpage1:", nuevaBusqueda);
    setBusqueda(nuevaBusqueda);
  };

  return (
    <div id="container-mainpage1">
      <div id="left">
        <Topleft />
        <Friends onCardClick={handleCardClick} busqueda2={busqueda1} />
        <SearchFriends busqueda={handleBusquedaChange} />
      </div>
      <div id="right">
        <Topright user_id={toprightTitle} toggleCaja={toggleCaja} />
        <Chatpage user_id={toprightTitle} mostrarCaja={mostrarCaja} />
      </div>
    </div>
  )
}
