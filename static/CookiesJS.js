var i = 0;
var txt = "The cookies are made with a secret ingredient, only found in the rainforests of the Amazon...";
var speed = 50;
      
function PrintAfterSubmit() {
    if (i<txt.length) {
        document.getElementById("Text1").innerHTML +=txt.charAt(i);
        i++;
        setTimeout(PrintAfterSubmit, speed);
        }
      }


function startTimer(duration, display) {
        var timer = duration, minutes, seconds;
        setInterval(function () {
            minutes = parseInt(timer / 60, 10);
            seconds = parseInt(timer % 60, 10);
    
            minutes = minutes < 10 ? "0" + minutes : minutes;
            seconds = seconds < 10 ? "0" + seconds : seconds;
    
            display.textContent = minutes + ":" + seconds;
    
            if (--timer < 0) {
                timer = duration;
            }
        }, 1000);
 }

window.onload = function () {
        var oneMinute = 60,
            display = document.querySelector('#time');
        startTimer(oneMinute, display);
};


//pull the pathname from window location
const activePage = window.location.pathname;


/*create an arey of the links in nav, 
compare each to pathname and mark the one that is active
*/ 
const navLinks = document.querySelectorAll('nav a').forEach(link => {    
  if(link.href.includes(`${activePage}`)){
    link.classList.add('active');
  }
});

//----------NEW-------------

function find_user(user_id){
    fetch('https://reqres.in/api/users/'+user_id).then(
        response => response.json()
    ).then(
        responseOBJECT => createUser(responseOBJECT.data)
    ).catch(
        err => console.log(err)
    );
}

function createUser(response){
    let user = response;
    const currMain = document.querySelector("main")

    const section = document.createElement('section')
    section.innerHTML = `
        <img src="${user.avatar}" alt="Profile Picture"/>
        <div>
         <span>${user.first_name} ${user.last_name}</span>
         <br>
         <a href="mailto:${user.email}">Send Email</a>
        </div> 
        `
    currMain.appendChild(section)
}
