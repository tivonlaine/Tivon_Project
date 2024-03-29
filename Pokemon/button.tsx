import './index.css'
import EnterName from './entername';
import fetchPokemon from './api'
import { useState } from 'react';
import pic from './loading.webp';


export interface PokemonData{
    name:string;
    weight: number;
    picture: string;
}

function Button({pokemonName}:{pokemonName: string}){

    const[pokemonData, setPokemonData]=useState<PokemonData | null>(null);
    const[error, setError]=useState(null);
    const[loading, setLoading]=useState(false);

const click = async () =>{
    setLoading(true);
    try{
        console.log(pokemonName);
        const data=await fetchPokemon(pokemonName);
        console.log(data.name);
        console.log("helo");
        setPokemonData(data);
        setError(null);
        setLoading(false);
    }catch(error: any){
        setPokemonData(null);
        setError(error.message);
        setLoading(false);

    }
}

    if(loading){
        return (
        <div className='load'>
            <p >Loading...</p>
            <img className="pic" src={pic} alt="" />
        </div>
        )
    }
    

    return(

        <div>
            <button onClick={click} id="but" className="button">
                Get Pokemon Fact
            </button>
            {error && <p className="facts">{error}</p>}
            {pokemonData &&(
                <div className="pokemoninfo">
                    <p className="facts">
                        This is {pokemonData.name} and he weighs {pokemonData.weight} pounds.
                        <br />
                        <img className="pic" src={pokemonData.picture} alt="sorry no pic" />
                    </p>
                </div>
            )}

        </div>


    )


}

export default Button;