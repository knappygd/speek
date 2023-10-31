export default function Chatpage() {
  return (
    <div id="right-chat" style={{
      backgroundImage: `url(/background-mainpage.png)`,
      backgroundRepeat: 'no-repeat',
      backgroundPosition: 'center',
      backgroundSize: 'cover'
    }}>
      <div id="chat"></div>
      <div id="contenedor-de-la-barra">
        <form id="cont-barra">
        <input type="text" placeholder="Type a message..." id="barra"></input>
        <input type="submit" id="enviar-mensaje"></input>
        </form>
      </div>
    </div>
  )
}