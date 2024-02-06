import json
import boto3

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('WatchlistMovies')

def lambda_handler(event, context):
    # get watchlist by user_id
    print(event)
    try:
        username = event['requestContext']['authorizer']['claims']['cognito:username']
        table_items = table.scan()['Items']
    
        user_watchlist = []
        
        for item in table_items:
            if item['user_id'].split('_')[0] == username:
                user_watchlist.append(item)
        
        status_code = 200 if len(user_watchlist) != 0 else 201
        response = json.dumps(user_watchlist) if len(user_watchlist) != 0 else json.dumps("There're no movies in your watchlist yet.")

    except:
        status_code = 202
        response = json.dumps("Please, sign in to see your watchlist.")
    
    return {
        'statusCode': status_code,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': response
    }