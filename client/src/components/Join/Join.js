import React, { useState } from 'react';

// Link to ./chat path
import { Link } from 'react-router-dom';

const Join = () => {
    // initial value is ''
    const { name, setName } = useState('');
    const { room, setRoom } = useState('');

    return (
        <div className="joinOuterContainer">
            <div className="joinInnerContainer">
                <h1 className="heading">uwu Join</h1>
                <div><input placeholder="Name" className="joinInput" type="text" onChange={(event) => setName(event.target.value)} ></input></div>
                <div><input placeholder="Room" className="joinInput mt-20" type="text" onChange={(event) => setRoom(event.target.value)} ></input></div>
                // on click, if the name or room isn't entered prevent submitting
                <Link onclick={event => (!name || !room) ? event.preventDefault() : null} to={`/chat?name=${name}&room=${room}`}>
                    <button className="button mt-20" type="submit">Sign In</button>
                </Link>
            </div>
        </div>
    )
}

export default Join;