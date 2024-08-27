const nodemailer = require('nodemailer');

const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'your-email@gmail.com',
    pass: 'your-email-password'
  }
});

const sendPaymentDetails = (recipientEmail) => {
  const mailOptions = {
    from: 'your-email@gmail.com',
    to: recipientEmail,
    subject: 'Payment Details Request',
    text: 'Here are the payment details...'
  };
  return transporter.sendMail(mailOptions);
};

module.exports = { sendPaymentDetails };
