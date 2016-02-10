var express = require('express')
  , http = require('http');

var app = express();
var server = app.listen(4200);
var io = require('socket.io').listen(server);

// var routes = require('./routes/index');

io.on('connection', function(client) {  
    console.log('Client connected...');

    client.on('join', function(data) {
        console.log(data);
    });
});


console.log("Express server listening on port 4200");

app.get('/', function(req, res) {
	io.sockets.emit('messages', 'You got a new order');
	res.end();
});
app.post('/order', function(req, res) {
	io.sockets.emit('messages', 'You got a new order');
	res.end();
});
