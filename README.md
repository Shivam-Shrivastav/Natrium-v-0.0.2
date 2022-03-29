# Natrium-v-0.0.2


CREATE A FUNCTION IN PYTHON IN ORDER TO FILTER BEST MATCHING USER FROM AN ARRAY OF USER 

FILTERATION IS BASED ON THE NUMBER OF MATCHES BETWEEN THE USER AND THE USER IN THE ARRAY


reference to boto3 for aws dynamodb (https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.scan)

reference for api gateway boto3 module ()




FILTERATION IS BASED PRIMARILY ON THE TYPE PROPERTY UNDER FILTERS 

IF A USER IS WITH STRICT filter["type"] THEN THE USER WILL BE FILTERED WITH ONLY THE USERS MATHCHING THE FILTER TYPE ONLY /-
ELIF A USER IS WITH filter["type"] = "ANY" THEN THE USER WILL BE FILTERED WITH THE DEFINED WAY /-


BELOW LISTED ARE THE PRIORITIES 


1. user["filter"]["location"]
2. user["age"]
3. user["gender"]
5. user ['languages']
4. user['profession']
5. user['AccountType']
6. user['Interest1'], user['Interest2'],user['Interest3']





1. CREATE A FUNCTION THAT TAKES IN AN ARRAY OF USERS AND A USER
2. CREATE A FOR LOOP THAT ITERATES THROUGH THE ARRAY OF USERS
3. CREATE A FOR LOOP THAT ITERATES THROUGH THE USER'S PREFERENCES

## SAMPLE USER

```
user = {
 "id": "0a45c971-aa4d-4521-9d4a-a2bb24ba15cb",
 "__typename": "User",
 "following": 80,
 "EmailId": "Pragya@ayesavi.com",
 "_lastChangedAt": 1648577463231,
 "followers": 90,
 "createdAt": "2022-03-29T18:11:03.197Z",
 "UserName": "pragya_meshram@aye",
 "Profession": "Engineer",
 "Gender": "FEMALE",
 "_version": 1,
 "PhoneNumber": "+89632987429",
 "updatedAt": "2022-03-29T18:11:03.197Z",
 "Stories": [],
 "userConfig": {
  "Interest1": " Food",
  "location": {
      "country":"canada",
      "city":"vancouver"
  },
  "Interest3": "coding",
  "Interest2": "love",
  "ShortDescription": "Im a aeronautical  engineer working with national aeronautics"
 },
 "AccountType": "PUBLIC",
 "Name": "pragya meshram",
 "Age": "42",
 "languages":["English","Czech","Spanish","French","Hindi"],
 "filters":{
     "type":"strict",     # 1st priority 
      "regional_Filter": True,  # 2nd priority
      "category":{
          "Profession":"Engineer",
          "Gender":"Male",
          "location":"India",
          "languages":["french"]
      }
 }
}

```


