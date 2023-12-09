const express = require("express");
const { PythonShell } = require("python-shell");

const app = express();

app.listen(3000, () => {
  console.log("Application started and Listening on port 3000");
});

app.use(express.static(__dirname));

app.get("/home", (req, res) => {
  res.sendFile(__dirname + "/Index.html");
});

app.get("/notation", (req, res) => {
  res.sendFile(__dirname + "/Notations.html");
});

app.get("/tutorial1", (req, res) => {
  res.sendFile(__dirname + "/Tutorial1.html");
});

app.get("/tutorial2", (req, res) => {
  res.sendFile(__dirname + "/Tutorial2.html");
});

app.get("/tutorial3", (req, res) => {
  res.sendFile(__dirname + "/Tutorial3.html");
});

app.get("/tutorial4", (req, res) => {
  res.sendFile(__dirname + "/Tutorial4.html");
});

app.get("/tutorial5", (req, res) => {
  res.sendFile(__dirname + "/Tutorial5.html");
});

app.get("/scan", (req, res) => {
  PythonShell.run("algorithms.py", null).then((messages) => {
    console.log("SUCCESSSSSS!");
  });
});
