var express = require('express');
var router = express.Router();

var app = express();

// var server = app.listen(4201);
// var io = require('socket.io').listen(server);



router.get('/', function(req, res, next) {
  io.sockets.emit('message', data);
  console.log(1);
});


module.exports = router;