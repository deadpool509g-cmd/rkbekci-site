

document.addEventListener('DOMContentLoaded',function(){
 const lb=document.getElementById('rkLightbox'), big=document.getElementById('rkLbImg'),
       cap=document.getElementById('rkCaption'), closeBtn=document.getElementById('rkClose');
 if(!lb||!big||!closeBtn)return;
 const shareBtn=document.getElementById('shareBtn');
 if(shareBtn){shareBtn.addEventListener('click',async()=>{try{if(navigator.share){await navigator.share({title:document.title,text:'RKBEKCI dijital arşivi',url:location.href});}else{await navigator.clipboard.writeText(location.href);shareBtn.textContent='Bağlantı kopyalandı';setTimeout(()=>shareBtn.textContent='Sayfayı paylaş',1800);}}catch(e){}});}
 document.querySelectorAll('img:not(#rkLbImg)').forEach(img=>{
   img.addEventListener('error',function(){
     img.dataset.rkBroken='true';
   });
   img.addEventListener('click',function(e){
     e.preventDefault(); e.stopPropagation();
     big.src=img.currentSrc||img.src; big.alt=img.alt||'';
     cap.textContent=img.alt||'';
     lb.classList.add('open'); document.body.style.overflow='hidden';
   });
 });
 function close(){lb.classList.remove('open');document.body.style.overflow='';}
 closeBtn.onclick=close;
 lb.addEventListener('click',e=>{if(e.target===lb)close()});
 document.addEventListener('keydown',e=>{if(e.key==='Escape')close()});
});
