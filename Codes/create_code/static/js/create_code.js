let colorButtonArray = document.getElementsByClassName("color");
let bgColorButtonArray = document.getElementsByClassName("bgColor");
let inputColor = document.getElementById("inputColor");
let inputBgColor = document.getElementById("inputBgColor");
let previousColor;
let previousBgColor;
console.log(colorButtonArray);

let blackColorArray = document.querySelectorAll("#black");
let whiteColorArray = document.querySelectorAll("#white")
console.log("blackColorArray =", blackColorArray);
let blackColor = blackColorArray[0];
blackColor.classList.add("current");
let whiteBgColor = whiteColorArray[1];
console.log("whiteBgColor =", whiteBgColor);
whiteBgColor.classList.add("currentBg");
inputColor.value = "black";
inputBgColor.value = "white";

// colorButtonArray.forEach((colorButton) => {
// for (let index = 0; ){
for (let colorButton of colorButtonArray){
    console.log(colorButton);
    colorButton.addEventListener("click", () => {
        previousColor = document.querySelector(".current");
        console.log(previousColor.classList);
        previousColor.classList.remove("current");
        console.log(previousColor.classList);
        colorButton.classList.add("current");
        inputColor.value = colorButton.id;
        console.log("inputColor =", inputColor.value);
    })
}

for (let bgColorButton of bgColorButtonArray){
    console.log(bgColorButton);
    bgColorButton.addEventListener("click", () => {
        previousBgColor = document.querySelector(".currentBg");
        console.log(previousBgColor.classList);
        previousBgColor.classList.remove("currentBg");
        console.log(previousBgColor.classList);
        bgColorButton.classList.add("currentBg");
        console.log("bgColorButton.id =", bgColorButton.id);
        inputBgColor.value = bgColorButton.id;
        console.log("inputBgColor.value =", inputBgColor.value);
    })
}