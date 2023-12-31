import React, { useEffect, useState } from "react";
import Friends from "./Friends-Mainpage"
import Chatpage from "./ChatPage"
import Topleft from "./Top-left"
import Topright from "./Top-right"
import SearchFriends from "./Search_friends"
import axios from 'axios';

export default function Mainpage() {
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
    console.log("Búsqueda recibida en Mainpage:", nuevaBusqueda);
    setBusqueda(nuevaBusqueda);
  };

  const baseURL = 'http://127.0.0.1:5000';
  const [personal_id, setId] = useState("");
  useEffect(() => {
    axios.get(`${baseURL}/api/v1/get_id`)
      .then(response => {
        setId(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  return (
    <div id="container-mainpage1">
      <div id="left">
        <Topleft />
        <Friends onCardClick={handleCardClick} busqueda2={busqueda1} personal_id={personal_id} />
        <SearchFriends busqueda={handleBusquedaChange} />
      </div>
      <div id="right">
        <Topright user_id={toprightTitle} toggleCaja={toggleCaja} />
        <Chatpage user_id={toprightTitle} mostrarCaja={mostrarCaja} personal_id={personal_id} />
      </div>
    </div>
  )
}
