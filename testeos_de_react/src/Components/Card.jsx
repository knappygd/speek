
import "./Card.css";

export default function Card({ title = "titulo por defecto",
  description = "descripcion por defecto" }) {
  return (
    <div className='Card'>
      <h3>{title}</h3>
      {/*<p>{description}</p>*/}
    </div>
  );
}
