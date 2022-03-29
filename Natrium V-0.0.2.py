import json
import boto3    



def lambda_handler(event, context):
   
    URl =  "https://XX.XX.XX.XX.amazonaws.com/production"
    dynamo = boto3.client("dynamodb")
    client_id = str(event["requestContext"].get("connectionId"))
    usersArray = json.loads(event["body"]).get("connectedUsersArray")
    print(usersArray)
    client = boto3.client("apigatewaymanagementapi",endpoint_url = URl)
    value  = 0
    message = {
        "type":"byAnotherUser",
        "partnerConnectionId":client_id,
    }
    response = dynamo.scan(TableName="Websockets_ConnectionIDS")
    print(response)
    userids = response["Items"]
    settosend = {}
    if userids == []:
         dynamo.put_item(TableName="Websockets_ConnectionIDS",Item= {"connectionId":{"S":client_id}} )
    
    else:
        for USERconnectionIDS in userids:
            value = USERconnectionIDS.get("connectionId").get("S")
            if value != client_id and value not in  usersArray:
                dynamo.delete_item(TableName = "Websockets_ConnectionIDS",Key = {"connectionId":{"S":value}})
                settosend = {
                       "partnerConnectionId":value,
                        "type":"ready",
                        "yourID":client_id,
                }
                message["yourID"] = value;
                respond = client.post_to_connection(ConnectionId = value,Data=json.dumps(message))
    return {
    'statusCode': 200,
    'headers': {'Content-Type': 'application/json'},
    'body': json.dumps(settosend)
}