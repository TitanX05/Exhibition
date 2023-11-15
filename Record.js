// let {PythonShell} = require("python-shell");
// function f(){
//   PythonShell.run("camera.py",null).then(messages=>{
//     console.log("finished");
//   })
// }
const express=require('express');
const app=express();

 
//Import PythonShell module.
const {PythonShell} =require('python-shell');
 
//Router to handle the incoming request.
app.get("/", (req, res, next)=>{
    //Here are the option object in which arguments can be passed for the python_test.js.
    // let options = {
    //     mode: 'text',
    //     pythonOptions: ['-u'], // get print results in real-time
    //       scriptPath: 'path/to/my/scripts', //If you are having python_test.py script in same folder, then it's optional.
    //     args: ['shubhamk314'] //An argument which can be accessed in the script using sys.argv[1]
    // };
     
 
    PythonShell.run('algorithms.py', null, function (err, result){
          if (err) throw err;
          // result is an array consisting of messages collected 
          //during execution of script.
          console.log('result: ', result.toString());
          res.send(result.toString())
    });
});

 
//Creates the server on default port 3000 and can be accessed through localhost:3000node

const port=3000;
app.listen(port, ()=>console.log(`Server connected to ${port}`));

// const http = require('http');

// const hostname = '127.0.0.1';
// const port = 3000;

// const server = http.createServer((req, res) => {
//   res.statusCode = 200;
//   res.setHeader('Content-Type', 'text/plain');
//   res.end('Hello World\n');
// });

// server.listen(port, hostname, () => {
//   console.log(`Server running at http://${hostname}:${port}/`);
// });