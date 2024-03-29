import { PokemonData } from "./button";

async function fetchPokemon(name: string){

    try{
        const response=await fetch(`https://pokeapi.co/api/v2/pokemon/${name}`)

        if(!response.ok){
            throw new Error("Pokemon not found, try again.")
        }

        const data=await response.json();
        const pokemonData: PokemonData={
            name: data.name,
            weight: data.weight,
            picture: data.sprites.front_default
        };
        return pokemonData;
    }catch(error){
        throw new Error("Failed to fetch data.")
    }
}

 

export default fetchPokemon;