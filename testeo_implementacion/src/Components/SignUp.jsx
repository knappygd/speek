export default function SignUp() {
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
          <input type='password' id="button-log" placeholder="Repeat your password" class='button-signup'></input>
          <button id='button-log-login' class='button-login-next' style={{
            backgroundImage: `url(/Button-next.png)`,
            backgroundRepeat: 'no-repeat',
            backgroundPosition: 'center',
            backgroundSize: 'cover'}}>hola</button>
        </div>
      </div>
    </div>
  )
}