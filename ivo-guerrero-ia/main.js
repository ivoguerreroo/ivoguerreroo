(function () {
  'use strict';

  window.__BRAND__ = window.__BRAND__ || { name: 'Ivo Guerrero' };

  function safe(fn, name) {
    try { fn(); } catch (err) {
      console.warn('[init failed]', name, err);
    }
  }

  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }

  /* ---------- Splash: double safety net ---------- */
  function initSplash() {
    var splash = document.getElementById('splash');
    if (!splash) return;
    var hidden = false;
    function hide() {
      if (hidden) return;
      hidden = true;
      splash.style.opacity = '0';
      splash.style.visibility = 'hidden';
      splash.style.pointerEvents = 'none';
    }
    window.addEventListener('load', function () { setTimeout(hide, 300); });
    setTimeout(hide, 4500); // CSS animation is also 4.5s — belt and suspenders
  }

  /* ---------- Year in footer ---------- */
  function initYear() {
    var el = document.getElementById('year');
    if (!el) return;
    if (el.textContent) return; // idempotent
    el.textContent = new Date().getFullYear();
  }

  /* ---------- Mobile nav toggle ---------- */
  function initNav() {
    var toggle = document.querySelector('.nav-toggle');
    var nav = document.querySelector('.main-nav');
    if (!toggle || !nav) return;
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        nav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* ---------- Cursor glow (desktop only) ---------- */
  function initCursorGlow() {
    var glow = document.querySelector('.cursor-glow');
    if (!glow || window.matchMedia('(hover: none)').matches) return;
    window.addEventListener('mousemove', function (e) {
      glow.style.left = e.clientX + 'px';
      glow.style.top = e.clientY + 'px';
    }, { passive: true });
  }

  /* ---------- Reveal on scroll (IntersectionObserver, low threshold + safety timeout) ---------- */
  function initReveal() {
    var items = document.querySelectorAll('.reveal');
    if (!items.length) return;

    items.forEach(function (el) {
      el.style.transition = 'opacity 0.7s ease, transform 0.7s ease';
      el.style.transform = 'translateY(18px)';
      el.style.opacity = '0';
    });

    function reveal(el) {
      el.style.opacity = '1';
      el.style.transform = 'none';
    }

    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            reveal(entry.target);
            io.unobserve(entry.target);
          }
        });
      }, { threshold: 0.05, rootMargin: '0px 0px -5% 0px' });

      items.forEach(function (el) { io.observe(el); });
    } else {
      items.forEach(reveal);
    }

    // Safety net: anything still hidden after 6s gets revealed regardless.
    setTimeout(function () {
      items.forEach(function (el) {
        if (getComputedStyle(el).opacity === '0') reveal(el);
      });
    }, 6000);
  }

  /* ---------- Animated counters in "En un minuto" ---------- */
  function initCounters() {
    var nums = document.querySelectorAll('.stat-num');
    if (!nums.length) return;

    function animate(el) {
      if (el.dataset.animated === 'true') return; // idempotent
      el.dataset.animated = 'true';
      var target = parseInt(el.getAttribute('data-count'), 10) || 0;
      var start = 0;
      var duration = 900;
      var startTime = null;

      function step(ts) {
        if (!startTime) startTime = ts;
        var progress = Math.min((ts - startTime) / duration, 1);
        el.textContent = Math.round(start + (target - start) * progress);
        if (progress < 1) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    }

    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            animate(entry.target);
            io.unobserve(entry.target);
          }
        });
      }, { threshold: 0.4 });
      nums.forEach(function (el) { io.observe(el); });
    } else {
      nums.forEach(animate);
    }
  }

  /* ---------- GSAP-enhanced hero parallax (progressive enhancement) ---------- */
  function initHeroParallax() {
    if (typeof gsap === 'undefined') return; // page still works without GSAP
    var grid = document.querySelector('.hero-grid');
    if (!grid) return;
    gsap.to(grid, {
      backgroundPosition: '28px 28px',
      ease: 'none',
      scrollTrigger: {
        trigger: '.hero',
        start: 'top top',
        end: 'bottom top',
        scrub: 0.6
      }
    });
  }

  ready(function () {
    safe(initSplash, 'initSplash');
    safe(initYear, 'initYear');
    safe(initNav, 'initNav');
    safe(initCursorGlow, 'initCursorGlow');
    safe(initReveal, 'initReveal');
    safe(initCounters, 'initCounters');
    safe(initHeroParallax, 'initHeroParallax');
  });
})();
