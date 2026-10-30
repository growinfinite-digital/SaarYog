document.addEventListener("DOMContentLoaded",function(){var y=document.getElementById("yr");if(y)y.textContent=new Date().getFullYear();
document.querySelectorAll("[data-cta]").forEach(function(a){a.addEventListener("click",function(){if(window.gtag)gtag("event","cta_click",{method:a.dataset.cta,page:location.pathname})})})});
(function(){
  var links=[].slice.call(document.querySelectorAll("[data-lb]")),box=null,idx=0,x0=0;
  function show(i){idx=(i+links.length)%links.length;box.querySelector("img").src=links[idx].href}
  function open(i){
    box=document.createElement("div");
    box.className="lb2";box.setAttribute("role","dialog");box.setAttribute("aria-modal","true");
    box.innerHTML='<button class="lb2-x" aria-label="Close">&times;</button><button class="lb2-n lb2-prev" aria-label="Previous">&#8249;</button><img alt="Parent testimonial"><button class="lb2-n lb2-next" aria-label="Next">&#8250;</button>';
    document.body.appendChild(box);document.body.classList.add("lb2-open");
    show(i);history.pushState({lb:1},"");
    box.addEventListener("click",function(e){
      if(e.target.closest(".lb2-prev"))show(idx-1);
      else if(e.target.closest(".lb2-next"))show(idx+1);
      else close(true);
    });
    box.addEventListener("touchstart",function(e){x0=e.touches[0].clientX},{passive:true});
    box.addEventListener("touchend",function(e){
      var dx=e.changedTouches[0].clientX-x0;
      if(Math.abs(dx)>60)show(idx+(dx<0?1:-1));
    },{passive:true});
  }
  function close(fromUi){
    if(!box)return;
    box.remove();box=null;document.body.classList.remove("lb2-open");
    if(fromUi&&history.state&&history.state.lb)history.back();
  }
  links.forEach(function(a,i){a.addEventListener("click",function(e){e.preventDefault();open(i)})});
  window.addEventListener("popstate",function(){close(false)});
  document.addEventListener("keydown",function(e){
    if(!box)return;
    if(e.key==="Escape")close(true);
    if(e.key==="ArrowLeft")show(idx-1);
    if(e.key==="ArrowRight")show(idx+1);
  });
})();