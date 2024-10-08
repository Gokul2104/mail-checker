# mail-checker
1) This will read from inbox and save your messages to database
2) From the list of messages saved in db we can apply rules from json file and do the following actions
   1) mark as read
   2) mark as unread
   3) Move to labels 
3) Rules can be applied only on the following fields

### Prerequisites
    1) Create Credentials for Oauth in Google
    2) Download the credentials and update the path of cred_file in config.py

## How to write rules
1) create Json File and save the rule_path path in config 
2) It should be a array of object where each object has set of 
   rules and actions
3) ```json
      [
         {
            "rule": {
               "apply": "any",
               "filter":[
              {
                "Field": "Subject",
                "Predicate": "contains",
                "Value": "Email"
              }
            ]
            },
            "action":[{
              "Type": "mark",
               "To": "read"
            }]
         }
      ]
      ```
   
4) Allowed Values and Type
```
rule:Object - with Keys(apply, filter)
   apply: String - oneof(any, all) any will have or condition,
    all will have and condition
   filter: Array(object) - (Field,Predicate,Value,Metrics)
      
      Field:String (From,To,Subject,Message,Received At)
      (Field not Received At)
         Predicate:String ("contains", "not contains", "equals", "does not equals")
         Value:String 
      (Field = Received At)
         Predicate:String ("less than", "greater than")
         Value:Int
         Metrics:String ("days", Months)
         
Action:  Array(object) - (Type, To)
   Type:String - (mark, move)
   (Type = mark)
      To: String(read, unread)
   (Type = Move)
      To: String <labelName>
```

## How to run
```commandline
python driver.py pull  
```
This will pull the data from email to sqlite
```commandline
python driver.py rule  
```
The above command will apply the rule and actions
