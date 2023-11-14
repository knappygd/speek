export default function Message({ sender, content, user_id }) {

  if (sender === user_id) {
    return (
      <div id="blockmessage1">
        <p className="msj_box" id="sender"> {content} </p>
      </div>
    )
  }
  return (
    <div id="blockmessage2">
      <p className="msj_box" id="receiver"> {content} </p>
    </div>
  )
}