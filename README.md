#Internet of Things demo

Using an Arduino with an RFID module to read tags, pushing tag data to Python which sends a HTTP request with the data to a Websocket server on Heroku. On th e salesforce side a Visualforce page is connected to the Heroku server and receives the emmited data, bringing up an associated Contact record.
