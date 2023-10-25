import React from 'react';
import ReactDOM from 'react-dom';
import './App.css';
import './Main-Page.css';
import SignUpLogin from './Components/SignUp-Login';
import Login from './Components/Login';
import SignUp from './Components/SignUp';
import MainPage from './Components/Main-Page';
import { BrowserRouter, Route, Routes } from "react-router-dom";

// Definimos un componente funcional llamado "Contador"
function App() {

  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path='' element={<SignUpLogin />}/>
          <Route path='login' element={<Login />} />
          <Route path='signup' element={<SignUp />} />
          <Route path='mainpage' element={<MainPage />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));

export default App;