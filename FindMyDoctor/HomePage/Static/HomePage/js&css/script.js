// cart

var cart= document.querySelector('.cart');

function open_cart(){
    cart.classList.add('active');
};

function close_cart(){
    cart.classList.remove('active');
};


var all_products_json;

var items_in_cart = document.querySelector(".items_in_cart");
let product_cart = [];

function add_to_cart(id, btn) {
    product_cart.push(all_products_json[id]);
    btn.classList.add('active');
    console.log(product_cart);
    get_cart_items();
}



let pirce_cart_head = document.querySelector('.pirce_cart_head')
let count_item_cart = document.querySelector('.count_item_cart')
let price_cart_total = document.querySelector('.price_cart_total')

function get_cart_items() {
    let total_price = 0;
    
    let items_c = "";
    for (let i = 0; i < product_cart.length; i++) {
        items_c += `
        <div class="item_cart" data-index="${i}">
            <img src="${product_cart[i].img}" alt="1">
            <div class="content">
                <h4>${product_cart[i].name}</h4>
                <p class="price_cart">$${product_cart[i].price}</p>
            </div>
            <button class="delete_item" onclick="remove_from_cart(${i})"><i class="fa-solid fa-trash-can"></i></button>
        </div>
        `;
        total_price += product_cart[i].price

    }
    items_in_cart.innerHTML = items_c;

    pirce_cart_head.innerHTML = '$' + total_price
    count_item_cart.innerHTML = product_cart.length
    price_cart_total.innerHTML = '$' + total_price
}

function remove_from_cart(index) {
    product_cart.splice(index, 1);
    get_cart_items();
}



// slide images 

var slideIndex = 0;

function plusSlides(position) {
    slideIndex +=position;
    if (slideIndex> slides.length) {slideIndex = 1}
    else if(slideIndex<1){slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
       slides[i].style.display = "none";  
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex-1].style.display = "block";  
    dots[slideIndex-1].className += " active";
}

function currentSlide(index) {
    if (index> slides.length) {index = 1}
    else if(index<1){index = slides.length}
    for (i = 0; i < slides.length; i++) {
       slides[i].style.display = "none";  
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[index-1].style.display = "block";  
    dots[index-1].className += " active";
}


// footer

let backToTop = document.querySelector('.back-to-top');
backToTop.addEventListener('click',function(){
    window.scrollTo({
        top: 0,
        behavior:"smooth"
    })
})



