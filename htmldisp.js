const express = require("express");
const path = require("path");
const app = express();
app.use(express.static('public'))
app.listen(3000, () => {
  console.log("Application started and Listening on port 3000");
console.log(__dirname);
});

app.get("/", (req, res) => {
res.sendFile(__dirname+"\\public\\base.html");
})