const express = require("express");
const app = express();
const { PythonShell } = require("python-shell");
app.get("/", (req, res, next) => {
  PythonShell.run("algorithms.py", null, function (err, result) {
    if (err) throw err;
    console.log("result: ", result.toString());
    res.send(result.toString());
  });
});
const port = 8500;
app.listen(port, () => console.log(`Server connected to ${port}`));
