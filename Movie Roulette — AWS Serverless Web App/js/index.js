// Get random movie button

document.getElementById('getRandomMovieButton').addEventListener('click', () => {
    document.getElementById('movieInfo').innerText = 'Loading...';
    const apiUrl = _config.api.invokeUrl + '/getrandommovie';

    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const movieInfo = JSON.parse(data.body);
            displayMovieInfo(movieInfo);
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });
});

function displayMovieInfo(movie) {
    const movieInfoDiv = document.getElementById('movieInfo');
    movieInfoDiv.innerHTML = `
        <div class="movie flex-row">
            <div class="movie-container flex-row">
                <div class="movie-poster"><img src="${movie.poster}" alt="${movie.title} Poster" class="img"></div>
                <div class="movie-info">
                    <h2 class="movie-info-header movie-title">
                        ${movie.title}
                        <span class="movie-year">(${movie.year})</span>
                    </h2>
                    <div class="movie-info-chars flex-row">
                        <div class="movie-genre">${movie.genre}</div>
                        <div class="movie-rating-container flex-row">
                            <div class="movie-rating"><img src="img/star.png" alt="Rating" class="img"></div>
                            <div class="movie-rating-value">${movie.rating}</div>
                        </div>
                    </div>
                    <h3 class="strong-heading">Overview</h3>
                    <p>
                        ${movie.overview}
                    </p>

                    <form id="aiQuestionForm" class="flex-row">
                        <input type="text" name="movieQuestion" placeholder="Ask AI about ${movie.title}..." class="form-input">
                        <div><input type="submit" value="Ask" class="button black-btn"></div>
                    </form>

                    <div id="AIAnswer"></div>

                </div>
            </div>
            <div class="saveToWatchlist flex-column">
                <button id="saveToWatchlistButton" class="black-btn flex-row">
                    <div class="watchlist-btn-img"></div>
                    <div>To watchlist</div>
                </button>
                <div id="SaveStatus"></div>
            </div>
        </div>
    `;



    // Ask AI about a movie

    const form = document.getElementById('aiQuestionForm');
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the form from submitting the traditional way
        document.getElementById('AIAnswer').innerText = 'Loading...';
        const question = form.movieQuestion.value; // Get the question from the input field

        // Define the API URL for posting the question
        const postApiUrl = _config.api.invokeUrl + '/getaianswer';

        // Make the POST request with the movie title and question
        fetch(postApiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                movie_title: movie.title,
                movie_question: question
            })
        })
        .then(response => response.json())
        .then(data => {
            // Display the answer in the AIAnswer div
            document.getElementById('AIAnswer').innerText = JSON.parse(data.body);
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('AIAnswer').innerText = 'It\'s a free version of Bard. The cookies changed, so the function has broken down. If you wish to see how this function works, please contact ekatiees@gmail.com.';
        });
    });



    // Save a movie to watchlist

    document.getElementById('saveToWatchlistButton').addEventListener('click', () => {

        var MovieRoulette = window.MovieRoulette || {};
        var authToken;

        // Retrieve the auth token and ensure the user is signed in before proceeding
        MovieRoulette.authToken.then(function setAuthToken(token) {
            if (token) {
                authToken = token;
                const postApiUrlWatchlist = _config.api.invokeUrl + '/savetowatchlist';

                // Proceed with the POST request if the user is authenticated
                fetch(postApiUrlWatchlist, {
                    method: 'POST',
                    headers: {
                        'Authorization': authToken,
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        id: movie.id,
                        title: movie.title,
                        year: movie.year,
                        rating: movie.rating,
                        genre: movie.genre,
                        overview: movie.overview,
                        poster: movie.poster
                    })
                })
                .then(response => response.json())
                .then(data => {
                    // Display the answer in the SaveStatus div
                    document.getElementById('SaveStatus').innerText = 'saved';
                })
                .catch(error => {
                    console.error('Error:', error);
                    document.getElementById('SaveStatus').innerText = 'error';
                });
            } else {
                // Redirect to sign-in page if the user is not authenticated
                window.location.href = 'signin.html';
            }
        }).catch(function handleTokenError(error) {
            alert(error);
            window.location.href = 'signin.html';
        });
    });

}