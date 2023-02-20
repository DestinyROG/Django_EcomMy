function increment(){
    var a=parseInt(document.getElementById(' qty-box').value)
    if(parseInt(document.getElementById('hid-qty').value)>a){
        document.getElementById(' qty-box').value=a+1
    }
}

function decrement(){
    var a=parseInt(document.getElementById(' qty-box').value)
    if(a>1){
        document.getElementById(' qty-box').value=a-1
    }
}

function addtocart(){
    var  a=parseInt(document.getElementById(' qty-box').value)
    document.getElementById('add-to-cart').href=`/addToCart/${document.getElementById('cate').value}/${document.getElementById('name').value}/${a}`
}