/* AMS Crafters Concept Redesign | main.js
   Vanilla JS. No libraries, no CDNs. */
(function () {
  'use strict';

  /* Mobile nav + dropdowns on touch */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.textContent = open ? '✕' : '☰';
    });
    nav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        if (window.innerWidth <= 640 && !link.parentElement.classList.contains('has-dropdown')) {
          nav.classList.remove('open');
          toggle.setAttribute('aria-expanded', 'false');
          toggle.textContent = '☰';
        }
      });
    });
  }
  document.querySelectorAll('.has-dropdown > a').forEach(function (link) {
    link.addEventListener('click', function (e) {
      if (window.innerWidth <= 640) {
        e.preventDefault();
        link.parentElement.classList.toggle('open');
      }
    });
  });

  /* Scroll reveal */
  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    revealEls.forEach(function (el) { revealObserver.observe(el); });
    /* Above-the-fold content must be visible at once, not after a transition delay */
    revealEls.forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.top < window.innerHeight && r.bottom > 0) el.classList.add('visible');
    });
  } else {
    revealEls.forEach(function (el) { el.classList.add('visible'); });
  }

  /* Animated counters: start at 0, count up when scrolled into view */
  function animateCounter(el) {
    var target = parseInt(el.getAttribute('data-target'), 10);
    var suffix = el.getAttribute('data-suffix') || '';
    var duration = 1600;
    var start = null;
    function step(timestamp) {
      if (!start) start = timestamp;
      var progress = Math.min((timestamp - start) / duration, 1);
      var eased = 1 - Math.pow(1 - progress, 3);
      el.innerHTML = Math.round(target * eased) + '<span class="suffix">' + suffix + '</span>';
      if (progress < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  var counters = document.querySelectorAll('[data-target]');
  if ('IntersectionObserver' in window) {
    var counterObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          counterObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.25 });
    counters.forEach(function (el) { counterObserver.observe(el); });
  } else {
    counters.forEach(function (el) {
      el.innerHTML = el.getAttribute('data-target') + '<span class="suffix">' + (el.getAttribute('data-suffix') || '') + '</span>';
    });
  }

  /* Statue image fallback: if a supplied PNG is missing, show a gradient placeholder.
     The <img> reference is always kept in the HTML; the gradient glow behind it
     (statue-wrap::before) shows while it loads, and a failed file is swapped for
     a gradient placeholder block of the same size. */
  document.querySelectorAll('img[data-statue]').forEach(function (img) {
    function swapForPlaceholder() {
      if (!img.isConnected) return;
      var tint = img.getAttribute('data-statue') || '';
      var holder = document.createElement('div');
      holder.className = 'statue-placeholder' + (tint ? ' tint-' + tint : '');
      holder.textContent = 'Greek statue artwork';
      img.replaceWith(holder);
    }
    img.addEventListener('error', swapForPlaceholder);
    if (img.complete && img.naturalWidth === 0) swapForPlaceholder();
  });

  /* Testimonial slider */
  var slider = document.querySelector('.slider');
  if (slider) {
    var slides = Array.prototype.slice.call(slider.querySelectorAll('.slide'));
    var dotsWrap = slider.querySelector('.slider-dots');
    var current = 0;
    var timer = null;
    var pausedUntil = 0;
    slides.forEach(function (_, i) {
      var dot = document.createElement('button');
      dot.type = 'button';
      dot.setAttribute('aria-label', 'Show testimonial ' + (i + 1));
      if (i === 0) dot.classList.add('active');
      dot.addEventListener('click', function () { pausedUntil = Date.now() + 8000; goTo(i); restart(); });
      dotsWrap.appendChild(dot);
    });
    var dots = Array.prototype.slice.call(dotsWrap.querySelectorAll('button'));
    function goTo(i) {
      slides[current].classList.remove('active');
      dots[current].classList.remove('active');
      current = (i + slides.length) % slides.length;
      slides[current].classList.add('active');
      dots[current].classList.add('active');
    }
    function restart() {
      if (timer) clearInterval(timer);
      timer = setInterval(function () {
        if (Date.now() < pausedUntil) return;
        goTo(current + 1);
      }, 6000);
    }
    var prev = slider.querySelector('.slider-prev');
    var next = slider.querySelector('.slider-next');
    if (prev) prev.addEventListener('click', function () { pausedUntil = Date.now() + 8000; goTo(current - 1); restart(); });
    if (next) next.addEventListener('click', function () { pausedUntil = Date.now() + 8000; goTo(current + 1); restart(); });
    slider.addEventListener('mouseenter', function () { if (timer) clearInterval(timer); });
    slider.addEventListener('mouseleave', restart);
    restart();
  }

  /* Package tabs */
  var tabs = document.querySelectorAll('.tab-btn');
  var panels = document.querySelectorAll('.tab-panel');
  tabs.forEach(function (btn) {
    btn.addEventListener('click', function () {
      tabs.forEach(function (b) { b.classList.remove('active'); b.setAttribute('aria-selected', 'false'); });
      panels.forEach(function (p) { p.classList.remove('active'); });
      btn.classList.add('active');
      btn.setAttribute('aria-selected', 'true');
      var panel = document.getElementById('tab-' + btn.getAttribute('data-tab'));
      if (panel) panel.classList.add('active');
    });
  });

  /* Portfolio filters */
  var filterBtns = document.querySelectorAll('.filter-btn');
  var projectCards = document.querySelectorAll('.project-card');
  filterBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      filterBtns.forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
      var filter = btn.getAttribute('data-filter');
      projectCards.forEach(function (card) {
        var show = filter === 'all' || card.getAttribute('data-category') === filter;
        card.style.display = show ? '' : 'none';
      });
    });
  });

  /* FAQ accordion */
  document.querySelectorAll('.faq-q').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var item = btn.closest('.faq-item');
      var wasOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item.open').forEach(function (i) { i.classList.remove('open'); });
      if (!wasOpen) item.classList.add('open');
    });
  });

  /* Forms: client-side validation + success message (front-end demo, no backend) */
  document.querySelectorAll('form[data-demo-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var valid = true;
      form.querySelectorAll('[required]').forEach(function (field) {
        var wrap = field.closest('.field');
        var value = (field.value || '').trim();
        var bad = !value;
        if (!bad && field.type === 'email') {
          bad = !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
        }
        if (wrap) wrap.classList.toggle('invalid', bad);
        if (bad) valid = false;
      });
      var success = form.parentElement.querySelector('.form-success');
      if (valid) {
        if (success) success.classList.add('show');
        form.reset();
        if (success) success.scrollIntoView({ behavior: 'smooth', block: 'center' });
      } else {
        if (success) success.classList.remove('show');
        var firstBad = form.querySelector('.field.invalid input, .field.invalid select, .field.invalid textarea');
        if (firstBad) firstBad.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    });
  });
})();
