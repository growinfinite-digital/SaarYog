// (function(){var b=document.querySelector(".burger"),n=document.getElementById("nav");
// b.addEventListener("click",function(){var o=n.classList.toggle("open");b.setAttribute("aria-expanded",o)});
// n.addEventListener("click",function(e){if(e.target.tagName==="A"){n.classList.remove("open");b.setAttribute("aria-expanded","false")}});
// var y=document.getElementById("yr");if(y)y.textContent=new Date().getFullYear();
// document.querySelectorAll("[data-lb]").forEach(function(a){a.addEventListener("click",function(ev){ev.preventDefault();var d=document.createElement("div");d.className="lb";d.innerHTML='<img alt="" src="'+a.href+'">';d.onclick=function(){d.remove()};document.body.appendChild(d)})});
// document.querySelectorAll("[data-cta]").forEach(function(a){a.addEventListener("click",function(){if(window.gtag)gtag("event","cta_click",{method:a.dataset.cta,page:location.pathname})})});})();


(function () {
    // ==========================================
    // SECTION 1: SELECT MOBILE NAVIGATION ELEMENTS
    // ==========================================
    var burger = document.querySelector(".burger");
    var nav = document.getElementById("nav");

    // ==========================================
    // SECTION 2: TOGGLE MOBILE NAVIGATION MENU
    // ==========================================
    burger.addEventListener("click", function () {
        var isOpen = nav.classList.toggle("open");
        burger.setAttribute("aria-expanded", isOpen);
    });

    // ==========================================
    // SECTION 3: CLOSE MENU AFTER CLICKING A LINK
    // ==========================================
    nav.addEventListener("click", function (event) {
        if (event.target.tagName === "A") {
            nav.classList.remove("open");
            burger.setAttribute("aria-expanded", "false");
        }
    });

    // ==========================================
    // SECTION 4: UPDATE THE FOOTER COPYRIGHT YEAR
    // ==========================================
    var year = document.getElementById("yr");

    if (year) {
        year.textContent = new Date().getFullYear();
    }

    // ==========================================
    // SECTION 5: IMAGE LIGHTBOX FUNCTIONALITY
    // ==========================================
    document.querySelectorAll("[data-lb]").forEach(function (link) {
        link.addEventListener("click", function (event) {
            event.preventDefault();

            var lightbox = document.createElement("div");
            lightbox.className = "lb";
            lightbox.innerHTML =
                '<img alt="" src="' + link.href + '">';

            // Close the lightbox when clicked
            lightbox.onclick = function () {
                lightbox.remove();
            };

            document.body.appendChild(lightbox);
        });
    });

    // ==========================================
    // SECTION 6: GOOGLE ANALYTICS CTA CLICK TRACKING
    // ==========================================
    document.querySelectorAll("[data-cta]").forEach(function (link) {
        link.addEventListener("click", function () {
            if (window.gtag) {
                gtag("event", "cta_click", {
                    method: link.dataset.cta,
                    page: location.pathname
                });
            }
        });
    });
})();
