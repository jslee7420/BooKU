const openBtn = document.getElementById("forgot_password");
const modal = document.querySelector(".modal_wrap");
const closeBtn = modal.querySelector(".close_btn");
const overlay= modal.querySelector(".modal_overlay");

const openModal = () => {
    modal.classList.remove("hidden");
}

const closeModal = () => {
    modal.classList.add("hidden");
}
overlay.addEventListener("click", closeModal);
closeBtn.addEventListener("click", closeModal);
openBtn.addEventListener("click",openModal);