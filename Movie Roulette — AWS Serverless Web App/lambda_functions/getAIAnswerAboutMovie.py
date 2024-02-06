from bardapi import BardCookies
import os
import json

def lambda_handler(event, context):
    # get cookies and set up bard
    cookie_dict = {
        "__Secure-1PSID": os.environ.get("BARD_1PSID"),
        "__Secure-1PSIDTS": os.environ.get("BARD_1PSIDTS"),
        "__Secure-1PSIDCC": os.environ.get("BARD_1PSIDCC")
    }

    bard = BardCookies(cookie_dict = cookie_dict)

    # get AI answer to a user's question
    movie_answer = bard.get_answer(f"Answer the following question about the movie {event['movie_title']}: " + event['movie_question'] + ". Don't format the text.")
    movie_answer = movie_answer['content']
    
    # return the AI answer to the user
    return {
        'statusCode': 200,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps(movie_answer)
    }