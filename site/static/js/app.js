window.onload = () =>
{           
    const btn = document.getElementsByClassName('btn')  [0]   
    const div = document.getElementById('m')  
    var audio = document.getElementById('play')
   
    
    const delay = ms => new Promise(res => setTimeout(res, ms));
 
    
    btn.addEventListener('click',async ()=>{
        document.getElementById("my_audio").play();       
        btn.classList.add('e') 
        const a = Math.floor(Math.random() * 20); 
        let select = `img${a}`       
        const imga = document.getElementById(select) 
        imga.classList.remove('nd')      
        imga.classList.add('d')     
        
        await delay(3500);         
        alert("ممنون بابت همراهی تون")          
    })                                                           
}
