function expandSibling(el) {
    var chevron = el.querySelector("td:first-child > i").classList;
    chevron.toggle("fa-angle-down");
    chevron.toggle("fa-angle-right");
    el.nextElementSibling.classList.toggle("hide");
}
