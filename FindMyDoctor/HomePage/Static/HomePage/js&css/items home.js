 

fetch('jsonFile/items.json')
            .then(Response => Response.json())
            .then(data =>{
                const item_sale= document.querySelector("#item_sale");
                
                all_products_json= data
                
                data.forEach(product =>{
                    if(product.old_price){
                        item_sale.innerHTML += `
                            <div class="product"> 
                            <div class="img_product">
                               <span class="add-to-cart " onclick="add_to_cart(${product.id},this)"><img src="${product.img}" alt=""></span>
                            </div>
                            <h3 class="name_product"> ${product.name}</h3>

                            <div class="price">
                                <p><span>$${product.price}</span></p>
                                <p class="old_price">$${product.old_price}</p>
                            </div>
                        </div>
                        `
                    
                    
                        
                        }   
                        


                        


                        
                    })
                })


// let jsondata = fetch('jsonFile/items.json').then;
// console.log(jsondata)

// function add_to_cart(){
//     const items_in_cart= document.getElementsByClassName("items_in_cart");
//     items_in_cart.innerHTML +=`
//     <div class="item_cart">
//                 <img src="${product.img}" alt="1">
//                 <div class="content">
//                     <h4>${all_data.product.name}</h4>
//                     <p class="price_cart">$${all_data.product.price}</p>
//                 </div>
//                 <button class="delete_item"><i class="fa-solid fa-trash-can"></i></button>
//             </div>

    
//     `

// }   


