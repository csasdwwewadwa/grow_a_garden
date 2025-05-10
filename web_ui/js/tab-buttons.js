document.addEventListener('DOMContentLoaded', () => {
    const tabButtons = document.querySelectorAll('.tab');
    const tabContents = document.querySelectorAll('.tab-content');

    const tabMap = {
        'Buying': 'tab-content-buying',
        'Alts': 'tab-content-alts',
        'Configs': 'tab-content-configs'
    };

    tabButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove "active" class from all buttons
            tabButtons.forEach(b => b.classList.remove('active-tab'));
            btn.classList.add('active-tab');

            // Hide all tab contents
            tabContents.forEach(tc => tc.classList.remove('active-tab-content'));

            // Show the selected one
            const targetId = tabMap[btn.textContent.trim()];
            document.getElementById(targetId)?.classList.add('active-tab-content');
        });
    });
});