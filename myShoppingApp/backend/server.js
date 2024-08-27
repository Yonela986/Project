const express = require('express');
const bodyParser = require('body-parser');
const emailService = require('./emailService');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));

app.post('/request-payment', (req, res) => {
  const { email } = req.body;
  emailService.sendPaymentDetails(email)
    .then(() => res.status(200).send('Request sent'))
    .catch(error => res.status(500).send('Failed to send request'));
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
