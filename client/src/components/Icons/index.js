import React from 'react';
import { FaSpotify, FaYoutube, FaInstagram, FaFacebookF, FaTwitter } from "react-icons/fa";

function Icons() {

    return (
        <>
            <div className="social-icons">
                <span> <FaSpotify /></span>
                <span> <FaYoutube /></span>
                <span> <FaInstagram /></span>
                <span>  <FaFacebookF /></span>
                <span>  <FaTwitter /></span>
            </div>
        </>
    );
};

export default Icons;
