export default function LandingPage2() {
    return (
        <div id='container-landing'>
            <div id='logo-landing'></div>
            <div style="height: 150px; overflow: hidden;" ><svg viewBox="0 0 500 150" preserveAspectRatio="none" style="height: 100%; width: 100%;"><path d="M0.00,49.98 C149.99,150.00 271.49,-49.98 500.00,49.98 L500.00,0.00 L0.00,0.00 Z" style="stroke: none; fill: #08f;"></path></svg></div>
            <div id='login'>
                <div id="bloque">
                    <div id="banner" style={{
                        backgroundImage: `url(/speek_word_logo.jpg)`,
                        backgroundRepeat: 'no-repeat',
                        backgroundPosition: 'center',
                        backgroundSize: 'cover'
                    }}></div>
                    <h1>Speek es un chat para poliglotas que quieren practicar un idioma</h1>
                    <h3>
                        Este es nuestro proyecto final de Holberton school - Foundations in Computer Science,
                        con esta plataforma trabajamos en todas las habilidades trabajadas a lo largo del año,
                        desarrollando todo el proyecto, desde la planifiacion, organizacion, al desarrollo, testeo y produccion.
                        Nuestra plataforma busca ayudar a poliglotas a practicar para recuperar o mejorar su nivel en un lenguaje.
                    </h3>
                    {/*<NavLink to='/register' id="bloque">
                        <button id='button-log' class='button-login' style={{
                            backgroundImage: `url(/Next_botton_Login.png)`,
                            backgroundRepeat: 'no-repeat',
                            backgroundPosition: 'center',
                            backgroundSize: 'cover'
                        }} to='/register'>SPEEKEA CONMIGO :)</button>
                    </NavLink>*/}
                </div>
            </div>
            <div id="bloque">
                <div id="bloque">
                    <h1>INCERTE FOTO AQUI!!!!!!!!</h1>
                    <div>
                        <h2>Envia mensajes</h2>
                        <p>Envia y recive mensajes a tiempo real con otros usuarios de todo el mundo</p>
                    </div>
                </div>
                <div id="bloque">
                    <h1>INCERTE FOTO AQUI!!!!!!!!</h1>
                    <div>
                        <h2>Practica con Amigos</h2>
                        <p>Crea conversaciones unicas y especiales con tus amigos, aprende junto a ellos y refuerza tus conocimientos con tus seres mas cercanos</p>
                    </div>
                </div>
                <div id="bloque">
                    <h1>INCERTE FOTO AQUI!!!!!!!!</h1>
                    <div>
                        <h2>Practica con extraños</h2>
                        <p>Interactua con desconocidos de todo el mundo de forma unica, expande tu vocabulario y nutrete de la cultura que cada usuario puede brindarte</p>
                    </div>
                </div>
            </div>
            <div id="bloque">
                <div>
                    <h1>About us</h1>
                </div>
                <div>
                    <div>
                        <h2>¿Que nos inspira a crear eso?</h2>
                    </div>
                    <div>
                        <p>Como poliglotas que somos, sentimos que con el paso del tiempo hemos perdido habilidad al comunicarnos en ciertos idiomas,
                            habilidades que habiamos trabajado arduamente durante años se desvanecian en meses de abandono.
                            Al no practicar nustras capacidades y conocimientos se olvidan, por eso queriamos volver a utilizar estos idiomas, pero no encontrabamos
                            una forma que fuera practica, sencilla y efectiva de hacerlo, de ahi nace la idea de Speek, brindar una plataforma para que poliglotas
                            puedan practicar cualquier idioma de forma sencilla y efectiva.</p>
                    </div>
                </div>
                <div>
                    <div>
                        <h2>¿Quienes somos?</h2>
                    </div>
                    <div id="authors">
                        <div id="pics1">
                            <div id='pic' style={{
                                backgroundImage: `url(/lucas.jpg)`,
                                backgroundRepeat: 'no-repeat',
                                backgroundPosition: 'center',
                                backgroundSize: 'cover'
                            }}></div>
                            <div id="pic_text">
                                <p>Lucas Soria</p>
                                <p>Front-End and UX/UI Designer</p>
                                <div id="ico">
                                    <a href="https://github.com/lucassoriabusto">
                                        <div id='pic' style={{
                                            backgroundImage: `url(/lucas_qr.png)`,
                                            backgroundRepeat: 'no-repeat',
                                            backgroundPosition: 'center',
                                            backgroundSize: 'cover'
                                        }}></div>
                                    </a>
                                </div>
                            </div>
                        </div>
                        <div id="pics2">
                            <div id='pic' style={{
                                backgroundImage: `url(/mishel.jpg)`,
                                backgroundRepeat: 'no-repeat',
                                backgroundPosition: 'center',
                                backgroundSize: 'cover'
                            }}></div>
                            <div id="pic_text">
                                <p>Mishel Tomas</p>
                                <p>Front-End</p>
                                <div id="ico">
                                    <a href="https://github.com/Mishel450">
                                        <div id='pic' style={{
                                            backgroundImage: `url(/mishel_qr.png)`,
                                            backgroundRepeat: 'no-repeat',
                                            backgroundPosition: 'center',
                                            backgroundSize: 'cover'
                                        }}></div>
                                    </a>
                                </div>
                            </div>
                        </div>
                        <div id="pics1">
                            <div id='pic' style={{
                                backgroundImage: `url(/emilio.jpg)`,
                                backgroundRepeat: 'no-repeat',
                                backgroundPosition: 'center',
                                backgroundSize: 'cover'
                            }}></div>
                            <div id="pic_text">
                                <p>Emilio Damasco</p>
                                <p>Back-End</p>
                                <div id="ico">
                                    <a href="https://github.com/knappygd">
                                        <div id='pic' style={{
                                            backgroundImage: `url(/emilio_qr.png)`,
                                            backgroundRepeat: 'no-repeat',
                                            backgroundPosition: 'center',
                                            backgroundSize: 'cover'
                                        }}></div>
                                    </a>
                                </div>
                            </div>
                        </div>
                        <div id="pics2">
                            <div id='pic' style={{
                                backgroundImage: `url(/leonardo.jpg)`,
                                backgroundRepeat: 'no-repeat',
                                backgroundPosition: 'center',
                                backgroundSize: 'cover'
                            }}></div>
                            <div id="pic_text">
                                <p>Leonardo Rodriguez</p>
                                <p>Full-Stack</p>
                                <div id="ico">
                                    <a href="https://github.com/LeoRod17">
                                        <div id='pic' style={{
                                            backgroundImage: `url(/leonardo_qr.png)`,
                                            backgroundRepeat: 'no-repeat',
                                            backgroundPosition: 'center',
                                            backgroundSize: 'cover'
                                        }}></div>
                                    </a>
                                </div>
                            </div>
                        </div>
                        <div id="pics1">
                            <div id='pic' style={{
                                backgroundImage: `url(/guillermo.jpg)`,
                                backgroundRepeat: 'no-repeat',
                                backgroundPosition: 'center',
                                backgroundSize: 'cover'
                            }}></div>
                            <div id="pic_text">
                                <p>Guillermo Vega</p>
                                <p>Full-Stack and Project Manager</p>
                                <div id="ico">
                                    <a href="https://github.com/Korchea">
                                        <div id='pic' style={{
                                            backgroundImage: `url(/guillermo_qr.png)`,
                                            backgroundRepeat: 'no-repeat',
                                            backgroundPosition: 'center',
                                            backgroundSize: 'cover'
                                        }}></div>
                                    </a>
                                </div>
                            </div>
                        </div >
                    </div>
                </div>
                <div>
                    <h2>Git Hub Repo</h2>
                    <a href="https://github.com/knappygd/speek">
                        <div id='pic' style={{
                            backgroundImage: `url(/GitHub-icon.png)`,
                            backgroundRepeat: 'no-repeat',
                            backgroundPosition: 'center',
                            backgroundSize: 'cover'
                        }}></div>
                    </a>
                </div>
            </div>
        </div>
    )
}