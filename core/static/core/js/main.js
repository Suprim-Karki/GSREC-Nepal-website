// Mobile Menu Logic
document.addEventListener('DOMContentLoaded', function () {
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navLinksContainer = document.querySelector('.nav-links-container');
    const icon = mobileMenuBtn.querySelector('i');

    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', function () {
            navLinksContainer.classList.toggle('open');
            if (navLinksContainer.classList.contains('open')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-xmark');
            } else {
                icon.classList.remove('fa-xmark');
                icon.classList.add('fa-bars');
            }
        });
    }

    // Dropdown Logic for Mobile
    const dropdownWrappers = document.querySelectorAll('.dropdown-wrapper');

    // Helper to check if we are in mobile view
    const isMobileView = () => window.innerWidth <= 1024; // Matching CSS breakpoint

    dropdownWrappers.forEach(wrapper => {
        const trigger = wrapper.querySelector('.nav-item');
        const menu = wrapper.querySelector('.dropdown-menu'); // Note: logic assumes this exists

        trigger.addEventListener('click', function (e) {
            // Only toggle on mobile (or let CSS handle hover on desktop)
            // If we are in mobile view, we want click-to-toggle
            if (isMobileView()) {
                e.preventDefault();

                // Close others
                dropdownWrappers.forEach(other => {
                    if (other !== wrapper) {
                        const otherMenu = other.querySelector('.dropdown-menu');
                        if (otherMenu) otherMenu.classList.remove('mobile-visible');
                    }
                });

                if (menu) menu.classList.toggle('mobile-visible');
            }
        });
    });
});
