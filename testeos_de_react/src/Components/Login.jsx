import React, { useRef } from "react";

export default function Login() {  
  const error = useRef(null);
  const aparecererror = () => {
    error.current.style.display = 'block';
  }

  return (
    <div id='container'>
      <div id='logo' style={{
        backgroundImage: `url(/logo-para-el-login-speek.png)`,
        backgroundRepeat: 'no-repeat',
        backgroundPosition: 'center',
        backgroundSize: 'cover'}}></div>
      <div id='login'>
        <div id='bloque'>
          <input id='button-log' placeholder="Enter your email" class='button-signup'></input>
          <input type='password' id="button-log" placeholder="Enter your password" class='button-signup'></input>
          <div id="error-invisible" ref={error}>
            <p>haces todo mal pibe</p>
          </div>
          <button id='button-log-login' class='button-login' onClick={aparecererror} style={{
            backgroundImage: `url(/Next_botton_Login.png)`,
            backgroundRepeat: 'no-repeat',
            backgroundPosition: 'center',
            backgroundSize: 'cover'}}>Log in</button>
        </div>
      </div>
    </div>
  )
}