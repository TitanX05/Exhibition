var http = require("http");
var fs = require("fs");
var url = require("url");

http
  .createServer(function (req, res) {
    var x = url.parse(req.url, true);
    var file = "." + x.pathname;
    fs.readFile(file, function (err, data) {
      if (err) {
        res.writeHead(404, { "Content-Type": "text/html" });
        res.end("404 not found");
      }
      res.writeHead(200, { "Content-Type": "text/html" });
      res.write(data);
      res.end();
    });
  })
  .listen(8080);
