function toggleMenu() {
    var menu = document.querySelector('.submenu');
    menu.classList.toggle('active');

    // Toggle animation class for menu button
    var menuButton = document.getElementById('menu-button');
    menuButton.classList.toggle('active');
}

// Function to fetch distance measurements from the server
function fetchDistanceMeasurements() {
    return fetch('api/tag/upload/') // Adjust the URL to match your server's endpoint
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch distance measurements');
            }
            return response.json();
        });
}

// Function to update the position of the dot based on distance measurements
function updateDotPosition() {
    // Fetch distance measurements from the server
    fetchDistanceMeasurements()
        .then(distanceMeasurements => {
            // Calculate position based on distance measurements (example: trilateration)
            const x = calculateXPosition(distanceMeasurements);
            const y = calculateYPosition(distanceMeasurements);

            // Update dot's position on the webpage
            const dot = document.querySelector('.dot');
            dot.style.left = x + 'px';
            dot.style.top = y + 'px';
        })
        .catch(error => {
            console.error('Error fetching or updating dot position:', error);
        });
}

// Example function to calculate X position based on distance measurements
function calculateXPosition(distanceMeasurements) {
    // Example implementation (replace with your actual calculation)
    // For simplicity, let's assume the X position is the average of all X distances
    const xDistances = distanceMeasurements.map(measurement => measurement.xDistance);
    const averageXDistance = xDistances.reduce((total, distance) => total + distance, 0) / xDistances.length;
    return averageXDistance;
}

// Example function to calculate Y position based on distance measurements
function calculateYPosition(distanceMeasurements) {
    // Example implementation (replace with your actual calculation)
    // For simplicity, let's assume the Y position is the average of all Y distances
    const yDistances = distanceMeasurements.map(measurement => measurement.yDistance);
    const averageYDistance = yDistances.reduce((total, distance) => total + distance, 0) / yDistances.length;
    return averageYDistance;
}

// Update dot's position initially
updateDotPosition();

// Periodically update dot's position (every 5 seconds)
setInterval(updateDotPosition, 5000);


// ---------------------------------------------------------------
// JavaScript for fetching data and rendering the chart
document.addEventListener('DOMContentLoaded', function () {
    fetchDataAndRenderChart();
});

function fetchDataAndRenderChart() {
    // Simulated data for demonstration (replace with actual data fetched from server)
    const data = [
        { site_number: 'Site1', number_of_assets: getRandomNumber(1, 20) },
        { site_number: 'Site2', number_of_assets: getRandomNumber(1, 20) },
        { site_number: 'Site3', number_of_assets: getRandomNumber(1, 20) },
        { site_number: 'Site4', number_of_assets: getRandomNumber(1, 20) },
        { site_number: 'Site5', number_of_assets: getRandomNumber(1, 20) }
    ];

    // Extract site numbers and number of assets from data
    const siteNumbers = data.map(item => item.site_number);
    const numberOfAssets = data.map(item => item.number_of_assets);

    // Render the chart
    renderChart(siteNumbers, numberOfAssets);
}

function renderChart(siteNumbers, numberOfAssets) {
    var ctx = document.getElementById('assetChart').getContext('2d');
    var assetChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: siteNumbers,
            datasets: [{
                label: 'Number of Assets',
                data: numberOfAssets,
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}

// Function to generate a random number between min and max (inclusive)
function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
