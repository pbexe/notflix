function create_movie:
    if post request:
        Get the movie information from the post request
        Add the movie to the database
    else:
        Return the create movie page

function get_movie_details:
    if the user is logged in:
        Get the movie primary key from the URL
        Check if the movie exists
        if it does:
            Render the movie information
        else:
            Return a 404 page
    else:
        Redirect to the login screen

function like_movie:
    if the user is logged in:
        Get the movie pk from the POST request
        Update the DB to reflect the user's like
    else:
        Redirect to a login page

function dislike_movie:
    if the user is logged in:
        Get the movie pk from the POST request
        Update the DB to reflect the user's dislike
    else:
        Redirect to a login page

function index:
    if the user is logged in:
        Display movies they may like using their previous likes and dislikes and the reccomendation alogrithm
    else:
        Render advertising and encourage login/signup

function signup:
    if the request is POST:
        Create a user using the information in the POST request
    else:
        Render the signup from

function login:
    if the request is POST:
        Login a user using the information in the POST request
    else:
        Render the login from

function logout:
    if the request is POST:
        Log the user out
        Redirect to the logged out page