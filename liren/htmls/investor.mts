<!DOCTYPE html>
<html lang="en" dir="ltr" prefix="og: https://ogp.me/ns#">
  <head>
    <meta charset="utf-8" /><script type="text/javascript">(window.NREUM||(NREUM={})).loader_config={licenseKey:"761e715901",applicationID:"39077635"};window.NREUM||(NREUM={}),__nr_require=function(e,t,n){function r(n){if(!t[n]){var i=t[n]={exports:{}};e[n][0].call(i.exports,function(t){var i=e[n][1][t];return r(i||t)},i,i.exports)}return t[n].exports}if("function"==typeof __nr_require)return __nr_require;for(var i=0;i<n.length;i++)r(n[i]);return r}({1:[function(e,t,n){function r(){}function i(e,t,n){return function(){return o(e,[u.now()].concat(c(arguments)),t?null:this,n),t?void 0:this}}var o=e("handle"),a=e(7),c=e(8),f=e("ee").get("tracer"),u=e("loader"),s=NREUM;"undefined"==typeof window.newrelic&&(newrelic=s);var d=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit","addRelease"],p="api-",l=p+"ixn-";a(d,function(e,t){s[t]=i(p+t,!0,"api")}),s.addPageAction=i(p+"addPageAction",!0),s.setCurrentRouteName=i(p+"routeName",!0),t.exports=newrelic,s.interaction=function(){return(new r).get()};var m=r.prototype={createTracer:function(e,t){var n={},r=this,i="function"==typeof t;return o(l+"tracer",[u.now(),e,n],r),function(){if(f.emit((i?"":"no-")+"fn-start",[u.now(),r,i],n),i)try{return t.apply(this,arguments)}catch(e){throw f.emit("fn-err",[arguments,this,e],n),e}finally{f.emit("fn-end",[u.now()],n)}}}};a("actionText,setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(e,t){m[t]=i(l+t)}),newrelic.noticeError=function(e,t){"string"==typeof e&&(e=new Error(e)),o("err",[e,u.now(),!1,t])}},{}],2:[function(e,t,n){function r(){return c.exists&&performance.now?Math.round(performance.now()):(o=Math.max((new Date).getTime(),o))-a}function i(){return o}var o=(new Date).getTime(),a=o,c=e(9);t.exports=r,t.exports.offset=a,t.exports.getLastTimestamp=i},{}],3:[function(e,t,n){function r(e){return!(!e||!e.protocol||"file:"===e.protocol)}t.exports=r},{}],4:[function(e,t,n){function r(e,t){var n=e.getEntries();n.forEach(function(e){"first-paint"===e.name?d("timing",["fp",Math.floor(e.startTime)]):"first-contentful-paint"===e.name&&d("timing",["fcp",Math.floor(e.startTime)])})}function i(e,t){var n=e.getEntries();n.length>0&&d("lcp",[n[n.length-1]])}function o(e){e.getEntries().forEach(function(e){e.hadRecentInput||d("cls",[e])})}function a(e){if(e instanceof m&&!g){var t=Math.round(e.timeStamp),n={type:e.type};t<=p.now()?n.fid=p.now()-t:t>p.offset&&t<=Date.now()?(t-=p.offset,n.fid=p.now()-t):t=p.now(),g=!0,d("timing",["fi",t,n])}}function c(e){d("pageHide",[p.now(),e])}if(!("init"in NREUM&&"page_view_timing"in NREUM.init&&"enabled"in NREUM.init.page_view_timing&&NREUM.init.page_view_timing.enabled===!1)){var f,u,s,d=e("handle"),p=e("loader"),l=e(6),m=NREUM.o.EV;if("PerformanceObserver"in window&&"function"==typeof window.PerformanceObserver){f=new PerformanceObserver(r);try{f.observe({entryTypes:["paint"]})}catch(v){}u=new PerformanceObserver(i);try{u.observe({entryTypes:["largest-contentful-paint"]})}catch(v){}s=new PerformanceObserver(o);try{s.observe({type:"layout-shift",buffered:!0})}catch(v){}}if("addEventListener"in document){var g=!1,w=["click","keydown","mousedown","pointerdown","touchstart"];w.forEach(function(e){document.addEventListener(e,a,!1)})}l(c)}},{}],5:[function(e,t,n){function r(e,t){if(!i)return!1;if(e!==i)return!1;if(!t)return!0;if(!o)return!1;for(var n=o.split("."),r=t.split("."),a=0;a<r.length;a++)if(r[a]!==n[a])return!1;return!0}var i=null,o=null,a=/Version\/(\S+)\s+Safari/;if(navigator.userAgent){var c=navigator.userAgent,f=c.match(a);f&&c.indexOf("Chrome")===-1&&c.indexOf("Chromium")===-1&&(i="Safari",o=f[1])}t.exports={agent:i,version:o,match:r}},{}],6:[function(e,t,n){function r(e){function t(){e(a&&document[a]?document[a]:document[i]?"hidden":"visible")}"addEventListener"in document&&o&&document.addEventListener(o,t,!1)}t.exports=r;var i,o,a;"undefined"!=typeof document.hidden?(i="hidden",o="visibilitychange",a="visibilityState"):"undefined"!=typeof document.msHidden?(i="msHidden",o="msvisibilitychange"):"undefined"!=typeof document.webkitHidden&&(i="webkitHidden",o="webkitvisibilitychange",a="webkitVisibilityState")},{}],7:[function(e,t,n){function r(e,t){var n=[],r="",o=0;for(r in e)i.call(e,r)&&(n[o]=t(r,e[r]),o+=1);return n}var i=Object.prototype.hasOwnProperty;t.exports=r},{}],8:[function(e,t,n){function r(e,t,n){t||(t=0),"undefined"==typeof n&&(n=e?e.length:0);for(var r=-1,i=n-t||0,o=Array(i<0?0:i);++r<i;)o[r]=e[t+r];return o}t.exports=r},{}],9:[function(e,t,n){t.exports={exists:"undefined"!=typeof window.performance&&window.performance.timing&&"undefined"!=typeof window.performance.timing.navigationStart}},{}],ee:[function(e,t,n){function r(){}function i(e){function t(e){return e&&e instanceof r?e:e?u(e,f,a):a()}function n(n,r,i,o,a){if(a!==!1&&(a=!0),!l.aborted||o){e&&a&&e(n,r,i);for(var c=t(i),f=v(n),u=f.length,s=0;s<u;s++)f[s].apply(c,r);var p=d[h[n]];return p&&p.push([b,n,r,c]),c}}function o(e,t){y[e]=v(e).concat(t)}function m(e,t){var n=y[e];if(n)for(var r=0;r<n.length;r++)n[r]===t&&n.splice(r,1)}function v(e){return y[e]||[]}function g(e){return p[e]=p[e]||i(n)}function w(e,t){s(e,function(e,n){t=t||"feature",h[n]=t,t in d||(d[t]=[])})}var y={},h={},b={on:o,addEventListener:o,removeEventListener:m,emit:n,get:g,listeners:v,context:t,buffer:w,abort:c,aborted:!1};return b}function o(e){return u(e,f,a)}function a(){return new r}function c(){(d.api||d.feature)&&(l.aborted=!0,d=l.backlog={})}var f="nr@context",u=e("gos"),s=e(7),d={},p={},l=t.exports=i();t.exports.getOrSetContext=o,l.backlog=d},{}],gos:[function(e,t,n){function r(e,t,n){if(i.call(e,t))return e[t];var r=n();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(e,t,{value:r,writable:!0,enumerable:!1}),r}catch(o){}return e[t]=r,r}var i=Object.prototype.hasOwnProperty;t.exports=r},{}],handle:[function(e,t,n){function r(e,t,n,r){i.buffer([e],r),i.emit(e,t,n)}var i=e("ee").get("handle");t.exports=r,r.ee=i},{}],id:[function(e,t,n){function r(e){var t=typeof e;return!e||"object"!==t&&"function"!==t?-1:e===window?0:a(e,o,function(){return i++})}var i=1,o="nr@id",a=e("gos");t.exports=r},{}],loader:[function(e,t,n){function r(){if(!E++){var e=x.info=NREUM.info,t=l.getElementsByTagName("script")[0];if(setTimeout(u.abort,3e4),!(e&&e.licenseKey&&e.applicationID&&t))return u.abort();f(h,function(t,n){e[t]||(e[t]=n)});var n=a();c("mark",["onload",n+x.offset],null,"api"),c("timing",["load",n]);var r=l.createElement("script");r.src="https://"+e.agent,t.parentNode.insertBefore(r,t)}}function i(){"complete"===l.readyState&&o()}function o(){c("mark",["domContent",a()+x.offset],null,"api")}var a=e(2),c=e("handle"),f=e(7),u=e("ee"),s=e(5),d=e(3),p=window,l=p.document,m="addEventListener",v="attachEvent",g=p.XMLHttpRequest,w=g&&g.prototype;if(d(p.location)){NREUM.o={ST:setTimeout,SI:p.setImmediate,CT:clearTimeout,XHR:g,REQ:p.Request,EV:p.Event,PR:p.Promise,MO:p.MutationObserver};var y=""+location,h={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-1208.min.js"},b=g&&w&&w[m]&&!/CriOS/.test(navigator.userAgent),x=t.exports={offset:a.getLastTimestamp(),now:a,origin:y,features:{},xhrWrappable:b,userAgent:s};e(1),e(4),l[m]?(l[m]("DOMContentLoaded",o,!1),p[m]("load",r,!1)):(l[v]("onreadystatechange",i),p[v]("onload",r)),c("mark",["firstbyte",a.getLastTimestamp()],null,"api");var E=0}},{}],"wrap-function":[function(e,t,n){function r(e,t){function n(t,n,r,f,u){function nrWrapper(){var o,a,s,p;try{a=this,o=d(arguments),s="function"==typeof r?r(o,a):r||{}}catch(l){i([l,"",[o,a,f],s],e)}c(n+"start",[o,a,f],s,u);try{return p=t.apply(a,o)}catch(m){throw c(n+"err",[o,a,m],s,u),m}finally{c(n+"end",[o,a,p],s,u)}}return a(t)?t:(n||(n=""),nrWrapper[p]=t,o(t,nrWrapper,e),nrWrapper)}function r(e,t,r,i,o){r||(r="");var c,f,u,s="-"===r.charAt(0);for(u=0;u<t.length;u++)f=t[u],c=e[f],a(c)||(e[f]=n(c,s?f+r:r,i,f,o))}function c(n,r,o,a){if(!m||t){var c=m;m=!0;try{e.emit(n,r,o,t,a)}catch(f){i([f,n,r,o],e)}m=c}}return e||(e=s),n.inPlace=r,n.flag=p,n}function i(e,t){t||(t=s);try{t.emit("internal-error",e)}catch(n){}}function o(e,t,n){if(Object.defineProperty&&Object.keys)try{var r=Object.keys(e);return r.forEach(function(n){Object.defineProperty(t,n,{get:function(){return e[n]},set:function(t){return e[n]=t,t}})}),t}catch(o){i([o],n)}for(var a in e)l.call(e,a)&&(t[a]=e[a]);return t}function a(e){return!(e&&e instanceof Function&&e.apply&&!e[p])}function c(e,t){var n=t(e);return n[p]=e,o(e,n,s),n}function f(e,t,n){var r=e[t];e[t]=c(r,n)}function u(){for(var e=arguments.length,t=new Array(e),n=0;n<e;++n)t[n]=arguments[n];return t}var s=e("ee"),d=e(8),p="nr@original",l=Object.prototype.hasOwnProperty,m=!1;t.exports=r,t.exports.wrapFunction=c,t.exports.wrapInPlace=f,t.exports.argsToArray=u},{}]},{},["loader"]);</script>
<meta property="og:site_name" content="MTS Systems Corporation" />
<meta property="og:type" content="website" />
<meta property="og:title" content="Presentations | MTS Systems Corporation" />
<meta name="referrer" content="no-referrer" />
<meta name="Generator" content="Drupal 8 (https://www.drupal.org)" />
<meta name="MobileOptimized" content="width" />
<meta name="HandheldFriendly" content="true" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<link rel="shortcut icon" href="/sites/g/files/knoqqb53126/files/favicon_0_0.ico" type="image/vnd.microsoft.icon" />
<link rel="alternate" hreflang="en" href="https://investor.mts.com/events-and-presentations/presentations" />
<link rel="canonical" href="https://investor.mts.com/events-and-presentations/presentations" />
<link rel="shortlink" href="https://investor.mts.com/node/5831" />
<link rel="revision" href="https://investor.mts.com/events-and-presentations/presentations" />

    <title>Presentations | Investor Relations | MTS Systems Corporation</title>
    <link rel="stylesheet" media="all" href="/sites/g/files/knoqqb53126/files/css/css_rfjm6CJ_0NMC2yDcg2-ndYMEx1qfufTwwHO3KArx5Oc.css" />
<link rel="stylesheet" media="all" href="/sites/g/files/knoqqb53126/files/css/css_rn4huHxaUT3n9ohKfKrBRJ0o3IRFkU_UzNtSAEqRwyU.css" />
<link rel="stylesheet" media="all" href="//maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" />
<link rel="stylesheet" media="all" href="//pro.fontawesome.com/releases/v5.12.0/css/all.css" />
<link rel="stylesheet" media="all" href="/sites/g/files/knoqqb53126/files/css/css_b7cmOV4hM3bp_OMzgtQUOWBOKi1_QfYm4I2aFcxUQhA.css" />
<link rel="stylesheet" media="print" href="/sites/g/files/knoqqb53126/files/css/css_e0y_SzBy7MVJj-XFkPuY2Z-XJWINvqZL9IAXUkPGGQA.css" />
<link rel="stylesheet" media="all" href="/sites/g/files/knoqqb53126/files/css/css_qLuPmFlMcxpHL3VKttWDc6WzBmUZd9ShhdXf572_MDQ.css" />
<link rel="stylesheet" media="all" href="//fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;700&amp;display=swap" />
<link rel="stylesheet" media="all" href="/sites/g/files/knoqqb53126/files/css/css_BDvbTtwMdb2zClIMO-gimAxN39r1nwyOFCOtI0-iJSg.css" />

    
<!--[if lte IE 8]>
<script src="/sites/g/files/knoqqb53126/files/js/js_VtafjXmRvoUgAzqzYTA3Wrjkx9wcWhjP0G4ZnnqRamA.js"></script>
<![endif]-->
<script src="/core/assets/vendor/modernizr/modernizr.min.js?v=3.3.1"></script>

    <script type="text/javascript">
piAId = '806953';
piCId = '9285';
piHostname = 'pi.pardot.com';
 
(function() {
                function async_load(){
                                var s = document.createElement('script'); s.type = 'text/javascript';
                                s.src = ('https:' == document.location.protocol ? 'https://pi' : 'http://cdn') + '.pardot.com/pd.js';
                                var c = document.getElementsByTagName('script')[0]; c.parentNode.insertBefore(s, c);
                }
                if(window.attachEvent) { window.attachEvent('onload', async_load); }
                else { window.addEventListener('load', async_load, false); }
})();
</script>

<script type="text/javascript"> 
 var _gaq = _gaq || [];
 _gaq.push(['_setAccount', 'UA-1236542-1']);
 _gaq.push(['_trackPageview']);
 _gaq.push(['_trackPageLoadTime']);
 (function() {
   var ga = document.createElement('script'); ga.type =
'text/javascript'; ga.async = true;
   ga.src = ('https:' == document.location.protocol ? 'https://ssl' :
'http://www') + '.google-analytics.com/ga.js';
   var s = document.getElementsByTagName('script')[0];
s.parentNode.insertBefore(ga, s);
 })();
</script>
  </head>
  <body class="body-sidebars-first nir-node nir-node--type-nir-landing-page nir-node--5831 path-node page-node-type-nir-landing-page">
    <div id="skip">
      <a class="visually-hidden focusable skip-link" href="#main-menu">
        Skip to main navigation
      </a>
    </div>
    
      <div class="dialog-off-canvas-main-canvas" data-off-canvas-main-canvas>
    
<header role="banner">
    <div class="top-bar sticky is-at-top is-stuck">
        <div class="row">
            <div class="top-bar-left"> <a href="http://www.mts.com/"><img src="/sites/g/files/knoqqb53126/themes/site/nir_pid326/dist/images/logo.png" alt="logo" width="65" height="38"></a> </div>
            <div class="top-bar-right">
                <div class="title-bar hide-for-large" data-hide-for="large">
                    <div >
                        <button class="menu-icon" type="button" aria-label="Open Search" ></button>
                    </div>
                </div>
                <div class="" id="main-menu">
                    <div class="top-bar-search">
                        <a class="nonblock nontext clearfix shared_content" id="u1773109-5" href="https://test.mts.com/en?utm_medium=referral&amp;utm_source=mts-com&amp;utm_campaign=onsite-search&amp;utm_content=prod-svc-link" data-content-guid="u1773109-5_content"><!-- content -->
                            <p id="u1773109-3">
                                <span id="u1773109">Search</span>
                                <span id="u1773109-2"> Test &amp; Simulation Products and Services</span>
                            </p>
                        </a>
                        <a class="nonblock nontext clip_frame shared_content" id="u1773110" href="https://test.mts.com/en?utm_medium=referral&amp;utm_source=mts-com&amp;utm_campaign=onsite-search&amp;utm_content=prod-svc-link" data-content-guid="u1773110_content"><!-- image -->
                            <img class="block" id="u1773110_img" alt="" width="16" height="16" src="/sites/g/files/knoqqb53126/themes/site/nir_pid326/dist/images/mag.png">
                            <img class="block" id="u1773255_img" alt="" width="16" height="16" src="/sites/g/files/knoqqb53126/themes/site/nir_pid326/dist/images/magwht.png">
                        </a>
                    </div>
                                            

                        
                                <ul class="menu vertical large-horizontal expanded large-text-center" data-responsive-menu="accordion large-dropdown" data-multi-open="false">
                                    
          

          
                              <li class="has-submenu">
                                                  <a href="https://www.mts.com/home/index.html">Business</a>
                                                        <ul class="submenu menu vertical" data-submenu>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="https://www.mts.com/home/index.html">MTS Home</a>
                                      </li>
                                    
          

          
                    <li class="spacer side-menu__item">
                              <a href="">Test</a>
                                      </li>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="https://test.mts.com/">Test &amp; Simulation</a>
                                      </li>
                                    
          

          
                    <li class="child side-menu__item">
                              <a href="https://test.mts.com/services/overview">Services</a>
                                      </li>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="https://www.e2mtechnologies.eu/">E2M Technologies</a>
                                      </li>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="https://www.rd-as.com/">R&amp;D Group</a>
                                      </li>
                                    
          

          
                    <li class="spacer side-menu__item">
                              <a href="">Sensors</a>
                                      </li>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="http://www.mtssensors.com/">Temposonics</a>
                                      </li>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="https://www.pcb.com/">PCB Peizotronics</a>
                                      </li>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="https://endevco.com/">Endevco</a>
                                      </li>
                              </ul>
            
  
                  </li>
                                    
          

          
                              <li class="has-submenu">
                                                  <a href="https://www.mts.com/home/careers.html">Careers</a>
                                                        <ul class="submenu menu vertical" data-submenu>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="https://www.mts.com/home/careers.html">Careers Home</a>
                                      </li>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="https://www.mts.com/home/benefits.html">Benefits</a>
                                      </li>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="https://jobs.mts.com/?utm_source=careersite">Job Search</a>
                                      </li>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="https://www.mts.com/home/students.html">Internship</a>
                                      </li>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="https://www.mts.com/home/culture.html">Culture</a>
                                      </li>
                              </ul>
            
  
                  </li>
                                    
          

          
                              <li class="active-trail has-submenu">
                                                  <a href="/">Investor Relations</a>
                                                        <ul class="submenu menu vertical" data-submenu>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="/">Investor Home</a>
                                      </li>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="/stock-information/stock-quote">Stock Information</a>
                                      </li>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="/press-releases">Press Release Archive</a>
                                      </li>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="https://www.mts.com/home/leadership.html">Corporate Governance</a>
                                      </li>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="/financial-information/sec-filings">Financial Information</a>
                                      </li>
                                    
          

          
                    <li class="active-trail side-menu__item">
                              <a href="/events-and-presentations/presentations">Events &amp; Presentations</a>
                                      </li>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="/shareholder-services/investor-faqs">Shareholder Services</a>
                                      </li>
                              </ul>
            
  
                  </li>
                                    
          

          
                              <li class="has-submenu">
                                                  <a href="https://www.mts.com/home/sustainability.html">Sustainability</a>
                                                        <ul class="submenu menu vertical" data-submenu>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="https://www.mts.com/home/sustainability.html">Sustainability Home</a>
                                      </li>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="https://www.mts.com/home/environment.html">Environment</a>
                                      </li>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="https://www.mts.com/home/social.html">Social</a>
                                      </li>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="https://www.mts.com/home/governance.html">Governance</a>
                                      </li>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="https://www.mts.com/home/solutions.html">Solutions</a>
                                      </li>
                              </ul>
            
  
                  </li>
                                    
          

          
                              <li class="has-submenu">
                                                  <a href="https://www.mts.com/home/suppliers.html">Suppliers</a>
                                                        <ul class="submenu menu vertical" data-submenu>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="https://www.mts.com/home/products_services.html">Product &amp; Services</a>
                                      </li>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="https://www.mts.com/home/suppliers.html">Supplier Home</a>
                                      </li>
                              </ul>
            
  
                  </li>
                                    
          

          
                              <li class="has-submenu">
                                                  <a href="https://www.mts.com/home/about.html">About MTS</a>
                                                        <ul class="submenu menu vertical" data-submenu>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="https://www.mts.com/home/about.html">About Home</a>
                                      </li>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="https://www.mts.com/home/history.html">History Timeline</a>
                                      </li>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="https://www.mts.com/home/culture.html">Culture</a>
                                      </li>
                                    
          

          
                    <li class="side-menu__item">
                              <a href="https://www.mts.com/home/leadership.html">Corporate Governance</a>
                                      </li>
                              </ul>
            
  
                  </li>
                                </ul>
            
  

    
    
                    
                </div>
            </div>
        </div>
    </div>
</header>
<div role="main">
            <div class="banner interior" id="skip-to-content">
                    </div>
        <div class="reveal ndq-modal-reveal" id="presentationModal" data-reveal>
        <h2>2018 Investor Presentation</h2>
        <embed width="100%" height="100%" name="plugin" id="plugin" src="https://iesholdingsinc.gcs-web.com/static-files/dcbd5815-6458-404a-a792-03af10b0a88f" type="application/pdf" internalinstanceid="18">
            <button class="close-button" data-close aria-label="Close modal" type="button"><span aria-hidden="true">&times;</span></button>
    </div>
    <div id="ndq-content" class="mobile-only headline">
        <div class="row">
            <div class="column large-12">
                <h1 class="main-heading">
                                            Presentations
                                    </h1>
            </div>
        </div>
    </div>

              <div class="region region-hero-banner-below">
    

<nav role="navigation" aria-labelledby="block-eventspresentations-menu" id="block-eventspresentations" class="block--system-menu-blockevents-presentations block--system-menu-blockevents-presentations--5831 block--hero-banner-below--system-menu-block--events-presentations block--hero-banner-below--system-menu-block--events-presentations--5831 block--7b957b7c-939d-45ea-b302-1f00974bc115 block--7b957b7c-939d-45ea-b302-1f00974bc115--5831 block block-menu navigation block-system-menublock menu--events-presentations">
                        
    <h2 class="visually-hidden" id="block-eventspresentations-menu">Events &amp; Presentations</h2>
    

                              <ul data-block-uuid="7b957b7c-939d-45ea-b302-1f00974bc115" class="menu side-menu">
                  <li class="side-menu__item">
          <a href="/events-and-presentations/calendar" target="" rel="" data-drupal-link-system-path="node/10906">Investor Calendar</a>
                  </li>
              <li class="side-menu__item">
          <a href="/events-and-presentations/presentations" target="" rel="" data-drupal-link-system-path="node/5831" class="is-active">Presentations</a>
                  </li>
              <li class="side-menu__item">
          <a href="/events-and-presentations/transcripts" target="" rel="" data-drupal-link-system-path="node/13811">Transcripts</a>
                  </li>
          </ul>
  


    </nav>

  </div>

    
    <div id="ndq-content" class="ndq-5831">
            <div class="row desktop-only">
                <div class="column large-12">
                    <h1 class="main-heading">
                                                    Presentations
                                            </h1>
                </div>
            </div>
                                   <div class="region region-content">
    <div data-drupal-messages-fallback class="hidden"></div>
<div id="block-nir-pid326-content" class="block--system-main-block block--system-main-block--5831 block--content--system-main-block block--content--system-main-block--5831 block--501a9747-b354-4abd-9b4f-6d35e2fb2829 block--501a9747-b354-4abd-9b4f-6d35e2fb2829--5831 block block-system block-system-main-block">
  
    
      <article class="node node--type-nir_landing_page node--view-mode-full clearfix">
  
      <h1>
              Presentations
          </h1>
    

  <div>
    
<div class="panel-display boxton clearfix " >

  <div class="container-fluid">
    <div class="row">
      <div class="column medium-12 radix-layouts-content">
        <div class="panel-panel-inner">
          <div class="block-region-contentmain"><div class="block--nir-events__widget block--nir-events__widget--5831 block--contentmain--nir-events__widget block--contentmain--nir-events__widget--5831 block--6aa2c675-20df-4008-ae52-21ec0340f4d0 block--6aa2c675-20df-4008-ae52-21ec0340f4d0--5831 block block-nir-events block-nir-events__widget">
  
    
      <div class="nir-widget">
    <div class="nir-widget--content">
        <div class="nir-widget--list">
              
<article role="article" class="clearfix node node--nir-event--nir-widget-list node--type-nir-event node--view-mode-nir-widget-list">

  
      <div class="nir-widget--field nir-widgets--event--title">
      
<div class="field-nir-event-title">
      <div class="field__item"><a href="/events/event-details/q4-2020-mts-systems-earnings-conference-call" hreflang="en">Q4 2020 MTS Systems Earnings Conference Call</a></div>
  </div>
    </div>
  
      <div class="nir-widget--field nir-widget--event--date">
      <div class="">
      
      
            Dec 15, 2020 at 10:00 AM EST
      </div>  

    </div>
  
  
  
  
  
  
  
    <div class="nir-widget--field nir-widget--event--group nir-widget--event--group--live-telco">

          <div class="nir-widget--event--section-title nir-widget--event--section-title--live-telco">
        <label>Live Teleconference Information</label>
      </div>
    
    
  <div class="field field--name-field-nir-event-live-prim field--type-telephone field--label-inline">
    <div class="field__label">Primary # - </div>
              <div class="field__item"><a href="tel:800-367-2403">800-367-2403</a></div>
          </div>

    
  <div class="field field--name-field-nir-event-live-sec field--type-telephone field--label-inline">
    <div class="field__label">Secondary # - </div>
              <div class="field__item"><a href="tel:1-334-777-6978">1-334- 777-6978</a></div>
          </div>

    

<div class="field field--name-field-nir-event-live-pass field--type-string field--label-inline">
  <div class="field__label">Passcode - </div>
        <div class="field__item">7354821</div>
    </div>

    
    

  </div>
  
  
  
  
</article>

          </div>
    <div class="nir-widget--pager">
      
    </div>
    <div class="nir-widget--total-results">
      
    </div>
  </div>
</div>
  </div>
<div class="block--table2 block--nir-assets__widget block--nir-assets__widget--5831 block--contentmain--nir-assets__widget block--contentmain--nir-assets__widget--5831 block--352dec6b-8b61-4cf0-a78f-cfffbab6372f block--352dec6b-8b61-4cf0-a78f-cfffbab6372f--5831 block block-nir-assets block-nir-assets__widget">
  
    
      <div class="wpb_raw_code wpb_content_element wpb_raw_html">
  <div class="wpb_wrapper">
        <div class="nir-widget--content">
            <div class="nir-widget--list">
                <table class="nirtable collapse-table">
            <thead>
              <tr>
                <th width="15%">Date</th>
                <th width="85%">Title</th>
              </tr>
            </thead>
            <tbody>
              
<tr>

  <td>
      <div class="nir-widget--field nir-widget--asset--date">
      
<div class="field-nir-asset-date">
      <div class="field__item">Dec 09, 2020</div>
  </div>
    </div>
    </td>

  <td>
  
      <div class="nir-widget--field nir-widgets--asset--title">
      <span class="nir-widget--asset--title--title">
<div class="field-nir-asset-title">
      <div class="file file--mime-application-pdf file--application-pdf field__item"><a href="https://investor.mts.com/static-files/7b7abbbf-669e-4710-b332-319af4646516" type="application/pdf">Amphenol to Acquire MTS</a></div>
  </div></span>
      <span class="nir-widget--asset--title-file-size"></span>
    </div>
  
  
  
  
  
  </td>

  <td>
    </td>

</tr>

<tr>

  <td>
      <div class="nir-widget--field nir-widget--asset--date">
      
<div class="field-nir-asset-date">
      <div class="field__item">Sep 24, 2020</div>
  </div>
    </div>
    </td>

  <td>
  
      <div class="nir-widget--field nir-widgets--asset--title">
      <span class="nir-widget--asset--title--title">
<div class="field-nir-asset-title">
      <div class="file file--mime-application-pdf file--application-pdf field__item"><a href="https://investor.mts.com/static-files/ff3e9cbb-a701-44f8-8f8f-e5ad007e0018" type="application/pdf">Sidoti Fall Conference Presentation</a></div>
  </div></span>
      <span class="nir-widget--asset--title-file-size"></span>
    </div>
  
  
  
  
  
  </td>

  <td>
    </td>

</tr>

<tr>

  <td>
      <div class="nir-widget--field nir-widget--asset--date">
      
<div class="field-nir-asset-date">
      <div class="field__item">Aug 04, 2020</div>
  </div>
    </div>
    </td>

  <td>
  
      <div class="nir-widget--field nir-widgets--asset--title">
      <span class="nir-widget--asset--title--title">
<div class="field-nir-asset-title">
      <div class="file file--mime-application-pdf file--application-pdf field__item"><a href="https://investor.mts.com/static-files/3dc081b1-7720-4aeb-863f-b6b385dfe6f7" type="application/pdf">Investor Relations Presentation</a></div>
  </div></span>
      <span class="nir-widget--asset--title-file-size"></span>
    </div>
  
  
  
  
  
  </td>

  <td>
    </td>

</tr>

<tr>

  <td>
      <div class="nir-widget--field nir-widget--asset--date">
      
<div class="field-nir-asset-date">
      <div class="field__item">Sep 04, 2019</div>
  </div>
    </div>
    </td>

  <td>
  
      <div class="nir-widget--field nir-widgets--asset--title">
      <span class="nir-widget--asset--title--title">
<div class="field-nir-asset-title">
      <div class="file file--mime-application-pdf file--application-pdf field__item"><a href="https://investor.mts.com/static-files/83750216-2ce2-4e6b-858d-6a88c0c2f710" type="application/pdf">Analyst Day Presentation</a></div>
  </div></span>
      <span class="nir-widget--asset--title-file-size"></span>
    </div>
  
  
  
  
  
  </td>

  <td>
    </td>

</tr>

<tr>

  <td>
      <div class="nir-widget--field nir-widget--asset--date">
      
<div class="field-nir-asset-date">
      <div class="field__item">Sep 04, 2019</div>
  </div>
    </div>
    </td>

  <td>
  
      <div class="nir-widget--field nir-widgets--asset--title">
      <span class="nir-widget--asset--title--title">
<div class="field-nir-asset-title">
      <div class="file file--mime-video-mp4 file--video field__item"><a href="https://investor.mts.com/static-files/9033b2ee-e525-4de0-bbc3-3e731035af1e" type="video/mp4">Test Video</a></div>
  </div></span>
      <span class="nir-widget--asset--title-file-size"></span>
    </div>
  
  
  
  
  
  </td>

  <td>
    </td>

</tr>

<tr>

  <td>
      <div class="nir-widget--field nir-widget--asset--date">
      
<div class="field-nir-asset-date">
      <div class="field__item">Sep 04, 2019</div>
  </div>
    </div>
    </td>

  <td>
  
      <div class="nir-widget--field nir-widgets--asset--title">
      <span class="nir-widget--asset--title--title">
<div class="field-nir-asset-title">
      <div class="file file--mime-video-mp4 file--video field__item"><a href="https://investor.mts.com/static-files/0ca0d053-607a-4858-94c8-2a43ce19e8b4" type="video/mp4">Opening Video</a></div>
  </div></span>
      <span class="nir-widget--asset--title-file-size"></span>
    </div>
  
  
  
  
  
  </td>

  <td>
    </td>

</tr>

<tr>

  <td>
      <div class="nir-widget--field nir-widget--asset--date">
      
<div class="field-nir-asset-date">
      <div class="field__item">Sep 04, 2019</div>
  </div>
    </div>
    </td>

  <td>
  
      <div class="nir-widget--field nir-widgets--asset--title">
      <span class="nir-widget--asset--title--title">
<div class="field-nir-asset-title">
      <div class="file file--mime-video-mp4 file--video field__item"><a href="https://investor.mts.com/static-files/7e8580ed-4bb4-4b8a-a107-050e6fc4cef7" type="video/mp4">Sensors Video </a></div>
  </div></span>
      <span class="nir-widget--asset--title-file-size"></span>
    </div>
  
  
  
  
  
  </td>

  <td>
    </td>

</tr>

            </tbody>
          </table>
              </div>
      <div class="nir-widget--pager">
        
      </div>
      <div class="nir-widget--total-results">
        
      </div>
    </div>
  </div>
</div>
  </div>
</div>
        </div>
      </div>
    </div>
  </div>

</div><!-- /.boxton -->

  </div>
</article>

  </div>

  </div>

                        </div>


    <!-- row wrap-->
        
</div>
<!-- role main -->

<footer role="contentinfo">
    <div class="column primary footer-blue">
        <div class="row">
            <div class="medium-12 columns">
                <div class="mobile-footer-menu">
                                              <div class="region region-nav-footer-mobile">
    

<nav role="navigation" aria-labelledby="block-footermobilenavigation-menu" id="block-footermobilenavigation" class="block--system-menu-blockfooter-mobile-navigation block--system-menu-blockfooter-mobile-navigation--5876 block--nav-footer-mobile--system-menu-block--footer-mobile-navigation block--nav-footer-mobile--system-menu-block--footer-mobile-navigation--5876 block--ea4c916f-e62b-4a8f-baac-30f1e70899df block--ea4c916f-e62b-4a8f-baac-30f1e70899df--5876 block block-menu navigation block-system-menublock menu--footer-mobile-navigation">
                        
    <h2 class="visually-hidden" id="block-footermobilenavigation-menu">Footer mobile navigation</h2>
    

                              <ul class="footer-mobile-nav">
                  <li class="corporate">
          <a href="" target="" rel="">Corporate</a>
                                              <ul>
                  <li class="careers">
          <a href="https://www.mts.com/home/careers.html" target="" rel="">Careers</a>
                                  <li class="investor-relations">
          <a href="/" target="" rel="" class="active" data-drupal-link-system-path="&lt;front&gt;">Investor Relations</a>
                                  <li class="sustainability">
          <a href="https://www.mts.com/home/sustainability.html" target="" rel="">Sustainability</a>
                                  <li class="suppliers">
          <a href="https://www.mts.com/home/suppliers.html" target="" rel="">Suppliers</a>
                              </ul>
  
                        <li class="mts-sensors">
          <a href="" target="" rel="">MTS Sensors</a>
                                              <ul>
                  <li class="temposonics">
          <a href="http://www.mtssensors.com/" target="" rel="">Temposonics</a>
                                  <li class="pcb-peizotronics">
          <a href="https://www.pcb.com/" target="" rel="">PCB Peizotronics</a>
                                  <li class="endevco">
          <a href="https://endevco.com/" target="" rel="">Endevco</a>
                                  <li class="about-mts">
          <a href="https://www.mts.com/home/about.html" target="" rel="" class="about">About MTS</a>
                              </ul>
  
                        <li class="mts-test">
          <a href="" target="" rel="">MTS Test</a>
                                              <ul>
                  <li class="test--simulation">
          <a href="https://test.mts.com/" target="" rel="">Test &amp; Simulation</a>
                                  <li class="e2m-technologies">
          <a href="https://www.e2mtechnologies.eu/" target="" rel="">E2M Technologies</a>
                                  <li class="rd-group">
          <a href="https://www.rd-as.com/" target="" rel="">R&amp;D Group</a>
                              </ul>
  
                        <li class="contact">
          <a href="" target="" rel="" class="contact">Contact:</a>
                      <p>14000 Technology Drvie</p>
            <p>Eden Prairie, MN 55344</p>
            <p>info@mts.com</p>
            <p>952.937.4000</p>
                              </ul>
  


    </nav>

  </div>

                                    </div>
                <ul class="mobile-footer-menu-button">
                    <li><button>MENU</button></li>
                </ul>
                                      <div class="region region-nav-footer">
    

<nav role="navigation" aria-labelledby="block-footernavigation-menu" id="block-footernavigation" class="block--system-menu-blockmain block--system-menu-blockmain--5876 block--nav-footer--system-menu-block--main block--nav-footer--system-menu-block--main--5876 block--5e257e0a-5d74-401c-b317-c315808c618b block--5e257e0a-5d74-401c-b317-c315808c618b--5876 block block-menu navigation block-system-menublock menu--main">
                        
    <h2 class="visually-hidden" id="block-footernavigation-menu">Footer navigation</h2>
    

                              <ul class="click-nav">
                  <li class="with-sub">
          <a href="">TEST ></a>
                                    <ul class="sub">
                  <li >
          <a href="https://test.mts.com/">Test &amp; Simulation </a>
                  </li>
              <li >
          <a href="https://www.e2mtechnologies.eu/">E2M Technologies </a>
                  </li>
              <li >
          <a href="https://www.rd-as.com/">R&amp;D Group </a>
                  </li>
          </ul>
  
                  </li>
              <li class="with-sub">
          <a href="">Sensors ></a>
                                    <ul class="sub">
                  <li >
          <a href="http://www.mtssensors.com/">Temposonics </a>
                  </li>
              <li >
          <a href="https://www.pcb.com/">PBC Piezotronics </a>
                  </li>
              <li >
          <a href="https://endevco.com/">Endevco </a>
                  </li>
          </ul>
  
                  </li>
              <li class="with-sub">
          <a href="">Corporate ></a>
                                    <ul class="sub">
                  <li >
          <a href="http://www.mts.com/">Home </a>
                  </li>
              <li >
          <a href="https://www.mts.com/home/careers.html">Careers </a>
                  </li>
              <li >
          <a href="/index.php/">Investor Relations </a>
                  </li>
              <li >
          <a href="https://www.mts.com/home/sustainability.html">Sustainability </a>
                  </li>
              <li >
          <a href="https://www.mts.com/home/suppliers.html">Suppliers </a>
                  </li>
          </ul>
  
                  </li>
              <li class="with-sub">
          <a href="">About MTS ></a>
                                    <ul class="sub">
                  <li >
          <a href="https://www.mts.com/home/about.html">About Home </a>
                  </li>
              <li >
          <a href="https://www.mts.com/home/history.html">History Timeline </a>
                  </li>
              <li >
          <a href="https://www.mts.com/home/culture.html">Culture </a>
                  </li>
              <li >
          <a href="https://www.mts.com/home/leadership.html">Corporate Governance </a>
                  </li>
          </ul>
  
                  </li>
              <li class="with-sub">
          <a href="">Contact ></a>
                                    <ul class="sub">
                  <li >
          <a href="">MTS Headquarters  14000 Technology Dr. Eden Prairie, MN </a>
                  </li>
              <li >
          <a href="">952.937.4000 </a>
                  </li>
              <li >
          <a href="mailto:info@mts.com">info@mts.com </a>
                  </li>
          </ul>
  
                  </li>
          </ul>
  


    </nav>


<nav role="navigation" aria-labelledby="block-social-menu" id="block-social" class="block--system-menu-blocksocial block--system-menu-blocksocial--5816 block--nav-footer--system-menu-block--social block--nav-footer--system-menu-block--social--5816 block--8f4ebf59-61ee-494a-8b1b-c601a4d36527 block--8f4ebf59-61ee-494a-8b1b-c601a4d36527--5816 block block-menu navigation block-system-menublock menu--social">
                        
    <h2 class="visually-hidden" id="block-social-menu">Social</h2>
    

                              <ul class="social-nav">
                  <li class="facebook">
          <a href="http://www.facebook.com/mtssystemscorp/" target="" rel="">facebook</a>
                  </li>
              <li class="youtube">
          <a href="https://www.youtube.com/channel/UCBZqUHA2vnZmsIwwavVGN3A" target="" rel="">youtube</a>
                  </li>
              <li class="instagram">
          <a href="http://www.instagram.com/mtssystemscorporation/?hl=en" target="" rel="">instagram</a>
                  </li>
              <li class="linkedin">
          <a href="http://www.linkedin.com/company/214560/" target="" rel="">linkedin</a>
                  </li>
              <li class="twitter">
          <a href="http://twitter.com/MTSSystemsCorp" target="" rel="">twitter</a>
                  </li>
          </ul>
  


    </nav>

  </div>

                            </div>
        </div>
    </div>
    <div class="column primary footer-global">
        <div class="row">
            <div class="medium-12 columns">
                                      <div class="region region-nav-utility">
    <div id="block-gbfooterinfo" class="block-content--nir-global-block block-content--nir-global-block--13766 block--block-content8b67b645-332b-414d-bf4d-58868bbd2c9c block--block-content8b67b645-332b-414d-bf4d-58868bbd2c9c--5831 block--nav-utility--block-content--8b67b645-332b-414d-bf4d-58868bbd2c9c block--nav-utility--block-content--8b67b645-332b-414d-bf4d-58868bbd2c9c--5831 block--927a89f5-7259-4c57-8f97-746279ada7fc block--927a89f5-7259-4c57-8f97-746279ada7fc--5831 block block-block-content block-block-content8b67b645-332b-414d-bf4d-58868bbd2c9c">
  
    
      
            <div class="field field--name-field-nir-global-block-node field--type-entity-reference field--label-hidden field__item">  
            <div class="clearfix text-formatted field field--name-field-nir-global-block-body field--type-text-long field--label-hidden field__item">MTS Company Headquarters | 14000 Technology Drive | Eden Prairie, MN 55433 | 952.937.4000</div>
      
</div>
      
  </div>

  </div>

                                <ul class="menu text-center">
                    <li class="menu-text">&#169; 2004 - 2021 MTS Systems Corporation. All Rights Reserved.</li>
                    <li class="menu-text"><a href="http://www.mts.com/corpdocs/privacyPolicy.pdf">Privacy Policy</a></li>
                    <li class="menu-text"><a href="http://www.mts.com/corpdocs/terms.pdf">MTS.com Terms &amp; Conditions</a></li>
                </ul>
            </div>
        </div>
    </div>
</footer>
  </div>

    
          <script type="text/javascript">var s_CCSWebHostingAccount = "trcgclientweb3265";</script>
        <script type="application/json" data-drupal-selector="drupal-settings-json">{"path":{"baseUrl":"\/","scriptPath":null,"pathPrefix":"","currentPath":"node\/5831","currentPathIsAdmin":false,"isFront":false,"currentLanguage":"en"},"pluralDelimiter":"\u0003","suppressDeprecationErrors":true,"ajaxPageState":{"libraries":"classy\/node,core\/html5shiv,nir_analytics\/nir_analytics.adobe_launch,nir_analytics\/nir_analytics.adobe_prod,nir_base\/nir_icons,nir_base\/nir_toolbar,nir_ckeditor_datatables\/datatables,nir_multimedia\/nir_multimedia,nir_pid326\/override,radix_layouts\/radix_layouts,system\/base","theme":"nir_pid326","theme_token":null},"ajaxTrustedUrl":[],"user":{"uid":0,"permissionsHash":"06c5fbcbff88cd76d09cbe90f3f0c2d3de84d8e3680b3d4bc584bac711192d81"}}</script>
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<script src="//maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
<script src="/sites/g/files/knoqqb53126/files/js/js_RJuXWMHS4P4TD7sjIJms224t0Ubho_FDpqCXaVZBOZg.js"></script>
<script src="//assets.adobedtm.com/898335afd880/c52ee8aa1e90/launch-5ef258dce664.min.js" async></script>

    
  <script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"beacon":"bam-cell.nr-data.net","licenseKey":"761e715901","applicationID":"39077635,24276188","transactionName":"ZlVXYRcAW0ZRW0QKX18fYEcMTlxbVF1ITUBZQA==","queueTime":0,"applicationTime":128,"atts":"ShJUF18aSEg=","errorBeacon":"bam-cell.nr-data.net","agent":""}</script></body>
</html>
