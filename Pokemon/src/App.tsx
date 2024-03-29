import ListGroup from "../ListGroup";
import Header from "../Header"
import FirstLine from "../firstline"
import EnterName from "../entername"
import Button from "../button"
import fetchPokemon from "../api";
import { PokemonData } from "../button";
import { useState
 } from "react";
function App() {

  const[pokemonName, setPokemonName]=useState(" ");

  return (
    <div className="background">
      <Header></Header>
      <FirstLine></FirstLine>
      <EnterName updatePokemonName={setPokemonName}></EnterName>
      <Button pokemonName={pokemonName}></Button>
    </div>
  
  );
}
export default App;
