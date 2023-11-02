export default function Message({ sender, content }) {

    if (sender === 20) {
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