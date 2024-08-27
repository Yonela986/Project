document.addEventListener('DOMContentLoaded', () => {
    // Load clothes items
    loadClothes();
  
    // Contact form submit event
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
      contactForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const email = document.getElementById('email').value;
        const message = document.getElementById('message').value;
        alert(`Message sent! Email: ${email}, Message: ${message}`);
      });
    }
  });
  
  function loadClothes() {
    // This is where you would fetch clothes from your backend
    const clothesList = document.getElementById('clothes-list');
    const clothes = [
      { name: 'Traditional Attire 1', price: 'R100' },
      { name: 'Traditional Attire 2', price: 'R150' }
    ];
  
    clothes.forEach(item => {
      const div = document.createElement('div');
      div.className = 'clothes-item col-md-4';
      div.innerHTML = `
        <div class="card">
          <img src="https://via.placeholder.com/300" class="card-img-top" alt="${item.name}">
          <div class="card-body">
            <h5 class="card-title">${item.name}</h5>
            <p class="card-text">${item.price}</p>
            <button class="btn btn-primary">Add to Cart</button>
            <button class="btn btn-secondary">Add to Wishlist</button>
          </div>
        </div>
      `;
      clothesList.appendChild(div);
    });
  }
  
  function filterClothes() {
    // Filtering logic would go here
  }
  
  function requestPayment() {
    const email = prompt('Enter your email for payment details:');
    if (email) {
      fetch('/request-payment', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email })
      })
      .then(response => response.text())
      .then(data => alert(data))
      .catch(error => alert('Error: ' + error));
    }
  }
  