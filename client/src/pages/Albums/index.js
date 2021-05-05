import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Albums = () => {

    const [albums, setAlbums] = useState([])
    const [albumName, setAlbumName] = useState('')
    const [albumYear, setAlbumYear] = useState('')
    const [newAlbum, setNewAlbum] = useState('')

    useEffect(async () => {
        const {data} = await axios.get('http://localhost:5000/albums')
        setAlbums(data)
    }, [newAlbum])

    const renderAlbums = albums.map(a => {
            return (<div key={a.id}>
            <h3>{a.name}</h3>
            <h4>{a['year-released']}</h4>
            </div>)
        })

    const handleSubmit = async (e) => {
        e.preventDefault();
        await axios.post('http://localhost:5000/albums', {name: albumName, "year-released": albumYear})
        setNewAlbum(albumName)
        setAlbumName('')
        setAlbumYear('')
    }

    const updateName = e => {
        const input = e.target.value
        setAlbumName(input)
    }

    const updateYear = e => {
        const input = e.target.value
        setAlbumYear(input)
    }

    return (
        <>
            <header>
                <h1>Albums</h1>
                <form className="room-form" onSubmit={handleSubmit} role="form">
                    <label>Album Name 
                        <input type="text" value={albumName} onChange={updateName} />
                    </label>
                    <label>Year Album Released 
                        <input type="text" value={albumYear} onChange={updateYear} />
                    </label>
                    <button type="submit">Add New Album</button>
                </form>
                {renderAlbums}
            </header>
        </>
    )
}

export default Albums;