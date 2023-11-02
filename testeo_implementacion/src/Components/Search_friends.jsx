import "../CSS/Search_friends.css"

export default function SearchFriends() {
    return (
        <div id="Search_friends">
            <div id="searcher">
            <div id="lupita" style={{
            backgroundImage: `url(/lupita.png)`,
            backgroundRepeat: 'no-repeat',
            backgroundSize: '30px 30px',
            backgroundPositionX: 'right'}}></div>
                <input type="text" id="buscador"></input> 
            </div>
        </div>
    )
}