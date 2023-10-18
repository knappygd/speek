import {  NavLink } from "react-router-dom"

export default function SignUpLogin() {
  return (
    <div id='container'>
      <div id='logo' style={{
        backgroundImage: `url(/logo-para-el-login-speek.png)`,
        backgroundRepeat: 'no-repeat',
        backgroundPosition: 'center',
        backgroundSize: 'cover'}}></div>
      <div id='login'>
        <div id='bloque'>
          <NavLink to='/signup' id="bloque">
            <button id='button-log' class='button-signup'>Sign up</button>
          </NavLink>
          <NavLink to='/login' id="bloque">
          <button id='button-log' class='button-login' style={{
            backgroundImage: `url(/Next_botton_Login.png)`,
            backgroundRepeat: 'no-repeat',
            backgroundPosition: 'center',
            backgroundSize: 'cover'}} to='/login'>Log in</button>
          </NavLink>
          <p>or</p>
          <NavLink to='/example' id="bloque">
          <button id='button-log' class='button-google'>Continue with Google</button>
          </NavLink>
          <button id='button-log' class='button-facebook'>Continue with Facebook</button>
        </div>
      </div>
    </div>
  )
}