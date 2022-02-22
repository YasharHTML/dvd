const express = require("express");
const app = express();
const path = require('path')
app.use("/css", express.static("./public"))
app.get("/", (req, res) => {
    res.sendFile(__dirname + "/public/index.html")
});

app.listen(3000, () => console.log("Listening at 3000"));