/* ==========================================================================
   Site script: shared header/footer, animated backgrounds, content renderers,
   forms. Requires config.js and data.js to load first.
   ========================================================================== */
(function(){
  "use strict";
  var S = window.SITE || {}, NAV = window.NAV || [], IND = window.INDUSTRIES || [], CTRY = window.COUNTRIES || [], PK = window.PAKISTAN;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var page = document.body.getAttribute("data-page") || "";
  function $(s, r){ return (r || document).querySelector(s); }
  function $$(s, r){ return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  function esc(t){ return String(t).replace(/[&<>"']/g, function(c){ return {"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#39;"}[c]; }); }
  function flagSrc(code){ return "assets/flags/" + code + ".svg"; }

  /* ---------------- logo & icons ---------------- */
  var LOGO = '<svg class="brand-mark" viewBox="0 0 64 64" aria-hidden="true"><defs><clipPath id="rsl-clip"><rect x="22" y="32" width="20" height="14"/></clipPath></defs><path d="M32 3 57.1 17.5v29L32 61 6.9 46.5v-29Z" fill="#123444" stroke="#3DBB8A" stroke-width="3" stroke-linejoin="round"/><g transform="rotate(-45 32 32)" fill="none" stroke-width="5.6"><rect x="11" y="24.5" width="26" height="15" rx="7.5" stroke="#3DBB8A"/><rect x="27" y="24.5" width="26" height="15" rx="7.5" stroke="#F0B545"/><rect x="11" y="24.5" width="26" height="15" rx="7.5" stroke="#3DBB8A" clip-path="url(#rsl-clip)"/></g></svg>';
  var I = {
    crane:'<path d="M4 21h7M7.5 21V4M7.5 4 20 7M7.5 4 4 8h3.5M18 7v5"/><rect x="16" y="12" width="4" height="3"/>',
    bolt:'<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
    spark:'<path d="m3 21 7-7M9 12l3 3 5-5-3-3zM16 3v2M21 8h-2M19.5 4.5 18 6"/>',
    factory:'<path d="M3 21V10l6 4v-4l6 4V5l6-2v18z"/><path d="M7 17h2M12 17h2M17 17h1"/>',
    truck:'<path d="M2 6h12v10H2zM14 9h4l3 3v4h-7"/><circle cx="6.5" cy="18" r="2"/><circle cx="17.5" cy="18" r="2"/>',
    heart:'<path d="M20.8 5.6a5 5 0 0 0-7.1 0L12 7.3l-1.7-1.7a5 5 0 1 0-7.1 7.1L12 21.5l8.8-8.8a5 5 0 0 0 0-7.1z"/><path d="M3.5 12h4l1.5-3 3 6 1.5-3h7"/>',
    chef:'<path d="M6 14a4 4 0 0 1-.5-8 5 5 0 0 1 9.4-1.5A4 4 0 0 1 18 14z"/><path d="M6 14v6h12v-6M9 17h6"/>',
    shield:'<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
    leaf:'<path d="M11 20A7 7 0 0 1 4 13c0-6 6-9 16-10-1 10-4 16-9 17z"/><path d="M4 21c3-6 7-9 11-11"/>',
    wrench:'<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/>',
    boxes:'<path d="M3 13h8v8H3zM13 13h8v8h-8zM8 3h8v8H8z"/>',
    clipboard:'<rect x="5" y="4" width="14" height="18" rx="2"/><path d="M9 2h6v4H9zM9 12h6M9 16h4"/>',
    arrow:'<path d="M5 12h14M13 6l6 6-6 6"/>',
    check:'<path d="M20 6 9 17l-5-5"/>',
    pin:'<circle cx="12" cy="10" r="3"/><path d="M12 21s-7-5.6-7-11a7 7 0 0 1 14 0c0 5.4-7 11-7 11z"/>',
    phone:'<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
    mail:'<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
    clock:'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    globe:'<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
    users:'<circle cx="9" cy="8" r="3.2"/><circle cx="17" cy="9" r="2.4"/><path d="M3 19c.8-3.2 3.2-5 6-5s5.2 1.8 6 5M15 14.5c2.6-.3 4.8 1.2 5.5 4.5"/>',
    handshake:'<path d="m11 17 2 2a1.4 1.4 0 0 0 2-2M14 14l2.5 2.5a1.4 1.4 0 0 0 2-2l-3.5-3.5-3 1.5-2-2 4-4h3l4 4M3 7l4 4M2 13l5 5 2-2"/><path d="m7 11 3-3 2 1"/>',
    chart:'<path d="M3 3v18h18"/><path d="m7 15 4-4 3 3 6-7"/>',
    target:'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
    book:'<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/><path d="M4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5"/>',
    megaphone:'<path d="M3 11v2a1 1 0 0 0 1 1h3l6 5V5L7 10H4a1 1 0 0 0-1 1zM17 8a5 5 0 0 1 0 8M20 5a9 9 0 0 1 0 14"/>',
    doc:'<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h4"/>',
    search:'<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
    building:'<rect x="4" y="3" width="16" height="18" rx="1"/><path d="M9 21v-4h6v4M8 7h2M14 7h2M8 11h2M14 11h2"/>',
    route:'<circle cx="6" cy="19" r="2"/><circle cx="18" cy="5" r="2"/><path d="M8 19h8.5a3.5 3.5 0 0 0 0-7h-9a3.5 3.5 0 0 1 0-7H16"/>',
    star:'<path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>'
  };
  function icon(n, sw){ return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="' + (sw || 1.8) + '" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + (I[n] || "") + '</svg>'; }
  window.ICON = icon;
  var SOCIAL = {
    facebook:'<path d="M14 8h3V4h-3a4 4 0 0 0-4 4v3H7v4h3v7h4v-7h3l1-4h-4V8z"/>',
    instagram:'<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".8"/>',
    linkedin:'<path d="M4 9h4v11H4zM6 3.5a2 2 0 1 1 0 4 2 2 0 0 1 0-4zM10 9h4v1.6c.6-1 1.9-1.9 3.6-1.9 3 0 3.9 2 3.9 5V20h-4v-5.4c0-1.4-.3-2.6-1.8-2.6s-2 1.1-2 2.6V20h-4z"/>',
    tiktok:'<path d="M16 3c.4 2.4 1.9 4 4 4.2v3.4c-1.5 0-2.9-.4-4-1.2v6.1A5.5 5.5 0 1 1 10.5 10v3.5a2 2 0 1 0 2 2V3z"/>',
    youtube:'<path d="M22 8.2a3 3 0 0 0-2.1-2.1C18 5.6 12 5.6 12 5.6s-6 0-7.9.5A3 3 0 0 0 2 8.2 31 31 0 0 0 1.6 12a31 31 0 0 0 .4 3.8 3 3 0 0 0 2.1 2.1c1.9.5 7.9.5 7.9.5s6 0 7.9-.5a3 3 0 0 0 2.1-2.1 31 31 0 0 0 .4-3.8 31 31 0 0 0-.4-3.8z"/><path d="m10 15 5-3-5-3z"/>'
  };
  var WA_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.7-.8-2-.9-.3-.1-.5-.1-.7.1-.2.3-.8.9-.9 1.1-.2.2-.3.2-.6.1-.3-.1-1.2-.5-2.3-1.4-.9-.8-1.4-1.7-1.6-2-.2-.3 0-.5.1-.6l.4-.5c.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.7-.7 1.9-1.4.2-.7.2-1.2.2-1.4-.1-.1-.3-.2-.6-.3zM12 21.8c-1.8 0-3.5-.5-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 1 1 12 21.8zM12 0a12 12 0 0 0-10.3 18L0 24l6.2-1.6A12 12 0 1 0 12 0z"/></svg>';

  var totalRoles = IND.reduce(function(n, c){ return n + c.roles.length; }, 0);

  /* ---------------- header / footer / chrome ---------------- */
  function brandHTML(){ return LOGO + '<span class="brand-name">' + esc(S.name).replace(/^(\S+)/, "<i>$1</i>") + '<small>' + esc(S.tagline) + '</small></span>'; }
  var header = $("#site-header");
  if(header){
    header.outerHTML =
      '<a class="skip" href="#main">Skip to content</a><div class="progress" id="progress"></div>' +
      '<header class="nav" id="nav"><div class="wrap nav-inner">' +
        '<a class="brand" href="index.html" aria-label="' + esc(S.name) + ' home">' + brandHTML() + '</a>' +
        '<nav aria-label="Main"><ul class="nav-links" id="navLinks">' + NAV.map(function(n){
          return '<li><a href="' + n.href + '"' + (n.id === page ? ' aria-current="page"' : '') + '>' + esc(n.label) + '</a></li>';
        }).join("") + '</ul></nav>' +
        '<a class="btn btn-primary nav-cta" href="contact.html#employer">Hire manpower</a>' +
        '<button class="menu-btn" id="menuBtn" aria-label="Open menu" aria-expanded="false" aria-controls="navLinks"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>' +
      '</div></header>';
  }
  document.body.insertAdjacentHTML("afterbegin", '<div class="ambient" aria-hidden="true"><span class="orb o1"></span><span class="orb o2"></span><span class="orb o3"></span></div>');

  var footer = $("#site-footer");
  if(footer){
    var socials = Object.keys(SOCIAL).filter(function(k){ return S.social && S.social[k]; }).map(function(k){
      return '<a href="' + esc(S.social[k]) + '" target="_blank" rel="noopener" aria-label="' + k + '"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">' + SOCIAL[k] + '</svg></a>';
    }).join("");
    footer.outerHTML =
      '<footer><canvas class="foot-canvas" data-scene="stars" aria-hidden="true"></canvas><div class="wrap">' +
        '<div class="foot">' +
          '<div><a class="brand" href="index.html">' + brandHTML() + '</a>' +
            '<p style="max-width:40ch">' + esc(S.legalName) + ' is a recruitment and HR consultancy in Rawalpindi–Islamabad supplying skilled, semi-skilled and general manpower to employers in Pakistan and abroad.</p>' +
            '<div class="foot-flags">' + CTRY.map(function(c){ return '<img src="' + flagSrc(c.code) + '" alt="' + esc(c.name) + '" title="' + esc(c.name) + '" loading="lazy">'; }).join("") + '</div>' +
            (socials ? '<div class="socials">' + socials + '</div>' : '') +
          '</div>' +
          '<div><h4>Company</h4><ul>' + NAV.map(function(n){ return '<li><a href="' + n.href + '">' + esc(n.label) + '</a></li>'; }).join("") + '</ul></div>' +
          '<div><h4>Industries</h4><ul>' + IND.slice(0, 7).map(function(c){ return '<li><a href="recruitment.html#' + c.id + '">' + esc(c.name.split(" & ")[0].split(",")[0]) + '</a></li>'; }).join("") + '<li><a href="recruitment.html">All ' + totalRoles + ' roles →</a></li></ul></div>' +
          '<div><h4>Contact</h4><ul>' +
            '<li>' + esc(S.address) + '</li>' +
            '<li><a data-cfg="phone" href="tel:' + esc(S.phone.replace(/[^+\d]/g, "")) + '">' + esc(S.phone) + '</a></li>' +
            '<li><a href="mailto:' + esc(S.email) + '">' + esc(S.email) + '</a></li>' +
            '<li>' + esc(S.hours) + '</li>' +
          '</ul></div>' +
        '</div>' +
        '<div class="foot-bottom"><span>© ' + new Date().getFullYear() + ' ' + esc(S.legalName || S.name) + '. All rights reserved.</span>' +
          '<nav aria-label="Legal"><a href="privacy.html">Privacy policy</a><a href="terms.html">Terms of use</a><a href="contact.html">Contact</a></nav></div>' +
      '</div></footer>';
  }
  document.body.insertAdjacentHTML("beforeend", '<a class="wa" href="https://wa.me/' + esc(S.whatsapp) + '" target="_blank" rel="noopener" aria-label="Chat with us on WhatsApp">' + WA_SVG + '</a>');

  // fill any [data-cfg] placeholders in page content
  $$("[data-cfg]").forEach(function(el){
    var k = el.getAttribute("data-cfg"); if(!S[k]) return;
    el.textContent = S[k];
    if(el.tagName === "A"){
      if(k === "phone") el.href = "tel:" + S.phone.replace(/[^+\d]/g, "");
      if(k === "email") el.href = "mailto:" + S.email;
      if(k === "address") el.href = S.mapUrl;
    }
  });
  $$("[data-wa]").forEach(function(a){ a.href = "https://wa.me/" + S.whatsapp; });
  $$("[data-stat='roles']").forEach(function(el){ el.textContent = totalRoles; el.setAttribute("data-count", totalRoles); });
  $$("[data-stat='industries']").forEach(function(el){ el.textContent = IND.length; el.setAttribute("data-count", IND.length); });
  $$("[data-stat='countries']").forEach(function(el){ el.textContent = CTRY.length; el.setAttribute("data-count", CTRY.length); });
  $$("[data-name]").forEach(function(el){ el.textContent = S.name; });
  $$("[data-legal-name]").forEach(function(el){ el.textContent = S.legalName || S.name; });
  $$("[data-icon]").forEach(function(el){ el.innerHTML = icon(el.getAttribute("data-icon")) ; });

  /* nav behaviour */
  var nav = $("#nav"), menuBtn = $("#menuBtn"), prog = $("#progress");
  function onScroll(){
    if(nav) nav.classList.toggle("scrolled", window.scrollY > 20);
    if(prog){ var h = document.documentElement.scrollHeight - window.innerHeight; prog.style.width = (h > 0 ? window.scrollY / h * 100 : 0) + "%"; }
  }
  window.addEventListener("scroll", onScroll, {passive:true}); onScroll();
  if(menuBtn) menuBtn.addEventListener("click", function(){ var o = nav.classList.toggle("open"); menuBtn.setAttribute("aria-expanded", o); });

  /* ---------------- content renderers ---------------- */
  // flag marquee
  $$("[data-render='flag-marquee']").forEach(function(el){
    var items = CTRY.map(function(c){ return '<li><img src="' + flagSrc(c.code) + '" alt="" loading="lazy">' + esc(c.name) + ' <span>' + esc(c.hub.split(" · ")[0]) + '</span></li>'; }).join("");
    el.innerHTML = '<div class="marquee-track"><ul>' + items + '</ul><ul aria-hidden="true">' + items + '</ul></div>';
    el.setAttribute("aria-label", "Countries we recruit for: " + CTRY.map(function(c){ return c.name; }).join(", "));
  });
  // trade marquee
  $$("[data-render='trade-marquee']").forEach(function(el){
    var picks = []; IND.forEach(function(c){ picks = picks.concat(c.roles.slice(0, 2)); });
    var items = picks.map(function(r){ return "<li>" + esc(r) + "</li>"; }).join("");
    el.innerHTML = '<div class="marquee-track"><ul>' + items + '</ul><ul aria-hidden="true">' + items + '</ul></div>';
  });
  // industry tiles (home)
  $$("[data-render='industry-tiles']").forEach(function(el){
    el.innerHTML = IND.map(function(c){
      return '<a class="card ind-tile reveal" href="recruitment.html#' + c.id + '"><div class="ico">' + icon(c.icon) + '</div><h3>' + esc(c.name) + '</h3><p class="roles">' + esc(c.roles.slice(0, 4).join(", ")) + ' and more</p><span class="count">' + c.roles.length + ' roles</span></a>';
    }).join("");
  });
  // country cards grouped by region
  $$("[data-render='country-cards']").forEach(function(el){
    var compact = el.hasAttribute("data-compact"), html = "";
    if(compact){
      html = '<div class="grid g4">' + CTRY.map(countryCard).join("") + "</div>";
    } else {
      var regions = []; CTRY.forEach(function(c){ if(regions.indexOf(c.region) < 0) regions.push(c.region); });
      regions.forEach(function(r){
        html += '<h3 class="region-label">' + esc(r) + '</h3><div class="grid g3">' + CTRY.filter(function(c){ return c.region === r; }).map(countryCard).join("") + "</div>";
      });
    }
    el.innerHTML = html;
    function countryCard(c){
      return '<a class="card country-card reveal" href="countries.html#' + c.code + '"><div class="cc-top"><span class="flag"><img src="' + flagSrc(c.code) + '" alt="Flag of ' + esc(c.name) + '" loading="lazy"></span><div><h3>' + esc(c.name) + '</h3><div class="hub">' + esc(c.hub) + '</div></div></div>' +
        '<div class="cc-body"><div class="tags">' + c.sectors.slice(0, compact ? 3 : 5).map(function(s){ return "<span>" + esc(s) + "</span>"; }).join("") + '</div></div></a>';
    }
  });
  // countries explorer
  var explorer = $("[data-render='explorer']");
  if(explorer){
    explorer.innerHTML = '<div class="explorer-list" role="tablist" aria-label="Countries">' + CTRY.map(function(c, i){
      return '<button role="tab" id="ex-' + c.code + '" aria-selected="' + (i === 0) + '" data-code="' + c.code + '"><span class="flag"><img src="' + flagSrc(c.code) + '" alt=""></span><span>' + esc(c.name) + '<small>' + esc(c.region) + '</small></span></button>';
    }).join("") + '</div><div class="explorer-panel" id="exPanel" role="tabpanel" aria-live="polite"></div>';
    var panel = $("#exPanel");
    function showCountry(code, scroll){
      var c = CTRY.filter(function(x){ return x.code === code; })[0] || CTRY[0];
      $$(".explorer-list button", explorer).forEach(function(b){ b.setAttribute("aria-selected", b.dataset.code === c.code); });
      panel.style.animation = "none"; panel.offsetHeight; panel.style.animation = "";
      panel.innerHTML =
        '<div class="head"><span class="flag"><img src="' + flagSrc(c.code) + '" alt="Flag of ' + esc(c.name) + '"></span><div><h3>' + esc(c.name) + '</h3><div class="hub">' + esc(c.hub) + '</div></div></div>' +
        '<p>' + esc(c.note) + '</p>' +
        '<div class="facts"><div><small>Work authorisation</small><b>' + esc(c.permit) + '</b></div><div><small>Typical contract</small><b>' + esc(c.contract) + '</b></div><div><small>Language</small><b>' + esc(c.lang) + '</b></div></div>' +
        '<div style="display:grid;gap:10px"><h4>Sectors hiring</h4><div class="tags">' + c.sectors.map(function(s){ return "<span>" + esc(s) + "</span>"; }).join("") + '</div></div>' +
        '<div style="display:grid;gap:10px"><h4>Roles we recruit</h4><ul class="roles-list">' + c.roles.map(function(s){ return "<li>" + esc(s) + "</li>"; }).join("") + '</ul></div>' +
        '<div style="display:flex;flex-wrap:wrap;gap:12px"><a class="btn btn-solid" href="contact.html#employer">Hire for ' + esc(c.name) + '</a><a class="btn btn-line" href="contact.html#jobseeker">Apply for jobs in ' + esc(c.name) + '</a></div>' +
        '<p style="font-size:13px">Requirements differ by employer and change over time. We confirm the exact visa route, salary and conditions in writing for every vacancy.</p>';
      $$("canvas[data-scene='routes']").forEach(function(cv){ cv.dataset.highlight = c.code; });
      if(scroll && window.innerWidth < 820) panel.scrollIntoView({behavior:"smooth", block:"start"});
    }
    explorer.addEventListener("click", function(e){ var b = e.target.closest("button[data-code]"); if(b) showCountry(b.dataset.code, true); });
    var h0 = (location.hash || "").slice(1);
    showCountry(CTRY.some(function(c){ return c.code === h0; }) ? h0 : CTRY[0].code, false);
  }
  // industries directory
  var dir = $("[data-render='directory']");
  if(dir){
    var chips = $("#dirChips"), search = $("#dirSearch"), count = $("#dirCount"), curr = "all";
    chips.innerHTML = '<button type="button" class="chip" data-id="all" aria-pressed="true">All industries</button>' + IND.map(function(c){ return '<button type="button" class="chip" data-id="' + c.id + '" aria-pressed="false">' + esc(c.name.split(" & ")[0].split(",")[0]) + '</button>'; }).join("");
    function renderDir(){
      var q = (search.value || "").trim().toLowerCase(), shown = 0, roles = 0;
      var html = IND.filter(function(c){ return curr === "all" || c.id === curr; }).map(function(c){
        var hits = q ? c.roles.filter(function(r){ return r.toLowerCase().indexOf(q) >= 0; }) : [];
        var catHit = q && (c.name.toLowerCase().indexOf(q) >= 0);
        if(q && !hits.length && !catHit) return "";
        shown++; roles += q && !catHit ? hits.length : c.roles.length;
        return '<article class="card dir-card" id="' + c.id + '"><div class="dc-head"><div class="ico">' + icon(c.icon) + '</div><div><h3>' + esc(c.name) + '</h3><p>' + esc(c.blurb) + '</p></div></div>' +
          '<ul class="roles-list">' + c.roles.map(function(r){ return '<li' + (q && r.toLowerCase().indexOf(q) >= 0 ? ' class="hit"' : '') + '>' + esc(r) + '</li>'; }).join("") + '</ul>' +
          '<div class="dc-foot"><span>' + c.roles.length + ' positions</span><a class="link-arrow" href="contact.html#employer">Request workers ' + icon("arrow", 2) + '</a></div></article>';
      }).join("");
      dir.innerHTML = html || '<div class="dir-empty">No role matches “' + esc(q) + '”. We recruit many more trades than listed here, so <a href="contact.html#employer">send us your requirement</a>.</div>';
      count.textContent = q ? roles + " matching roles in " + shown + " industries" : totalRoles + " roles across " + IND.length + " industries";
    }
    chips.addEventListener("click", function(e){
      var b = e.target.closest(".chip"); if(!b) return;
      curr = b.dataset.id; $$(".chip", chips).forEach(function(x){ x.setAttribute("aria-pressed", x === b); }); renderDir();
    });
    search.addEventListener("input", renderDir);
    renderDir();
    var hid = (location.hash || "").slice(1);
    if(hid && IND.some(function(c){ return c.id === hid; })){
      setTimeout(function(){ var t = document.getElementById(hid); if(t){ t.scrollIntoView({block:"center"}); t.style.borderColor = "var(--accent)"; } }, 60);
    }
  }

  /* ---------------- home hero: typing + requisition card ---------------- */
  var tradeEl = $("#trade");
  if(tradeEl && !reduce){
    var trades = ["Welders","Heavy drivers","Caregivers","Electricians","Masons","Farm workers","Cooks","Forklift operators"];
    var ti = 0, ci = trades[0].length, del = true;
    (function tick(){
      var w = trades[ti];
      if(del){ ci--; if(ci <= 0){ del = false; ti = (ti + 1) % trades.length; w = trades[ti]; } }
      else { ci++; if(ci >= w.length){ del = true; tradeEl.textContent = w; return setTimeout(tick, 2000); } }
      tradeEl.textContent = w.slice(0, Math.max(ci, 0)) || "​";
      setTimeout(tick, del ? 45 : 85);
    })();
  }
  var req = $("#req");
  if(req){
    var reqs = [["Welders (6G)",40,"ro"],["HTV drivers",60,"sa"],["Caregivers",25,"pt"],["Masons",80,"by"],["Security guards",50,"ae"],["Sewing operators",45,"tr"],["Electricians",30,"kg"],["Warehouse staff",35,"pl"]];
    var ri = 0, stage = 0;
    function showReq(){
      var r = reqs[ri], c = CTRY.filter(function(x){ return x.code === r[2]; })[0];
      $("#reqRole").textContent = r[0]; $("#reqQty").textContent = r[1] + " positions";
      $("#reqFlag").src = flagSrc(c.code); $("#reqFlag").alt = "Flag of " + c.name; $("#reqTo").textContent = c.name;
      $("#reqNo").textContent = "REQ-" + (2610 + ri * 7);
    }
    function stageTick(){
      stage++;
      if(stage > 5){ stage = 0; ri = (ri + 1) % reqs.length; showReq(); }
      $$(".req-stages div", req).forEach(function(d, i){ d.classList.toggle("done", i < stage); });
      $("#reqStatus").textContent = ["Requirement received","Sourcing","Screening","Trade testing","Mobilising","Mobilising"][stage];
    }
    showReq();
    if(reduce){ stage = 3; stageTick(); } else setInterval(stageTick, 900);
  }

  /* ---------------- animated canvas scenes ---------------- */
  function cssRGB(){ var v = getComputedStyle(document.documentElement).getPropertyValue("--deco").trim(); return v || "18,112,79"; }
  function quad(a, b, t, lift){
    var mx = (a.x + b.x) / 2, my = (a.y + b.y) / 2 - Math.hypot(b.x - a.x, b.y - a.y) * (lift || .28), u = 1 - t;
    return {x:u*u*a.x + 2*u*t*mx + t*t*b.x, y:u*u*a.y + 2*u*t*my + t*t*b.y, cx:mx, cy:my};
  }
  function particles(n, W, H){ var a = []; for(var i = 0; i < n; i++) a.push({x:Math.random()*W, y:Math.random()*H, vx:(Math.random()-.5)*.3, vy:(Math.random()-.5)*.3, r:Math.random()*1.4+.4}); return a; }
  function drawParticles(ctx, P, W, H, mouse, link, color){
    for(var i = 0; i < P.length; i++){
      var p = P[i]; p.x += p.vx; p.y += p.vy;
      if(p.x < 0 || p.x > W) p.vx *= -1; if(p.y < 0 || p.y > H) p.vy *= -1;
      if(mouse){ var dx = p.x - mouse.x, dy = p.y - mouse.y, d = Math.hypot(dx, dy); if(d < 110 && d > 0){ p.x += dx/d*1.1; p.y += dy/d*1.1; } }
      ctx.fillStyle = "rgba(" + color + ",.55)"; ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, 6.283); ctx.fill();
      for(var j = i + 1; j < P.length; j++){
        var q = P[j], dd = Math.hypot(p.x - q.x, p.y - q.y);
        if(dd < link){ ctx.strokeStyle = "rgba(61,187,138," + (.16 * (1 - dd / link)) + ")"; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(p.x, p.y); ctx.lineTo(q.x, q.y); ctx.stroke(); }
      }
      if(mouse){ var dm = Math.hypot(p.x - mouse.x, p.y - mouse.y); if(dm < 150){ ctx.strokeStyle = "rgba(240,181,69," + (.35 * (1 - dm / 150)) + ")"; ctx.beginPath(); ctx.moveTo(p.x, p.y); ctx.lineTo(mouse.x, mouse.y); ctx.stroke(); } }
    }
  }

  var SCENES = {
    /* flight routes from Pakistan to each destination */
    routes: function(cv, ctx){
      var W, H, view, P, frame = 0, full = cv.hasAttribute("data-full");
      var R = CTRY.map(function(c, i){ return {c:c, t:Math.random(), sp:.003 + Math.random()*.002, delay:i*20}; });
      var flags = {}; CTRY.forEach(function(c){ var im = new Image(); im.src = flagSrc(c.code); flags[c.code] = im; });
      function pr(lon, lat){ return {x:view.x0 + (lon - view.lon0) * view.k, y:view.y0 - (lat - view.lat0) * view.k}; }
      return {
        resize:function(w, h){
          W = w; H = h;
          var lonSpan = 94, latSpan = 42, wide = W > 960 && !full;
          var aw = wide ? W * .62 : W * .92, ah = H * (wide ? .7 : .62);
          var k = Math.min(aw / lonSpan, ah / latSpan);
          view = {k:k, lon0:-14, lat0:18, x0: wide ? W - lonSpan * k - W * .03 : (W - lonSpan * k) / 2, y0: (wide ? H * .16 : H * (full ? .2 : .32)) + latSpan * k};
          P = particles(Math.round(Math.min(100, W * H / 14000)), W, H);
        },
        draw:function(mouse){
          frame++; ctx.clearRect(0, 0, W, H);
          ctx.strokeStyle = "rgba(147,169,167,.07)"; ctx.lineWidth = 1;
          for(var lon = -10; lon <= 80; lon += 10){ var a = pr(lon, 16), b = pr(lon, 62); ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke(); }
          for(var lat = 20; lat <= 60; lat += 10){ var c1 = pr(-16, lat), c2 = pr(82, lat); ctx.beginPath(); ctx.moveTo(c1.x, c1.y); ctx.lineTo(c2.x, c2.y); ctx.stroke(); }
          drawParticles(ctx, P, W, H, mouse, 105, "200,220,215");
          var o = pr(PK.lon, PK.lat), hl = cv.dataset.highlight, small = W < 620;
          R.forEach(function(r){
            var b = pr(r.c.lon, r.c.lat), m = quad(o, b, 0), on = !hl || hl === r.c.code;
            ctx.strokeStyle = on ? (hl ? "rgba(240,181,69,.7)" : "rgba(61,187,138,.3)") : "rgba(61,187,138,.1)";
            ctx.lineWidth = hl && on ? 1.6 : 1; ctx.setLineDash([3, 5]);
            ctx.beginPath(); ctx.moveTo(o.x, o.y); ctx.quadraticCurveTo(m.cx, m.cy, b.x, b.y); ctx.stroke(); ctx.setLineDash([]);
            if(frame > r.delay){ r.t += r.sp * (hl && on ? 1.6 : 1); if(r.t > 1.15) r.t = 0; }
            var t = Math.min(r.t, 1);
            if(on) for(var s = 0; s < 14; s++){
              var tt = t - s * .012; if(tt < 0) break;
              var pt = quad(o, b, tt); ctx.fillStyle = "rgba(240,181,69," + (.9 * (1 - s / 14)) + ")";
              ctx.beginPath(); ctx.arc(pt.x, pt.y, 2.4 * (1 - s / 14) + .4, 0, 6.283); ctx.fill();
            }
            var glow = r.t > 1 ? 1 - (r.t - 1) / .15 : 0;
            if(glow > 0 && on){ ctx.strokeStyle = "rgba(61,187,138," + glow + ")"; ctx.beginPath(); ctx.arc(b.x, b.y, 4 + (1 - glow) * 16, 0, 6.283); ctx.stroke(); }
            var fw = small ? 16 : (hl === r.c.code ? 30 : 22), fh = fw * .75, im = flags[r.c.code];
            ctx.globalAlpha = on ? 1 : .35;
            if(im.complete && im.naturalWidth){ ctx.save(); ctx.beginPath(); ctx.rect(b.x - fw/2, b.y - fh/2, fw, fh); ctx.clip(); ctx.drawImage(im, b.x - fw/2, b.y - fh/2, fw, fh); ctx.restore(); ctx.strokeStyle = "rgba(255,255,255,.5)"; ctx.strokeRect(b.x - fw/2, b.y - fh/2, fw, fh); }
            else { ctx.fillStyle = "#3DBB8A"; ctx.beginPath(); ctx.arc(b.x, b.y, 3, 0, 6.283); ctx.fill(); }
            if(!small){ ctx.fillStyle = "rgba(200,215,212,.85)"; ctx.font = "500 10px 'IBM Plex Mono', monospace"; ctx.fillText(r.c.name.toUpperCase(), b.x + fw/2 + 6, b.y + 3); }
            ctx.globalAlpha = 1;
          });
          var pulse = (frame % 120) / 120;
          ctx.strokeStyle = "rgba(240,181,69," + (1 - pulse) + ")"; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.arc(o.x, o.y, 6 + pulse * 24, 0, 6.283); ctx.stroke();
          ctx.fillStyle = "#F0B545"; ctx.beginPath(); ctx.arc(o.x, o.y, 5, 0, 6.283); ctx.fill();
          ctx.fillStyle = "#E8EFEC"; ctx.font = "600 11px 'IBM Plex Mono', monospace"; ctx.fillText("RAWALPINDI · ISLAMABAD", o.x - 60, o.y + 26);
        }
      };
    },
    /* glowing hexagon grid (industries) */
    hex: function(cv, ctx){
      var W, H, cells = [], size, P;
      return {
        resize:function(w, h){
          W = w; H = h; size = w < 600 ? 26 : 34; cells = [];
          var hw = Math.sqrt(3) * size, vh = size * 1.5;
          for(var r = -1; r * vh < H + size; r++) for(var q = -1; q * hw < W + hw; q++) cells.push({x:q * hw + (r % 2 ? hw / 2 : 0), y:r * vh, g:0});
          P = particles(Math.round(Math.min(60, W * H / 22000)), W, H);
        },
        draw:function(mouse){
          ctx.clearRect(0, 0, W, H);
          if(Math.random() < .12){ var c = cells[(Math.random() * cells.length) | 0]; c.g = 1; }
          cells.forEach(function(c){
            if(mouse){ var d = Math.hypot(c.x - mouse.x, c.y - mouse.y); if(d < size * 2.2) c.g = Math.max(c.g, 1 - d / (size * 2.6)); }
            ctx.beginPath();
            for(var i = 0; i < 6; i++){ var a = Math.PI / 3 * i + Math.PI / 6, x = c.x + (size - 2) * Math.cos(a), y = c.y + (size - 2) * Math.sin(a); if(i) ctx.lineTo(x, y); else ctx.moveTo(x, y); }
            ctx.closePath();
            ctx.strokeStyle = "rgba(147,169,167," + (.07 + c.g * .4) + ")"; ctx.lineWidth = 1; ctx.stroke();
            if(c.g > .02){ ctx.fillStyle = (c.x + c.y) % 3 < 1.2 ? "rgba(240,181,69," + c.g * .22 + ")" : "rgba(61,187,138," + c.g * .25 + ")"; ctx.fill(); c.g *= .965; }
          });
          drawParticles(ctx, P, W, H, null, 90, "200,220,215");
        }
      };
    },
    /* two connected talent/employer clusters (partnerships) */
    network: function(cv, ctx){
      var W, H, A = [], B = [], E = [], pulses = [], stacked;
      function cluster(cx, cy, rad, n){ var a = []; for(var i = 0; i < n; i++){ var an = Math.random() * 6.283, d = Math.sqrt(Math.random()) * rad; a.push({bx:cx + Math.cos(an) * d, by:cy + Math.sin(an) * d, ph:Math.random() * 6.283, r:Math.random() * 2 + 1.4}); } return a; }
      return {
        resize:function(w, h){
          W = w; H = h; stacked = W < 760;
          var rad = Math.min(W, H) * (stacked ? .2 : .26);
          A = cluster(stacked ? W * .5 : W * .5, stacked ? H * .3 : H * .5, rad, 26);
          B = cluster(stacked ? W * .5 : W * .82, stacked ? H * .78 : H * .5, rad, 26);
          if(!stacked){ A.forEach(function(n){ n.bx -= W * .0; }); }
          E = []; for(var i = 0; i < 22; i++) E.push([A[(Math.random() * A.length) | 0], B[(Math.random() * B.length) | 0]]);
          pulses = [];
        },
        draw:function(mouse, time){
          ctx.clearRect(0, 0, W, H);
          var all = A.concat(B);
          all.forEach(function(n){ n.x = n.bx + Math.sin(time / 1600 + n.ph) * 6; n.y = n.by + Math.cos(time / 1900 + n.ph) * 6; });
          [A, B].forEach(function(C){
            for(var i = 0; i < C.length; i++) for(var j = i + 1; j < C.length; j++){ var d = Math.hypot(C[i].x - C[j].x, C[i].y - C[j].y); if(d < 70){ ctx.strokeStyle = "rgba(147,169,167," + (.18 * (1 - d / 70)) + ")"; ctx.beginPath(); ctx.moveTo(C[i].x, C[i].y); ctx.lineTo(C[j].x, C[j].y); ctx.stroke(); } }
          });
          E.forEach(function(e){ var m = quad(e[0], e[1], 0, .18); ctx.strokeStyle = "rgba(61,187,138,.12)"; ctx.beginPath(); ctx.moveTo(e[0].x, e[0].y); ctx.quadraticCurveTo(m.cx, m.cy, e[1].x, e[1].y); ctx.stroke(); });
          if(Math.random() < .08) pulses.push({e:E[(Math.random() * E.length) | 0], t:0, back:Math.random() < .5});
          pulses = pulses.filter(function(p){ p.t += .012; return p.t < 1; });
          pulses.forEach(function(p){ var t = p.back ? 1 - p.t : p.t, pt = quad(p.e[0], p.e[1], t, .18); ctx.fillStyle = p.back ? "rgba(61,187,138,.95)" : "rgba(240,181,69,.95)"; ctx.beginPath(); ctx.arc(pt.x, pt.y, 2.6, 0, 6.283); ctx.fill(); });
          A.forEach(function(n){ ctx.fillStyle = "rgba(240,181,69,.85)"; ctx.beginPath(); ctx.arc(n.x, n.y, n.r, 0, 6.283); ctx.fill(); });
          B.forEach(function(n){ ctx.fillStyle = "rgba(61,187,138,.9)"; ctx.beginPath(); ctx.arc(n.x, n.y, n.r, 0, 6.283); ctx.fill(); });
        }
      };
    },
    /* rising line & bar charts (consultancy) */
    chart: function(cv, ctx){
      var W, H, lines = [], bars = [], off = 0;
      return {
        resize:function(w, h){
          W = w; H = h; lines = [];
          for(var l = 0; l < 3; l++){ var pts = [], v = .6 + l * .08; for(var i = 0; i < 80; i++){ v += (Math.random() - .46) * .05; v = Math.max(.15, Math.min(.85, v)); pts.push(v); } lines.push(pts); }
          bars = []; for(var b = 0; b < 40; b++) bars.push({h:Math.random() * .25 + .05, t:Math.random() * .25 + .05});
        },
        draw:function(mouse){
          ctx.clearRect(0, 0, W, H); off += .6;
          ctx.strokeStyle = "rgba(147,169,167,.07)"; ctx.lineWidth = 1;
          for(var gx = -(off % 60); gx < W; gx += 60){ ctx.beginPath(); ctx.moveTo(gx, 0); ctx.lineTo(gx, H); ctx.stroke(); }
          for(var gy = 0; gy < H; gy += 60){ ctx.beginPath(); ctx.moveTo(0, gy); ctx.lineTo(W, gy); ctx.stroke(); }
          var bw = W / bars.length;
          bars.forEach(function(b, i){ b.h += (b.t - b.h) * .03; if(Math.abs(b.t - b.h) < .005) b.t = Math.random() * .28 + .04; ctx.fillStyle = "rgba(61,187,138,.08)"; ctx.fillRect(i * bw + 3, H - b.h * H, bw - 6, b.h * H); });
          var step = W / 40, shift = (off % step) / step;
          lines.forEach(function(pts, li){
            if(off % step < .6){ pts.shift(); var v = pts[pts.length - 1] + (Math.random() - .45) * .06; pts.push(Math.max(.15, Math.min(.85, v))); }
            ctx.beginPath();
            for(var i = 0; i < pts.length; i++){ var x = (i - shift) * step, y = H * (1 - pts[i] * .8) ; if(i) ctx.lineTo(x, y); else ctx.moveTo(x, y); }
            ctx.strokeStyle = li === 0 ? "rgba(240,181,69,.55)" : "rgba(61,187,138," + (.45 - li * .12) + ")"; ctx.lineWidth = li === 0 ? 2 : 1.4; ctx.stroke();
            var lx = Math.min(pts.length - 1, Math.floor(W * .78 / step)), ly = H * (1 - pts[lx] * .8), x0 = (lx - shift) * step;
            if(li === 0){ ctx.fillStyle = "#F0B545"; ctx.beginPath(); ctx.arc(x0, ly, 4, 0, 6.283); ctx.fill(); ctx.strokeStyle = "rgba(240,181,69,.3)"; ctx.beginPath(); ctx.arc(x0, ly, 10, 0, 6.283); ctx.stroke(); }
          });
        }
      };
    },
    /* radar sweep finding candidates (about / contact) */
    radar: function(cv, ctx){
      var W, H, cx, cy, R, blips = [], ang = 0, P;
      var labels = []; IND.forEach(function(c){ labels = labels.concat(c.roles.slice(0, 3)); });
      return {
        resize:function(w, h){ W = w; H = h; var wide = W > 960; cx = wide ? W * .76 : W * .5; cy = wide ? H * .52 : H * .62; R = Math.min(wide ? W * .3 : W * .6, H * .7); P = particles(Math.round(Math.min(50, W * H / 26000)), W, H); blips = []; },
        draw:function(mouse){
          ctx.clearRect(0, 0, W, H);
          drawParticles(ctx, P, W, H, mouse, 90, "200,220,215");
          for(var i = 1; i <= 4; i++){ ctx.strokeStyle = "rgba(61,187,138," + (.18 - i * .025) + ")"; ctx.lineWidth = 1; ctx.beginPath(); ctx.arc(cx, cy, R * i / 4, 0, 6.283); ctx.stroke(); }
          ctx.strokeStyle = "rgba(61,187,138,.08)"; ctx.beginPath(); ctx.moveTo(cx - R, cy); ctx.lineTo(cx + R, cy); ctx.moveTo(cx, cy - R); ctx.lineTo(cx, cy + R); ctx.stroke();
          ang += .012;
          var g = ctx.createConicGradient ? ctx.createConicGradient(ang - .6, cx, cy) : null;
          if(g){ g.addColorStop(0, "rgba(61,187,138,0)"); g.addColorStop(.09, "rgba(61,187,138,.22)"); g.addColorStop(.1, "rgba(61,187,138,0)"); g.addColorStop(1, "rgba(61,187,138,0)"); ctx.fillStyle = g; ctx.beginPath(); ctx.arc(cx, cy, R, 0, 6.283); ctx.fill(); }
          ctx.strokeStyle = "rgba(61,187,138,.6)"; ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx + Math.cos(ang) * R, cy + Math.sin(ang) * R); ctx.stroke();
          if(Math.random() < .04 && blips.length < 9){ var a = ang + (Math.random() - .5) * .1, d = R * (.25 + Math.random() * .7); blips.push({x:cx + Math.cos(a) * d, y:cy + Math.sin(a) * d, life:1, label:labels[(Math.random() * labels.length) | 0]}); }
          blips = blips.filter(function(b){ b.life -= .004; return b.life > 0; });
          blips.forEach(function(b){
            ctx.fillStyle = "rgba(240,181,69," + b.life + ")"; ctx.beginPath(); ctx.arc(b.x, b.y, 3.5, 0, 6.283); ctx.fill();
            ctx.strokeStyle = "rgba(240,181,69," + b.life * .5 + ")"; ctx.beginPath(); ctx.arc(b.x, b.y, 3.5 + (1 - b.life) * 20, 0, 6.283); ctx.stroke();
            if(W > 620){ ctx.fillStyle = "rgba(220,230,228," + b.life * .8 + ")"; ctx.font = "500 10px 'IBM Plex Mono', monospace"; ctx.fillText(b.label.toUpperCase(), b.x + 9, b.y + 3); }
          });
          ctx.fillStyle = "#F0B545"; ctx.beginPath(); ctx.arc(cx, cy, 4, 0, 6.283); ctx.fill();
        }
      };
    },
    /* plain constellation (legal pages, footer, CTA) */
    stars: function(cv, ctx){
      var W, H, P;
      return {
        resize:function(w, h){ W = w; H = h; P = particles(Math.round(Math.min(80, W * H / 12000)), W, H); },
        draw:function(mouse){ ctx.clearRect(0, 0, W, H); drawParticles(ctx, P, W, H, mouse, 100, "200,220,215"); }
      };
    },
    /* floating outlined shapes behind light sections */
    deco: function(cv, ctx){
      var W, H, S = [], rgb;
      return {
        resize:function(w, h){
          W = w; H = h; rgb = cssRGB(); S = [];
          var n = Math.max(6, Math.round(W * H / 60000));
          for(var i = 0; i < n; i++) S.push({x:Math.random() * W, y:Math.random() * H, s:14 + Math.random() * 46, rot:Math.random() * 6, vr:(Math.random() - .5) * .004, vx:(Math.random() - .5) * .18, vy:(Math.random() - .5) * .18, k:i % 4});
        },
        draw:function(){
          ctx.clearRect(0, 0, W, H);
          S.forEach(function(p){
            p.x += p.vx; p.y += p.vy; p.rot += p.vr;
            if(p.x < -60) p.x = W + 60; if(p.x > W + 60) p.x = -60; if(p.y < -60) p.y = H + 60; if(p.y > H + 60) p.y = -60;
            ctx.save(); ctx.translate(p.x, p.y); ctx.rotate(p.rot);
            ctx.strokeStyle = p.k === 3 ? "rgba(201,138,18,.22)" : "rgba(" + rgb + ",.18)"; ctx.lineWidth = 1.4;
            ctx.beginPath();
            if(p.k === 0){ for(var i = 0; i < 6; i++){ var a = Math.PI / 3 * i; ctx.lineTo(Math.cos(a) * p.s, Math.sin(a) * p.s); } ctx.closePath(); }
            else if(p.k === 1){ ctx.arc(0, 0, p.s * .7, 0, 6.283); }
            else if(p.k === 2){ ctx.moveTo(-p.s * .4, 0); ctx.lineTo(p.s * .4, 0); ctx.moveTo(0, -p.s * .4); ctx.lineTo(0, p.s * .4); }
            else { ctx.moveTo(-p.s * .5, p.s * .25); ctx.lineTo(0, -p.s * .25); ctx.lineTo(p.s * .5, p.s * .25); }
            ctx.stroke(); ctx.restore();
          });
        }
      };
    }
  };

  // auto-add a deco canvas behind every light section that asks for one
  $$(".section[data-deco]").forEach(function(sec){ var c = document.createElement("canvas"); c.className = "deco-canvas"; c.setAttribute("data-scene", "deco"); c.setAttribute("aria-hidden", "true"); sec.insertBefore(c, sec.firstChild); });

  var live = [];
  $$("canvas[data-scene]").forEach(function(cv){
    var make = SCENES[cv.getAttribute("data-scene")]; if(!make) return;
    var ctx = cv.getContext("2d"), sc = make(cv, ctx), item = {cv:cv, ctx:ctx, sc:sc, vis:true, mouse:null};
    function size(){
      var dpr = Math.min(window.devicePixelRatio || 1, 2), w = cv.clientWidth, h = cv.clientHeight;
      if(!w || !h) return; cv.width = w * dpr; cv.height = h * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0); sc.resize(w, h); item.ready = true;
    }
    item.size = size; size();
    var host = cv.parentElement;
    if(cv.getAttribute("data-scene") !== "deco"){
      host.addEventListener("pointermove", function(e){ var r = cv.getBoundingClientRect(); item.mouse = {x:e.clientX - r.left, y:e.clientY - r.top}; });
      host.addEventListener("pointerleave", function(){ item.mouse = null; });
    }
    live.push(item);
  });
  if("IntersectionObserver" in window){
    var vio = new IntersectionObserver(function(es){ es.forEach(function(e){ live.forEach(function(it){ if(it.cv === e.target) it.vis = e.isIntersecting; }); }); });
    live.forEach(function(it){ vio.observe(it.cv); });
  }
  var rT; window.addEventListener("resize", function(){ clearTimeout(rT); rT = setTimeout(function(){ live.forEach(function(it){ it.size(); }); }, 150); });
  function loop(time){
    live.forEach(function(it){ if(it.vis && it.ready) it.sc.draw(it.mouse, time); });
    if(!reduce) requestAnimationFrame(loop);
  }
  requestAnimationFrame(loop);

  /* ---------------- reveal, counters, spotlight ---------------- */
  function countUp(el){
    var target = parseFloat(el.getAttribute("data-count")), dec = parseInt(el.getAttribute("data-dec") || "0", 10), start = null;
    (function step(ts){ if(!start) start = ts; var p = Math.min((ts - start) / 1500, 1), e = 1 - Math.pow(1 - p, 3); el.textContent = (target * e).toFixed(dec); if(p < 1) requestAnimationFrame(step); })(performance.now());
  }
  $$("[data-count]").forEach(function(el){ el.textContent = parseFloat(el.getAttribute("data-count")).toFixed(parseInt(el.getAttribute("data-dec") || "0", 10)); });
  if("IntersectionObserver" in window && !reduce){
    var io = new IntersectionObserver(function(es){
      es.forEach(function(en){
        if(!en.isIntersecting) return;
        var el = en.target; el.classList.add("in");
        $$("[data-count]", el).forEach(function(c){ if(!c.dataset.done){ c.dataset.done = 1; countUp(c); } });
        io.unobserve(el);
      });
    }, {threshold:.12, rootMargin:"0px 0px -40px 0px"});
    $$(".reveal").forEach(function(el){ var r = el.getBoundingClientRect(); if(r.top < window.innerHeight && r.bottom > 0) return; io.observe(el); });
  }
  document.addEventListener("pointermove", function(e){
    var card = e.target.closest && e.target.closest(".card"); if(!card) return;
    var r = card.getBoundingClientRect(); card.style.setProperty("--mx", (e.clientX - r.left) + "px"); card.style.setProperty("--my", (e.clientY - r.top) + "px");
  });

  /* ---------------- enquiry forms ---------------- */
  $$("form[data-enquiry]").forEach(function(form){
    var status = $(".form-status", form);
    var hashType = (location.hash || "").slice(1);
    var radio = form.querySelector('input[name="type"][data-hash="' + hashType + '"]');
    if(radio) radio.checked = true;
    function sync(){
      var sel = form.querySelector('input[name="type"]:checked'); if(!sel) return;
      $$("[data-for]", form).forEach(function(el){ el.hidden = el.getAttribute("data-for").split(" ").indexOf(sel.getAttribute("data-hash")) < 0; });
    }
    $$('input[name="type"]', form).forEach(function(r){ r.addEventListener("change", sync); }); sync();
    form.addEventListener("submit", function(e){
      e.preventDefault();
      var F = form.elements, name = (F["name"].value || "").trim(), phone = (F["phone"].value || "").trim();
      if(!name || !phone){ status.textContent = "Please add your name and phone number so we can reply."; (name ? F["phone"] : F["name"]).focus(); return; }
      var data = {}, lines = [];
      $$("input,select,textarea", form).forEach(function(el){
        if(!el.name || (el.type === "radio" && !el.checked)) return;
        var wrap = el.closest("[data-for]"); if(wrap && wrap.hidden) return;
        var v = (el.value || "").trim(); if(!v) return;
        data[el.name] = v; var lab = form.querySelector('label[for="' + el.id + '"]');
        lines.push((lab ? lab.textContent : el.name) + ": " + v);
      });
      var wa = "https://wa.me/" + S.whatsapp + "?text=" + encodeURIComponent("New website enquiry\n" + lines.join("\n"));
      function fallback(msg){ status.innerHTML = ""; status.append(msg + " "); var a = document.createElement("a"); a.href = wa; a.target = "_blank"; a.rel = "noopener"; a.textContent = "Send it to us on WhatsApp"; status.appendChild(a); }
      if(S.formEndpoint){
        status.textContent = "Sending…";
        fetch(S.formEndpoint, {method:"POST", headers:{"Content-Type":"application/json", "Accept":"application/json"}, body:JSON.stringify(data)})
          .then(function(r){ if(!r.ok) throw 0; form.reset(); sync(); status.textContent = "Thank you, " + name + ". We've received your enquiry and will reply within one working day."; })
          .catch(function(){ fallback("We couldn't send the form just now."); });
      } else fallback("Your enquiry is ready.");
    });
  });
})();
