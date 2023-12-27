// typed below

var add = document.getElementById('add');
var remove = document.getElementById('remove');

function increment(icon) {
    var input_container = icon.parentNode;
    var item_no = input_container.querySelector('.item_no');
    item_no.stepUp();
    checkMaxMin();
};

function decrement(icon) {
    var input_container = icon.parentNode;
    var item_no = input_container.querySelector('.item_no');
    item_no.stepDown();
    checkMaxMin();
};

// document.getElementById("contact-button").addEventListener("click", function(){
//     document.getElementsByClassName("popup")[0].classList.add("active");
// })

// typed below

document.getElementById("contact-button").addEventListener("click", function () {
    // sleep before reset to submit the form first 
    document.getElementById("myForm").reset();
});

// document.getElementById("account_circle").addEventListener("click", function () {
//     var account = document.getElementById("dropdown");
//     account.style.display = 'none'
// })

function remove() {
    $('.error').hide()
}

$('.account_circle').click(function show() {
    $('.dropdown').show();         // check for syntax
})

// in Jquery, 

// semicolon present

// jquery not working

