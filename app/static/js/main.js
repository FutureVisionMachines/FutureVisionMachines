// FutureVisionMachines - Revolutionary Interactive Experience
// The New Industry Standard

document.addEventListener('DOMContentLoaded', function() {
    
    // Check if we're in admin portal - if so, skip custom cursor and galaxy background
    const isAdminPortal = document.body.classList.contains('admin-body');
    
    if (!isAdminPortal) {
        // ========================================
        // GALAXY BACKGROUND SYSTEM
        // Parallax star field with depth
        // ========================================
        
        // Create galaxy background structure
        const galaxyBg = document.createElement('div');
        galaxyBg.className = 'galaxy-background';
    
    // Add nebula layers
    const nebula1 = document.createElement('div');
    nebula1.className = 'nebula-layer nebula-1';
    const nebula2 = document.createElement('div');
    nebula2.className = 'nebula-layer nebula-2';
    
    // Add star layers
    const starsFar = document.createElement('div');
    starsFar.className = 'stars-layer stars-far';
    const starsMid = document.createElement('div');
    starsMid.className = 'stars-layer stars-mid';
    const starsNear = document.createElement('div');
    starsNear.className = 'stars-layer stars-near';
    
    // Add shooting stars
    for (let i = 0; i < 4; i++) {
        const shootingStar = document.createElement('div');
        shootingStar.className = 'shooting-star';
        galaxyBg.appendChild(shootingStar);
    }
    
    // Assemble galaxy
    galaxyBg.appendChild(nebula1);
    galaxyBg.appendChild(nebula2);
    galaxyBg.appendChild(starsFar);
    galaxyBg.appendChild(starsMid);
    galaxyBg.appendChild(starsNear);
    
    // Insert at beginning of body
    document.body.insertBefore(galaxyBg, document.body.firstChild);
    
    // Parallax effect on scroll
    function updateGalaxyParallax() {
        const scrollY = window.scrollY;
        
        // Different layers move at different speeds for depth
        // Far stars move slowest, near stars move fastest
        starsFar.style.transform = `translateY(${scrollY * 0.1}px)`;
        starsMid.style.transform = `translateY(${scrollY * 0.2}px)`;
        starsNear.style.transform = `translateY(${scrollY * 0.35}px)`;
        nebula1.style.transform = `translateY(${scrollY * 0.15}px) scale(1.1)`;
        nebula2.style.transform = `translateY(${scrollY * 0.08}px) scale(1.1)`;
    }
    
    // Mouse parallax for subtle depth
    function handleMouseParallax(e) {
        const centerX = window.innerWidth / 2;
        const centerY = window.innerHeight / 2;
        const moveX = (e.clientX - centerX) / centerX;
        const moveY = (e.clientY - centerY) / centerY;
        
        // Very subtle mouse-based parallax on nebulae
        requestAnimationFrame(() => {
            const currentTransform1 = nebula1.style.transform || '';
            const currentTransform2 = nebula2.style.transform || '';
            
            if (!currentTransform1.includes('translateY')) {
                nebula1.style.transform = `translate(${moveX * 20}px, ${moveY * 20}px)`;
            }
            if (!currentTransform2.includes('translateY')) {
                nebula2.style.transform = `translate(${moveX * 10}px, ${moveY * 10}px)`;
            }
        });
    }
    
    // Debounced parallax updates
    let scrollTicking = false;
    window.addEventListener('scroll', () => {
        if (!scrollTicking) {
            requestAnimationFrame(() => {
                updateGalaxyParallax();
                scrollTicking = false;
            });
            scrollTicking = true;
        }
    });
    
    // Mouse parallax (throttled)
    let mouseThrottle = false;
    window.addEventListener('mousemove', (e) => {
        if (!mouseThrottle) {
            handleMouseParallax(e);
            mouseThrottle = true;
            setTimeout(() => mouseThrottle = false, 50);
        }
    });
    
        // ========================================
        // CUSTOM CURSOR SYSTEM - OPTIMIZED
        // ========================================
        const cursor = document.createElement('div');
        const cursorFollower = document.createElement('div');
        cursor.classList.add('custom-cursor');
        cursorFollower.classList.add('custom-cursor-follower');
        document.body.appendChild(cursor);
        document.body.appendChild(cursorFollower);
    let followerX = 0, followerY = 0;
    
    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
        
        // Main cursor follows instantly for responsive feel
        cursor.style.left = mouseX + 'px';
        cursor.style.top = mouseY + 'px';
    });
    
    // Smooth follower animation with reduced lag
    function animateCursorFollower() {
        // Faster interpolation for smoother, more responsive feel
        followerX += (mouseX - followerX) * 0.25;
        followerY += (mouseY - followerY) * 0.25;
        
        cursorFollower.style.left = followerX + 'px';
        cursorFollower.style.top = followerY + 'px';
        
        requestAnimationFrame(animateCursorFollower);
    }
    animateCursorFollower();
    
    // Cursor interactions
    const interactiveElements = document.querySelectorAll('a, button, .btn-primary, .btn-secondary, .feature-card, .glass-panel');
    interactiveElements.forEach(el => {
        el.addEventListener('mouseenter', () => {
            cursor.style.transform = 'translate(-50%, -50%) scale(1.5)';
            cursor.style.borderColor = 'var(--color-secondary)';
            cursorFollower.style.transform = 'translate(-50%, -50%) scale(2)';
        });
        el.addEventListener('mouseleave', () => {
            cursor.style.transform = 'translate(-50%, -50%) scale(1)';
            cursor.style.borderColor = 'var(--color-primary)';
            cursorFollower.style.transform = 'translate(-50%, -50%) scale(1)';
        });
    });
    
    } // End of !isAdminPortal check
    
    // ========================================
    // SCROLL PROGRESS BAR (works on all pages)
    // ========================================
    const scrollProgress = document.createElement('div');
    scrollProgress.classList.add('scroll-progress');
    document.body.appendChild(scrollProgress);
    
    window.addEventListener('scroll', () => {
        const windowHeight = document.documentElement.scrollHeight - window.innerHeight;
        const scrolled = (window.scrollY / windowHeight) * 100;
        scrollProgress.style.width = scrolled + '%';
    });
    
    // ========================================
    // NAVIGATION SCROLL EFFECT
    // ========================================
    const navbar = document.querySelector('.navbar');
    let lastScroll = 0;
    
    window.addEventListener('scroll', () => {
        const currentScroll = window.scrollY;
        
        if (currentScroll > 100) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        lastScroll = currentScroll;
    });
    
    // ========================================
    // SCROLL-TRIGGERED ANIMATIONS
    // ========================================
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observe elements
    const animatedElements = document.querySelectorAll('.feature-card, .service-card, .glass-panel, .blog-card, .saas-card');
    animatedElements.forEach((el, index) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(40px)';
        el.style.transition = `all 0.8s cubic-bezier(0.4, 0, 0.2, 1) ${index * 0.1}s`;
        observer.observe(el);
    });
    
    // ========================================
    // MAGNETIC BUTTON EFFECT
    // ========================================
    const buttons = document.querySelectorAll('.btn-primary, .btn-secondary, .btn-primary-outline, .btn-secondary-outline');
    
    buttons.forEach(button => {
        button.addEventListener('mousemove', (e) => {
            const rect = button.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;
            
            button.style.transform = `translate(${x * 0.3}px, ${y * 0.3}px) scale(1.05)`;
        });
        
        button.addEventListener('mouseleave', () => {
            button.style.transform = 'translate(0, 0) scale(1)';
        });
    });
    
    // ========================================
    // 3D TILT EFFECT ON CARDS
    // ========================================
    const cards = document.querySelectorAll('.feature-card, .floating-card');
    
    cards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            
            const rotateX = (y - centerY) / 10;
            const rotateY = (centerX - x) / 10;
            
            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-10px)`;
        });
        
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateY(0)';
        });
    });
    
    // ========================================
    // ENHANCED PARTICLE SYSTEM FOR HERO (Public site only)
    // Floating energy particles with depth
    // ========================================
    if (!isAdminPortal) {
        const hero = document.querySelector('.hero');
    if (hero) {
        const particleCount = 80;
        const particles = document.createElement('div');
        particles.className = 'hero-particles';
        particles.style.position = 'absolute';
        particles.style.top = '0';
        particles.style.left = '0';
        particles.style.width = '100%';
        particles.style.height = '100%';
        particles.style.overflow = 'hidden';
        particles.style.pointerEvents = 'none';
        particles.style.zIndex = '1';
        hero.appendChild(particles);
        
        for (let i = 0; i < particleCount; i++) {
            const particle = document.createElement('div');
            const size = Math.random() * 6 + 2;
            const isCyan = Math.random() > 0.5;
            const depth = Math.random();
            
            particle.style.position = 'absolute';
            particle.style.width = size + 'px';
            particle.style.height = size + 'px';
            particle.style.background = isCyan ? 'rgba(0, 229, 255, 0.6)' : 'rgba(123, 97, 255, 0.6)';
            particle.style.borderRadius = '50%';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.top = Math.random() * 100 + '%';
            particle.style.opacity = Math.random() * 0.4 + 0.2;
            particle.style.boxShadow = '0 0 ' + (size * 3) + 'px ' + (isCyan ? 'rgba(0, 229, 255, 0.8)' : 'rgba(123, 97, 255, 0.8)');
            particle.style.animation = 'floatParticle ' + (Math.random() * 15 + 10) + 's linear infinite';
            particle.style.animationDelay = Math.random() * 8 + 's';
            particle.dataset.depth = depth;
            particles.appendChild(particle);
        }
        
        // Mouse-based parallax on hero particles
        hero.addEventListener('mousemove', (e) => {
            const rect = hero.getBoundingClientRect();
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const mouseX = e.clientX - rect.left;
            const mouseY = e.clientY - rect.top;
            const moveX = (mouseX - centerX) / centerX;
            const moveY = (mouseY - centerY) / centerY;
            
            particles.querySelectorAll('div').forEach((particle) => {
                const depth = parseFloat(particle.dataset.depth);
                const x = moveX * depth * 30;
                const y = moveY * depth * 30;
                particle.style.transform = 'translate(' + x + 'px, ' + y + 'px)';
            });
        });
        
        // Add particle animation keyframes
        const style = document.createElement('style');
        style.textContent = '@keyframes floatParticle { 0% { transform: translateY(0) translateX(0); opacity: 0; } 10% { opacity: 0.6; } 50% { opacity: 0.8; } 90% { opacity: 0.3; } 100% { transform: translateY(-120vh) translateX(' + (Math.random() * 100 - 50) + 'px); opacity: 0; } } @keyframes slideInRight { from { transform: translateX(100%); opacity: 0; } to { transform: translateX(0); opacity: 1; } } @keyframes slideOutRight { to { transform: translateX(100%); opacity: 0; } }';
        document.head.appendChild(style);
        }
    } // End of particle system (public site only)
    
    // ========================================
    // FLASH MESSAGES WITH ANIMATION
    // ========================================
    const flashMessages = document.querySelectorAll('.flash');
    flashMessages.forEach(flash => {
        flash.style.animation = 'slideInRight 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55)';
        
        const closeBtn = flash.querySelector('.flash-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                flash.style.animation = 'slideOutRight 0.3s ease';
                setTimeout(() => flash.remove(), 300);
            });
        }
        
        // Auto-dismiss after 5 seconds
        setTimeout(() => {
            if (flash.parentElement) {
                flash.style.animation = 'slideOutRight 0.3s ease';
                setTimeout(() => flash.remove(), 300);
            }
        }, 5000);
    });
    
    // ========================================
    // SMOOTH SCROLL FOR ANCHOR LINKS
    // ========================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href !== '#' && document.querySelector(href)) {
                e.preventDefault();
                const target = document.querySelector(href);
                const offset = 80; // navbar height
                const targetPosition = target.offsetTop - offset;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // ========================================
    // PARALLAX EFFECT
    // ========================================
    window.addEventListener('scroll', () => {
        const scrolled = window.scrollY;
        const parallaxElements = document.querySelectorAll('.floating-card, .hero-visual');
        
        parallaxElements.forEach(el => {
            const speed = 0.5;
            el.style.transform = `translateY(${scrolled * speed}px)`;
        });
    });
    
    // ========================================
    // GLITCH EFFECT ON LOGO
    // ========================================
    const logo = document.querySelector('.logo-text');
    if (logo) {
        setInterval(() => {
            if (Math.random() > 0.95) {
                logo.style.animation = 'glitch 0.2s ease-in-out';
                setTimeout(() => {
                    logo.style.animation = 'none';
                }, 200);
            }
        }, 3000);
    }
    
    // Add glitch animation
    const glitchStyle = document.createElement('style');
    glitchStyle.textContent = `
        @keyframes glitch {
            0%, 100% { transform: translate(0); }
            20% { transform: translate(-2px, 2px); }
            40% { transform: translate(-2px, -2px); }
            60% { transform: translate(2px, 2px); }
            80% { transform: translate(2px, -2px); }
        }
        @keyframes slideInRight {
            from {
                transform: translateX(100%);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }
        @keyframes slideOutRight {
            from {
                transform: translateX(0);
                opacity: 1;
            }
            to {
                transform: translateX(100%);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(glitchStyle);
    
    // ========================================
    // MOBILE MENU TOGGLE
    // ========================================
    const mobileToggle = document.getElementById('mobileToggle');
    const navMenu = document.getElementById('navMenu');
    
    if (mobileToggle && navMenu) {
        mobileToggle.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            mobileToggle.classList.toggle('active');
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (!navMenu.contains(e.target) && !mobileToggle.contains(e.target)) {
                navMenu.classList.remove('active');
                mobileToggle.classList.remove('active');
            }
        });
    }
    
    // ========================================
    // FORM ENHANCEMENT
    // ========================================
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        const inputs = form.querySelectorAll('input, textarea, select');
        
        inputs.forEach(input => {
            // Floating label effect
            input.addEventListener('focus', () => {
                input.parentElement.classList.add('focused');
            });
            
            input.addEventListener('blur', () => {
                if (!input.value) {
                    input.parentElement.classList.remove('focused');
                }
            });
        });
    });
    
    console.log('%c🚀 FutureVisionMachines', 'font-size: 20px; color: #00E5FF; font-weight: bold;');
    console.log('%cThe New Industry Standard', 'font-size: 14px; color: #7B61FF;');
});

