import React from 'react'
import { Switch, Route } from 'react-router-dom';
import * as Pages from './pages';
import { Header, Footer } from './layout'

import './style.css';

function App(){

    return(
      <>
        <Header />
           <Switch>
          <Route exact path="/">
            <Pages.Home />
          </Route>
          <Route path="/albums">
            <Pages.Albums />
          </Route>
          <Route>
            <Pages.NotFound />
          </Route>
        </Switch>
        <Footer />
      </>
    );
  
  };
  
export default App;