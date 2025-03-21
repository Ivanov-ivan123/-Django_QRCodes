const buttonsBuy = document.querySelectorAll('#buy');
const main = document.querySelector('main');
const formCont = document.querySelector(".form-container");
const inputsDiv = document.querySelector("#inputs");
const subscriptionInput = document.querySelector(".hidden-input");
// const desktopNumberInput = document.createElement("input");
const desktopQuantity = document.querySelector("#DesktopQuantity");

console.log(buttonsBuy);
buttonsBuy.forEach((buttonBuy) => {
    buttonBuy.addEventListener('click', () => {
        main.style.display = "None";
        formCont.style.display = "block";
        const buttonChild = buttonBuy.children[0];
        console.log("buttonChild id =", buttonChild.id);
        const subscription = buttonChild.id.split("sub")[1];
        console.log(subscription);
        if (subscription != "Desktop"){
            console.log("desktop quantity =", desktopQuantity)
            desktopQuantity.style.display = "none";
        }
        subscriptionInput.value = subscription;
            // desktopQuantity.classList = 'card-info';
            // desktopQuantity.type = 'number';
            // desktopNumberInput.type = "number";
            // desktopNumberInput.classList = "form-input";
            // desktopQuantity.textContent = 'Максимальна кількість qr-кодів, що ви хочете створити';
            // desktopQuantity.name = "quantity"
            // inputsDiv.appendChild(desktopQuantity);
            // inputsDiv.appendChild(desktopNumberInput);
    })
})