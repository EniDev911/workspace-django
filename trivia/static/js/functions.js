const btnAudio = document.querySelector(".btn-volume");
const audioMain = new Audio("/static/music/home.wav");

btnAudio.addEventListener("click", async () => {
    const childBtnAudio = btnAudio.firstElementChild;
    if (childBtnAudio.classList.contains("fa-volume-high")) {
        childBtnAudio.classList.replace("fa-volume-high", "fa-volume-xmark");
        audioMain.muted = true
    } else {
        childBtnAudio.classList.replace("fa-volume-xmark", "fa-volume-high");
        audioMain.muted = false
        audioMain.loop = true;
        await audioMain.play();
    }
})

document.addEventListener("load", async () => {
    console.log(audioMain);
    audioMain.loop = true;
    await audioMain.play();
})
