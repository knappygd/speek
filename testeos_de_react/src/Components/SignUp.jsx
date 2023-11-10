import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from 'axios';


export default function SignUp() {

  const [nameValue, setNameValue] = useState("");
  const [emailValue, setEmailValue] = useState("");
  const [passwordValue, setPasswordValue] = useState("");
  const [descValue, setDescValue] = useState("");
  let user_data = { "username": nameValue, "email": emailValue, "password": passwordValue, "desc": descValue };

  const navigate = useNavigate();
  const baseURL = 'http://127.0.0.1:5000';
  const [data, setData] = useState("not exist");
  const handleSignup = () => {
    // Realiza la solicitud a la API al hacer clic en el botón
    axios.get(`${baseURL}/api/v1/signup/${nameValue}/${emailValue}/${passwordValue}/${descValue}`)
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  };
  console.log(data);
  if (data === "created") {
    navigate("/mainpage");
  }
  if (data === "already exist") {
    navigate("/mainpage")
  }

  return (
    <div id='container'>
      <div id='logo' style={{
        backgroundImage: `url(/logo-para-el-login-speek.png)`,
        backgroundRepeat: 'no-repeat',
        backgroundPosition: 'center',
        backgroundSize: 'cover'
      }}></div>
      <div id='login'>
        <div id='bloque'>
          <input type='username'
            id="button-log"
            placeholder="Enter your username"
            class='button-signup'
            value={nameValue}
            onChange={(e) => setNameValue(e.target.value)}
            onKeyPress={(e) => {
              if (e.key === "Enter") {
                user_data["username"] = nameValue;
              }
            }}
          ></input>
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
          <input type='password'
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
          <input type='password'
            id="button-log"
            placeholder="Repeat your password"
            class='button-signup'
          ></input>
          <input type='desc'
            id="button-log"
            placeholder="ENter your desc"
            class='button-signup'
            value={descValue}
            onChange={(e) => setDescValue(e.target.value)}
            onKeyPress={(e) => {
              if (e.key === "Enter") {
                user_data["desc"] = descValue;
              }
            }}
          ></input>
          <button id='button-log-login' class='button-login-next' onClick={handleSignup} style={{
            backgroundImage: `url(/Button-next.png)`,
            backgroundRepeat: 'no-repeat',
            backgroundPosition: 'center',
            backgroundSize: 'cover'
          }}>hola</button>
        </div>
      </div>
    </div>
  )
}