import json
import boto3

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('WatchlistMovies')

def lambda_handler(event, context):
    # Add a movie to the WatchlistMovies table
    try:
        username = event['requestContext']['authorizer']['claims']['cognito:username']
        movie_info = json.loads(event['body'])
    
        table.put_item(
            Item={
                "user_id": username + '_' + str(movie_info['id']),
                "title": movie_info['title'],
                "year": movie_info['year'],
                "genre": movie_info['genre'],
                "rating": movie_info['rating'],
                "overview": movie_info['overview'],
                "poster": movie_info['poster']
            }
        )
        
        return {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'message': 'The movie has been successfully added to your watchlist.'})
        }
        
    except:
        return {
            'statusCode': 502,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'message': 'Error occurred.'})
        }
        
    