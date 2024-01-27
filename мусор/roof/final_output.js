document.addEventListener('DOMContentLoaded', function(){
    const buttons = document.querySelectorAll('button');

    buttons.forEach(btn => {
        btn.classList.add('updater');
        
        btn.addEventListener('click', function(){
            const selected_variable = document.querySelectorAll('.selected');

            if(selected_variable.length === 2){
                let output = document.querySelector('#user-order');
                let nums = document.querySelectorAll('span.count');

                output.innerHTML = `${selected_variable[0].textContent} ${selected_variable[1].textContent} в комнату ${nums[0].textContent} м2 (углов ${nums[1].textContent}). ${nums[2].textContent} светильников и ${nums[3].textContent} ламп`;
            }
        })
    })
})