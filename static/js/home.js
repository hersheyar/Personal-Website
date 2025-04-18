document.addEventListener('DOMContentLoaded', () => {
  const toggleHeader = document.getElementById('skills-toggle');
  const skillGrid = document.querySelector('.skill-grid');
  const arrow = toggleHeader.querySelector('span');

  toggleHeader.style.cursor = 'pointer';

  toggleHeader.addEventListener('click', () => {
    const isVisible = skillGrid.style.display !== 'none';
    skillGrid.style.display = isVisible ? 'none' : 'flex';
    arrow.textContent = isVisible ? '▶' : '▼';
  });

  // Optional: start hidden
  skillGrid.style.display = 'none';
  arrow.textContent = '▶';
});
