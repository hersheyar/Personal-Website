document.addEventListener('DOMContentLoaded', () => {
    // Skills toggle functionality
    const skillsToggle = document.getElementById('skills-toggle');
    const skillGrid = document.getElementById('skill-grid');
    const lockIcon = skillsToggle ? skillsToggle.querySelector('span') : null;

    if (skillsToggle && skillGrid && lockIcon) {
        skillsToggle.addEventListener('click', () => {
            const isVisible = skillGrid.style.display !== 'none';
            skillGrid.style.display = isVisible ? 'none' : 'grid';
            lockIcon.textContent = isVisible ? '🔒' : '🔓';

            if (!isVisible) {
                // Scroll to the skill grid when showing
                skillGrid.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            } else {
                // Optional: scroll back up to the toggle when hiding
                skillsToggle.scrollIntoView({
                    behavior: 'smooth',
                    block: 'center'
                });
            }
        });

        // Start with skills hidden
        skillGrid.style.display = 'none';
    }

    // Loading animations with Intersection Observer
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('loading');
            }
        });
    }, observerOptions);

    // Observe all elements with loading class
    document.querySelectorAll('.loading').forEach(el => {
        observer.observe(el);
    });

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});
