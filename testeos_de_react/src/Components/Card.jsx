import "../CSS/Card.css";

export default function Card({ title = "titulo por defecto", onCardClick}) {
  const handleCardClick = () => {
    onCardClick(title);
  };

  return (
    <button className="Card" onClick={handleCardClick}>
      <h3>{title}</h3>
    </button>
  );
}
