const express = require("express");
const cors = require("cors");

const app=express();
app.use(cors())

const port=3000;

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

app.get('/winProbability/:team1/:team2', (req, res) => {
  const team1 = req.params.team1;
  const team2 = req.params.team2;
    tm1 = parseInt(team1);
    tm2 = parseInt(team2);
  const winProbability = (tm2)/(tm1+tm2)
   // winProbability = winProbability.toFixed(2)
  res.json({
    team1,
    team2,
    winProbability
  });
});

app.get('/', (req, res) => {
    console.log('Hello World!');
    res.json({
        message: 'Hello World!'
    });
    });

