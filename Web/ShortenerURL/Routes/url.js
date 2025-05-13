const express = require("express");
const router = express.Router();
const Url = require("../Model/Url");
const {nanoid} = require("nanoid");

router.post("/shorter", async (req, res) =>{
    const {url} = req.body;

    if (!url) return res.status(400).json({error:"Bad Request"});

    //colisão
    const shorterId = nanoid(7);

    await Url.create({ shortId, originalUrl: url });

  res.json({ shortUrl: `http://localhost:3000/${shortId}` });
});

router.get('/:shortId', async (req, res) => {
  const { shortId } = req.params;

  const found = await Url.findOne({ shortId });

  if (found) {
    res.redirect(found.originalUrl);
  } else {
    res.status(404).json({ error: 'Link não encontrado' });
  }
});

module.exports = router;