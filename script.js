
(() => {
 const ready=()=>document.body.classList.add('page-ready');
 if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',ready); else ready();

 const selectors='img:not(#rkLbImg)';
 document.querySelectorAll(selectors).forEach((img)=>{
   img.addEventListener('click',(e)=>{
     e.preventDefault(); e.stopPropagation();
     const lb=document.getElementById('rkLightbox'), big=document.getElementById('rkLbImg');
     big.src=img.currentSrc||img.src; big.alt=img.alt||'';
     document.getElementById('rkCaption').textContent=img.alt||'';
     lb.classList.add('open'); lb.setAttribute('aria-hidden','false');
     document.body.style.overflow='hidden';
   });
 });
 const close=()=>{
   const lb=document.getElementById('rkLightbox');
   lb.classList.remove('open'); lb.setAttribute('aria-hidden','true');
   document.body.style.overflow='';
   setTimeout(()=>{if(!lb.classList.contains('open')) document.getElementById('rkLbImg').removeAttribute('src')},250);
 };
 document.getElementById('rkClose').onclick=close;
 document.getElementById('rkLightbox').addEventListener('click',e=>{if(e.target.id==='rkLightbox')close()});
 document.addEventListener('keydown',e=>{if(e.key==='Escape')close()});

 const items=document.querySelectorAll('.reveal');
 if('IntersectionObserver' in window){
   const io=new IntersectionObserver(es=>es.forEach(x=>{if(x.isIntersecting){x.target.classList.add('is-visible');io.unobserve(x.target)}}),{threshold:.1});
   items.forEach(x=>io.observe(x));
 } else items.forEach(x=>x.classList.add('is-visible'));
})();
