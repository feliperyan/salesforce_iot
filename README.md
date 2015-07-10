#Internet of Things demo
##Scan an rfid tag or card and have that automatically bring up a record on Salesforce and Salesforce1.


###Process flow
- Uses an Arduino with an rfid module to read tags.
- Pushes tag data to Python which sends a http request with the data to a Websocket server on Heroku.
- On the Salesforce side a Visualforce page is connected to the Heroku server via Socket.IO. 
- Visualforce receives the emmited rfid data, bringing up an associated Contact record.

###Notes:
- Demo uses a custom field in the Contact object called RFID to associate the tags id with a record.
- It requires Python and a few libraries installed.
- Demo can be run without an Arduino and the tags by using curl to issue the http post. Use the -d flag and data in the form of: {'the_id':'SF RAW ID HERE'} this is a lot simpler.

Example:

```
curl -i -H "Content-Type: application/json" -X POST -d '{"the_id":"0061500000RbkHs"}' https://cryptic-tor-2725.herokuapp.com/api/v1.0/scans
``` 
