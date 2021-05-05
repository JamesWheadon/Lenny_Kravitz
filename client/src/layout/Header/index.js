import React from 'react';
import { NavLink } from 'react-router-dom';

import './style.css'

const Header = () => {
    return (
        <nav role="navigation">
            <NavLink exact to="/" activeClassName="current">Home</NavLink>
            <NavLink to="/albums" activeClassName="current">Albums</NavLink>
        </nav>
    );
}

export default Header;
