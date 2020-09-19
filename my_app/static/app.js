let sound;

function preload() {
  sound = loadSound('timeup.mp3');
}

function setup() {
    sound = loadSound('timeup.mp3');
    preload();
    sound.play();
    noCanvas();
}

function notifyMe() {
    if (!Notification) {
        alert('Desktop notifications not available in your browser'); 
        return;
    }
    if (Notification.permission !== "granted")
        Notification.requestPermission();
    else {
        var notification = new Notification('Time is Up!', {
          icon: 'https://icons-for-free.com/download-icon-clock+minute+time+timer+watch+icon-1320086045717163975_512.png',
          body: 'Time is Up!',
        });
      }
  }

function countup() {
    console.log("Hello from app.js!");

    document.getElementById("time").innerHTML = "0";

    function timeIt() {
        document.getElementById("time").innerHTML++;
    }
    setInterval(timeIt,1000)
}

function countdown(time) {
    console.log("app.js");
    var n = new Notification("HI!");

    // if (!"Notification" in window) {
    //     alert("This browser does not support desktop notification");
    // }
    // else if (Notification.permission === "denied") {
    //     alert("This browser has notification blocked");
    // }
    // else if (Notification.permission !== 'denied') {
    //     Notification.requestPermission(function (permission) {
    //         if(!('permission' in Notification)) {
    //             Notification.permission = permission;
    //         }
    //         if (permission === "denied") {
    //             alert("This browser has notification blocked");
    //         }
    //     });
    // }

    document.getElementById("time").innerHTML = time;

    interv = setInterval(timeIt,1000)
    function timeIt() {
        if (document.getElementById("time").innerHTML > 0) {
            document.getElementById("time").innerHTML--;
        }
        else {
            notifyMe();
            clearInterval(interv)
        }
    }
}