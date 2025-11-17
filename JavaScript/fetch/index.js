
const row = document.getElementById('row')

async function getPost() {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts')

    if (!response.ok) {
        console.log('Error')
    }

    const posts = await response.json()
    return posts

}


async function createCard() {

    posts = await getPost()

    for (let post of posts) {

        let title = post.title

        let text = post.body

        let card = `<div class="col-3">
          <div class="card">
            <div class="card-body">
              <h5 class="card-title">${title}</h5>
              <p class="card-text">${text}</p>
              <a href="#" class="card-link">Card link</a>
            </div>
          </div>
        </div>`

        row.innerHTML += card
    }
}




createCard()


