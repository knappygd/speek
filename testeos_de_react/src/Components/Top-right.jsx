import data_users from "../Data/data_users";


export default function Topright({ user_id }) {

  let title = "Choose a chat to talk";
  for (const user of data_users) {
    if (user.id === user_id) {
      title = user.name;
    }
  };


  return (
    <div id="Topright">
      <h1> {title} </h1>
    </div>
  )
}
// Friends.Card.toggleContenido