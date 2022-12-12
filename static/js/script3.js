const url = window.location.href;
const searchForm = document.getElementById('search-form');
const searchInput = document.getElementById('search-input');
const resultsBox = document.getElementById('results-box');

const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;

const sendSearchData = (item) => {
    $.ajax({
        type: 'POST',
        url: `items/search/`,
        data: {
            'csrfmiddlewaretoken': csrf,
            'item': item,
        },
        success: (res) => {
            console.log(res.data)
            const data = res.data
            if (Array.isArray(data)) {
                resultsBox.innerHTML = "";
                data.forEach(item => {
                    resultsBox.innerHTML += `
                    <div class="border">
                        <a href="${url}items/${item.pk}/" class="item">
                            <div class="row justify-content-md-center">
                                <div class="col-sm">
                                    <img src="${item.image}" class="item-img">
                                </div>                            
                                <div class="col-sm">
                                    <h5>${item.title}</h5>
                                    <p class="text-muted">${item.type}</p>
                                </div>
                            </div>
                        </a>
                    </div>
                    `
                })
            }
            else {
                if (searchInput.value.length > 0) {
                    resultsBox.innerHTML = `<b>${data}</b>`
                }
                else {
                    resultsBox.classList.add('not-visible');
                }
            }
        },
        error: (err) => {
            console.log(err)
        }
    })
}


searchInput.addEventListener('keyup', e => {
    console.log(e.target.value)

    if (resultsBox.classList.contains('not-visible')) {
        resultsBox.classList.remove('not-visible');
    }

    sendSearchData(e.target.value);
});