import { useState } from 'react';
import './index.css'


interface EnterNameProps{
    updatePokemonName:(name:string)=>void;
}

function EnterName({updatePokemonName}:EnterNameProps){
    const[pokemonName, setPokemonName]=useState('');

    const handlechange=(event: React.ChangeEvent<HTMLInputElement>)=>{
        setPokemonName(event.target.value);
        updatePokemonName(event.target.value);
    }


    return(

        <div id="name" className="entername">
            <input onChange={handlechange} value={pokemonName} placeholder='Pokemon goes here' type="text" />
        </div>

    )


}

export default EnterName;