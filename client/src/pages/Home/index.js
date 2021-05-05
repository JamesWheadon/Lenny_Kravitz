import React, {useState} from 'react';
import { Icons, SignUp } from '../../components'

const Home = () => {

    const [subscribed, setSubscribed] = useState(false)

    const subscribe = (bool) => {
        setSubscribed(bool)
    }
 
    return (
        <>
            <header>
                <h1 className="heading">LENNY KRAVITZ</h1>
            </header>
            
            <main className="main-container">
                {subscribed ? <p>Subscribed!</p> : <SignUp subscribe={subscribe}/>}
            </main>

            <Icons />
        </>
    )
}

export default Home;