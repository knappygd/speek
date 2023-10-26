export default function MainPage() {
  return (
    <div id="container-mainpage">
      <div id="top">
        <div id='lefttop-mainpage'></div>
        <div id="righttop-mainpage"></div>
      </div>
      <div id="bottom">
        <div id="left-mainpage">
          <div id="people">
            <div id="randomchatbutton">
              <button id="randomchat">Random Chat</button>
              <select name="languages" id="languageRCB">
                <option value="eng">ENG</option>
                <option value="spa">SPA</option>
              </select>
              </div>
          </div>
        </div>
        <div id="right-mainpage" style={{
        backgroundImage: `url(/background-mainpage.png)`,
        backgroundRepeat: 'no-repeat',
        backgroundPosition: 'center',
        backgroundSize: 'cover'}}></div>
      </div>
    </div>
  )
}