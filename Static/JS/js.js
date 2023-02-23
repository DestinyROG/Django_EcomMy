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

function incrementc(){
    a=document.activeElement.id;
    hidQty=parseInt(document.getElementById('hid-qty'+a).value);
    qty=parseInt(document.getElementById('qty'+a).value);
    prod_id=document.getElementById('prod_id'+a).value;
    token=document.getElementsByName('csrfmiddlewaretoken')[parseInt(a)+1].value;
    if(qty<hidQty){
        document.getElementById('qty'+a).value=qty+1
        data= new FormData()
        data.append('prod_id',prod_id)
        data.append('qty',qty+1)
        data.append('csrfmiddlewaretoken',token)
        fetch("/update-cart",{
            method: "POST",
            body: data,
        })
    }
}

function decrementc(){
    a=document.activeElement.id
    hidQty=parseInt(document.getElementById('hid-qty'+a).value);
    qty=parseInt(document.getElementById('qty'+a).value);
    prod_id=document.getElementById('prod_id'+a).value;
    token=document.getElementsByName('csrfmiddlewaretoken')[0].value;
    if(qty>1){
        document.getElementById('qty'+a).value=qty-1
        data= new FormData()
        data.append('qty',qty-1)
        data.append('prod_id',prod_id)
        data.append('csrfmiddlewaretoken',token)
        fetch('/update-cart',{
            method:'POST',
            body:data,
        })
    }
}


function remove() {
    a=document.activeElement.classList[2].slice(6,)
    prod_id=document.getElementById('prod_id'+a).value
    token=document.getElementsByName('csrfmiddlewaretoken')[0].value
    data= new FormData()
    data.append('prod_id',prod_id)
    data.append('csrfmiddlewaretoken',token)
    console.log(prod_id)
    fetch('/remove',{
        method:"POST",
        body:data,
    })
    $('#mycart').load(location.href + ' #mycart')
}



function resistration(){
    first_name=document.getElementById('first_name').value
    last_name=document.getElementById('last_name').value
    username=document.getElementById('username').value
    email=document.getElementById('email').value
    password1=document.getElementById('password1').value
    password2=document.getElementById('password2').value
    token=document.getElementsByName('csrfmiddlewaretoken')[0].value 
    data=new FormData()
    data.append('first_name',first_name) 
    data.append('last_name',last_name)
    data.append('username',username)
    data.append('email',email)
    data.append('password1',password1)
    data.append('password2',password2)
    data.append('csrfmiddlewaretoken',token)
    p = fetch('/account/resister',{
            method:"POST",
            body:data,
        })

    p.then((value) =>{
        if(value.redirected == false){ 
            alertify.set('notifier','position', 'top-left');
            alertify.success('User name is already taken');
        }
        else{
            alertify.set('notifier','position', 'top-left');
            alertify.success('You resistered succesfully');
            target=document.getElementById('signup').getAttribute('data-bs-target')
            toggle=document.getElementById('signup').getAttribute('data-bs-toggle')
            target+='login'
            toggle='modal'
            console.log(toggle)
        }
    })
}