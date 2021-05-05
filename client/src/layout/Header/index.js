import React from 'react';
import { NavLink } from 'react-router-dom';

import './style.css'

const Header = () => {
    return (
        <nav role="navigation">
            <NavLink exact to="/" activeClassName="current">HOME</NavLink>
            <NavLink to="/albums" activeClassName="current">ALBUMS</NavLink>
        </nav>
    );
}

export default Header;
