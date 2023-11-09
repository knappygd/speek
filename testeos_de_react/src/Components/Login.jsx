import React, { useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from 'axios';

export default function Login() {
  const error = useRef(null);

  const [emailValue, setEmailValue] = useState("");
  const [passwordValue, setPasswordValue] = useState("");
  let user_data = { "email": emailValue, "password": passwordValue };

  const navigate = useNavigate();
  const baseURL = 'http://127.0.0.1:5000';
  const [data, setData] = useState([]);
  const handleLogin = () => {
    // Realiza la solicitud a la API al hacer clic en el botón
    axios.get(`${baseURL}/api/v1/signin/${emailValue}/${passwordValue}`)
      .then(response => {
        setData(response.data);
        if (response.data === '1') {
          navigate("/mainpage1");
        }
      })
      .catch(error => {
        console.error(error);
      });
  };
  console.log(data);

  const aparecererror = () => {
    // Aquí utilizamos la referencia 'error' para mostrar el error
    if (error.current) {
      error.current.style.display = 'block';
    }
  };

  return (
    <div id='container'>
      <div id='logo' style={{
        backgroundImage: `url(/logo-para-el-login-speek.svg)`,
        backgroundRepeat: 'no-repeat',
        backgroundPosition: 'center',
        backgroundSize: 'cover'
      }}></div>
      <div id='login'>
        <div id='bloque'>
          <input
            id='button-log'
            placeholder="Enter your email"
            class='button-signup'
            value={emailValue}
            onChange={(e) => setEmailValue(e.target.value)}
            onKeyPress={(e) => {
              if (e.key === "Enter") {
                user_data["email"] = emailValue;
              }
            }}
          ></input>
          <input
            type='password'
            id="button-log"
            placeholder="Enter your password"
            class='button-signup'
            value={passwordValue}
            onChange={(e) => setPasswordValue(e.target.value)}
            onKeyPress={(e) => {
              if (e.key === "Enter") {
                user_data["password"] = passwordValue;
              }
            }}
          ></input>
          <div id="error-invisible" ref={error}>
            <p>error</p>
          </div>
          <button id='button-log-login' class='button-login' onClick={handleLogin} style={{
            backgroundImage: `url(/Next_botton_Login.png)`,
            backgroundRepeat: 'no-repeat',
            backgroundPosition: 'center',
            backgroundSize: 'cover'
          }}>Log in</button>
        </div>
      </div>
    </div>
  )
}