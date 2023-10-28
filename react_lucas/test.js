import React, { useState } from 'react';
import ReactDOM from 'react-dom';

// Definimos un componente funcional llamado "Contador"
function Contador() {
  // Definimos un estado "contador" inicializado en 0
  // y una función "setContador" para actualizarlo
  const [contador, setContador] = useState(0);

  // Función para incrementar el contador cuando se hace clic en el botón
  const incrementarContador = () => {
    setContador(contador + 1);
  };

  return (
    <div>
      <h1>Contador: {contador}</h1>
      <button onClick={incrementarContador}>Incrementar</button>
    </div>
  );
}

// Renderizamos el componente "Contador" en el elemento con id "root" en el HTML
ReactDOM.render(<Contador />, document.getElementById('root'));
