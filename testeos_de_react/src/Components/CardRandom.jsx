import "../CSS/CardRandom.css";

export default function CardRandom({ title = "titulo por defecto", last_message = "last message", user_id, friends_initials = "S", onCardClick }) {
    const handleCardClick = () => {
        onCardClick(user_id);
    };

    return (
        <button className="CardR" onClick={handleCardClick}>
            <div className="perfilLogoR">
                <h2>{friends_initials}</h2>
            </div>
            <div className="userInfoR">
                <h3>{title}</h3>
            </div>
        </button>
    );
}
