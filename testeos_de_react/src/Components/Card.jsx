import "../CSS/Card.css";

export default function Card({ title = "titulo por defecto", last_message = "last message", friends_initials = "LS", onCardClick, user_id }) {
  const handleCardClick = () => {
    onCardClick(user_id);
  };

  return (
    <button className="Card" onClick={handleCardClick}>
      <div className="perfilLogo">
        <h2>{friends_initials}</h2>
      </div>
      <div className="userInfo">
        <h3>{title}</h3>
        <h4>{last_message}</h4>
      </div>
    </button>
  );
}
