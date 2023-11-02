import data_users from "../Data/data_users";
import "../CSS/TopCard.css";


export default function Topright({ user_id, toggleCaja }) {

  let title = "Choose a chat to talk";
  for (const user of data_users) {
    if (user.id === user_id) {
      title = user.name;
    }
  };

  const mostrarOcultarCaja = () => {
    toggleCaja();
  };

  return (
    <div id="Topright">
      <button onClick={mostrarOcultarCaja}><h1> {title} </h1></button>
    </div>
  )
}
// Friends.Card.toggleContenido