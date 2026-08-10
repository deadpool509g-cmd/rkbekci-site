const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');io.unobserve(e.target)}}),{threshold:.08});document.querySelectorAll('.reveal').forEach(x=>io.observe(x));document.querySelectorAll('a[href^="#"]').forEach(a=>a.addEventListener('click',e=>{const el=document.querySelector(a.getAttribute('href'));if(el){e.preventDefault();el.scrollIntoView({behavior:'smooth'})}}));


(() => {
  const ready = () => document.body.classList.add('page-ready');
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', ready);
  else ready();

  // Scroll reveal
  const items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries, obs) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('is-visible');
          obs.unobserve(e.target);
        }
      });
    }, {threshold: .12});
    items.forEach(el => io.observe(el));
  } else items.forEach(el => el.classList.add('is-visible'));

  // Fullscreen image viewer: any local/remote image on the page
  const lb = document.getElementById('imageLightbox');
  const lbImg = document.getElementById('lightboxImage');
  const cap = document.getElementById('lightboxCaption');
  const close = () => {
    lb.classList.remove('open');
    lb.setAttribute('aria-hidden','true');
    document.body.style.overflow = '';
  };
  const open = (img) => {
    lbImg.src = img.currentSrc || img.src;
    lbImg.alt = img.alt || '';
    cap.textContent = img.alt || '';
    lb.classList.add('open');
    lb.setAttribute('aria-hidden','false');
    document.body.style.overflow = 'hidden';
  };

  document.querySelectorAll('img').forEach(img => {
    img.addEventListener('click', e => {
      if (img.closest('#imageLightbox')) return;
      e.preventDefault();
      open(img);
    });
  });
  document.querySelector('.lightbox-close').addEventListener('click', close);
  lb.addEventListener('click', e => { if (e.target === lb) close(); });
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && lb.classList.contains('open')) close();
  });

  // Smooth transition for internal links
  document.querySelectorAll('a[href]').forEach(a => {
    const href = a.getAttribute('href');
    if (!href || href.startsWith('#') || a.target === '_blank' ||
        href.startsWith('mailto:') || href.startsWith('tel:')) return;
    try {
      const url = new URL(href, location.href);
      if (url.origin !== location.origin) return;
      a.addEventListener('click', e => {
        e.preventDefault();
        document.body.classList.add('page-leaving');
        setTimeout(() => location.href = url.href, 280);
      });
    } catch {}
  });
})();
