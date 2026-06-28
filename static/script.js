const button = document.getElementById("startButton");
const camera = document.getElementById("camera");
const canvas = document.getElementById("canvas");


button.addEventListener("click", async () => {

    try{
        const stream = await navigator.mediaDevices.getUserMedia({
            video:true
        });
        camera.srcObject = stream;
    }
    catch(err){

        alert("Camera tidak bisa dibuka.");

    }

});

const detectButton = document.getElementById("detectButton");
const emotionText = document.getElementById("emotion");

const titleText =
    document.getElementById("episodeTitle");

const storyText =
    document.getElementById("story"); 

const classText =
    document.getElementById("class");

const spiritText =
    document.getElementById("spirit");

const rankText =
    document.getElementById("rank");


detectButton.addEventListener("click", async () => {

    canvas.width = camera.videoWidth;
    canvas.height = camera.videoHeight;

    const ctx = canvas.getContext("2d");

    ctx.drawImage(
        camera,
        0,
        0,
        canvas.width,
        canvas.height
    );

    const image =
        canvas.toDataURL("image/jpeg");

    const response =
        await fetch("/emotion", {
            method: "POST",
            headers: {
                "Content-Type":
                    "application/json"
            },
            body: JSON.stringify({
                image: image
            })
        });

    const data = await response.json();
//  alert(JSON.stringify(data));

    emotionText.innerText =
        "Your Emotion,krub:" + data.emotion;

    titleText.innerText =
        "Your Episode,krub:" + data.title;

    storyText.innerText =
        data.story;

classText.innerText =
    "Class,krub: " + data.class;

spiritText.innerText =
    "Spirit,krub: " + data.spirit;

rankText.innerText =
    "Rank,krub: " + data.rank;
});
const buttons =
    document.querySelectorAll("button");

buttons.forEach(btn => {
    btn.addEventListener("click", () => {

        btn.animate(
            [
                { transform: "scale(1)" },
                { transform: "scale(0.95)" },
                { transform: "scale(1.08)" },
                { transform: "scale(1)" }
            ],
            {
                duration: 500
            }
        );

    });
});