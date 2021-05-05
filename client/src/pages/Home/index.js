import React, {useState} from 'react';
import { SignUp } from '../../components'

const Home = () => {

    const [subscribed, setSubscribed] = useState(false)

    const subscribe = (bool) => {
        setSubscribed(bool)
    }
 
    return (
        <>
            <header>
                <h1>Hello World!</h1>
                {subscribed ? <p>Subscribed!</p> : <SignUp subscribe={subscribe}/>}
            </header>
        </>
    )
}

export default Home;