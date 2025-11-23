const ctx = document.getElementById('securityChart');

new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Accès autorisés (200)', 'Accès refusés (403)'],
        datasets: [{
            label: 'Nombre de Requêtes',
            data: [12, 3],  // tu peux modifier pour ton exemple
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: { beginAtZero: true }
        }
    }
});
