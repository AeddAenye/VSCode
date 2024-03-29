import { sha256 } from "./passwd_hashing.js";
import {shake} from "./shake.js"
let btn = document.querySelector('.button-reg');

btn.addEventListener('click', () => {
    let inputs = Array.from(document.querySelectorAll('input'));
    let empty = inputs.filter(el => el.value.trim() === '');

    if (empty != 0){
        empty.forEach(input => {shake(input)})
        return
    }

    async function postUser(){
        let response = await fetch('/registrarion.php', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email: inputs[0].value,
                username: inputs[1].value,
                password: await sha256(inputs[2].value)
            })
        })
        if(!response.ok){
            console.error(response.status)
            return
        }
        return await response.json()
    }
})