export default function Message({ sender, content }) {

    if (sender === 20) {
        return (
            <div className="msj_box" id="sender">
                <p> {content} </p>
            </div>
        )
    }
    return (
        <div className="msj_box" id="receiver">
            <p> {content} </p>
        </div>
    )
}