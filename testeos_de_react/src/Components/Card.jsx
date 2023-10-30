
import "../CSS/Card.css";

export let username = "Some user";
export default function Card({ title = "titulo por defecto",
  description = "descripcion por defecto" }) {

  const toggleContenido = () => {
    username = title;
  };
  return (
    <button className='Card' onClick={toggleContenido}>
      <h3>{title}</h3>
      {/*<p>{description}</p>*/}
    </button>
  );
}
