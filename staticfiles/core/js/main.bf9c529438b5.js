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

    // Dropdown Logic for Mobile - Toggle only on chevron click
    const dropdownWrappers = document.querySelectorAll('.dropdown-wrapper');

    // Helper to check if we are in mobile view
    const isMobileView = () => window.innerWidth <= 1024; // Matching CSS breakpoint

    dropdownWrappers.forEach(wrapper => {
        const chevron = wrapper.querySelector('.dropdown-chevron');
        const menu = wrapper.querySelector('.dropdown-menu');

        if (chevron && menu) {
            chevron.addEventListener('click', function (e) {
                // Only toggle on mobile (or let CSS handle hover on desktop)
                if (isMobileView()) {
                    e.preventDefault();
                    e.stopPropagation(); // Prevent event from bubbling

                    // Close others
                    dropdownWrappers.forEach(other => {
                        if (other !== wrapper) {
                            const otherMenu = other.querySelector('.dropdown-menu');
                            if (otherMenu) otherMenu.classList.remove('mobile-visible');
                        }
                    });

                    menu.classList.toggle('mobile-visible');
                }
            });
        }
    });
});
