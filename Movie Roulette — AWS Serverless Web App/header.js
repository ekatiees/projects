MovieRoulette.authToken.then(function setAuthToken(token) {
    var authButtonHTML;
    if (token) {
        // User is signed in, display "Sign Out" button
        authButtonHTML = '<a id="signOutButton" class="button black-btn" onclick="MovieRoulette.signOut();" href="index.html">Sign Out</a>';
    } else {
        // User is not signed in, display "Sign In" button
        authButtonHTML = '<a id="signInButton" class="button black-btn" href="signin.html">Sign In</a>';
    }

    // Write the HTML content to the document, including the appropriate authentication button
    document.write(`
        <header id="includeHeader" class="flex-row">
            <div class="app-title">
                <h1>Movie Roulette</h1>
                <p class="subtitle">Discover new films with one click</p>
            </div>
            <div class="app-menu flex-row">
                <div><a href="index.html">Home</a></div>
                <div><a href="watchlist.html">Watchlist</a></div>
                <div>${authButtonHTML}</div>
            </div>
        </header>
    `);
}).catch(function handleTokenError(error) {
    console.error('Error with token:', error);
    // Fallback content in case of error, showing only "Sign In" button
    document.write(`
        <header id="includeHeader" class="flex-row">
            <div class="app-title">
                <h1>Movie Roulette</h1>
                <p class="subtitle">Discover new films with one click</p>
            </div>
            <div class="app-menu flex-row">
                <div><a href="index.html" class="app-menu-a">Home</a></div>
                <div><a href="watchlist.html" class="app-menu-a">Watchlist</a></div>
                <div><a id="signInButton" class="button black-btn" href="signin.html">Sign In</a></div>
            </div>
        </header>
    `);
});
