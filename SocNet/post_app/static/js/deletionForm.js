const deletionForm = document.querySelector('#deletionForm')
const deleteIDInput = document.querySelector('#deleteIDInput')
const deletePostButtons = document.querySelectorAll('#deletePost')

deletePostButtons.forEach((button) => {
    button.addEventListener('click', (event) => {
        postID = button.parentElement.id.split('-')[1]
        deleteIDInput.setAttribute('value', postID)
        deletionForm.submit()
    })
})