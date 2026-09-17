document.addEventListener('DOMContentLoaded', () => {
    const galleryImages = document.querySelectorAll('.gallery-img');
    
    galleryImages.forEach(img => {
        img.addEventListener('click', () => {
            openLightbox(img.src, img.alt);
        });
    });
});

function openLightbox(src, alt) {
    window.open(src, '_blank');
}
