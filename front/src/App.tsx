import React from 'react';
import './App.css';
import Nav from "./components/Nav";
import Menu from "./components/Menu";
import Products from "./products/Products";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Main from "./flask/Flask";

function App() {
    return (
        <div className="App">
            <Nav/>

            <div className="container-fluid">
                <div className="row">
                    <Menu/>

                    <main className="col-md-9 ms-sm-auto col-lg-10 px-md-4">

                        <BrowserRouter>
                            <Routes>
                                <Route path='/' Component={Main}/>
                                <Route path='/products' Component={Products}/>
                            </Routes>
                        </BrowserRouter>

                    </main>
                </div>
            </div>
        </div>
    );
}

export default App;
