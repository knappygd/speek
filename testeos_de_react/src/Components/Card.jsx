import "../CSS/Card.css";

export default function Card({ title = "titulo por defecto", last_message = "last message", onCardClick, user_id }) {
  const handleCardClick = () => {
    onCardClick(user_id);
  };

  return (
    <button className="Card" onClick={handleCardClick}>
      <div className="perfilLogo"></div>
      <div className="userInfo">
        <h3>{title}</h3>
        <h4>{last_message}</h4>
      </div>
    </button>
  );
}
