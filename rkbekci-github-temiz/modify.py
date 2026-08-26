from pathlib import Path
from PIL import Image
import re, json, shutil
root=Path('/tmp/rk')
idx=root/'index.html'
html=idx.read_text(encoding='utf-8')

# Head: stronger metadata, social cards, robots, theme, preload hero.
old='<meta name="description" content="RKBEKCI arşivi — haberler, görseller ve yayıncılık hikâyeleri."><title>RKBEKCI — Arşiv</title><link rel="preconnect" href="https://fonts.googleapis.com">'
new='''<meta name="description" content="RKBEKCI dijital arşivi: Gorilla draması, Şahinler Market, yayıncılık notları ve 2026 fotoğraf arşivi.">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<meta name="theme-color" content="#0a0a0b">
<meta property="og:type" content="website">
<meta property="og:title" content="RKBEKCI — Dijital Arşiv">
<meta property="og:description" content="RKBEKCI hakkında kronik, arşiv görselleri ve 2026 medya kayıtları.">
<meta property="og:image" content="media/2026/04/dil.png">
<meta property="og:image:alt" content="RKBEKCI arşiv fotoğrafı">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="RKBEKCI — Dijital Arşiv">
<meta name="twitter:description" content="RKBEKCI hakkında kronik, arşiv görselleri ve 2026 medya kayıtları.">
<meta name="twitter:image" content="media/2026/04/dil.png">
<title>RKBEKCI — Dijital Arşiv | Fotoğraflar ve Kronik</title>
<link rel="preload" as="image" href="media/2026/04/dil.png" fetchpriority="high">
<link rel="preconnect" href="https://fonts.googleapis.com">'''
html=html.replace(old,new)

# Header navigation + top CTA.
old='<nav class="wrap"><a class="brand" href="#top">RK<span>BEKCI</span></a><div class="links"><a href="#hikaye">Hikâye</a><a href="#galeri">Galeri</a></div></nav>'
new='''<nav class="wrap"><a class="brand" href="#top">RK<span>BEKCI</span></a><div class="links"><a href="#hikaye">Hikâye</a><a href="#vakalar">Vakalar</a><a href="#sss">SSS</a><a href="#galeri">Galeri</a><a class="nav-cta" href="404.html">Arşiv sayfaları</a></div></nav>'''
html=html.replace(old,new)

# Hero image replacement and CTA/internal links.
html=html.replace('src="media/2026/08/rkbekci-giris-yeni.jpg" alt="RKBEKCI arşiv giriş görseli" loading="eager" fetchpriority="high"', 'src="media/2026/04/dil.png" alt="RKBEKCI arşiv giriş fotoğrafı" width="602" height="461" loading="eager" fetchpriority="high" decoding="async"')
html=html.replace('<a class="btn" href="#galeri">Görsellere bak</a>', '<a class="btn" href="#galeri">Görsellere bak</a><a class="btn" href="#vakalar">Vaka çalışmalarına git</a>')

# Breadcrumb before story.
marker='<section id="hikaye"><div class="wrap">'
replacement='<section id="hikaye"><div class="wrap"><nav class="breadcrumbs" aria-label="Sayfa işaret yolu"><a href="#top">Ana sayfa</a><span>›</span><a href="#hikaye">Hikâye</a><span>›</span><span>Bekçi Kronikleri</span></nav>'
html=html.replace(marker,replacement)

# Insert case studies, FAQ, media/social sections before gallery.
gallery_marker='<section id="galeri"><div class="wrap">'
insert='''<section id="vakalar"><div class="wrap"><div class="section-head"><div><div class="eyebrow">Dosyalar</div><h2>Vaka Çalışmaları</h2></div><p>Sitedeki mevcut hikâye ve medya kayıtlarından türetilen kısa vaka özetleri.</p></div><div class="case-grid"><article class="case-card"><span class="tag">VAKA 01</span><h3>Gorilla draması</h3><p>Gorilla enerji içeceğinin 35 TL'lik toptan teklifinden başlayan süreç, ürün, yayın ve topluluk etrafında büyüyen ana arşiv başlıklarından biri.</p><a class="text-link" href="#galeri">İlgili karelere bak →</a></article><article class="case-card"><span class="tag">VAKA 02</span><h3>Market ve Coca-Cola</h3><p>Şahinler Market, Coca-Cola fiyatı ve tente/yatırım konusu; sitenin ticari taraftaki kroniğini oluşturan kayıtlar arasında yer alıyor.</p><a class="text-link" href="#hikaye">Kroniği oku →</a></article><article class="case-card"><span class="tag">VAKA 03</span><h3>Kamera olayı</h3><p>Chat tartışmaları sonrasında kameranın zarar gördüğü an, arşivde ayrı bir medya başlığı olarak tutuluyor.</p><a class="text-link" href="#galeri">Medya kaydını aç →</a></article></div></div></section>

<section id="sss"><div class="wrap"><div class="section-head"><div><div class="eyebrow">Yardım</div><h2>5 ADET SSS</h2></div><p>Mevcut site içeriğine dayanarak cevaplanabilen temel sorular.</p></div><div class="faq-grid"><details><summary>RKBEKCI arşivi ne hakkında?</summary><p>2026 tarihli fotoğraflar, yayıncılık notları ve sitede anlatılan olayların kroniğini topluyor.</p></details><details><summary>Gorilla draması nasıl başladı?</summary><p>Sitedeki kroniğe göre, Gorilla enerji içeceğinin toplu olarak 35 TL'den teklif edilmesi olayların başlangıç noktası olarak anlatılıyor.</p></details><details><summary>Şahinler Market neden hikâyede geçiyor?</summary><p>Arşiv metninde RKBEKCI'nin Şahinler Market'i de yönettiği ve marketle ilgili ticari olayların kroniğe dahil edildiği belirtiliyor.</p></details><details><summary>Fotoğrafları büyütebilir miyim?</summary><p>Evet. Galerideki görsellere tıklayarak tam ekran ışık kutusunu açabilir, Escape ile kapatabilirsin.</p></details><details><summary>Arşivde kaç medya kaydı var?</summary><p>Ana sayfadaki sayaç ve galeri yapısına göre 24 medya kaydı bulunuyor.</p></details></div></div></section>

<section id="paylas"><div class="wrap share-panel"><div><div class="eyebrow">Paylaş</div><h2>Arşivi paylaş</h2><p>Bu sayfanın sosyal paylaşım kartları için mevcut arşiv fotoğrafı tanımlandı.</p></div><button class="btn primary" id="shareBtn" type="button">Sayfayı paylaş</button></div></section>

'''
html=html.replace(gallery_marker,insert+gallery_marker)

# Add alt text/decoding/async and dimensions from actual files.
def repl_img(m):
    tag=m.group(0)
    srcm=re.search(r'src="([^"]+)"',tag)
    if not srcm: return tag
    src=srcm.group(1)
    if src.startswith('http'): return tag
    p=root/src
    try:
        w,h=Image.open(p).size
        if ' width=' not in tag: tag=tag.replace('>',f' width="{w}" height="{h}" decoding="async">')
        elif 'decoding=' not in tag: tag=tag.replace('>', ' decoding="async">')
    except Exception: pass
    tag=tag.replace('loading="eager" src="rkbekci-testo-xxl.jpg"','loading="lazy" src="rkbekci-testo-xxl.jpg"')
    return tag
html=re.sub(r'<img\b[^>]*>', repl_img, html)

# Add footer links and legal-ish utility links.
html=html.replace('<span>RKBEKCI ARŞİVİ &middot; DOSYA KAPANMADI</span><span class="rec"><i></i>KAYIT SÜRÜYOR</span>', '<span>RKBEKCI ARŞİVİ &middot; DOSYA KAPANMADI</span><span><a href="404.html">404</a> &middot; <a href="tesekkur.html">Teşekkür</a></span><span class="rec"><i></i>KAYIT SÜRÜYOR</span>')

# Structured data: WebSite + ImageObject + FAQPage + BreadcrumbList.
schema={
  "@context":"https://schema.org",
  "@graph":[
    {"@type":"WebSite","name":"RKBEKCI — Dijital Arşiv","description":"RKBEKCI hakkında kronik, fotoğraf ve medya arşivi.","inLanguage":"tr-TR"},
    {"@type":"ImageObject","name":"RKBEKCI arşiv giriş fotoğrafı","contentUrl":"media/2026/04/dil.png","description":"RKBEKCI arşiv giriş görseli."},
    {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Ana sayfa","item":"#top"},{"@type":"ListItem","position":2,"name":"Hikâye","item":"#hikaye"}]},
    {"@type":"FAQPage","mainEntity":[
      {"@type":"Question","name":"RKBEKCI arşivi ne hakkında?","acceptedAnswer":{"@type":"Answer","text":"2026 tarihli fotoğraflar, yayıncılık notları ve sitede anlatılan olayların kroniğini topluyor."}},
      {"@type":"Question","name":"Gorilla draması nasıl başladı?","acceptedAnswer":{"@type":"Answer","text":"Sitedeki kroniğe göre, Gorilla enerji içeceğinin toplu olarak 35 TL'den teklif edilmesi olayların başlangıç noktası olarak anlatılıyor."}},
      {"@type":"Question","name":"Şahinler Market neden hikâyede geçiyor?","acceptedAnswer":{"@type":"Answer","text":"Arşiv metninde RKBEKCI'nin Şahinler Market'i de yönettiği ve marketle ilgili ticari olayların kroniğe dahil edildiği belirtiliyor."}},
      {"@type":"Question","name":"Fotoğrafları büyütebilir miyim?","acceptedAnswer":{"@type":"Answer","text":"Evet. Galerideki görsellere tıklayarak tam ekran ışık kutusunu açabilirsin."}},
      {"@type":"Question","name":"Arşivde kaç medya kaydı var?","acceptedAnswer":{"@type":"Answer","text":"Ana sayfadaki sayaç ve galeri yapısına göre 24 medya kaydı bulunuyor."}}
    ]}
  ]
}
jsonld='<script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False,separators=(',',':'))+'</script>'
html=html.replace('</head>',jsonld+'</head>')

idx.write_text(html,encoding='utf-8')

# Append CSS additions.
css=root/'style.css'
cs=css.read_text(encoding='utf-8')
add=r'''
/* ---------- SEO / conversion additions ---------- */
.nav-cta{border:1px solid var(--line-strong);padding:7px 10px!important;color:var(--ink)!important}
.nav-cta:hover{border-color:var(--red)}
.breadcrumbs{display:flex;gap:9px;align-items:center;color:var(--muted);font-family:var(--mono);font-size:.68rem;letter-spacing:.04em;margin-bottom:20px}
.breadcrumbs a:hover{color:var(--ink)}
.case-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.case-card{padding:28px 26px;border:1px solid var(--line);background:var(--panel);transition:.25s transform ease,.25s border-color ease}
.case-card:hover{transform:translateY(-4px);border-color:var(--line-strong)}
.case-card h3{font-family:var(--display);font-size:2rem;font-weight:400;text-transform:uppercase;margin:0 0 10px}
.case-card p{color:var(--muted);font-size:.93rem;margin:0 0 18px}
.text-link{font-family:var(--mono);font-size:.72rem;text-transform:uppercase;color:var(--amber);letter-spacing:.06em}
.faq-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:12px}
.faq-grid details{background:var(--panel);border:1px solid var(--line);padding:18px 20px}
.faq-grid details[open]{border-color:var(--line-strong)}
.faq-grid summary{cursor:pointer;font-weight:700}
.faq-grid p{color:var(--muted);margin:12px 0 0;font-size:.92rem}
.share-panel{display:flex;align-items:center;justify-content:space-between;gap:24px;padding:28px;border:1px solid var(--line);background:linear-gradient(120deg,var(--panel),var(--panel-2))}
.share-panel h2{font-family:var(--display);font-size:2.5rem;font-weight:400;text-transform:uppercase;margin:6px 0}
.share-panel p{color:var(--muted);margin:0}
.footer-row a:hover{color:var(--ink)}
@media(max-width:900px){.case-grid{grid-template-columns:1fr}.faq-grid{grid-template-columns:1fr}.share-panel{display:block}.share-panel .btn{margin-top:18px}}
'''
cs += add
css.write_text(cs,encoding='utf-8')

# Script: share button + image error fallback + lightbox.
script=root/'script.js'
sc=script.read_text(encoding='utf-8')
sc=sc.replace("document.querySelectorAll('img:not(#rkLbImg)').forEach(img=>{", "const shareBtn=document.getElementById('shareBtn');\n if(shareBtn){shareBtn.addEventListener('click',async()=>{try{if(navigator.share){await navigator.share({title:document.title,text:'RKBEKCI dijital arşivi',url:location.href});}else{await navigator.clipboard.writeText(location.href);shareBtn.textContent='Bağlantı kopyalandı';setTimeout(()=>shareBtn.textContent='Sayfayı paylaş',1800);}}catch(e){}});}\n document.querySelectorAll('img:not(#rkLbImg)').forEach(img=>{")
script.write_text(sc,encoding='utf-8')

# 404 page
base='''<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,follow"><meta name="theme-color" content="#0a0a0b"><title>404 — Kayıt Bulunamadı | RKBEKCI</title><link rel="stylesheet" href="style.css"></head><body><main class="error-page"><div class="wrap error-inner"><div class="eyebrow">DOSYA KAYIP</div><h1>404</h1><p>Aradığın arşiv sayfası bulunamadı. Ana dosyaya dönüp mevcut kayıtları inceleyebilirsin.</p><div class="actions"><a class="btn primary" href="index.html">Ana sayfaya dön</a><a class="btn" href="index.html#galeri">Galeriye git</a></div></div></main></body></html>'''
(root/'404.html').write_text(base,encoding='utf-8')

# Thank-you page
thanks='''<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,follow"><meta name="theme-color" content="#0a0a0b"><title>Teşekkürler | RKBEKCI</title><link rel="stylesheet" href="style.css"></head><body><main class="error-page"><div class="wrap error-inner"><div class="eyebrow">KAYIT ALINDI</div><h1>TEŞEKKÜR</h1><p>İlgin için teşekkürler. Arşive dönerek hikâyeyi ve mevcut fotoğraf kayıtlarını inceleyebilirsin.</p><div class="actions"><a class="btn primary" href="index.html">Arşive dön</a></div></div></main></body></html>'''
(root/'tesekkur.html').write_text(thanks,encoding='utf-8')

# Utility pages CSS
css=css.read_text(encoding='utf-8')
css += '\n.error-page{min-height:100vh;display:grid;place-items:center;text-align:center;padding:40px}.error-inner{max-width:720px}.error-inner h1{font-family:var(--display);font-size:clamp(6rem,18vw,12rem);font-weight:400;line-height:.8;margin:18px 0}.error-inner p{color:var(--muted);max-width:620px;margin:0 auto}.error-inner .actions{justify-content:center}\n'
(root/'style.css').write_text(css,encoding='utf-8')

# robots: known local/static-friendly file; sitemap is intentionally relative because deployment host is unknown.
(root/'robots.txt').write_text('User-agent: *\nAllow: /\nDisallow: /source-wordpress-export.xml\n',encoding='utf-8')

print('done')
