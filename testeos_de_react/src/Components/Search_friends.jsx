import React, { useState } from 'react';

import "../CSS/Search_friends.css"

export default function SearchFriends() {
    const [busqueda, setBusqueda] = useState("");

    // console.log("Valor inicial de busqueda:", busqueda);

    /*const handleInputChange = (e) => {
        setBusqueda(e.target.value);
        console.log(busqueda);
    };*/

    return (
        <div id="Search_friends">
            <div id="searcher">
                <div id="lupita" style={{
                    backgroundImage: `url(/lupita.svg)`,
                    backgroundRepeat: 'no-repeat',
                    backgroundSize: '30px 30px',
                    backgroundPositionX: 'right'
                }}></div>
                <input
                    type="text"
                    placeholder="Find friend"
                    id="buscador"
                    value={busqueda}
                    /*onChange={handleInputChange}*/
                    onChange={(e) => setBusqueda(e.target.value)}
                    onKeyPress={(e) => {
                        if (e.key === "Enter") {
                            console.log("Búsqueda realizada:", busqueda);
                        }
                    }}
                />
            </div>
        </div>
    )
}