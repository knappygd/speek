import { NavLink } from "react-router-dom"

export default function Authors() {
    return (
        <div id='container'>
            <div id='logo' style={{
                backgroundImage: `url(/logo-para-el-login-speek.png)`,
                backgroundRepeat: 'no-repeat',
                backgroundPosition: 'center',
                backgroundSize: 'cover'
            }}></div>
            <div id='login'>
                <div id="bloque">
                    <div id="authors">
                        <div id="pics">
                            <div id='pic' style={{
                                backgroundImage: `url(/lucas.jpg)`,
                                backgroundRepeat: 'no-repeat',
                                backgroundPosition: 'center',
                                backgroundSize: 'cover'
                            }}></div>
                            <div id="pic_text">
                                <a href="https://github.com/lucassoriabusto">Lucas Soria</a>
                                <p>Front-End and UX/UI Designer</p>
                            </div>
                        </div>
                        <div id="pics">
                            <div id='pic' style={{
                                backgroundImage: `url(/mishel.jpg)`,
                                backgroundRepeat: 'no-repeat',
                                backgroundPosition: 'center',
                                backgroundSize: 'cover'
                            }}></div>
                            <div id="pic_text">
                                <a href="https://github.com/Mishel450">Mishel Tomas</a>
                                <p>Front-End</p>
                            </div>
                        </div>
                        <div id="pics">
                            <div id='pic' style={{
                                backgroundImage: `url(/emilio.jpg)`,
                                backgroundRepeat: 'no-repeat',
                                backgroundPosition: 'center',
                                backgroundSize: 'cover'
                            }}></div>
                            <div id="pic_text">
                                <a href="https://github.com/knappygd">Emilio Damasco</a>
                                <p>Back-End</p>
                            </div>
                        </div>
                        <div id="pics">
                            <div id='pic' style={{
                                backgroundImage: `url(/leonardo.jpg)`,
                                backgroundRepeat: 'no-repeat',
                                backgroundPosition: 'center',
                                backgroundSize: 'cover'
                            }}></div>
                            <div id="pic_text">
                                <a href="https://github.com/LeoRod17">Leonardo Rodriguez</a>
                                <p>Full-Stack</p>
                            </div>
                        </div>
                        <div id="pics">
                            <div id='pic' style={{
                                backgroundImage: `url(/guillermo.jpg)`,
                                backgroundRepeat: 'no-repeat',
                                backgroundPosition: 'center',
                                backgroundSize: 'cover'
                            }}></div>
                            <div id="pic_text">
                                <a href="https://github.com/Korchea">Guillermo Vega</a>
                                <p>Full-Stack and Project Manager</p>
                            </div>
                        </div>
                        <NavLink to='/register' id="bloque">
                            <button id='button-log' class='button-login' style={{
                                backgroundImage: `url(/Next_botton_Login.png)`,
                                backgroundRepeat: 'no-repeat',
                                backgroundPosition: 'center',
                                backgroundSize: 'cover'
                            }} to='/register'>SPEEKEA CON NOSOTROS :)</button>
                        </NavLink>
                    </div>
                </div>
            </div>
        </div >
    )
}