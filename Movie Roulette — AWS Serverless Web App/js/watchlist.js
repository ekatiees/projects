//document.getElementById('button_test').addEventListener('click', () => {
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('movieList').innerText = 'Loading...';
    var MovieRoulette = window.MovieRoulette || {};
    var authToken;

    let currentPage = 1;

    // Retrieve the auth token and ensure the user is signed in before proceeding
    MovieRoulette.authToken.then(function setAuthToken(token) {
        if (token) {
            authToken = token;
            const postApiUrlWatchlist = _config.api.invokeUrl + '/getwatchlist';

            const itemsPerPage = 5;

            function fetchMovies() {
                fetch(postApiUrlWatchlist, {
                    method: 'POST',
                    headers: {
                        'Authorization': authToken,
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({})
                })
                .then(response => response.json())
                .then(data => {
                    const movies = data;
                    displayMovies(movies.slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage));
                    setupPagination(movies.length, currentPage);
                })
                .catch(error => {
                    console.error('Error:', error);
                    document.getElementById('movieList').innerHTML = 'You have not saved any movies yet.';
                });
            }

            function displayMovies(movies) {
                const container = document.getElementById('movieList');
                container.innerHTML = '';
                movies.forEach((movie, index) => {
                    const movieElement = document.createElement('div');
                    movieElement.innerHTML = `
                        <div class="movie-watchlist flex-row">
                            <div class="movie-poster-watchlist">
                                <img src="${movie.poster}" alt="${movie.title} Poster" class="img">
                            </div>
                            <div class="movie-watchlist-info-container flex-row">
                                <div class="movie-info-watchlist">
                                    <h3 class="movie-title-watchlist">
                                        ${movie.title}
                                        <span class="movie-year-watchlist">(${movie.year})</span>
                                    </h3>
                                    <div class="movie-info-chars-watchlist flex-row">
                                        <p class="movie-genre-watchlist">${movie.genre}</p>
                                        <div class="movie-rating-watchlist-container flex-row">
                                            <img src="img/star.png" alt="Rating">
                                            <p class="movie-rating-watchlist">${movie.rating}</p>
                                        </div>
                                    </div>
                                    <p>${movie.overview}</p>
                                </div>
                            
                                <div class="remove-button">
                                    <button class="removeFromWatchlist black-btn" id="removeFromWatchlist-${index}">Remove</button>
                                </div>
                            </div>
                        </div>
                    `;
                    container.appendChild(movieElement);


                    // Add event listener for the remove button
                    document.getElementById(`removeFromWatchlist-${index}`).addEventListener('click', function() {
                        const deleteApiUrlWatchlist = 'https://nml8hdt8la.execute-api.eu-central-1.amazonaws.com/prod/removefromwatchlist';
                        fetch(deleteApiUrlWatchlist, {
                            method: 'DELETE',
                            headers: {
                                'Authorization': authToken,
                                'Content-Type': 'application/json'
                            },
                            body: JSON.stringify({ user_id: movie.user_id })
                        })
                        .then(response => {
                            if (response.ok) {
                                fetchMovies(); // Refresh the movie list to reflect the removal
                            } else {
                                console.error('Failed to remove movie from watchlist.');
                            }
                        })
                        .catch(error => console.error('Error:', error));
                    });
                });
            }

            function setupPagination(totalItems) {
                const pageCount = Math.ceil(totalItems / itemsPerPage);
                const paginationContainer = document.getElementById('pagination');
                paginationContainer.innerHTML = '';

                for (let i = 1; i <= pageCount; i++) {
                    const pageButton = document.createElement('button');
                    pageButton.innerText = i;
                    pageButton.className = `yellow-btn ${i === currentPage ? 'yellow-btn' : 'black-btn'}`;
                    pageButton.addEventListener('click', () => {
                        currentPage = i;
                        fetchMovies();
                    });
                    paginationContainer.appendChild(pageButton);
                }
            }

            fetchMovies();
        } else {
            document.getElementById('movieList').innerText = 'Sign in to see your watchlist.';
        }
    }).catch(function handleTokenError(error) {
        alert(error);
        document.getElementById('movieList').innerText = 'Error';
    });
});