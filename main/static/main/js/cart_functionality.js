let updateBtn = document.getElementsByClassName('update-cart')

for (let i = 0; i < updateBtn.length; i++) {
    updateBtn[i].addEventListener('click', function () {
        let productId = updateBtn[i].dataset.id
        let action = this.dataset.action

        console.log(productId, action)

        console.log('USER', user)
        if (user === 'AnonymousUser') {
            console.log('Not LogIn')
            redirectLogin()
        } else {
            console.log('Sending Data')
            updateUserCart(productId, action)
        }
    })
}

function redirectLogin(){

   window.location.href = "/login/"


}

function updateUserCart(productId, action) {

    let url = '/update_cart/'

    fetch(url,{
        method: 'POST',
        headers: {
            'Content-Type': "application/json",
            'X-CSRFToken': csrftoken
        },
        body:JSON.stringify({
            'productId': productId,
            'action': action
        })
    }).then((response)=>{
        return response.json()
    }).then((data)=>{
        console.log('data', data)
        location.reload()
    })


}