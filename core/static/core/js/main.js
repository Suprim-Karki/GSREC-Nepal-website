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
    if (window.innerWidth <= 1100) {
        dropdownWrappers.forEach(wrapper => {
            const trigger = wrapper.querySelector('.nav-item');
            const menu = wrapper.querySelector('.dropdown-menu');

            trigger.addEventListener('click', function (e) {
                e.preventDefault();
                // Close others
                dropdownWrappers.forEach(other => {
                    if (other !== wrapper) {
                        other.querySelector('.dropdown-menu').classList.remove('mobile-visible');
                    }
                });

                menu.classList.toggle('mobile-visible');
            });
        });
    }
});
