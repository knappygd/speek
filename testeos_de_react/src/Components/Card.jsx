import "../CSS/Card.css";

export default function Card({ title = "titulo por defecto", onCardClick, user_id }) {
  const handleCardClick = () => {
    onCardClick(user_id);
  };

  return (
    <button className="Card" onClick={handleCardClick}>
      <h3>{title}</h3>
    </button>
  );
}
