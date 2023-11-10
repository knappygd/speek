import React from 'react';
import ReactDOM from 'react-dom';
import './App.css';
import './CSS/Friends-Mainpage.css';
import './CSS/ChatPage.css';
import './CSS/Top-left.css';
import './CSS/Top-right.css';
import SignUpLogin from './Components/SignUp-Login';
import Login from './Components/Login';
import SignUp from './Components/SignUp';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Mainpage1 from './Components/Mainpage1';


// Definimos un componente funcional llamado "Contador"
function App() {

  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<SignUpLogin />} />
          <Route path='login' element={<Login />} />
          <Route path='signup' element={<SignUp />} />
          <Route path='mainpage' element={<Mainpage1 />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));

export default App;