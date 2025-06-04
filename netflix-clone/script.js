// Basic script to demonstrate dynamic interactions
// In a real application you would load data from a server

console.log('MyFlix loaded');

// Example: show an alert when a poster is clicked
const posters = document.querySelectorAll('.poster');
posters.forEach(poster => {
    poster.addEventListener('click', () => {
        alert('This is a demo. Streaming not implemented.');
    });
});
