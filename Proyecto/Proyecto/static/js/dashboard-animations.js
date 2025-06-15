// Archivo de animaciones para el dashboard usando anime.js
// Aquí se implementarán las animaciones según la especificación.

// Estructura para animaciones del dashboard con anime.js
// Cada sección está preparada para implementar la lógica según la especificación.

document.addEventListener('DOMContentLoaded', function () {
    // 1. Animación de contracción/expansión del panel lateral
    // Sidebar: animación de contraer/expandir y hover
    function animarPanelLateral() {
        const sidebar = document.getElementById('sidebar');
        // Hover animaciones en ítems
        const links = sidebar.querySelectorAll('.sidebar-link');
        links.forEach(link => {
            link.addEventListener('mouseenter', () => {
                anime({
                    targets: link,
                    backgroundColor: '#e0e7ff',
                    scale: 1.04,
                    boxShadow: '0 2px 8px 0 rgba(30,64,175,0.08)',
                    duration: 200,
                    easing: 'easeOutQuad'
                });
            });
            link.addEventListener('mouseleave', () => {
                anime({
                    targets: link,
                    backgroundColor: '#fff',
                    scale: 1,
                    boxShadow: '0 0px 0px 0 rgba(0,0,0,0)',
                    duration: 200,
                    easing: 'easeOutQuad'
                });
            });
        });
    }

    // 2. Efectos hover en menú lateral
    function animarHoverMenuLateral() {
        const items = document.querySelectorAll('aside nav ul li a');
        items.forEach(item => {
            item.addEventListener('mouseenter', () => {
                anime({
                    targets: item,
                    backgroundColor: '#e0e7ff',
                    scale: 1.04,
                    boxShadow: '0 2px 8px 0 rgba(30,64,175,0.08)',
                    duration: 200,
                    easing: 'easeOutQuad'
                });
            });
            item.addEventListener('mouseleave', () => {
                anime({
                    targets: item,
                    backgroundColor: '#fff',
                    scale: 1,
                    boxShadow: '0 0px 0px 0 rgba(0,0,0,0)',
                    duration: 200,
                    easing: 'easeOutQuad'
                });
            });
        });
    }

    // 3. Animación del botón de salir
    function animarBotonSalir() {
        const btn = document.querySelector('button.bg-red-500');
        if (!btn) return;
        btn.addEventListener('mouseenter', () => {
            anime({
                targets: btn,
                backgroundColor: '#dc2626',
                duration: 200,
                easing: 'easeOutQuad'
            });
            const icon = btn.querySelector('i');
            if (icon) {
                anime({
                    targets: icon,
                    translateX: 6,
                    duration: 200,
                    easing: 'easeOutQuad'
                });
            }
        });
        btn.addEventListener('mouseleave', () => {
            anime({
                targets: btn,
                backgroundColor: '#ef4444',
                duration: 200,
                easing: 'easeOutQuad'
            });
            const icon = btn.querySelector('i');
            if (icon) {
                anime({
                    targets: icon,
                    translateX: 0,
                    duration: 200,
                    easing: 'easeOutQuad'
                });
            }
        });
    }

    // 4. Animación de aparición de tarjetas de resumen
    function animarTarjetasResumen() {
        const cards = document.querySelectorAll('.dashboard-card');
        anime({
            targets: cards,
            opacity: [0, 1],
            translateY: [40, 0],
            delay: anime.stagger(120),
            duration: 500,
            easing: 'easeOutCubic'
        });
    }

    // Animaciones en los paneles principales de las aplicaciones (Socios, Libros, Préstamos, Multas)
    function animarPanelesAplicaciones() {
        // Animar aparición de panel principal
        const mainPanels = document.querySelectorAll('.main-panel-anim');
        anime({
            targets: mainPanels,
            opacity: [0, 1],
            translateY: [40, 0],
            duration: 500,
            delay: anime.stagger(100),
            easing: 'easeOutCubic'
        });
        // Animar botones principales (Crear, acciones)
        const mainBtns = document.querySelectorAll('.main-btn-anim');
        mainBtns.forEach(btn => {
            btn.addEventListener('mouseenter', () => {
                anime({
                    targets: btn,
                    scale: 1.07,
                    boxShadow: '0 2px 8px 0 rgba(59,130,246,0.10)',
                    duration: 180,
                    easing: 'easeOutQuad'
                });
            });
            btn.addEventListener('mouseleave', () => {
                anime({
                    targets: btn,
                    scale: 1,
                    boxShadow: '0 0px 0px 0 rgba(0,0,0,0)',
                    duration: 180,
                    easing: 'easeOutQuad'
                });
            });
        });
    }

    // Animación de gráfica de torta en estadísticas
    function animarGraficaTortaEstadisticas() {
        const pies = document.querySelectorAll('.pie-chart');
        pies.forEach(pie => {
            const segments = pie.querySelectorAll('path');
            anime({
                targets: segments,
                strokeDashoffset: [anime.setDashoffset, 0],
                easing: 'easeOutCubic',
                duration: 900,
                delay: anime.stagger(120)
            });
            segments.forEach(seg => {
                seg.addEventListener('mouseenter', () => {
                    anime({
                        targets: seg,
                        scale: 1.06,
                        duration: 200,
                        easing: 'easeOutQuad'
                    });
                });
                seg.addEventListener('mouseleave', () => {
                    anime({
                        targets: seg,
                        scale: 1,
                        duration: 200,
                        easing: 'easeOutQuad'
                    });
                });
            });
        });
    }

    // --- INTEGRACIÓN CON DASHBOARD UPDATES ---
    // Disparar evento para actualizar dashboard tras cada alta exitosa
    function triggerDashboardUpdate() {
        if (typeof window.dispatchEvent === 'function') {
            window.dispatchEvent(new Event('dashboardUpdate'));
        }
    }

    // Agregar eventos de actualización después de insertar elementos
    document.addEventListener('DOMNodeInserted', function(e) {
        const target = e.target;
        if (target.id && (target.id.includes('socio-') || target.id.includes('libro-') || 
                         target.id.includes('prestamo-') || target.id.includes('multa-'))) {
            setTimeout(triggerDashboardUpdate, 100);
        }
    });

    // Llamar a las funciones de animación
    animarPanelLateral();
    animarPanelesAplicaciones();
    animarHoverMenuLateral();
    animarBotonSalir();
    animarTarjetasResumen();
    animarGraficaTortaEstadisticas();
});
