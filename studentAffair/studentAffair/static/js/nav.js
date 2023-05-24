const nav = document.querySelector('nav');
const toggle_btn = document.getElementById('toggle-btn');
const smallTap = document.getElementById('.smallTap');
// const content = document.querySelector('section');
const divcon = document.querySelector('.content');

const procon = document.querySelector('.projects');
const partcon = document.querySelector('.part')
// const smallTap = document.getElementById('.smallTap');
// const btn = document.getElementById('toggle-btn');
const MEC = document.getElementById('.marginedited');


toggle_btn.onclick = function() {
    nav.classList.toggle('hide');
    if (partcon === null) {
    } else {
        partcon.classList.toggle('expand');
    }
    if (smallTap === null) {
    } else {
        smallTap.classList.toggle('expand');
    }
    if (procon === null) {
    } else {
        procon.classList.toggle('expand');
    }
    if (MEC === null) {
    } else {
        MEC.classList.toggle('expand');
    }
    if (divcon === null) {}
    else{
      divcon.classList.toggle('expand');
    }
    // smallTap.classList.toggle('expand');
    // content.classList.toggle('expand');
    // divcon.classList.toggle('expand');
};

// const body = document.querySelector('body');
// const bgModeBtn = document.getElementById('bgModeBtn');
// const bgModeIcon = document.getElementById('bgModeIcon');
// const sectionHeader = document.querySelector('section h1');

// bgModeBtn.onclick = function(){
//     body.classList.toggle("dark-mode");
//     bgModeIcon.classList.toggle("fa fa-sun");
//     bgModeIcon.classList.toggle("far fa-moon");
//     sectionHeader.classList.toggle("dark-mode");
// }

function toggleMode() {
    var icon = document.getElementById("bgModeIcon");
    var body = document.body;
    
    if (body.classList.contains("light-mode")) {
      body.classList.remove("light-mode");
      icon.classList.remove("fa-moon");
      icon.classList.add("fa-sun");
    } else {
      body.classList.add("light-mode");
      icon.classList.remove("fa-sun");
      icon.classList.add("fa-moon");
    }
    body.classList.toggle("dark-mode");
  }
  
  document.getElementById("bgModeBtn").addEventListener("click", toggleMode);