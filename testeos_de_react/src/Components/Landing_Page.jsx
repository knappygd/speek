import { NavLink } from "react-router-dom"

export default function LandingPage() {
    return (
        <div id='container'>
            <div id='logo' style={{
                backgroundImage: `url(/logo-para-el-login-speek.svg)`,
                backgroundRepeat: 'no-repeat',
                backgroundPosition: 'center',
                backgroundSize: 'cover'
            }}></div>
            <div id='login'>
                <div id="bloque">
                    <div id="banner" style={{
                        backgroundImage: `url(/speek_word_logo.jpg)`,
                        backgroundRepeat: 'no-repeat',
                        backgroundPosition: 'center',
                        backgroundSize: 'cover'
                    }}></div>
                    <h2>¿Quieres practicar un idioma?</h2>
                    <h3>Speek es una plataforma dirigida a poliglotas que tienen el objetivo de practicar un idioma</h3>
                    <p>
                        Este es nuestro proyecto final de Holberton school - Foundations in Computer Science,
                        con esta plataforma trabajamos en todas las habilidades trabajadas a lo largo del año,
                        desarrollando todo el proyecto, desde la planifiacion, organizacion, al desarrollo, testeo y produccion.
                        Nuestra plataforma busca ayudar a poliglotas a practicar para recuperar o mejorar su nivel en un lenguaje.
                    </p>
                    <NavLink to='/register' id="bloque">
                        <button id='button-log' class='button-login' style={{
                            backgroundImage: `url(/Next_botton_Login.png)`,
                            backgroundRepeat: 'no-repeat',
                            backgroundPosition: 'center',
                            backgroundSize: 'cover'
                        }} to='/register'>SPEEKEA CONMIGO :)</button>
                    </NavLink>
                    <NavLink to='/authors' id="bloque">
                        <button id='button-log' class='button-login' style={{
                            backgroundImage: `url(/Next_botton_Login.png)`,
                            backgroundRepeat: 'no-repeat',
                            backgroundPosition: 'center',
                            backgroundSize: 'cover'
                        }} to='/authors'>AUTORES</button>
                    </NavLink>
                </div>
            </div>
        </div >
    )
}