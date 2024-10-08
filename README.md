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
```json
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
   3) Allowed Values and Type
```
rule - Object with Keys(apply, filter)
   apply: String - oneof(any, all) any will have or condition,
    all will have and condition
   filter: Array(object) - (Field,Predicate,Value, metrics)
```
   

## Setup info

## How to run
