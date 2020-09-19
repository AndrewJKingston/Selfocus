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
    if (document.getElementById("time").innerHTML == 0 || document.getElementById("time").innerHTML === "____") {
        document.getElementById("info-msg").innerHTML = "You will get notified after the time ends!";
        document.getElementById("info-msg").style = "color:black;";

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
    else {
        alert("You cannot start a new timer until this one ends!");
        document.getElementById("info-msg").innerHTML = "You cannot start a new timer until this one ends!";
        document.getElementById("info-msg").style = "color:red;";
    }
}