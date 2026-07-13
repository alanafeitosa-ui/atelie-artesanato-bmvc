document.addEventListener('DOMContentLoaded', () => {
    const linksInternos = document.querySelectorAll('a[href^="#"]');

    linksInternos.forEach((link) => {
        link.addEventListener('click', (evento) => {
            const destino = document.querySelector(link.getAttribute('href'));
            if (destino) {
                evento.preventDefault();
                destino.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    const topo = document.querySelector('.topo');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 20) {
            topo.style.boxShadow = '0 2px 12px rgba(0, 0, 0, 0.06)';
        } else {
            topo.style.boxShadow = 'none';
        }
    });
});