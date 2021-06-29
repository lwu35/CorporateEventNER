<!DOCTYPE HTML>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en-US" xml:lang="en-US">
<head><title>
	Cloudflare, Inc. - Events &amp; Presentations
</title><meta content="text/html; charset=UTF-8" http-equiv="Content-type" /><meta content="RevealTrans(Duration=0,Transition=0)" http-equiv="Page-Enter" /><meta content="IE=edge,chrome=1" http-equiv="X-UA-Compatible" /><script src="/cdn-cgi/apps/head/YWukMtUa1ks7I80f82NG6UatlME.js"></script><script type="text/javascript">window.NREUM||(NREUM={});NREUM.info = {"beacon":"bam-cell.nr-data.net","errorBeacon":"bam-cell.nr-data.net","licenseKey":"4b6f7f959c","applicationID":"229922501","transactionName":"b1xWMUIDWBdWARFYX1YWdTZgTVIBUQMQXUQWWEcVSA==","queueTime":0,"applicationTime":734,"agent":"","atts":""}</script><script type="text/javascript">(window.NREUM||(NREUM={})).init={privacy:{cookies_enabled:false}};(window.NREUM||(NREUM={})).loader_config={xpid:"VQYBUlRVChACVlhbBQMCVlU=",licenseKey:"4b6f7f959c",applicationID:"229922501"};window.NREUM||(NREUM={}),__nr_require=function(t,e,n){function r(n){if(!e[n]){var i=e[n]={exports:{}};t[n][0].call(i.exports,function(e){var i=t[n][1][e];return r(i||e)},i,i.exports)}return e[n].exports}if("function"==typeof __nr_require)return __nr_require;for(var i=0;i<n.length;i++)r(n[i]);return r}({1:[function(t,e,n){function r(t){try{c.console&&console.log(t)}catch(e){}}var i,o=t("ee"),a=t(24),c={};try{i=localStorage.getItem("__nr_flags").split(","),console&&"function"==typeof console.log&&(c.console=!0,i.indexOf("dev")!==-1&&(c.dev=!0),i.indexOf("nr_dev")!==-1&&(c.nrDev=!0))}catch(s){}c.nrDev&&o.on("internal-error",function(t){r(t.stack)}),c.dev&&o.on("fn-err",function(t,e,n){r(n.stack)}),c.dev&&(r("NR AGENT IN DEVELOPMENT MODE"),r("flags: "+a(c,function(t,e){return t}).join(", ")))},{}],2:[function(t,e,n){function r(t,e,n,r,c){try{p?p-=1:i(c||new UncaughtException(t,e,n),!0)}catch(f){try{o("ierr",[f,s.now(),!0])}catch(d){}}return"function"==typeof u&&u.apply(this,a(arguments))}function UncaughtException(t,e,n){this.message=t||"Uncaught error with no additional information",this.sourceURL=e,this.line=n}function i(t,e){var n=e?null:s.now();o("err",[t,n])}var o=t("handle"),a=t(25),c=t("ee"),s=t("loader"),f=t("gos"),u=window.onerror,d=!1,l="nr@seenError",p=0;s.features.err=!0,t(1),window.onerror=r;try{throw new Error}catch(h){"stack"in h&&(t(9),t(8),"addEventListener"in window&&t(5),s.xhrWrappable&&t(10),d=!0)}c.on("fn-start",function(t,e,n){d&&(p+=1)}),c.on("fn-err",function(t,e,n){d&&!n[l]&&(f(n,l,function(){return!0}),this.thrown=!0,i(n))}),c.on("fn-end",function(){d&&!this.thrown&&p>0&&(p-=1)}),c.on("internal-error",function(t){o("ierr",[t,s.now(),!0])})},{}],3:[function(t,e,n){t("loader").features.ins=!0},{}],4:[function(t,e,n){function r(t){}if(window.performance&&window.performance.timing&&window.performance.getEntriesByType){var i=t("ee"),o=t("handle"),a=t(9),c=t(8),s="learResourceTimings",f="addEventListener",u="resourcetimingbufferfull",d="bstResource",l="resource",p="-start",h="-end",m="fn"+p,w="fn"+h,v="bstTimer",g="pushState",y=t("loader");y.features.stn=!0,t(7),"addEventListener"in window&&t(5);var x=NREUM.o.EV;i.on(m,function(t,e){var n=t[0];n instanceof x&&(this.bstStart=y.now())}),i.on(w,function(t,e){var n=t[0];n instanceof x&&o("bst",[n,e,this.bstStart,y.now()])}),a.on(m,function(t,e,n){this.bstStart=y.now(),this.bstType=n}),a.on(w,function(t,e){o(v,[e,this.bstStart,y.now(),this.bstType])}),c.on(m,function(){this.bstStart=y.now()}),c.on(w,function(t,e){o(v,[e,this.bstStart,y.now(),"requestAnimationFrame"])}),i.on(g+p,function(t){this.time=y.now(),this.startPath=location.pathname+location.hash}),i.on(g+h,function(t){o("bstHist",[location.pathname+location.hash,this.startPath,this.time])}),f in window.performance&&(window.performance["c"+s]?window.performance[f](u,function(t){o(d,[window.performance.getEntriesByType(l)]),window.performance["c"+s]()},!1):window.performance[f]("webkit"+u,function(t){o(d,[window.performance.getEntriesByType(l)]),window.performance["webkitC"+s]()},!1)),document[f]("scroll",r,{passive:!0}),document[f]("keypress",r,!1),document[f]("click",r,!1)}},{}],5:[function(t,e,n){function r(t){for(var e=t;e&&!e.hasOwnProperty(u);)e=Object.getPrototypeOf(e);e&&i(e)}function i(t){c.inPlace(t,[u,d],"-",o)}function o(t,e){return t[1]}var a=t("ee").get("events"),c=t("wrap-function")(a,!0),s=t("gos"),f=XMLHttpRequest,u="addEventListener",d="removeEventListener";e.exports=a,"getPrototypeOf"in Object?(r(document),r(window),r(f.prototype)):f.prototype.hasOwnProperty(u)&&(i(window),i(f.prototype)),a.on(u+"-start",function(t,e){var n=t[1],r=s(n,"nr@wrapped",function(){function t(){if("function"==typeof n.handleEvent)return n.handleEvent.apply(n,arguments)}var e={object:t,"function":n}[typeof n];return e?c(e,"fn-",null,e.name||"anonymous"):n});this.wrapped=t[1]=r}),a.on(d+"-start",function(t){t[1]=this.wrapped||t[1]})},{}],6:[function(t,e,n){function r(t,e,n){var r=t[e];"function"==typeof r&&(t[e]=function(){var t=o(arguments),e={};i.emit(n+"before-start",[t],e);var a;e[m]&&e[m].dt&&(a=e[m].dt);var c=r.apply(this,t);return i.emit(n+"start",[t,a],c),c.then(function(t){return i.emit(n+"end",[null,t],c),t},function(t){throw i.emit(n+"end",[t],c),t})})}var i=t("ee").get("fetch"),o=t(25),a=t(24);e.exports=i;var c=window,s="fetch-",f=s+"body-",u=["arrayBuffer","blob","json","text","formData"],d=c.Request,l=c.Response,p=c.fetch,h="prototype",m="nr@context";d&&l&&p&&(a(u,function(t,e){r(d[h],e,f),r(l[h],e,f)}),r(c,"fetch",s),i.on(s+"end",function(t,e){var n=this;if(e){var r=e.headers.get("content-length");null!==r&&(n.rxSize=r),i.emit(s+"done",[null,e],n)}else i.emit(s+"done",[t],n)}))},{}],7:[function(t,e,n){var r=t("ee").get("history"),i=t("wrap-function")(r);e.exports=r;var o=window.history&&window.history.constructor&&window.history.constructor.prototype,a=window.history;o&&o.pushState&&o.replaceState&&(a=o),i.inPlace(a,["pushState","replaceState"],"-")},{}],8:[function(t,e,n){var r=t("ee").get("raf"),i=t("wrap-function")(r),o="equestAnimationFrame";e.exports=r,i.inPlace(window,["r"+o,"mozR"+o,"webkitR"+o,"msR"+o],"raf-"),r.on("raf-start",function(t){t[0]=i(t[0],"fn-")})},{}],9:[function(t,e,n){function r(t,e,n){t[0]=a(t[0],"fn-",null,n)}function i(t,e,n){this.method=n,this.timerDuration=isNaN(t[1])?0:+t[1],t[0]=a(t[0],"fn-",this,n)}var o=t("ee").get("timer"),a=t("wrap-function")(o),c="setTimeout",s="setInterval",f="clearTimeout",u="-start",d="-";e.exports=o,a.inPlace(window,[c,"setImmediate"],c+d),a.inPlace(window,[s],s+d),a.inPlace(window,[f,"clearImmediate"],f+d),o.on(s+u,r),o.on(c+u,i)},{}],10:[function(t,e,n){function r(t,e){d.inPlace(e,["onreadystatechange"],"fn-",c)}function i(){var t=this,e=u.context(t);t.readyState>3&&!e.resolved&&(e.resolved=!0,u.emit("xhr-resolved",[],t)),d.inPlace(t,g,"fn-",c)}function o(t){y.push(t),h&&(b?b.then(a):w?w(a):(E=-E,R.data=E))}function a(){for(var t=0;t<y.length;t++)r([],y[t]);y.length&&(y=[])}function c(t,e){return e}function s(t,e){for(var n in t)e[n]=t[n];return e}t(5);var f=t("ee"),u=f.get("xhr"),d=t("wrap-function")(u),l=NREUM.o,p=l.XHR,h=l.MO,m=l.PR,w=l.SI,v="readystatechange",g=["onload","onerror","onabort","onloadstart","onloadend","onprogress","ontimeout"],y=[];e.exports=u;var x=window.XMLHttpRequest=function(t){var e=new p(t);try{u.emit("new-xhr",[e],e),e.addEventListener(v,i,!1)}catch(n){try{u.emit("internal-error",[n])}catch(r){}}return e};if(s(p,x),x.prototype=p.prototype,d.inPlace(x.prototype,["open","send"],"-xhr-",c),u.on("send-xhr-start",function(t,e){r(t,e),o(e)}),u.on("open-xhr-start",r),h){var b=m&&m.resolve();if(!w&&!m){var E=1,R=document.createTextNode(E);new h(a).observe(R,{characterData:!0})}}else f.on("fn-end",function(t){t[0]&&t[0].type===v||a()})},{}],11:[function(t,e,n){function r(t){if(!c(t))return null;var e=window.NREUM;if(!e.loader_config)return null;var n=(e.loader_config.accountID||"").toString()||null,r=(e.loader_config.agentID||"").toString()||null,f=(e.loader_config.trustKey||"").toString()||null;if(!n||!r)return null;var h=p.generateSpanId(),m=p.generateTraceId(),w=Date.now(),v={spanId:h,traceId:m,timestamp:w};return(t.sameOrigin||s(t)&&l())&&(v.traceContextParentHeader=i(h,m),v.traceContextStateHeader=o(h,w,n,r,f)),(t.sameOrigin&&!u()||!t.sameOrigin&&s(t)&&d())&&(v.newrelicHeader=a(h,m,w,n,r,f)),v}function i(t,e){return"00-"+e+"-"+t+"-01"}function o(t,e,n,r,i){var o=0,a="",c=1,s="",f="";return i+"@nr="+o+"-"+c+"-"+n+"-"+r+"-"+t+"-"+a+"-"+s+"-"+f+"-"+e}function a(t,e,n,r,i,o){var a="btoa"in window&&"function"==typeof window.btoa;if(!a)return null;var c={v:[0,1],d:{ty:"Browser",ac:r,ap:i,id:t,tr:e,ti:n}};return o&&r!==o&&(c.d.tk=o),btoa(JSON.stringify(c))}function c(t){return f()&&s(t)}function s(t){var e=!1,n={};if("init"in NREUM&&"distributed_tracing"in NREUM.init&&(n=NREUM.init.distributed_tracing),t.sameOrigin)e=!0;else if(n.allowed_origins instanceof Array)for(var r=0;r<n.allowed_origins.length;r++){var i=h(n.allowed_origins[r]);if(t.hostname===i.hostname&&t.protocol===i.protocol&&t.port===i.port){e=!0;break}}return e}function f(){return"init"in NREUM&&"distributed_tracing"in NREUM.init&&!!NREUM.init.distributed_tracing.enabled}function u(){return"init"in NREUM&&"distributed_tracing"in NREUM.init&&!!NREUM.init.distributed_tracing.exclude_newrelic_header}function d(){return"init"in NREUM&&"distributed_tracing"in NREUM.init&&NREUM.init.distributed_tracing.cors_use_newrelic_header!==!1}function l(){return"init"in NREUM&&"distributed_tracing"in NREUM.init&&!!NREUM.init.distributed_tracing.cors_use_tracecontext_headers}var p=t(21),h=t(13);e.exports={generateTracePayload:r,shouldGenerateTrace:c}},{}],12:[function(t,e,n){function r(t){var e=this.params,n=this.metrics;if(!this.ended){this.ended=!0;for(var r=0;r<l;r++)t.removeEventListener(d[r],this.listener,!1);e.aborted||(n.duration=a.now()-this.startTime,this.loadCaptureCalled||4!==t.readyState?null==e.status&&(e.status=0):o(this,t),n.cbTime=this.cbTime,u.emit("xhr-done",[t],t),c("xhr",[e,n,this.startTime]))}}function i(t,e){var n=s(e),r=t.params;r.host=n.hostname+":"+n.port,r.pathname=n.pathname,t.parsedOrigin=s(e),t.sameOrigin=t.parsedOrigin.sameOrigin}function o(t,e){t.params.status=e.status;var n=w(e,t.lastSize);if(n&&(t.metrics.rxSize=n),t.sameOrigin){var r=e.getResponseHeader("X-NewRelic-App-Data");r&&(t.params.cat=r.split(", ").pop())}t.loadCaptureCalled=!0}var a=t("loader");if(a.xhrWrappable){var c=t("handle"),s=t(13),f=t(11).generateTracePayload,u=t("ee"),d=["load","error","abort","timeout"],l=d.length,p=t("id"),h=t(17),m=t(16),w=t(14),v=window.XMLHttpRequest;a.features.xhr=!0,t(10),t(6),u.on("new-xhr",function(t){var e=this;e.totalCbs=0,e.called=0,e.cbTime=0,e.end=r,e.ended=!1,e.xhrGuids={},e.lastSize=null,e.loadCaptureCalled=!1,t.addEventListener("load",function(n){o(e,t)},!1),h&&(h>34||h<10)||window.opera||t.addEventListener("progress",function(t){e.lastSize=t.loaded},!1)}),u.on("open-xhr-start",function(t){this.params={method:t[0]},i(this,t[1]),this.metrics={}}),u.on("open-xhr-end",function(t,e){"loader_config"in NREUM&&"xpid"in NREUM.loader_config&&this.sameOrigin&&e.setRequestHeader("X-NewRelic-ID",NREUM.loader_config.xpid);var n=f(this.parsedOrigin);if(n){var r=!1;n.newrelicHeader&&(e.setRequestHeader("newrelic",n.newrelicHeader),r=!0),n.traceContextParentHeader&&(e.setRequestHeader("traceparent",n.traceContextParentHeader),n.traceContextStateHeader&&e.setRequestHeader("tracestate",n.traceContextStateHeader),r=!0),r&&(this.dt=n)}}),u.on("send-xhr-start",function(t,e){var n=this.metrics,r=t[0],i=this;if(n&&r){var o=m(r);o&&(n.txSize=o)}this.startTime=a.now(),this.listener=function(t){try{"abort"!==t.type||i.loadCaptureCalled||(i.params.aborted=!0),("load"!==t.type||i.called===i.totalCbs&&(i.onloadCalled||"function"!=typeof e.onload))&&i.end(e)}catch(n){try{u.emit("internal-error",[n])}catch(r){}}};for(var c=0;c<l;c++)e.addEventListener(d[c],this.listener,!1)}),u.on("xhr-cb-time",function(t,e,n){this.cbTime+=t,e?this.onloadCalled=!0:this.called+=1,this.called!==this.totalCbs||!this.onloadCalled&&"function"==typeof n.onload||this.end(n)}),u.on("xhr-load-added",function(t,e){var n=""+p(t)+!!e;this.xhrGuids&&!this.xhrGuids[n]&&(this.xhrGuids[n]=!0,this.totalCbs+=1)}),u.on("xhr-load-removed",function(t,e){var n=""+p(t)+!!e;this.xhrGuids&&this.xhrGuids[n]&&(delete this.xhrGuids[n],this.totalCbs-=1)}),u.on("addEventListener-end",function(t,e){e instanceof v&&"load"===t[0]&&u.emit("xhr-load-added",[t[1],t[2]],e)}),u.on("removeEventListener-end",function(t,e){e instanceof v&&"load"===t[0]&&u.emit("xhr-load-removed",[t[1],t[2]],e)}),u.on("fn-start",function(t,e,n){e instanceof v&&("onload"===n&&(this.onload=!0),("load"===(t[0]&&t[0].type)||this.onload)&&(this.xhrCbStart=a.now()))}),u.on("fn-end",function(t,e){this.xhrCbStart&&u.emit("xhr-cb-time",[a.now()-this.xhrCbStart,this.onload,e],e)}),u.on("fetch-before-start",function(t){function e(t,e){var n=!1;return e.newrelicHeader&&(t.set("newrelic",e.newrelicHeader),n=!0),e.traceContextParentHeader&&(t.set("traceparent",e.traceContextParentHeader),e.traceContextStateHeader&&t.set("tracestate",e.traceContextStateHeader),n=!0),n}var n,r=t[1]||{};"string"==typeof t[0]?n=t[0]:t[0]&&t[0].url?n=t[0].url:window.URL&&t[0]&&t[0]instanceof URL&&(n=t[0].href),n&&(this.parsedOrigin=s(n),this.sameOrigin=this.parsedOrigin.sameOrigin);var i=f(this.parsedOrigin);if(i&&(i.newrelicHeader||i.traceContextParentHeader))if("string"==typeof t[0]||window.URL&&t[0]&&t[0]instanceof URL){var o={};for(var a in r)o[a]=r[a];o.headers=new Headers(r.headers||{}),e(o.headers,i)&&(this.dt=i),t.length>1?t[1]=o:t.push(o)}else t[0]&&t[0].headers&&e(t[0].headers,i)&&(this.dt=i)})}},{}],13:[function(t,e,n){var r={};e.exports=function(t){if(t in r)return r[t];var e=document.createElement("a"),n=window.location,i={};e.href=t,i.port=e.port;var o=e.href.split("://");!i.port&&o[1]&&(i.port=o[1].split("/")[0].split("@").pop().split(":")[1]),i.port&&"0"!==i.port||(i.port="https"===o[0]?"443":"80"),i.hostname=e.hostname||n.hostname,i.pathname=e.pathname,i.protocol=o[0],"/"!==i.pathname.charAt(0)&&(i.pathname="/"+i.pathname);var a=!e.protocol||":"===e.protocol||e.protocol===n.protocol,c=e.hostname===document.domain&&e.port===n.port;return i.sameOrigin=a&&(!e.hostname||c),"/"===i.pathname&&(r[t]=i),i}},{}],14:[function(t,e,n){function r(t,e){var n=t.responseType;return"json"===n&&null!==e?e:"arraybuffer"===n||"blob"===n||"json"===n?i(t.response):"text"===n||""===n||void 0===n?i(t.responseText):void 0}var i=t(16);e.exports=r},{}],15:[function(t,e,n){function r(){}function i(t,e,n){return function(){return o(t,[f.now()].concat(c(arguments)),e?null:this,n),e?void 0:this}}var o=t("handle"),a=t(24),c=t(25),s=t("ee").get("tracer"),f=t("loader"),u=NREUM;"undefined"==typeof window.newrelic&&(newrelic=u);var d=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit","addRelease"],l="api-",p=l+"ixn-";a(d,function(t,e){u[e]=i(l+e,!0,"api")}),u.addPageAction=i(l+"addPageAction",!0),u.setCurrentRouteName=i(l+"routeName",!0),e.exports=newrelic,u.interaction=function(){return(new r).get()};var h=r.prototype={createTracer:function(t,e){var n={},r=this,i="function"==typeof e;return o(p+"tracer",[f.now(),t,n],r),function(){if(s.emit((i?"":"no-")+"fn-start",[f.now(),r,i],n),i)try{return e.apply(this,arguments)}catch(t){throw s.emit("fn-err",[arguments,this,t],n),t}finally{s.emit("fn-end",[f.now()],n)}}}};a("actionText,setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(t,e){h[e]=i(p+e)}),newrelic.noticeError=function(t,e){"string"==typeof t&&(t=new Error(t)),o("err",[t,f.now(),!1,e])}},{}],16:[function(t,e,n){e.exports=function(t){if("string"==typeof t&&t.length)return t.length;if("object"==typeof t){if("undefined"!=typeof ArrayBuffer&&t instanceof ArrayBuffer&&t.byteLength)return t.byteLength;if("undefined"!=typeof Blob&&t instanceof Blob&&t.size)return t.size;if(!("undefined"!=typeof FormData&&t instanceof FormData))try{return JSON.stringify(t).length}catch(e){return}}}},{}],17:[function(t,e,n){var r=0,i=navigator.userAgent.match(/Firefox[\/\s](\d+\.\d+)/);i&&(r=+i[1]),e.exports=r},{}],18:[function(t,e,n){function r(){return c.exists&&performance.now?Math.round(performance.now()):(o=Math.max((new Date).getTime(),o))-a}function i(){return o}var o=(new Date).getTime(),a=o,c=t(26);e.exports=r,e.exports.offset=a,e.exports.getLastTimestamp=i},{}],19:[function(t,e,n){function r(t){return!(!t||!t.protocol||"file:"===t.protocol)}e.exports=r},{}],20:[function(t,e,n){function r(t,e){var n=t.getEntries();n.forEach(function(t){"first-paint"===t.name?d("timing",["fp",Math.floor(t.startTime)]):"first-contentful-paint"===t.name&&d("timing",["fcp",Math.floor(t.startTime)])})}function i(t,e){var n=t.getEntries();n.length>0&&d("lcp",[n[n.length-1]])}function o(t){t.getEntries().forEach(function(t){t.hadRecentInput||d("cls",[t])})}function a(t){if(t instanceof h&&!w){var e=Math.round(t.timeStamp),n={type:t.type};e<=l.now()?n.fid=l.now()-e:e>l.offset&&e<=Date.now()?(e-=l.offset,n.fid=l.now()-e):e=l.now(),w=!0,d("timing",["fi",e,n])}}function c(t){d("pageHide",[l.now(),t])}if(!("init"in NREUM&&"page_view_timing"in NREUM.init&&"enabled"in NREUM.init.page_view_timing&&NREUM.init.page_view_timing.enabled===!1)){var s,f,u,d=t("handle"),l=t("loader"),p=t(23),h=NREUM.o.EV;if("PerformanceObserver"in window&&"function"==typeof window.PerformanceObserver){s=new PerformanceObserver(r);try{s.observe({entryTypes:["paint"]})}catch(m){}f=new PerformanceObserver(i);try{f.observe({entryTypes:["largest-contentful-paint"]})}catch(m){}u=new PerformanceObserver(o);try{u.observe({type:"layout-shift",buffered:!0})}catch(m){}}if("addEventListener"in document){var w=!1,v=["click","keydown","mousedown","pointerdown","touchstart"];v.forEach(function(t){document.addEventListener(t,a,!1)})}p(c)}},{}],21:[function(t,e,n){function r(){function t(){return e?15&e[n++]:16*Math.random()|0}var e=null,n=0,r=window.crypto||window.msCrypto;r&&r.getRandomValues&&(e=r.getRandomValues(new Uint8Array(31)));for(var i,o="xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx",a="",c=0;c<o.length;c++)i=o[c],"x"===i?a+=t().toString(16):"y"===i?(i=3&t()|8,a+=i.toString(16)):a+=i;return a}function i(){return a(16)}function o(){return a(32)}function a(t){function e(){return n?15&n[r++]:16*Math.random()|0}var n=null,r=0,i=window.crypto||window.msCrypto;i&&i.getRandomValues&&Uint8Array&&(n=i.getRandomValues(new Uint8Array(31)));for(var o=[],a=0;a<t;a++)o.push(e().toString(16));return o.join("")}e.exports={generateUuid:r,generateSpanId:i,generateTraceId:o}},{}],22:[function(t,e,n){function r(t,e){if(!i)return!1;if(t!==i)return!1;if(!e)return!0;if(!o)return!1;for(var n=o.split("."),r=e.split("."),a=0;a<r.length;a++)if(r[a]!==n[a])return!1;return!0}var i=null,o=null,a=/Version\/(\S+)\s+Safari/;if(navigator.userAgent){var c=navigator.userAgent,s=c.match(a);s&&c.indexOf("Chrome")===-1&&c.indexOf("Chromium")===-1&&(i="Safari",o=s[1])}e.exports={agent:i,version:o,match:r}},{}],23:[function(t,e,n){function r(t){function e(){t(a&&document[a]?document[a]:document[i]?"hidden":"visible")}"addEventListener"in document&&o&&document.addEventListener(o,e,!1)}e.exports=r;var i,o,a;"undefined"!=typeof document.hidden?(i="hidden",o="visibilitychange",a="visibilityState"):"undefined"!=typeof document.msHidden?(i="msHidden",o="msvisibilitychange"):"undefined"!=typeof document.webkitHidden&&(i="webkitHidden",o="webkitvisibilitychange",a="webkitVisibilityState")},{}],24:[function(t,e,n){function r(t,e){var n=[],r="",o=0;for(r in t)i.call(t,r)&&(n[o]=e(r,t[r]),o+=1);return n}var i=Object.prototype.hasOwnProperty;e.exports=r},{}],25:[function(t,e,n){function r(t,e,n){e||(e=0),"undefined"==typeof n&&(n=t?t.length:0);for(var r=-1,i=n-e||0,o=Array(i<0?0:i);++r<i;)o[r]=t[e+r];return o}e.exports=r},{}],26:[function(t,e,n){e.exports={exists:"undefined"!=typeof window.performance&&window.performance.timing&&"undefined"!=typeof window.performance.timing.navigationStart}},{}],ee:[function(t,e,n){function r(){}function i(t){function e(t){return t&&t instanceof r?t:t?f(t,s,a):a()}function n(n,r,i,o,a){if(a!==!1&&(a=!0),!p.aborted||o){t&&a&&t(n,r,i);for(var c=e(i),s=m(n),f=s.length,u=0;u<f;u++)s[u].apply(c,r);var l=d[y[n]];return l&&l.push([x,n,r,c]),c}}function o(t,e){g[t]=m(t).concat(e)}function h(t,e){var n=g[t];if(n)for(var r=0;r<n.length;r++)n[r]===e&&n.splice(r,1)}function m(t){return g[t]||[]}function w(t){return l[t]=l[t]||i(n)}function v(t,e){u(t,function(t,n){e=e||"feature",y[n]=e,e in d||(d[e]=[])})}var g={},y={},x={on:o,addEventListener:o,removeEventListener:h,emit:n,get:w,listeners:m,context:e,buffer:v,abort:c,aborted:!1};return x}function o(t){return f(t,s,a)}function a(){return new r}function c(){(d.api||d.feature)&&(p.aborted=!0,d=p.backlog={})}var s="nr@context",f=t("gos"),u=t(24),d={},l={},p=e.exports=i();e.exports.getOrSetContext=o,p.backlog=d},{}],gos:[function(t,e,n){function r(t,e,n){if(i.call(t,e))return t[e];var r=n();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(t,e,{value:r,writable:!0,enumerable:!1}),r}catch(o){}return t[e]=r,r}var i=Object.prototype.hasOwnProperty;e.exports=r},{}],handle:[function(t,e,n){function r(t,e,n,r){i.buffer([t],r),i.emit(t,e,n)}var i=t("ee").get("handle");e.exports=r,r.ee=i},{}],id:[function(t,e,n){function r(t){var e=typeof t;return!t||"object"!==e&&"function"!==e?-1:t===window?0:a(t,o,function(){return i++})}var i=1,o="nr@id",a=t("gos");e.exports=r},{}],loader:[function(t,e,n){function r(){if(!E++){var t=b.info=NREUM.info,e=p.getElementsByTagName("script")[0];if(setTimeout(f.abort,3e4),!(t&&t.licenseKey&&t.applicationID&&e))return f.abort();s(y,function(e,n){t[e]||(t[e]=n)});var n=a();c("mark",["onload",n+b.offset],null,"api"),c("timing",["load",n]);var r=p.createElement("script");r.src="https://"+t.agent,e.parentNode.insertBefore(r,e)}}function i(){"complete"===p.readyState&&o()}function o(){c("mark",["domContent",a()+b.offset],null,"api")}var a=t(18),c=t("handle"),s=t(24),f=t("ee"),u=t(22),d=t(19),l=window,p=l.document,h="addEventListener",m="attachEvent",w=l.XMLHttpRequest,v=w&&w.prototype;if(d(l.location)){NREUM.o={ST:setTimeout,SI:l.setImmediate,CT:clearTimeout,XHR:w,REQ:l.Request,EV:l.Event,PR:l.Promise,MO:l.MutationObserver};var g=""+location,y={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-1208.min.js"},x=w&&v&&v[h]&&!/CriOS/.test(navigator.userAgent),b=e.exports={offset:a.getLastTimestamp(),now:a,origin:g,features:{},xhrWrappable:x,userAgent:u};t(15),t(20),p[h]?(p[h]("DOMContentLoaded",o,!1),l[h]("load",r,!1)):(p[m]("onreadystatechange",i),l[m]("onload",r)),c("mark",["firstbyte",a.getLastTimestamp()],null,"api");var E=0}},{}],"wrap-function":[function(t,e,n){function r(t,e){function n(e,n,r,s,f){function nrWrapper(){var o,a,u,l;try{a=this,o=d(arguments),u="function"==typeof r?r(o,a):r||{}}catch(p){i([p,"",[o,a,s],u],t)}c(n+"start",[o,a,s],u,f);try{return l=e.apply(a,o)}catch(h){throw c(n+"err",[o,a,h],u,f),h}finally{c(n+"end",[o,a,l],u,f)}}return a(e)?e:(n||(n=""),nrWrapper[l]=e,o(e,nrWrapper,t),nrWrapper)}function r(t,e,r,i,o){r||(r="");var c,s,f,u="-"===r.charAt(0);for(f=0;f<e.length;f++)s=e[f],c=t[s],a(c)||(t[s]=n(c,u?s+r:r,i,s,o))}function c(n,r,o,a){if(!h||e){var c=h;h=!0;try{t.emit(n,r,o,e,a)}catch(s){i([s,n,r,o],t)}h=c}}return t||(t=u),n.inPlace=r,n.flag=l,n}function i(t,e){e||(e=u);try{e.emit("internal-error",t)}catch(n){}}function o(t,e,n){if(Object.defineProperty&&Object.keys)try{var r=Object.keys(t);return r.forEach(function(n){Object.defineProperty(e,n,{get:function(){return t[n]},set:function(e){return t[n]=e,e}})}),e}catch(o){i([o],n)}for(var a in t)p.call(t,a)&&(e[a]=t[a]);return e}function a(t){return!(t&&t instanceof Function&&t.apply&&!t[l])}function c(t,e){var n=e(t);return n[l]=t,o(t,n,u),n}function s(t,e,n){var r=t[e];t[e]=c(r,n)}function f(){for(var t=arguments.length,e=new Array(t),n=0;n<t;++n)e[n]=arguments[n];return e}var u=t("ee"),d=t(25),l="nr@original",p=Object.prototype.hasOwnProperty,h=!1;e.exports=r,e.exports.wrapFunction=c,e.exports.wrapInPlace=s,e.exports.argsToArray=f},{}]},{},["loader",2,12,4,3]);</script><meta content="width=device-width, initial-scale=1" name="viewport" /><meta content="8fMNXy_z40gt7o8y1XWI6l_8Xt9zdqr5ZYPxY1wJFuI" name="google-site-verification" /><!--[if lte IE 8]>
<link id="respond-proxy" rel="respond-proxy" media="screen" href="https://cloudflare.net/files/js/respond-proxy.html" />
<link id="respond-redirect" rel="respond-redirect" media="screen" href="https://cloudflare.net/js/respond.proxy.gif" />
<![endif]-->

<link type="text/css" rel="stylesheet" media="all" href="https://fonts.googleapis.com/css?family=Lato:400,700" />
<link type="image/x-icon" rel="icon" media="" href="https://cloudflare.net/files/favicon.ico" />
<link type="image/x-icon" rel="shortcut icon" media="" href="https://cloudflare.net/files/favicon.ico" />
<link rel="stylesheet" media="print" href="https://cloudflare.net/files/css/print.css" />
<link id="htmlGlobalLinkCss" type="text/css" rel="stylesheet" media="all" href="https://cloudflare.net/files/css/global.css?v=34406" /><link id="htmlClientLinkCss" type="text/css" rel="stylesheet" media="all" href="https://cloudflare.net/files/css/client.css?v=34020" /><link id="htmlLinkPrintCss" type="text/css" rel="stylesheet" media="print" href="https://cloudflare.net/files/css/print.css" /><script type="text/javascript" src="https://cloudflare.net/files/js/q4.core.1.0.8.min.js"></script>
<script type="text/javascript" src="https://cloudflare.net/files/js/q4.app.1.0.8.min.js"></script>
<script type="text/javascript" src="https://widgets.q4app.com/widgets/q4.api.1.13.3.min.js"></script>
<!--[if lte IE 8]>
<script type="text/javascript" src="https://cloudflare.net/js/respond.proxy.js"></script>
<![endif]-->

<script type="text/javascript">(function (i, s, o, g, r, a, m) {
    i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function () {
        (i[r].q = i[r].q || []).push(arguments)
    }, i[r].l = 1 * new Date(); a = s.createElement(o),
        m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m)
})(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');

(function ($) {
    function initGaTracking(isp, org) {
        isp = isp || '(not set)';
        org = org || '(not set)';
        $.each(trackingCodes, function (i, data) {
            if (data.qualifier === "Q4") {
                ga('create', data.trackingCode, 'auto'); // Q4 tracker
                ga('set', { 'dimension1': isp });
                ga('set', { 'dimension2': org });
                ga('set', 'anonymizeIp', true);
                ga('send', 'pageview', { 'page': location.pathname + location.search + location.hash }); // send pageview to Q4 tracker
            } else {
                ga('create', data.trackingCode, 'auto', { 'name': data.qualifier }); // Client tracker
                ga(data.qualifier + '.set', 'anonymizeIp', true);
                ga(data.qualifier + '.send', 'pageview', { 'page': location.pathname + location.search + location.hash }); // send pageview to Client tracker
            }
        });
    }

    var trackingCodes = [{qualifier: 'Q4', trackingCode: 'UA-147420086-3'}];
    var ipSessStorageKey = 'ipApiInfo';
    var ipJsonStringified = sessionStorage.getItem(ipSessStorageKey);

    if (ipJsonStringified) {
        try {
            var ipJsonParsed = JSON.parse(ipJsonStringified);
            initGaTracking(ipJsonParsed.isp, ipJsonParsed.org);
        } catch (e) {
            console.error('Failed to JSON parse IP API session storage data\n', e);
            initGaTracking();
        }
    } else {
        $.getJSON('https://pro.ip-api.com/json/?key=xdjZbj0ZiVVozCo&fields=isp,org')
            .done(function (ipJson) {
                sessionStorage.setItem(ipSessStorageKey, JSON.stringify(ipJson));
                initGaTracking(ipJson.isp, ipJson.org);
            })
            .fail(function () {
                initGaTracking();
            });
    }
})(jQuery);
</script></head>
<body style="margin: 0px" class="BodyBackground">
    <input type="hidden" id="__RequestVerificationToken"/>
    <!-- Google Tag Manager -->
<noscript>
    <iframe src="//www.googletagmanager.com/ns.html?id=GTM-PKQFGQB"
            height="0" width="0" style="display:none;visibility:hidden"></iframe>
</noscript>
<script>
(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
        new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
        j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
        '//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window, document, 'script', 'dataLayer', 'GTM-PKQFGQB');
</script>
<!-- End Google Tag Manager -->
    
    <div id="pageClass" class="Sectionhome PageDefault PageEventsPresentations LayoutOneColumnLayout Languageen-US">
        <div class="PageDefaultInner">
            <div id="litPageDiv" class="PageEventsampPresentations SectionEventsampPresentations ParentSection_home">
                <a name="top"></a>
                <form action="default.aspx" method="post" id="fmForm1">
<div class="aspNetHidden">
<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="" />
<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="" />
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="" />
</div>

<script type="text/javascript">
//<![CDATA[
var theForm = document.forms['fmForm1'];
if (!theForm) {
    theForm = document.fmForm1;
}
function __doPostBack(eventTarget, eventArgument) {
    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
        theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
    }
}
//]]>
</script>


<script src="/WebResource.axd?d=pynGkmcFUV13He1Qd6_TZDSH1oVlXKNmZSXd3zYZ2Gq6ERm6jivSb4ijerOGYkuGRtePZg2&amp;t=637453852754849868" type="text/javascript"></script>


<script type="text/javascript">
//<![CDATA[
function GetViewType(){ return '2'; }
function GetRevisionNumber(){ return '1'; }
function GetLanguageId(){ return '1'; }
function GetVersionNumber(){ return '5.56.0.1'; }
function GetPoweredBy(){return 'q4inc';}
function GetViewDate(){{ return ''; }}
function GetSignature(){{ return ''; }}
//]]>
</script>

<script src="/WebResource.axd?d=x2nkrMJGXkMELz33nwnakMh5buNcZ-t3T4nCU0ZQt96Kk4JDhdv7pdb3Agzis1zDln1EUlimtVH-8O9nKu6Z_e6vBso1&amp;t=637453852754849868" type="text/javascript"></script>
<script type="text/javascript">
//<![CDATA[
function WebForm_OnSubmit() {
if (typeof(ValidatorOnSubmit) == "function" && ValidatorOnSubmit() == false) return false;
return true;
}
//]]>
</script>

                    
                    <a id="lnkPostback" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;lnkPostback&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))" style="display: none"></a>
                    
<div class="layout layout--one-column">
    <div class="layout_inner">
        <div class="layout_header">
            <div class="pane pane--header grid--no-gutter">
                <div class="pane_inner"><span class='HeaderPaneDiv'><span class='HeaderPaneDiv1'><div id="_ctrl0_ctl06_divModuleContainer" class="module module-embed module-skip">
    <div class="module_container module_container--outer">
        
        <div class="module_container module_container--inner">
            <a class="module-skip_link" href="#maincontent">Skip to main content</a>
        </div>
    </div>
</div></span><span class='HeaderPaneDiv2'><div id="_ctrl0_ctl09_divModuleContainer" class="module module-embed hidden">
    <div class="module_container module_container--outer">
        
        <div class="module_container module_container--inner">
            <script type="text/javascript">
var Q4ApiKey = 'BF185719B0464B3CB809D23926182246';
</script>
        </div>
    </div>
</div></span><span class='HeaderPaneDiv3'><div id="_ctrl0_ctl12_divModuleContainer" class="module module-embed module-logo grid_col grid_col--1-of-6 grid_col--lc-1-of-2 grid_col--md-1-of-2 grid_col--sm-1-of-2">
    <div class="module_container module_container--outer">
        
        <div class="module_container module_container--inner">
            <a href="https://www.cloudflare.com/"><img src="https://cloudflare.net/files/design/logo.svg" alt="Cloudflare, Inc. Logo"></a>
        </div>
    </div>
</div></span><span class='HeaderPaneDiv4'><nav class="nav nav--main grid_col grid_col--5-of-6"><ul class="level1">
	<li class="has-children home expanded"><a href="https://cloudflare.net/home/default.aspx">Home</a><ul class="level2">
		<li><a href="https://cloudflare.net/news/default.aspx">News</a></li><li class="selected"><a href="https://cloudflare.net/events-and-presentations/default.aspx">Events & Presentations</a></li><li class="has-children"><a href="https://cloudflare.net/stock-information/default.aspx">Stock Information</a><ul class="level3">
			<li><a href="https://cloudflare.net/stock-information/Stock-Quote--Chart/default.aspx">Stock Quote & Chart</a></li><li><a href="https://cloudflare.net/stock-information/analyst-coverage/default.aspx">Analyst Coverage</a></li>
		</ul></li><li class="has-children"><a href="https://cloudflare.net/financials/sec-filings/default.aspx">Financials</a><ul class="level3">
			<li><a href="https://cloudflare.net/financials/sec-filings/default.aspx">SEC Filings</a></li><li><a href="https://cloudflare.net/financials/quarterly-results/default.aspx">Quarterly Results</a></li>
		</ul></li><li class="has-children"><a href="https://cloudflare.net/governance/governance-documents/default.aspx">Governance</a><ul class="level3">
			<li><a href="https://cloudflare.net/governance/governance-documents/default.aspx">Governance Documents</a></li><li><a href="https://cloudflare.net/governance/leadership/default.aspx">Leadership</a></li><li><a href="https://cloudflare.net/governance/board-of-directors/default.aspx">Board of Directors</a></li><li><a href="https://cloudflare.net/governance/committee-composition/default.aspx">Committee Composition</a></li>
		</ul></li><li class="has-children"><a href="https://cloudflare.net/resources/information-request-form/default.aspx">Resources</a><ul class="level3">
			<li><a href="https://cloudflare.net/resources/information-request-form/default.aspx">Information Request Form</a></li><li><a href="https://cloudflare.net/resources/investor-email-alerts/default.aspx">Investor Email Alerts</a></li>
		</ul></li>
	</ul></li>
</ul></nav></span><span class='HeaderPaneDiv5'><div id="_ctrl0_ctl18_divModuleContainer" class="module module-search" role="search">
    <div class="module_container module_container--outer">
        <h2 id="_ctrl0_ctl18_lblTitle" class="module_title"><span id="_ctrl0_ctl18_lblModuleTitle" class="ModuleTitle"><span class="sr-only">Site Search</span><span class="q4-icon_search"></span></span></h2>
        <div class="module_container module_container--inner">
            <span id="_ctrl0_ctl18_lblSearchText" class="module-search_text"></span>
            <input name="_ctrl0$ctl18$txtSearchInput" type="text" maxlength="256" id="_ctrl0_ctl18_txtSearchInput" class="module_input module-search_input" aria-label="Search query" placeholder="Search investor relations" value="" onkeypress="javascript:var key; if (window.event) { key = window.event.keyCode; } else if (e) { key = e.which; } else { return true; } if (key == 13) __doPostBack(&#39;_ctrl0$ctl18$btnSearch&#39;, &#39;&#39;); " />
            <input type="submit" name="_ctrl0$ctl18$btnSearch" value="" id="_ctrl0_ctl18_btnSearch" class="module_button module-search_button" />
            
        </div>
    </div>
</div></span><span class='HeaderPaneDiv6'><div id="_ctrl0_ctl21_divModuleContainer" class="module module-embed layout_toggle grid_col grid_col--1-of-2 grid_col--sm-1-of-2">
    <div class="module_container module_container--outer">
        
        <div class="module_container module_container--inner">
            <i class="q4-icon_menu" tabindex="0"></i>
        </div>
    </div>
</div></span></span></div>
            </div>
            <div class="pane pane--banner grid">
                <div class="pane_inner"><span class='HeaderPane2Div7'><div id="_ctrl0_ctl24_divModuleContainer" class="module module-page-title">
    <div class="module_container module_container--outer">
        <div class="module_container module_container--inner">
            <h1 class="module_title">Events & Presentations</h1>
        </div>
    </div>
</div></span></div>
            </div>
            <div class="pane pane--navigation">
                <div class="pane_inner"><span class='NavigationPaneDiv8'><nav class="nav nav--secondary"><ul class="level1">
	<li class="has-children home expanded"><a href="https://cloudflare.net/home/default.aspx">Home</a><ul class="level2">
		<li><a href="https://cloudflare.net/news/default.aspx">News</a></li><li class="selected"><a href="https://cloudflare.net/events-and-presentations/default.aspx">Events & Presentations</a></li><li class="has-children"><a href="https://cloudflare.net/stock-information/default.aspx">Stock Information</a><ul class="level3">
			<li><a href="https://cloudflare.net/stock-information/Stock-Quote--Chart/default.aspx">Stock Quote & Chart</a></li><li><a href="https://cloudflare.net/stock-information/analyst-coverage/default.aspx">Analyst Coverage</a></li>
		</ul></li><li class="has-children"><a href="https://cloudflare.net/financials/sec-filings/default.aspx">Financials</a><ul class="level3">
			<li><a href="https://cloudflare.net/financials/sec-filings/default.aspx">SEC Filings</a></li><li><a href="https://cloudflare.net/financials/quarterly-results/default.aspx">Quarterly Results</a></li>
		</ul></li><li class="has-children"><a href="https://cloudflare.net/governance/governance-documents/default.aspx">Governance</a><ul class="level3">
			<li><a href="https://cloudflare.net/governance/governance-documents/default.aspx">Governance Documents</a></li><li><a href="https://cloudflare.net/governance/leadership/default.aspx">Leadership</a></li><li><a href="https://cloudflare.net/governance/board-of-directors/default.aspx">Board of Directors</a></li><li><a href="https://cloudflare.net/governance/committee-composition/default.aspx">Committee Composition</a></li>
		</ul></li><li class="has-children"><a href="https://cloudflare.net/resources/information-request-form/default.aspx">Resources</a><ul class="level3">
			<li><a href="https://cloudflare.net/resources/information-request-form/default.aspx">Information Request Form</a></li><li><a href="https://cloudflare.net/resources/investor-email-alerts/default.aspx">Investor Email Alerts</a></li>
		</ul></li>
	</ul></li>
</ul></nav></span><span class='NavigationPaneDiv9'><div id="_ctrl0_ctl30_divModuleContainer" class="module module-search" role="search">
    <div class="module_container module_container--outer">
        
        <div class="module_container module_container--inner">
            <span id="_ctrl0_ctl30_lblSearchText" class="module-search_text"></span>
            <input name="_ctrl0$ctl30$txtSearchInput" type="text" maxlength="256" id="_ctrl0_ctl30_txtSearchInput" class="module_input module-search_input" aria-label="Search query" placeholder="Search investor relations" value="" onkeypress="javascript:var key; if (window.event) { key = window.event.keyCode; } else if (e) { key = e.which; } else { return true; } if (key == 13) __doPostBack(&#39;_ctrl0$ctl30$btnSearch&#39;, &#39;&#39;); " />
            <input type="submit" name="_ctrl0$ctl30$btnSearch" value="" id="_ctrl0_ctl30_btnSearch" class="module_button module-search_button" />
            
        </div>
    </div>
</div></span></div>
            </div>
        </div>
        <div class="layout_content" id="maincontent">
            <div class="pane pane--breadcrumb">
                <div class="pane_inner"></div>
            </div>
            <div class="pane pane--left">
                <div class="pane_inner"><span class='LeftPaneDiv'></span></div>
            </div>
            <div class="pane pane--content">
                <div class="pane_inner"><span class='ContentPaneDiv'><span class='ContentPaneDiv1'><div id="_ctrl0_ctl51_divModuleContainer" class="module module-embed module--no-padding-bottom">
    <div class="module_container module_container--outer">
        
        <div class="module_container module_container--inner">
            <div class="grid">
    <div class="grid_col grid_col--1-of-2 grid_col--lc-1-of-1 grid_col--md-1-of-1">
        <div class="module module-event module-event-calendar module--no-padding-top">
            <div class="module_rss module_rss--top module_q4-icon-links">
                <a href="/rss/Event.aspx" class="module_rss-link" target="_blank">
                    <span class="sr-only">Press Release RSS Feed (opens in new window)</span>
                </a>
            </div>
            <h2 class="module_title">Upcoming Events</h2>
            <div class="module_container module_container--content" aria-hidden="true">
                <div class="module-event-calendar_calendar-container"></div>
                <div class="module-event-calendar_event-container"></div>
            </div>
        </div>
    </div>
    <div class="grid_col grid_col--1-of-2 grid_col--lc-1-of-1 grid_col--md-1-of-1">
        <div class="module module-slideshow module--no-padding-top">
            <h2 class="module_title">Featured Presentation</h2>
            <div class="module_container module_container--content"></div>
        </div>
    </div>
</div>
<script src="//widgets.q4app.com/widgets/requireslib/clndr.1.4.7.min.js"></script>
<script src="https://widgets.q4app.com/widgets/q4.calendar.1.3.1.min.js"></script>
<script type="text/javascript" src="https://widgets.q4app.com/widgets/q4.slideshow.1.1.3.min.js"></script>
<script type="text/javascript">
    $('.module-event-calendar_calendar-container').calendar({
        usePublic: GetViewType() != "0",
        apiKey: Q4ApiKey,
        dateFormat: 'MM/DD/YYYY',
        eventSelection: 3,
        triggerEventsLoad: false,
        useMoment: true,
        eventTemplates: {
            webcast: (
                '{{#webcast}}' +
                '<div class="module_webcast"><a href="{{webcast}}" target="_blank" class="module_link module_webcast-link"><span class="module_link-text">Webcast</span><span class="sr-only">(opens in new window)</span></a></div>' +
                '{{/webcast}}'
            ),
            news: (
                '{{#pressReleases}}' +
                '<div class="module_news"><a href="{{url}}" target="_blank" class="module_link module_news-link"><span class="module_link-text">Press Release</span><span class="sr-only">(opens in new window)</span></a></div>' +
                '{{/pressReleases}}'
            ),
            docs: (
                '{{#docs.length}}' +
                '<ul class="module_attachments">' +
                '{{#docs}}' +
                '<li class="module_attachment">' +
                '<a href="{{url}}" target="_blank" class="module_link module_attachment-link {{#type}}module_link-{{type}}{{/type}}"><span class="module_link-text">{{title}}</span><span class="sr-only">(opens in new window)</span></a>' +
                '</li>' +
                '{{/docs}}' +
                '</ul>' +
                '{{/docs.length}}'
            ),
            presentations: (
                '{{#presentations}}' +
                '<div class="module_presentation"><a href="{{url}}" target="_blank" class="module_link module_presentation-link"><span class="module_link-text">Presentation</span> <span class="sr-only">(opens in new window)</span></a></div>' +
                '{{/presentations}}'
            ),
            financials: (
                '{{#financialReports}}{{#docs.length}}' +
                '<ul class="module_financials">' +
                '{{#docs}}' +
                '<li>' +
                '<a href="{{docUrl}}" target="_blank" class="module_link module_financial-link"><span class="module_link-text">{{docTitle}}</span> <span class="sr-only">(opens in new window)</span></a>' +
                '</li>' +
                '{{/docs}}' +
                '</ul>' +
                '{{/docs.length}}{{/financialReports}}'
            ),
            addToCal: (
                '<div class="module_add-to-calendar">' +
                '<span class="module_link module_add-to-calendar-reveal"><span class="module_link-text">Add to Calendar</span></span>' +
                '<ul class="module_add-to-calendar-list">' +
                '<li class="module_add-to-calendar-item module_add-to-calendar-item--apple">' +
                '{{#isPreview}}<a href="/preview/DownloadICal.aspx?id={{id}}" class="module_add-to-calendar-link">{{/isPreview}}' +
                '{{^isPreview}}<a href="/DownloadICal.aspx?id={{id}}" class="module_add-to-calendar-link">{{/isPreview}}' +
                '<i class="q4-icon_apple"></i>' +
                '<span class="module_add-to-calendar-text sr-only">Add to Apple Calendar</span>' +
                '</a>' +
                '</li>' +
                '<li class="module_add-to-calendar-item module_add-to-calendar-item--google">' +
                '{{#isPreview}}<a href="/preview/DownloadICal.aspx?id={{id}}&amp;platform=GoogleCalendar" target="_blank" class="module_add-to-calendar-link">{{/isPreview}}' +
                '{{^isPreview}}<a href="/DownloadICal.aspx?id={{id}}&amp;platform=GoogleCalendar" target="_blank" class="module_add-to-calendar-link">{{/isPreview}}' +
                '<i class="q4-icon_google"></i>' +
                '<span class="module_add-to-calendar-text sr-only">Add to Google Calendar</span>' +
                '</a>' +
                '</li>' +
                '<li class="module_add-to-calendar-item module_add-to-calendar-item--outlook">' +
                '{{#isPreview}}<a href="/preview/DownloadICal.aspx?id={{id}}" target="_blank" class="module_add-to-calendar-link">{{/isPreview}}' +
                '{{^isPreview}}<a href="/DownloadICal.aspx?id={{id}}" target="_blank" class="module_add-to-calendar-link">{{/isPreview}}' +
                '<i class="q4-icon_microsoft"></i>' +
                '<span class="module_add-to-calendar-text sr-only">Add to Microsoft Outlook</span>' +
                '</a>' +
                '</li>' +
                '<li class="module_add-to-calendar-item module_add-to-calendar-item--ics">' +
                '{{#isPreview}}<a href="/preview/DownloadICal.aspx?id={{id}}" target="_blank" class="module_add-to-calendar-link">{{/isPreview}}' +
                '{{^isPreview}}<a href="/DownloadICal.aspx?id={{id}}" target="_blank" class="module_add-to-calendar-link">{{/isPreview}}' +
                '<i class="q4-icon_calendar"></i>' +
                '<span class="module_add-to-calendar-text sr-only">Add to iCalendar</span>' +
                '</a>' +
                '</li>' +
                '</ul>' +
                '</div>'
            ),
            event: function() {
                return (
                    /* beautify preserve:start */
                '{{#items}}' +
                    '<div class="module_item list--reset" data-cls="{{clndrDateCls}}">' +
                        '<div class="module_date-time">' +
                            '<span class="module_date-text">{{{date}}} {{time}} {{timeZone}}</span>' +
                        '</div>' +
                        '<div class="module_headline"><a href="{{url}}" class="module_headline-link">{{title}}</a></div>' +
                        this.location +
                        this.speakers +
                        '<div class="module_links module_links--separator module_q4-icon-links">' +
                            '{{#id}}' + this.addToCal + '{{/id}}' +
                            this.webcast +
                            this.presentations +
                            this.news +
                            this.docs +
                            this.financials +
                        '</div>' +
                    '</div>' +
                '{{/items}}'
                /* beautify preserve:end */
                );
            }
        },
        complete: function() {

            //click today
            if ($('.module-event-calendar_day--today.module-event-calendar_day--event').length) {
                console.log('today');
                $('.module-event-calendar_day--today').trigger('click');
            } else {
                console.log('future');
                $('.module-event-calendar_day--today').nextAll('.module-event-calendar_day--event').eq(0).trigger('click');
            }
            $('.PageEventsampPresentations .module-event-calendar_event-container:contains("Oppenheimer Annual Technology Internet & Communications Conference") .module_date-text').text('08/11/2020');
            $('.PageEventsampPresentations .module-event-calendar_event-container:contains("KeyBanc Future of Technology Series") .module_date-text').text('08/18/2020');
            $('.PageEventsampPresentations .module-event-calendar_event-container:contains("Jefferies Software Conference") .module_date-text').text('09/14/2020');
            // $('.PageEventsampPresentations .module-event-calendar_event-container .module_date-time:contains("12:00 AM")').find('.module_date-text').text("12/09/2020");
        
        $('.module-event-calendar_event-container:contains("Cloudflare Investor Day")').find('.module_webcast .module_link-text').text('Register');

        },

        calendar: {
            render: function(data) {
                return Mustache.render((
                    /* beautify preserve:start */
                '<div class="module-event-calendar_controls">' +
                    '<div class="module-event-calendar_previous-month clndr-previous-button"><i class="q4-icon_chevron-left"></i></div>' +
                    '<div class="module-event-calendar_month">{{month}} {{year}}</div>' +
                    '<div class="module-event-calendar_next-month clndr-next-button"><i class="q4-icon_chevron-right"></i></div>' +
                '</div>' +
                '<div class="module-event-calendar_day-container grid--no-gutter">' +
                    '<div class="module-event-calendar_week">{{#daysOfTheWeek}}' +
                        '<div class="module-event-calendar_day module-event-calendar_day--name grid_col">{{.}}</div>' +
                    '{{/daysOfTheWeek}}</div>' +
                    '{{#days}}' +
                        '<div class="{{classes}} grid_col">' +
                            '<span>{{day}}</span>' +
                        '</div>' +
                    '{{/days}}' +
                '</div>'+
                '<div class="module-event-calendar_legend">'+
                    '<ul class="list--reset">'+
                        '<li class="module-event-calendar_legend-item module-event-calendar_legend-item--current">Current day</li>'+
                        '<li class="module-event-calendar_legend-item module-event-calendar_legend-item--scheduled">Scheduled event</li>'+
                    '</ul>'+
                '</div>'
                /* beautify preserve:end */
                ), data);
            },
            doneRendering: function() {
                // console.log('done rendering');
                // $('.module-event-calendar_day--today').ready(function() {
                //     ;
                //     $('.module-event-calendar_day--today').trigger('click');
                // });
                // $('.module-event-calendar_day--today').trigger('click');
            //   $('.module-event-calendar').addClass('active').find('.date').text(function(){
            //         return $(this).text().replace(", 12:00 AM", "");
            //     });
                //
                // $('.module-event-calendar_day').on('click', function () {
                //     var eventTime = $('.PageEventsampPresentations .module-event-calendar_event-container .module_date-time').text();
                //     console.log('eventTime', eventTime);
                // });
            },
            
        }
    });
    $('.module-slideshow .module_container--content').slideshow({
        usePublic: GetViewType() != "0",
        apiKey: Q4ApiKey,
        dateFormat: 'mm/dd/yy',
        aspectRatio: [16, 10],
        tpl: (
            /* beautify preserve:start */
        '<div class="module-slideshow_viewer">' +
            '<div class="module-slideshow_ratio">' +
                '<iframe style="position: absolute; width: 100%; height: 100%;" src=\'/files/js/pdf-js/viewer.html?file={{url}}#zoom=page-fit\' allowfullscreen webkitallowfullscreen></iframe>' +
            '</div>' +
        '</div>' +
        '<div class="module-slideshow_date">{{date}}</div>' +
        '<div class="module-slideshow_title">{{{title}}}</div>' +
        '<div class="module-slideshow_link-container module_q4-icon-links">' +
            '<a class="module_link module_link-download" href="{{url}}" target="_blank"><span class="module_link-text">Download PDF</span> <span class="sr-only">(opens in new window)</span></a>' +
        '</div>'
        /* beautify preserve:end */
        )
    });

</script>

        </div>
    </div>
</div></span><span class='ContentPaneDiv2'><div id="_ctrl0_ctl54_divModuleContainer" class="module module-embed module--no-padding-top">
    <div class="module_container module_container--outer">
        
        <div class="module_container module_container--inner">
            <div class="grid">
    <div class="grid_col grid_col--1-of-1 grid_col--lc-1-of-1 grid_col--md-1-of-1 module--no-padding-top">
        <div class="module module-event module-event-upcoming">
            <div class="module_rss module_rss--top module_q4-icon-links">
                <a href="/rss/Event.aspx" class="module_rss-link" target="_blank">
                    <span class="sr-only">Press Release RSS Feed (opens in new window)</span>
                </a>
            </div>
            <h2 class="module_title">Upcoming Events</h2>
            <div class="module_container module_container--content"></div>
        </div>
    </div>
</div>

<script>
$('.module-event-upcoming').events({
    usePublic: GetViewType() != "0",
    apiKey: Q4ApiKey,
    showAllYears: true,
    dateFormat: {
        date: 'MM/DD/YYYY',
        time: 'h:mm A'
    },
    useMoment: true,
    showPast: false,
    sortAscending:true,
    itemContainer: '.module_container--content',
    itemTemplate: (
        /* beautify preserve:start */
        '<div class="module_item">' +
            '<div class="module_date-time">' +
                '<span class="module_date-text">{{date.date}}</span> <span class="module_time-text">{{date.time}} {{timeZone}}</span>' +
            '</div>' +
            '<div class="module_headline">' +
                '<a class="module_headline-link" href="{{url}}">{{title}}</a>' +
            '</div>' +
            '{{#location}}' +
                '<div class="module_location">' +
                    '<span class="module_location-text">{{location}}</span>' +
                '</div>' +
            '{{/location}}' +
            '{{#speakers.length}}' +
                '<div class="module_speakers list--reset">' +
                    '<h4>Speaker(s):</h4>' +
                    '<ul>' +
                        '{{#speakers}}' +
                            '<li class="module_speaker">' +
                                '<i class="q4-icon_user-fill"></i> ' +
                                '{{name}}, {{position}}' +
                            '</li> ' +
                        '{{/speakers}}' +
                    '</ul>' +
                '</div>' +
            '{{/speakers.length}}' +
            '<div class="module_links module_links--columns-3 module_q4-icon-links list--reset">' +
                '{{#isFuture}}' +
                    '<div class="module_add-to-calendar">' +
                        '<span class="module_link module_add-to-calendar-reveal" tabindex="0"><span class="module_link-text">Add to Calendar</span></span>' +
                        '<ul class="module_add-to-calendar-list">' +
                            '<li class="module_add-to-calendar-item module_add-to-calendar-item--apple">' +
                                '<a href="/DownloadICal.aspx?id={{id}}" target="_blank" class="module_add-to-calendar-link">' +
                                    '<i class="q4-icon_apple"></i>' +
                                    '<span class="module_add-to-calendar-text sr-only">Add to Apple Calendar</span>' +
                                '</a>' +
                            '</li>' +
                            '<li class="module_add-to-calendar-item module_add-to-calendar-item--google">' +
                                '<a href="/DownloadICal.aspx?id={{id}}&platform=GoogleCalendar" target="_blank" class="module_add-to-calendar-link">' +
                                    '<i class="q4-icon_google"></i>' +
                                    '<span class="module_add-to-calendar-text sr-only">Add to Google Calendar</span>' +
                                '</a>' +
                             '</li>' +
                            '<li class="module_add-to-calendar-item module_add-to-calendar-item--outlook">' +
                                '<a href="/DownloadICal.aspx?id={{id}}" target="_blank" class="module_add-to-calendar-link">' +
                                    '<i class="q4-icon_microsoft"></i>' +
                                    '<span class="module_add-to-calendar-text sr-only">Add to Microsoft Outlook</span>' +
                                '</a>' +
                            '</li>' +
                            '<li class="module_add-to-calendar-item module_add-to-calendar-item--ics">' +
                                '<a href="/DownloadICal.aspx?id={{id}}" target="_blank" class="module_add-to-calendar-link">' +
                                    '<i class="q4-icon_calendar"></i>' +
                                    '<span class="module_add-to-calendar-text sr-only">Add to iCalendar</span>' +
                                '</a>' +
                            '</li>' +
                        '</ul>' +
                    '</div>' +
                '{{/isFuture}}' +
                '{{#webcast}}' +
                    '<div class="module_webcast"><a href="{{webcast}}" target="_blank" class="module_link module_webcast-link"><span class="module_link-text">Webcast</span> <span class="sr-only">(opens in new window)</span></a></div>' +
                '{{/webcast}}' +
                '{{#presentations}}' +
                    '<div class="module_presentation"><a href="{{docUrl}}" target="_blank" class="module_link module_presentation-link"><span class="module_link-text">Presentation</span> <span class="sr-only">(opens in new window)</span></a></div>' +
                '{{/presentations}}' +
                '{{#pressReleases}}' +
                    '<div class="module_news"><a href="{{url}}" target="_blank" class="module_link module_news-link"><span class="module_link-text">Press Release</span> <span class="sr-only">(opens in new window)</span></a></div>' +
                '{{/pressReleases}}' +
                '{{#docs.length}}<ul class="module_attachments">' +
                    '{{#docs}}' +
                        '<li class="module_attachment {{type}}">' +
                            '<a href="{{url}}" target="_blank" class="module_link module_attachment-link"><span class="module_link-text">{{title}}</span> <span class="sr-only">(opens in new window)</span></a>' +
                        '</li>' +
                    '{{/docs}}' +
                '</ul>{{/docs.length}}' +
                '{{#financialReports}}{{#docs.length}}' +
                    '<ul class="module_financials">' +
                        '{{#docs}}{{^duplicateWebcast}}' +
                            '<li>' +
                                '<a href="{{docUrl}}" target="_blank" class="module_link module_financial-link {{docCategory}}"><span class="module_link-text"> {{docTitle}}</span> <span class="sr-only">(opens in new window)</span></a>' +
                            '</li>' +
                        '{{/duplicateWebcast}}{{/docs}}' +
                    '</ul>' +
                '{{/docs.length}}{{/financialReports}}' +
            '</div>'+
        '</div>'
        /* beautify preserve:end */
    ),
    beforeRenderItems: function(e, tpl){
        $.each(tpl.items, function(i,item){
            if (item.date.time == "12:00 AM") {
                item.date.time = "";
                item.timeZone = "";
            }
            $.each(item.financialReports, function(j, report){
                $.each(report.docs, function(k, doc){
                    if ( doc.docCategory == 'webcast' && doc.docUrl == item.webcast ) {
                        doc.duplicateWebcast = true;
                    }
                });
            });
        });
    },
    complete: function(e){
        q4App.addToCalendar($(e.target));
        
          $('.module_item:contains("02/12/2021")').find('.module_webcast .module_link-text').text('Register');
    }
});

</script>
        </div>
    </div>
</div></span><span class='ContentPaneDiv3'><div id="_ctrl0_ctl57_divModuleContainer" class="module module-embed module-event module-event-archive background--grey">
    <div class="module_container module_container--outer">
        <h2 id="_ctrl0_ctl57_lblTitle" class="module_title"><span id="_ctrl0_ctl57_lblModuleTitle" class="ModuleTitle">Archived Events & Presentations</span></h2>
        <div class="module_container module_container--inner">
            <div class="module_container module_container--widget">
    <div class="module_options">
        <label class="module_options-label sr-only" for="eventArchiveTag">Filter by:</label>
        <select class="dropdown module_options-select" id="eventArchiveTag">
            <option value="">All</option>
            <option value="event">Events</option>
            <option value="presentation">Presentations</option>
        </select>
        <label class="module_options-label sr-only" for="eventArchiveYear">Select Year: </label>
        <select class="dropdown module_options-select" id="eventArchiveYear"></select>
    </div>
    <div class="module_container module_container--content"></div>
    <div class="module_pager"></div>
</div>

<script type="text/javascript" src="https://widgets.q4app.com/widgets/q4.pager.1.2.0.min.js"></script>
<script>
$('.module-event-archive .module_container--widget').events({
    usePublic: GetViewType() != "0",
    apiKey: Q4ApiKey,
    dateFormat: {
        date: 'MM/DD/YYYY',
        time: 'hh:mm A'
    },
    useMoment: true,
    showFuture: false,
    tagSelect: '#eventArchiveTag',
    yearSelect: '#eventArchiveYear',
    yearContainer: '#eventArchiveYear',
    yearTemplate: '<option value="{{value}}">{{year}}</option>',
    itemContainer: '.module_container--content',
    itemTemplate: (
        /* beautify preserve:start */
        '<div class="module_item"><div class="module_item-wrap background--light">' +
            '<div class="grid">'+
                '<div class="grid_col grid_col--2-of-3 grid_col--lc-1-of-1 grid_col--md-1-of-1 grid_col--am">'+
                    '<div class="module_date-time">' +
                        '<span class="module_date-text">{{date.date}}</span> <span class="module_time-text">{{date.time}} {{timeZone}}</span>' +
                    '</div>' +
                    '<div class="module_headline">' +
                        '<a class="module_headline-link" href="{{url}}">{{title}}</a>' +
                    '</div>' +
                    '{{#location}}' +
                        '<div class="module_location">' +
                            '<span class="module_location-text">{{location}}</span>' +
                        '</div>' +
                    '{{/location}}' +
                    '{{#speakers.length}}' +
                        '<div class="module_speakers list--reset">' +
                            '<h4>Speaker(s):</h4>' +
                            '<ul>' +
                                '{{#speakers}}' +
                                    '<li class="module_speaker">' +
                                        '<i class="q4-icon_user-fill"></i> ' +
                                        '{{name}}, {{position}}' +
                                    '</li> ' +
                                '{{/speakers}}' +
                            '</ul>' +
                        '</div>' +
                    '{{/speakers.length}}' +
                '</div>'+
                '<div class="grid_col grid_col--1-of-3 grid_col--lc-1-of-1 grid_col--md-1-of-1 grid_col--am">'+
                    '<div class="module_links module_links--columns module_q4-icon-links list--reset">' +
                        '{{#webcast}}' +
                            '<div class="module_webcast"><a href="{{webcast}}" target="_blank" class="module_link module_webcast-link"><span class="module_link-text">Webcast </span><span class="sr-only">(opens in new window)</span></a></div>' +
                        '{{/webcast}}' +
                        '{{#presentations}}' +
                            '<div class="module_presentation"><a href="{{docUrl}}" target="_blank" class="module_link module_presentation-link"><span class="module_link-text">Presentation</span> <span class="sr-only">(opens in new window)</span></a></div>' +
                        '{{/presentations}}' +
                        '{{#pressReleases}}' +
                            '<div class="module_news"><a href="{{url}}" target="_blank" class="module_link module_news-link"><span class="module_link-text">Press Release</span> <span class="sr-only">(opens in new window)</span></a></div>' +
                        '{{/pressReleases}}' +
                        '{{#docs.length}}<ul class="module_attachments">' +
                            '{{#docs}}' +
                                '<li class="module_attachment {{type}}">' +
                                    '<a href="{{url}}" target="_blank" class="module_link module_attachment-link"><span class="module_link-text">{{title}}</span> <span class="sr-only">(opens in new window)</span></a>' +
                                '</li>' +
                            '{{/docs}}' +
                        '</ul>{{/docs.length}}' +
                        '{{#financialReports}}{{#docs.length}}' +
                            '<ul class="module_financials">' +
                                '{{#docs}}{{^duplicateWebcast}}' +
                                    '<li>' +
                                        '<a href="{{docUrl}}" target="_blank" class="module_link module_financial-link {{docCategory}}"><span class="module_link-text"> {{docTitle}}</span> <span class="sr-only">(opens in new window)</span></a>' +
                                    '</li>' +
                                '{{/duplicateWebcast}}{{/docs}}' +
                            '</ul>' +
                        '{{/docs.length}}{{/financialReports}}' +
                    '</div>' +
                '</div>'+
            '</div>'+
        '</div></div>'
        /* beautify preserve:end */
    ),
    beforeRenderItems: function(e, tpl){
        $.each(tpl.items, function(i,item){
            if (item.date.time == "12:00 AM") {
                item.date.time = "";
                item.timeZone = "";
            }
            $.each(item.financialReports, function(j, report){
                $.each(report.docs, function(k, doc){
                    if ( doc.docCategory == 'webcast' && doc.docUrl == item.webcast ) {
                        doc.duplicateWebcast = true;
                    }
                });
            });
        });
    },
    itemsComplete: function(e){
        $(e.target).find('.module_pager').pager({
            content: $(e.target).find('.module_item'),
            perPage: 3,
            append: false,
            showFirstLast: false,
            showPrevNext: false
        });
    },
    complete:function(){
    }
});
</script>
        </div>
    </div>
</div></span></span></div>
            </div>
            <div class="pane pane--right">
                <div class="pane_inner"><span class='RightPaneDiv'></span></div>
            </div>
        </div>
        <div class="layout_footer" role="contentinfo">
            <div class="pane pane--footer grid">
                <div class="pane_inner"><span class='FooterPaneDiv'><span class='FooterPaneDiv10'><div id="_ctrl0_ctl33_divModuleContainer" class="module module-html module-contact dark grid_col grid_col--1-of-4 grid_col--lc-1-of-2 grid_col--md-1-of-1">
    <div class="module_container module_container--outer">
        <h2 id="_ctrl0_ctl33_lblTitle" class="module_title"><span id="_ctrl0_ctl33_lblModuleTitle" class="ModuleTitle">Contact Us</span></h2>
        <div class="module_container module_container--inner">
            <p>Head of Investor Relations<br>
    Jayson Noland</p>
<p>
    <a href="/cdn-cgi/l/email-protection#347d667477585b415052585546511a575b59"><i class="q4-icon_envelope-fill"></i> <span class="uppercase">Send Email</span></a>
</p>
        </div>
    </div>
</div></span><span class='FooterPaneDiv11'><div id="_ctrl0_ctl36_RightBlock" class="hidden"></div>
<div id="_ctrl0_ctl36_divModuleContainer" class="module module-links dark list--reset grid_col grid_col--1-of-4 grid_col--lc-1-of-2 grid_col--md-1-of-1">
    <div class="module_container module_container--outer">
        <h2 id="_ctrl0_ctl36_lblTitle" class="module_title"><span id="_ctrl0_ctl36_lblModuleTitle" class="ModuleTitle">Quick Links</span></h2>
        <div class="module_container module_container--inner">
            <ul id="_ctrl0_ctl36_qlList" class="module-links_list">
                
                        <li id="_ctrl0_ctl36_QuickLinkList_ctl00_liQuickLink" class="QuickLinkRow">
                            
                            
                            <a href="https://cloudflare.net/financials/sec-filings/default.aspx" id="_ctrl0_ctl36_QuickLinkList_ctl00_link" class="module-links_list-item-link" target="_self">SEC Filings</a>
                            
                        </li>
                    
                        <li id="_ctrl0_ctl36_QuickLinkList_ctl01_liQuickLink" class="QuickLinkRowAlt">
                            
                            
                            <a href="https://cloudflare.net/resources/information-request-form/default.aspx" id="_ctrl0_ctl36_QuickLinkList_ctl01_link" class="module-links_list-item-link" target="_self">Information Request Form</a>
                            
                        </li>
                    
            </ul>
        </div>
    </div>
</div></span><span class='FooterPaneDiv15'><div id="_ctrl0_ctl48_divModuleContainer" class="module module-subscribe module-subscribe--footer dark grid_col grid_col--2-of-4 grid_col--md-1-of-1">
    <div class="module_container module_container--outer">
        <h2 id="_ctrl0_ctl48_lblTitle" class="module_title">
            <span id="_ctrl0_ctl48_lblModuleTitle" class="ModuleTitle">Investor Email Alerts</span>
            <span id="_ctrl0_ctl48_lblHelpPage"></span>
        </h2>
        <div class="module_container module_container--inner">
            <div class="module_introduction">
                <span id="_ctrl0_ctl48_lblIntroText" class="IntroText"><p>To opt-in for investor email alerts, please enter your email address in the field below and select at least one alert option. After submitting your request, you will receive an activation email to the requested email address. You must click the activation link in order to complete your subscription. You can sign up for additional alert options at any time.</p><p>At Cloudflare, Inc., we promise to treat your data with respect and will not share your information with any third party. You can unsubscribe to any of the investor alerts you are subscribed to by visiting the ‘unsubscribe’ section below. If you experience any issues with this process, please contact us for further assistance.</p><p><strong>By providing your email address below, you are providing consent to Cloudflare, Inc. to send you the requested Investor Email Alert updates.</strong></p><p class="module_required-text">* Required</p></span>
            </div>
            <div id="_ctrl0_ctl48_validationsummary" class="module_error-container" style="display:none;">

</div>
            <div class="module-subscribe_table-wrap">
                <table class="module-subscribe_table module-subscribe_form">
                    
                    
                    <tr id="_ctrl0_ctl48_rowEmailAddress" class="module-subscribe_table-input module-subscribe_email">
	<td id="_ctrl0_ctl48_ctl02">
                            <label for="_ctrl0_ctl48_txtEmail" id="_ctrl0_ctl48_lblEmailAddressText">Email Address</label>
                            <span id="_ctrl0_ctl48_lblRequiredEmailAddress" class="module_required">*</span>
                            <input name="_ctrl0$ctl48$txtEmail" type="text" maxlength="128" id="_ctrl0_ctl48_txtEmail" class="module_input" placeholder="Your email" />
                            <span id="_ctrl0_ctl48_regexEmailValidator1" style="display:none;"></span>
                            <span id="_ctrl0_ctl48_reqvalEmailValidator1" style="display:none;"></span>
                        </td>
</tr>

                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                </table>
                <table id="_ctrl0_ctl48_tableMailingLists" class="module-subscribe_table module-subscribe_mailing-list">
	<tr id="_ctrl0_ctl48_rowMailingListLabel" class="module-subscribe_table-input module-subscribe_list-header">
		<td id="_ctrl0_ctl48_ctl17">
                            <label for="_ctrl0_ctl48_chkLists" id="_ctrl0_ctl48_lblMailingListsText">Investor Alert Options</label>
                            <span id="_ctrl0_ctl48_lblRequiredMailingLists" class="module_required">*</span>
                        </td>
	</tr>
	<tr id="_ctrl0_ctl48_rowMailingLists" class="module-subscribe_table-input module-subscribe_list">
		<td id="_ctrl0_ctl48_ctl18">
                            <table id="_ctrl0_ctl48_chkLists">
			<tr>
				<td><input id="_ctrl0_ctl48_chkLists_0" type="checkbox" name="_ctrl0$ctl48$chkLists$0" value="37" /><label for="_ctrl0_ctl48_chkLists_0">News</label></td>
			</tr><tr>
				<td><input id="_ctrl0_ctl48_chkLists_1" type="checkbox" name="_ctrl0$ctl48$chkLists$1" value="39" /><label for="_ctrl0_ctl48_chkLists_1">Quarterly Reports</label></td>
			</tr><tr>
				<td><input id="_ctrl0_ctl48_chkLists_2" type="checkbox" name="_ctrl0$ctl48$chkLists$2" value="40" /><label for="_ctrl0_ctl48_chkLists_2">Annual Reports</label></td>
			</tr><tr>
				<td><input id="_ctrl0_ctl48_chkLists_3" type="checkbox" name="_ctrl0$ctl48$chkLists$3" value="41" /><label for="_ctrl0_ctl48_chkLists_3">SEC Filings</label></td>
			</tr><tr>
				<td><input id="_ctrl0_ctl48_chkLists_4" type="checkbox" name="_ctrl0$ctl48$chkLists$4" value="42" /><label for="_ctrl0_ctl48_chkLists_4">End of Day Stock Quote</label></td>
			</tr>
		</table>
                            
                            <span id="_ctrl0_ctl48_cusvalMailingListsValidator" style="display:none;"></span>
                        </td>
	</tr>
</table>

                <div id="_ctrl0_ctl48_recaptcha_divModuleContainer" class="RecaptchaContainer">
    <input type="hidden" name="_ctrl0$ctl48$recaptcha$hdnCaptchaToken" id="_ctrl0_ctl48_recaptcha_hdnCaptchaToken" />

    <script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script type="text/javascript">
        function onLoad__ctrl0_ctl48_recaptcha() {
            grecaptcha.render('_ctrl0_ctl48_btnSubmit', {
                'sitekey': '6LcKf8wZAAAAADYEeFvKUvdj80FVct5G98mSJ29W',
                'callback': 'onSubmit__ctrl0_ctl48_recaptcha',
                'size': 'invisible'
            });
        }

        function onSubmit__ctrl0_ctl48_recaptcha(token) {
            var captchaTokenField = document.getElementById('_ctrl0_ctl48_recaptcha_hdnCaptchaToken');

            captchaTokenField.value = token;
            __doPostBack('_ctrl0$ctl48$btnSubmit', "");
        }
    </script>

    <script src="https://www.google.com/recaptcha/api.js?onload=onLoad__ctrl0_ctl48_recaptcha&render=explicit" async defer></script>

    <style>
        .grecaptcha-badge {
            display: none !important;
        }
    </style>
</div>
                <span id="_ctrl0_ctl48_cusvalRecaptcha" style="display:none;"></span>
                <div class="module_actions">
                    <input type="submit" name="_ctrl0$ctl48$btnSubmit" value="Submit" onclick="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;_ctrl0$ctl48$btnSubmit&quot;, &quot;&quot;, true, &quot;b7e156ab-fa69-42f5-a1db-08ae6a1b8ae2&quot;, &quot;&quot;, false, false))" id="_ctrl0_ctl48_btnSubmit" class="button module-subscribe_submit-button" />
                </div>
            </div>
        </div>
    </div>
</div>
<div id="_ctrl0_ctl48_divEditSubscriberConfirmation" class="module module-subscribe module_confirmation-container" style="DISPLAY:none;">
    <div class="module_container module_container--outer">
        <h2 class="module_title">Email Alert Sign Up Confirmation</h2>
        <div class="module_container module_container--inner">
            
        </div>
    </div>
</div>
<div id="_ctrl0_ctl48_div1" class="EditSubscriberConfirmation">
    
</div>
<style>
.EditSubscriberConfirmation {
    display: inherit;
}
.module_actions .grecaptcha-badge {
    display: block !important;
}
</style><span id="_ctrl0_ctl48_ctl19" style="display:none;"></span></span></span></div>
            </div>
            <div class="pane pane--footer2">
                <div class="pane_inner clearfix"><span class='FooterPane2Div12'><div id="_ctrl0_ctl39_divModuleContainer" class="module module-html module-footer-corporate">
    <div class="module_container module_container--outer">
        
        <div class="module_container module_container--inner">
            <div class="module_container--content">
    <div class="module_item-group">
        <ul class="module_item-list">
            <li class="module_list-header">
                Sales
                <i class="q4-icon_caret-down"></i>
            </li>
            <li class="module_list-item">
                <a href="https://www.cloudflare.com/plans/enterprise/contact/">
                    Enterprise Sales
                </a>
            </li>
            <li class="module_list-item">
                <a href="https://www.cloudflare.com/partners/">
                    Become a Partner
                </a>
            </li>
        </ul>
        <p class="module_contact">
            Contact Sales:<br><a href="tel:+442035146970">+44 20 3514 6970</a>
            <noscript><a href="tel:+16503198930">+1 650 319 8930</a></noscript>
        </p>
    </div>
    <div class="module_item-group">
        <ul class="module_item-list">
            <li class="module_list-header">
                Getting Started
                <i class="q4-icon_caret-down"></i>
            </li>
            <li class="module_list-item">
                <a href="https://www.cloudflare.com/plans/">
                    Pricing
                </a>
            </li>
            <li class="module_list-item">
                <a href="https://www.cloudflare.com/case-studies/">
                    Case Studies
                </a>
            </li>
            <li class="module_list-item">
                <a href="https://www.cloudflare.com/resources/">
                    White Papers
                </a>
            </li>
            <li class="module_list-item">
                <a href="https://www.cloudflare.com/webinars/">
                    Webinars
                </a>
            </li>
            <li class="module_list-item">
                <a href="https://www.cloudflare.com/learning/">
                    Learning Center
                </a>
            </li>
        </ul>
    </div>
    <div class="module_item-group">
        <ul class="module_item-list">
            <li class="module_list-header">
                Community
                <i class="q4-icon_caret-down"></i>
            </li>
            <li class="module_list-item">
                <a href="https://community.cloudflare.com">
                    Community Hub
                </a>
            </li>
            <li class="module_list-item">
                <a href="https://blog.cloudflare.com">
                    Blog
                </a>
            </li>
            <li class="module_list-item">
                <a href="https://www.cloudflare.com/galileo/">
                    Project Galileo
                </a>
            </li>
            <li class="module_list-item">
                <a href="https://www.cloudflare.com/athenian/">
                    Athenian Project
                </a>
            </li>
        </ul>
    </div>
    <div class="module_item-group">
        <ul class="module_item-list">
            <li class="module_list-header">
                Developers
                <i class="q4-icon_caret-down"></i>
            </li>
            <li class="module_list-item">
                <a href="https://developers.cloudflare.com">
                    Developer Hub
                </a>
            </li>
            <li class="module_list-item">
                <a href="https://www.cloudflare.com/technical-resources/">
                    Technical Resources
                </a>
            </li>
            <li class="module_list-item">
                <a href="https://www.cloudflare.com/products/cloudflare-workers/">
                    Cloudflare Workers
                </a>
            </li>
            <li class="module_list-item">
                <a href="https://www.cloudflare.com/integrations/">
                    Integrations
                </a>
            </li>
        </ul>
    </div>
    <div class="module_item-group">
        <ul class="module_item-list">
            <li class="module_list-header">
                Support
                <i class="q4-icon_caret-down"></i>
            </li>
            <li class="module_list-item">
                <a href="https://support.cloudflare.com">
                    Support
                </a>
            </li>
            <li class="module_list-item">
                <a href="https://www.cloudflarestatus.com">
                    Cloudflare Status
                </a>
            </li>
            <li class="module_list-item">
                <a href="https://www.cloudflare.com/compliance/">
                    Compliance
                </a>
            </li>
            <li class="module_list-item">
                <a href="https://www.cloudflare.com/gdpr/introduction/">
                    GDPR
                </a>
            </li>
        </ul>
    </div>
    <div class="module_item-group">
        <ul class="module_item-list">
            <li class="module_list-header">
                Company
                <i class="q4-icon_caret-down"></i>
            </li>
            <li class="module_list-item">
                <a href="https://www.cloudflare.com/about-overview/">
                    About Cloudflare
                </a>
            </li>
            <li class="module_list-item">
                <a href="https://www.cloudflare.com/people/">
                    Our Team
                </a>
            </li>
            <li class="module_list-item">
                <a href="https://www.cloudflare.com/press/">
                    Press
                </a>
            </li>
            <li class="module_list-item">
                <a href="/home/default.aspx">
                    Investor Relations
                </a>
            </li>
            <li class="module_list-item">
                <a href="https://www.cloudflare.com/analysts/">
                    Industry Analysts
                </a>
            </li>
            <li class="module_list-item">
                <a href="https://www.cloudflare.com/careers/">
                    Careers
                </a>
            </li>
            <li class="module_list-item">
                <a href="https://www.cloudflare.com/internetsummit/">
                    Internet Summit
                </a>
            </li>
            <li class="module_list-item">
                <a href="https://www.cloudflare.com/logo/">
                    Logo
                </a>
            </li>
            <li class="module_list-item">
                <a href="https://www.cloudflare.com/network/">
                    Network Map
                </a>
            </li>
        </ul>
    </div>
</div>
        </div>
    </div>
</div></span><span class='FooterPane2Div13'><div id="_ctrl0_ctl42_divModuleContainer" class="module module-html module-footer-bottom">
    <div class="module_container module_container--outer">
        
        <div class="module_container module_container--inner">
            <div class="module_container--content">
        <div class="module_footer-social">
            <a target="_blank" rel="noopener" href="https://www.facebook.com/Cloudflare/">
                <i class="q4-icon_facebook">
                    <span class="path1"></span>
                    <span class="path2"></span>
                </i>
                <span class="sr-only">(Link to Facebook)</span>
            </a>
            <a target="_blank" rel="noopener" href="https://twitter.com/Cloudflare">
                <i class="q4-icon_twitter">
                    <span class="path1"></span>
                    <span class="path2"></span>
                </i>
                <span class="sr-only">(Link to Twitter)</span>
            </a>
            <a target="_blank" rel="noopener" href="https://www.linkedin.com/company/cloudflare-inc-">
                <i class="q4-icon_linkedin">
                    <span class="path1"></span>
                    <span class="path2"></span>
                    <span class="path3"></span>
                </i>
                <span class="sr-only">(Link to Linkedin)</span>
            </a>
            <a target="_blank" rel="noopener" href="https://www.youtube.com/cloudflare">
                <i class="q4-icon_youtube">
                    <span class="path1"></span>
                    <span class="path2"></span>
                    <span class="path3"></span>
                </i>
                <span class="sr-only">(Link to Youtube)</span>
            </a>
        </div>
        <div class="module_footer-legal">
            <span class="module_footer-legal--copyright">© <span class="copyright_year"></span> Cloudflare, Inc.</span>
            <div class="module_footer-legal--links">
                <a href="https://www.cloudflare.com/privacypolicy/">Privacy Policy</a>
                <a href="https://www.cloudflare.com/website-terms/">Terms of Use</a>
                <a href="https://www.cloudflare.com/abuse/">Trust &amp; Safety</a>
                <a href="https://www.cloudflare.com/trademark/">Trademark</a>
            </div>
        </div>
    </div>
        </div>
    </div>
</div></span></div>
            </div>
            <div class="pane pane--credits">
                <div class="pane_inner"><span class='Q4FooterDiv14'><div id="_ctrl0_ctl45_divModuleContainer" class="module module-embed hidden">
    <div class="module_container module_container--outer">
        
        <div class="module_container module_container--inner">
            <script>
var q4App = $.extend(true, q4Defaults, {
    options: {
        headerOffset: $('.pane--header').outerHeight(),
        mailingListConfig: {
            submitText: 'Sign Up'
        }
    },
    fancySignup: function () {
        var inst = this,
            validationLock = true,
            signup = inst.options.mailingListSignupCls,
            $signup = $(signup),
            confirm = 'div[id*="SubscriberConfirmation"]',
            $confirm = $('div[id*="SubscriberConfirmation"]'), // jshint ignore:line
            footerSuccess = inst.options.mailingListConfig.location + ' ' + confirm + ' .module_message--success',
            $footerSuccess = $(footerSuccess);

        // Subscriber Confirmation fix
        if ($confirm.is(':visible')) {
            if ($confirm.filter(':visible').closest(inst.options.mailingListConfig.location).length) {
                var successText = $confirm.filter(':visible').closest(inst.options.mailingListConfig.location).find('.module_message--success').text();
                $confirm.filter(':visible').parent().html(inst.options.mailingListConfig.tpl).find('.module_message--success').html(successText);
            }
            inst.scrollTo($('div[id*="SubscriberConfirmation"]').filter(':visible'), 0);
            if (!$footerSuccess.length) {
                $('.module-unsubscribe,' + inst.options.mailingListConfig.hideOnConfirmation).addClass('js--hidden');
            }
        }

        if (!$signup.length) {
            return;
        }

        $signup.each(function () {
            var $this = $(this);

            // If a confirmation or error message is visible on page load, scroll to the module
            if ($this.find('input.module_input').length && $this.find('input.module_input').val().length) {
                inst.scrollTo($this, 0);
            }
            // Create a second submit button to be displayed inside fancybox. Replace input type submit with button
            var $submit = $this.find('input[type="submit"]');
            $submit.addClass('js--hidden');
            $submit[0].outerHTML = $submit[0].outerHTML.replace(/^<input/, '<button') + '<span class="button_text">' + $submit[0].value + '</span></button>';
            $this.find('.module_actions').append('<button type="submit" class="button module-subscribe_submit-button module-subscribe_submit-button--fancy"><span class="button_text">' + inst.options.mailingListConfig.submitText + '</span></button>');

            $this.on('click', '.module-subscribe_submit-button--fancy', function (e) {
                e.preventDefault();
                validationLock = false;

                var $parent = $(this).closest(signup),
                    errors = inst._mailingListValidation($parent);

                if (!errors.length) {
                    $(this).closest(signup).find('.module_actions [type="submit"]').not(this).trigger('click');
                    return false;
                } else {
                    inst.scrollTo($this.find('.module_error-container'), 0);
                }

                return false;
            });

            // Run validation on change
            $this.find('input, select').on('change', function () {
                if (!validationLock) {
                    inst._mailingListValidation($this);
                }
            });

            // Validate submit on enter
            $this.find('input[type="text"], input[type="email"]').on('keydown', function (e) {
                if (e.keyCode == 13) {
                    e.preventDefault();
                    $(this).closest(signup).find('.module_actions [type="submit"]').trigger('click');
                    return false;
                }
            });
        });
    },
    subscribeFooterText: function() {
        $(".pane--footer .module-subscribe .module_actions").append(
            '<p class="module_actions-text">By clicking Sign Up, I agree to Cloudflare\'s <a href="https://www.cloudflare.com/subscriptionagreement/" class="">terms</a>, <a href="https://www.cloudflare.com/privacypolicy/" class="">privacy policy</a>, and <a href="https://www.cloudflare.com/cookie-policy/" class="">cookie policy</a>.</p>'
        );
    },
    subscribeFooterGTM: function() {
        if($('div[id*="SubscriberConfirmation"]').filter(':visible').length > 0){
            //dataLayer.push({ "eventCategory": "Investor Alert Sign Up", "eventAction": "News; Quarterly Reports; Annual Reports"});
            dataLayer.push({ event: 'FormSubmission', 'eventCategory': 'Form', 'eventAction': '(success) - Investor Alert Sign Up'});
        }
    },
    scollingTable: function(selector) {
        $(selector).not(selector + ' table').wrap('<div class="table-wrapper" />');
    },
    meetingFancy: function($selector, trigger) {
        var bCookie = document.cookie.replace(/(?:(?:^|.*;\s*)bCookie\s*\=\s*([^;]*).*$)|^.*$/, "$1");
        if (!bCookie.length) {
            $selector.removeClass('js--hidden');
        }
        $selector.on('click', '.button--cookie', function() {
            $selector.addClass('js--hidden');
            document.cookie = 'bCookie=true; path=/';
        });

        $selector.on('click', trigger, function(e) {
            e.preventDefault();
            $.fancybox.open({
                type: 'iframe',
                src: '/request-meeting-iframe/default.aspx',
                opts: {
                    smallBtn: false,
                    margin: [10, 0],
                    slideClass: 'fancybox-slide--form',
                    parentEl: 'form'
                }
            });
        });
        window.addEventListener('message', function(event) {
            if (event.data == 'close-fancybox') {
                $.fancybox.close();
            }
        }, false);
    },
    stickyNavBar: function() {
        var inst = this,
            $window = $(window),
            $layout = $('.layout'),
            $header = $('.pane--header'),
            $nav = $('.nav--secondary'),
            $navContainer = $('.pane--navigation'),
            navContainerPos = function() {
                return $navContainer.position().top;
            };

        $window.on('scroll', function() {
            if ($window.scrollTop() > 0) {
                $layout.addClass('js--header-small');
            } else {
                $layout.removeClass('js--header-small');
            }

            if ($window.width() > 1024) {
                $navContainer.css('min-height', $nav.outerHeight());

                if ($window.scrollTop() + $header.outerHeight() >= navContainerPos()) {
                    $layout.addClass('js--sticky');
                    $nav.css('top', $header.height());
                } else {
                    $layout.removeClass('js--sticky');
                    $nav.removeAttr('style');
                }
            } else {
                $layout.removeClass('js--sticky');
                $nav.removeAttr('style');
                $navContainer.removeAttr('style');
            }
        });
        $window.on('resize', function() {
            if ($window.width() > 1024) {
                $layout.removeClass('js--sticky');
                $navContainer.removeAttr('style').css('min-height', $nav.outerHeight());
                $nav.removeAttr('style');
            } else {
                $layout.removeClass('js--sticky');
                $nav.removeAttr('style');
                $navContainer.removeAttr('style');
            }
            $window.trigger('scroll');
        }).resize();
    },
    init: function() {
        var app = this;

        app.cleanUp();
        app.submitOnEnter('.module-unsubscribe');
        app.submitOnEnter('.module-search');
        app.validateSubmit('.module-search');
        app.superfish($('.nav--main .level2'), { cssArrows: false });
        app.mobileMenuToggle($('.layout'), '.pane--navigation', '.layout_toggle i');
        app.cleanQuickLinks($('.module-links'));
        app.copyright($('.copyright_year'));
        app.docTracking();
        app.fancySignup();
        app.resetDate(['.nav a[href*="s4.q4web.com"]:not([href$=".pdf"])']);
        app.previewToolbar();
        app.reveal('.pane--header .module-search', 'h2', 'input[type="text"]', false);
        app.stickyNavBar();
        app.meetingFancy($('.module-cta'), '.button--meeting');
        app.sections();
        app.reveal('.module-footer-corporate .module_item-list', '.module_list-header', '.module_list-item');
        app.subscribeFooterText();
        app.subscribeFooterGTM();
    }
});

q4App.init();
</script>
        </div>
    </div>
</div></span></div>
            </div>
        </div>
    </div>
</div>
                    <input type="hidden" name="__antiCSRF" id="__antiCSRF" value=""/>
                
<script type="text/javascript">
//<![CDATA[
var Page_ValidationSummaries =  new Array(document.getElementById("_ctrl0_ctl48_validationsummary"));
var Page_Validators =  new Array(document.getElementById("_ctrl0_ctl48_regexEmailValidator1"), document.getElementById("_ctrl0_ctl48_reqvalEmailValidator1"), document.getElementById("_ctrl0_ctl48_cusvalMailingListsValidator"), document.getElementById("_ctrl0_ctl48_cusvalRecaptcha"), document.getElementById("_ctrl0_ctl48_ctl19"));
//]]>
</script>

<script type="text/javascript">
//<![CDATA[
var _ctrl0_ctl48_validationsummary = document.all ? document.all["_ctrl0_ctl48_validationsummary"] : document.getElementById("_ctrl0_ctl48_validationsummary");
_ctrl0_ctl48_validationsummary.headertext = "<p class=\'module_message module_message--error\'>The following errors must be corrected:</p>";
_ctrl0_ctl48_validationsummary.displaymode = "List";
_ctrl0_ctl48_validationsummary.validationGroup = "b7e156ab-fa69-42f5-a1db-08ae6a1b8ae2";
var _ctrl0_ctl48_regexEmailValidator1 = document.all ? document.all["_ctrl0_ctl48_regexEmailValidator1"] : document.getElementById("_ctrl0_ctl48_regexEmailValidator1");
_ctrl0_ctl48_regexEmailValidator1.controltovalidate = "_ctrl0_ctl48_txtEmail";
_ctrl0_ctl48_regexEmailValidator1.errormessage = "Email address is not valid.";
_ctrl0_ctl48_regexEmailValidator1.display = "None";
_ctrl0_ctl48_regexEmailValidator1.enabled = "False";
_ctrl0_ctl48_regexEmailValidator1.evaluationfunction = "RegularExpressionValidatorEvaluateIsValid";
_ctrl0_ctl48_regexEmailValidator1.validationexpression = "^([a-zA-Z0-9_\\-\\.]+)@((\\[[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.)|(([a-zA-Z0-9\\-]+\\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\\]?)$";
var _ctrl0_ctl48_reqvalEmailValidator1 = document.all ? document.all["_ctrl0_ctl48_reqvalEmailValidator1"] : document.getElementById("_ctrl0_ctl48_reqvalEmailValidator1");
_ctrl0_ctl48_reqvalEmailValidator1.controltovalidate = "_ctrl0_ctl48_txtEmail";
_ctrl0_ctl48_reqvalEmailValidator1.errormessage = "Email address is required.";
_ctrl0_ctl48_reqvalEmailValidator1.display = "None";
_ctrl0_ctl48_reqvalEmailValidator1.validationGroup = "b7e156ab-fa69-42f5-a1db-08ae6a1b8ae2";
_ctrl0_ctl48_reqvalEmailValidator1.evaluationfunction = "RequiredFieldValidatorEvaluateIsValid";
_ctrl0_ctl48_reqvalEmailValidator1.initialvalue = "";
var _ctrl0_ctl48_cusvalMailingListsValidator = document.all ? document.all["_ctrl0_ctl48_cusvalMailingListsValidator"] : document.getElementById("_ctrl0_ctl48_cusvalMailingListsValidator");
_ctrl0_ctl48_cusvalMailingListsValidator.errormessage = "Mailing list selection is required.";
_ctrl0_ctl48_cusvalMailingListsValidator.display = "None";
_ctrl0_ctl48_cusvalMailingListsValidator.validationGroup = "b7e156ab-fa69-42f5-a1db-08ae6a1b8ae2";
_ctrl0_ctl48_cusvalMailingListsValidator.evaluationfunction = "CustomValidatorEvaluateIsValid";
var _ctrl0_ctl48_cusvalRecaptcha = document.all ? document.all["_ctrl0_ctl48_cusvalRecaptcha"] : document.getElementById("_ctrl0_ctl48_cusvalRecaptcha");
_ctrl0_ctl48_cusvalRecaptcha.errormessage = "The captcha test has failed. Please try again.";
_ctrl0_ctl48_cusvalRecaptcha.display = "None";
_ctrl0_ctl48_cusvalRecaptcha.validationGroup = "b7e156ab-fa69-42f5-a1db-08ae6a1b8ae2";
_ctrl0_ctl48_cusvalRecaptcha.evaluationfunction = "CustomValidatorEvaluateIsValid";
var _ctrl0_ctl48_ctl19 = document.all ? document.all["_ctrl0_ctl48_ctl19"] : document.getElementById("_ctrl0_ctl48_ctl19");
_ctrl0_ctl48_ctl19.controltovalidate = "_ctrl0_ctl48_txtEmail";
_ctrl0_ctl48_ctl19.errormessage = "Email Address is invalid.";
_ctrl0_ctl48_ctl19.display = "None";
_ctrl0_ctl48_ctl19.validationGroup = "b7e156ab-fa69-42f5-a1db-08ae6a1b8ae2";
//]]>
</script>


<script type="text/javascript">
//<![CDATA[

var Page_ValidationActive = false;
if (typeof(ValidatorOnLoad) == "function") {
    ValidatorOnLoad();
}

function ValidatorOnSubmit() {
    if (Page_ValidationActive) {
        return ValidatorCommonOnSubmit();
    }
    else {
        return true;
    }
}
        //]]>
</script>
</form>
            </div>
        </div>
    </div>
    
    <script type="text/javascript" src="/js/anti-csrf.js">
    </script>
</body>
</html>
