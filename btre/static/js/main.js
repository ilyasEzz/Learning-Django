const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

//  fade out effect on error messages using jquery
setTimeout(() => {
  $('#message').fadeOut('slow');
}, 1000);

// Total  Listing Price
const listing_prices = document.querySelectorAll('.listing_price');
const total_price = document.querySelector('#total_listing_price');
let prices = [];

if (total_price) {
  for (price of listing_prices) {
    prices.push(Number(price.textContent));
  }

  const sum = prices.reduce((acc, current) => acc + current);
  total_price.innerHTML = `${sum} &#8381 / в месяц`;
}
