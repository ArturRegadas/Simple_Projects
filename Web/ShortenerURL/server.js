const express = require("epress");
const mongoose = require("mongoose");
const urlRoutes = require("./routes/url");

const app = express();
app.use(express.json());

mongoose.connect("mongodb://localhost:27017/linkShortener", {
    useNewUrlParser:true,
    useUndefiedTopology:true
});

app.use("/", urlRoutes);

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Servidor rodando em http://localhost:${PORT}`);
});