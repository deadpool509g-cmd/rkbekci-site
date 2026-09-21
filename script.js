// Galeri önizleme: tıkla, oklarla ya da kaydırarak gez, Esc ile kapat.
(function () {
  const dialog = document.getElementById('lightbox');
  if (!dialog || typeof dialog.showModal !== 'function') return;

  const img = document.getElementById('lbImg');
  const title = document.getElementById('lbTitle');
  const caption = document.getElementById('lbCaption');
  const count = document.getElementById('lbCount');
  const items = Array.from(document.querySelectorAll('.thumb'));
  let current = 0;

  function show(i) {
    current = (i + items.length) % items.length;
    const btn = items[current];
    const src = btn.querySelector('img');
    img.src = btn.dataset.full;
    img.alt = src ? src.alt : '';
    title.textContent = btn.dataset.title || '';
    caption.textContent = btn.dataset.caption || '';
    count.textContent = (current + 1) + ' / ' + items.length;
    // Komşu görselleri önceden yükle
    [current - 1, current + 1].forEach(function (n) {
      const p = new Image();
      p.src = items[(n + items.length) % items.length].dataset.full;
    });
  }

  function open(i) {
    show(i);
    dialog.showModal();
    document.body.style.overflow = 'hidden';
  }

  items.forEach(function (btn, i) {
    btn.addEventListener('click', function () { open(i); });
  });

  dialog.querySelector('.lb-close').addEventListener('click', function () { dialog.close(); });
  dialog.querySelector('.lb-prev').addEventListener('click', function () { show(current - 1); });
  dialog.querySelector('.lb-next').addEventListener('click', function () { show(current + 1); });

  // Görselin dışına (koyu alana) tıklayınca kapat
  dialog.addEventListener('click', function (e) {
    if (e.target === dialog || e.target.classList.contains('lb-stage') || e.target.classList.contains('lb-info')) {
      dialog.close();
    }
  });

  dialog.addEventListener('close', function () { document.body.style.overflow = ''; });

  dialog.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowLeft') { e.preventDefault(); show(current - 1); }
    if (e.key === 'ArrowRight') { e.preventDefault(); show(current + 1); }
  });

  // Dokunmatik kaydırma
  let startX = null;
  dialog.addEventListener('pointerdown', function (e) { startX = e.clientX; });
  dialog.addEventListener('pointerup', function (e) {
    if (startX === null) return;
    const dx = e.clientX - startX;
    startX = null;
    if (Math.abs(dx) > 60) show(current + (dx < 0 ? 1 : -1));
  });
})();
