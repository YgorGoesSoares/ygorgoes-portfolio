// Scroll reveal animations
document.addEventListener('DOMContentLoaded', function () {
  const revealElements = document.querySelectorAll('.reveal');

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

  revealElements.forEach(el => revealObserver.observe(el));

  // Terminal typing effect on hero
  const typingEl = document.getElementById('typing-text');
  if (typingEl) {
    const phrases = ['whoami', 'dev', 'telecom', 'network', 'fullstack'];
    let phraseIndex = 0;
    let charIndex = 0;
    let isDeleting = false;

    function typeEffect() {
      const currentPhrase = phrases[phraseIndex];
      if (!isDeleting) {
        typingEl.textContent = currentPhrase.substring(0, charIndex + 1);
        charIndex++;
        if (charIndex === currentPhrase.length) {
          isDeleting = true;
          setTimeout(typeEffect, 2000);
          return;
        }
      } else {
        typingEl.textContent = currentPhrase.substring(0, charIndex - 1);
        charIndex--;
        if (charIndex === 0) {
          isDeleting = false;
          phraseIndex = (phraseIndex + 1) % phrases.length;
        }
      }
      setTimeout(typeEffect, isDeleting ? 60 : 100);
    }
    setTimeout(typeEffect, 500);
  }

  // Close flipped cards when clicking outside
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.flip-card')) {
      document.querySelectorAll('.flip-card.flipped').forEach(card => {
        card.classList.remove('flipped');
      });
    }
  });

  // Cursor glow effect
  const glow = document.getElementById('cursor-glow');
  if (glow) {
    let glowTimeout;
    document.addEventListener('mousemove', function (e) {
      glow.style.opacity = '1';
      glow.style.left = e.clientX + 'px';
      glow.style.top = e.clientY + 'px';
      clearTimeout(glowTimeout);
      glowTimeout = setTimeout(() => { glow.style.opacity = '0'; }, 2000);
    });
    document.addEventListener('mouseleave', function () {
      glow.style.opacity = '0';
    });
    // Force initial display check
    console.log('cursor-glow initialized');
  }
});
