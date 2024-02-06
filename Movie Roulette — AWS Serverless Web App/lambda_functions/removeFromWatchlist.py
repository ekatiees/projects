import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('WatchlistMovies')

def lambda_handler(event, context):
    # delete a movie from a user's watchlist
    try:
        movie_id = json.loads(event['body'])['user_id']
        response = table.delete_item(Key={'user_id': movie_id})
        
        status_code = 200
        body_content = 'The movie has been successfully deleted.'
    except:
        status_code = 502
        body_content = 'Error occurred.'
    
    return {
        'statusCode': status_code,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps(body_content)
    }
