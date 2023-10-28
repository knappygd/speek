import React from 'react';
import ReactDOM from 'react-dom';
import './App.css';
import './Main-Page.css';
import './Friends-Mainpage.css';
import './ChatPage.css';
import './Top-left.css';
import './Top-right.css';
import SignUpLogin from './Components/SignUp-Login';
import Login from './Components/Login';
import SignUp from './Components/SignUp';
import MainPage from './Components/Main-Page';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import LandingPage from './Components/Landing_Page';
import Authors from './Components/Authors';
import Mainpage1 from './Components/Mainpage1';


// Definimos un componente funcional llamado "Contador"
function App() {

  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path='' element={<LandingPage />} />
          <Route path='authors' element={<Authors />} />
          <Route path='register' element={<SignUpLogin />} />
          <Route path='login' element={<Login />} />
          <Route path='signup' element={<SignUp />} />
          <Route path='mainpage' element={<MainPage />} />
          <Route path='mainpage1' element={<Mainpage1 />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));

export default App;