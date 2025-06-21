document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.getElementById('theme-toggle');
    const htmlElement = document.documentElement; // The <html> tag
    const scrollToTopBtn = document.getElementById('scrollToTopBtn');

    // Load saved theme from localStorage
    const savedTheme = localStorage.getItem('theme') || 'dark'; // Default to dark
    htmlElement.setAttribute('data-theme', savedTheme);
    updateNavbarTheme(savedTheme); // Update navbar on load

    // Function to update navbar theme
    function updateNavbarTheme(theme) {
        const navbar = document.querySelector('.navbar');
        const footer = document.querySelector('footer');

        if (navbar) {
            if (theme === 'dark') {
                navbar.classList.remove('navbar-light', 'bg-light');
                navbar.classList.add('navbar-dark', 'bg-dark');
            } else {
                navbar.classList.remove('navbar-dark', 'bg-dark');
                navbar.classList.add('navbar-light', 'bg-light');
            }
        }
        if (footer) {
            if (theme === 'dark') {
                footer.classList.remove('bg-light', 'text-dark');
                footer.classList.add('bg-dark', 'text-white');
            } else {
                footer.classList.remove('bg-dark', 'text-white');
                footer.classList.add('bg-light', 'text-dark');
            }
        }
    }

    // Toggle theme on button click
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            let currentTheme = htmlElement.getAttribute('data-theme');
            let newTheme = (currentTheme === 'dark') ? 'light' : 'dark';
            htmlElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateNavbarTheme(newTheme);
        });
    }

    // Scroll to Top functionality
    window.onscroll = function() { scrollFunction() };

    function scrollFunction() {
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            scrollToTopBtn.style.display = "block";
        } else {
            scrollToTopBtn.style.display = "none";
        }
    }

    if (scrollToTopBtn) {
        scrollToTopBtn.addEventListener('click', function() {
            document.body.scrollTop = 0; // For Safari
            document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
        });
    }

    // Lazy Loading for images and videos (basic example)
    const lazyLoadElements = document.querySelectorAll('img[data-src], video[data-src]');

    const lazyLoad = function(entries, observer) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const element = entry.target;
                if (element.tagName === 'IMG' && element.dataset.src) {
                    element.src = element.dataset.src;
                    element.classList.add('lazyloaded');
                } else if (element.tagName === 'VIDEO' && element.dataset.src) {
                    element.src = element.dataset.src;
                    element.load(); // Load the video
                    element.classList.add('lazyloaded');
                }
                observer.unobserve(element);
            }
        });
    };

    const observer = new IntersectionObserver(lazyLoad, {
        rootMargin: '0px 0px 50px 0px' // Load when 50px from viewport
    });

    lazyLoadElements.forEach(element => observer.observe(element));

});