<!DOCTYPE HTML>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en-CA" xml:lang="en-CA">
<head><title>
	Juniper Networks - Investor Relations - Events
</title><meta content="text/html; charset=UTF-8" http-equiv="Content-type" /><meta content="RevealTrans(Duration=0,Transition=0)" http-equiv="Page-Enter" /><meta content="IE=edge,chrome=1" http-equiv="X-UA-Compatible" /><script type="text/javascript">window.NREUM||(NREUM={});NREUM.info = {"beacon":"bam-cell.nr-data.net","errorBeacon":"bam-cell.nr-data.net","licenseKey":"4b6f7f959c","applicationID":"229922501","transactionName":"b1xWMUIDWBdWARFYX1YWdTZgTVIBUQMQXUQWWEcVSA==","queueTime":0,"applicationTime":642,"agent":"","atts":""}</script><script type="text/javascript">(window.NREUM||(NREUM={})).init={privacy:{cookies_enabled:false}};(window.NREUM||(NREUM={})).loader_config={xpid:"VQYBUlRVChACVlhbBQMCVlU=",licenseKey:"4b6f7f959c",applicationID:"229922501"};window.NREUM||(NREUM={}),__nr_require=function(t,e,n){function r(n){if(!e[n]){var i=e[n]={exports:{}};t[n][0].call(i.exports,function(e){var i=t[n][1][e];return r(i||e)},i,i.exports)}return e[n].exports}if("function"==typeof __nr_require)return __nr_require;for(var i=0;i<n.length;i++)r(n[i]);return r}({1:[function(t,e,n){function r(t){try{c.console&&console.log(t)}catch(e){}}var i,o=t("ee"),a=t(24),c={};try{i=localStorage.getItem("__nr_flags").split(","),console&&"function"==typeof console.log&&(c.console=!0,i.indexOf("dev")!==-1&&(c.dev=!0),i.indexOf("nr_dev")!==-1&&(c.nrDev=!0))}catch(s){}c.nrDev&&o.on("internal-error",function(t){r(t.stack)}),c.dev&&o.on("fn-err",function(t,e,n){r(n.stack)}),c.dev&&(r("NR AGENT IN DEVELOPMENT MODE"),r("flags: "+a(c,function(t,e){return t}).join(", ")))},{}],2:[function(t,e,n){function r(t,e,n,r,c){try{p?p-=1:i(c||new UncaughtException(t,e,n),!0)}catch(f){try{o("ierr",[f,s.now(),!0])}catch(d){}}return"function"==typeof u&&u.apply(this,a(arguments))}function UncaughtException(t,e,n){this.message=t||"Uncaught error with no additional information",this.sourceURL=e,this.line=n}function i(t,e){var n=e?null:s.now();o("err",[t,n])}var o=t("handle"),a=t(25),c=t("ee"),s=t("loader"),f=t("gos"),u=window.onerror,d=!1,l="nr@seenError",p=0;s.features.err=!0,t(1),window.onerror=r;try{throw new Error}catch(h){"stack"in h&&(t(9),t(8),"addEventListener"in window&&t(5),s.xhrWrappable&&t(10),d=!0)}c.on("fn-start",function(t,e,n){d&&(p+=1)}),c.on("fn-err",function(t,e,n){d&&!n[l]&&(f(n,l,function(){return!0}),this.thrown=!0,i(n))}),c.on("fn-end",function(){d&&!this.thrown&&p>0&&(p-=1)}),c.on("internal-error",function(t){o("ierr",[t,s.now(),!0])})},{}],3:[function(t,e,n){t("loader").features.ins=!0},{}],4:[function(t,e,n){function r(t){}if(window.performance&&window.performance.timing&&window.performance.getEntriesByType){var i=t("ee"),o=t("handle"),a=t(9),c=t(8),s="learResourceTimings",f="addEventListener",u="resourcetimingbufferfull",d="bstResource",l="resource",p="-start",h="-end",m="fn"+p,w="fn"+h,v="bstTimer",g="pushState",y=t("loader");y.features.stn=!0,t(7),"addEventListener"in window&&t(5);var x=NREUM.o.EV;i.on(m,function(t,e){var n=t[0];n instanceof x&&(this.bstStart=y.now())}),i.on(w,function(t,e){var n=t[0];n instanceof x&&o("bst",[n,e,this.bstStart,y.now()])}),a.on(m,function(t,e,n){this.bstStart=y.now(),this.bstType=n}),a.on(w,function(t,e){o(v,[e,this.bstStart,y.now(),this.bstType])}),c.on(m,function(){this.bstStart=y.now()}),c.on(w,function(t,e){o(v,[e,this.bstStart,y.now(),"requestAnimationFrame"])}),i.on(g+p,function(t){this.time=y.now(),this.startPath=location.pathname+location.hash}),i.on(g+h,function(t){o("bstHist",[location.pathname+location.hash,this.startPath,this.time])}),f in window.performance&&(window.performance["c"+s]?window.performance[f](u,function(t){o(d,[window.performance.getEntriesByType(l)]),window.performance["c"+s]()},!1):window.performance[f]("webkit"+u,function(t){o(d,[window.performance.getEntriesByType(l)]),window.performance["webkitC"+s]()},!1)),document[f]("scroll",r,{passive:!0}),document[f]("keypress",r,!1),document[f]("click",r,!1)}},{}],5:[function(t,e,n){function r(t){for(var e=t;e&&!e.hasOwnProperty(u);)e=Object.getPrototypeOf(e);e&&i(e)}function i(t){c.inPlace(t,[u,d],"-",o)}function o(t,e){return t[1]}var a=t("ee").get("events"),c=t("wrap-function")(a,!0),s=t("gos"),f=XMLHttpRequest,u="addEventListener",d="removeEventListener";e.exports=a,"getPrototypeOf"in Object?(r(document),r(window),r(f.prototype)):f.prototype.hasOwnProperty(u)&&(i(window),i(f.prototype)),a.on(u+"-start",function(t,e){var n=t[1],r=s(n,"nr@wrapped",function(){function t(){if("function"==typeof n.handleEvent)return n.handleEvent.apply(n,arguments)}var e={object:t,"function":n}[typeof n];return e?c(e,"fn-",null,e.name||"anonymous"):n});this.wrapped=t[1]=r}),a.on(d+"-start",function(t){t[1]=this.wrapped||t[1]})},{}],6:[function(t,e,n){function r(t,e,n){var r=t[e];"function"==typeof r&&(t[e]=function(){var t=o(arguments),e={};i.emit(n+"before-start",[t],e);var a;e[m]&&e[m].dt&&(a=e[m].dt);var c=r.apply(this,t);return i.emit(n+"start",[t,a],c),c.then(function(t){return i.emit(n+"end",[null,t],c),t},function(t){throw i.emit(n+"end",[t],c),t})})}var i=t("ee").get("fetch"),o=t(25),a=t(24);e.exports=i;var c=window,s="fetch-",f=s+"body-",u=["arrayBuffer","blob","json","text","formData"],d=c.Request,l=c.Response,p=c.fetch,h="prototype",m="nr@context";d&&l&&p&&(a(u,function(t,e){r(d[h],e,f),r(l[h],e,f)}),r(c,"fetch",s),i.on(s+"end",function(t,e){var n=this;if(e){var r=e.headers.get("content-length");null!==r&&(n.rxSize=r),i.emit(s+"done",[null,e],n)}else i.emit(s+"done",[t],n)}))},{}],7:[function(t,e,n){var r=t("ee").get("history"),i=t("wrap-function")(r);e.exports=r;var o=window.history&&window.history.constructor&&window.history.constructor.prototype,a=window.history;o&&o.pushState&&o.replaceState&&(a=o),i.inPlace(a,["pushState","replaceState"],"-")},{}],8:[function(t,e,n){var r=t("ee").get("raf"),i=t("wrap-function")(r),o="equestAnimationFrame";e.exports=r,i.inPlace(window,["r"+o,"mozR"+o,"webkitR"+o,"msR"+o],"raf-"),r.on("raf-start",function(t){t[0]=i(t[0],"fn-")})},{}],9:[function(t,e,n){function r(t,e,n){t[0]=a(t[0],"fn-",null,n)}function i(t,e,n){this.method=n,this.timerDuration=isNaN(t[1])?0:+t[1],t[0]=a(t[0],"fn-",this,n)}var o=t("ee").get("timer"),a=t("wrap-function")(o),c="setTimeout",s="setInterval",f="clearTimeout",u="-start",d="-";e.exports=o,a.inPlace(window,[c,"setImmediate"],c+d),a.inPlace(window,[s],s+d),a.inPlace(window,[f,"clearImmediate"],f+d),o.on(s+u,r),o.on(c+u,i)},{}],10:[function(t,e,n){function r(t,e){d.inPlace(e,["onreadystatechange"],"fn-",c)}function i(){var t=this,e=u.context(t);t.readyState>3&&!e.resolved&&(e.resolved=!0,u.emit("xhr-resolved",[],t)),d.inPlace(t,g,"fn-",c)}function o(t){y.push(t),h&&(b?b.then(a):w?w(a):(E=-E,R.data=E))}function a(){for(var t=0;t<y.length;t++)r([],y[t]);y.length&&(y=[])}function c(t,e){return e}function s(t,e){for(var n in t)e[n]=t[n];return e}t(5);var f=t("ee"),u=f.get("xhr"),d=t("wrap-function")(u),l=NREUM.o,p=l.XHR,h=l.MO,m=l.PR,w=l.SI,v="readystatechange",g=["onload","onerror","onabort","onloadstart","onloadend","onprogress","ontimeout"],y=[];e.exports=u;var x=window.XMLHttpRequest=function(t){var e=new p(t);try{u.emit("new-xhr",[e],e),e.addEventListener(v,i,!1)}catch(n){try{u.emit("internal-error",[n])}catch(r){}}return e};if(s(p,x),x.prototype=p.prototype,d.inPlace(x.prototype,["open","send"],"-xhr-",c),u.on("send-xhr-start",function(t,e){r(t,e),o(e)}),u.on("open-xhr-start",r),h){var b=m&&m.resolve();if(!w&&!m){var E=1,R=document.createTextNode(E);new h(a).observe(R,{characterData:!0})}}else f.on("fn-end",function(t){t[0]&&t[0].type===v||a()})},{}],11:[function(t,e,n){function r(t){if(!c(t))return null;var e=window.NREUM;if(!e.loader_config)return null;var n=(e.loader_config.accountID||"").toString()||null,r=(e.loader_config.agentID||"").toString()||null,f=(e.loader_config.trustKey||"").toString()||null;if(!n||!r)return null;var h=p.generateSpanId(),m=p.generateTraceId(),w=Date.now(),v={spanId:h,traceId:m,timestamp:w};return(t.sameOrigin||s(t)&&l())&&(v.traceContextParentHeader=i(h,m),v.traceContextStateHeader=o(h,w,n,r,f)),(t.sameOrigin&&!u()||!t.sameOrigin&&s(t)&&d())&&(v.newrelicHeader=a(h,m,w,n,r,f)),v}function i(t,e){return"00-"+e+"-"+t+"-01"}function o(t,e,n,r,i){var o=0,a="",c=1,s="",f="";return i+"@nr="+o+"-"+c+"-"+n+"-"+r+"-"+t+"-"+a+"-"+s+"-"+f+"-"+e}function a(t,e,n,r,i,o){var a="btoa"in window&&"function"==typeof window.btoa;if(!a)return null;var c={v:[0,1],d:{ty:"Browser",ac:r,ap:i,id:t,tr:e,ti:n}};return o&&r!==o&&(c.d.tk=o),btoa(JSON.stringify(c))}function c(t){return f()&&s(t)}function s(t){var e=!1,n={};if("init"in NREUM&&"distributed_tracing"in NREUM.init&&(n=NREUM.init.distributed_tracing),t.sameOrigin)e=!0;else if(n.allowed_origins instanceof Array)for(var r=0;r<n.allowed_origins.length;r++){var i=h(n.allowed_origins[r]);if(t.hostname===i.hostname&&t.protocol===i.protocol&&t.port===i.port){e=!0;break}}return e}function f(){return"init"in NREUM&&"distributed_tracing"in NREUM.init&&!!NREUM.init.distributed_tracing.enabled}function u(){return"init"in NREUM&&"distributed_tracing"in NREUM.init&&!!NREUM.init.distributed_tracing.exclude_newrelic_header}function d(){return"init"in NREUM&&"distributed_tracing"in NREUM.init&&NREUM.init.distributed_tracing.cors_use_newrelic_header!==!1}function l(){return"init"in NREUM&&"distributed_tracing"in NREUM.init&&!!NREUM.init.distributed_tracing.cors_use_tracecontext_headers}var p=t(21),h=t(13);e.exports={generateTracePayload:r,shouldGenerateTrace:c}},{}],12:[function(t,e,n){function r(t){var e=this.params,n=this.metrics;if(!this.ended){this.ended=!0;for(var r=0;r<l;r++)t.removeEventListener(d[r],this.listener,!1);e.aborted||(n.duration=a.now()-this.startTime,this.loadCaptureCalled||4!==t.readyState?null==e.status&&(e.status=0):o(this,t),n.cbTime=this.cbTime,u.emit("xhr-done",[t],t),c("xhr",[e,n,this.startTime]))}}function i(t,e){var n=s(e),r=t.params;r.host=n.hostname+":"+n.port,r.pathname=n.pathname,t.parsedOrigin=s(e),t.sameOrigin=t.parsedOrigin.sameOrigin}function o(t,e){t.params.status=e.status;var n=w(e,t.lastSize);if(n&&(t.metrics.rxSize=n),t.sameOrigin){var r=e.getResponseHeader("X-NewRelic-App-Data");r&&(t.params.cat=r.split(", ").pop())}t.loadCaptureCalled=!0}var a=t("loader");if(a.xhrWrappable){var c=t("handle"),s=t(13),f=t(11).generateTracePayload,u=t("ee"),d=["load","error","abort","timeout"],l=d.length,p=t("id"),h=t(17),m=t(16),w=t(14),v=window.XMLHttpRequest;a.features.xhr=!0,t(10),t(6),u.on("new-xhr",function(t){var e=this;e.totalCbs=0,e.called=0,e.cbTime=0,e.end=r,e.ended=!1,e.xhrGuids={},e.lastSize=null,e.loadCaptureCalled=!1,t.addEventListener("load",function(n){o(e,t)},!1),h&&(h>34||h<10)||window.opera||t.addEventListener("progress",function(t){e.lastSize=t.loaded},!1)}),u.on("open-xhr-start",function(t){this.params={method:t[0]},i(this,t[1]),this.metrics={}}),u.on("open-xhr-end",function(t,e){"loader_config"in NREUM&&"xpid"in NREUM.loader_config&&this.sameOrigin&&e.setRequestHeader("X-NewRelic-ID",NREUM.loader_config.xpid);var n=f(this.parsedOrigin);if(n){var r=!1;n.newrelicHeader&&(e.setRequestHeader("newrelic",n.newrelicHeader),r=!0),n.traceContextParentHeader&&(e.setRequestHeader("traceparent",n.traceContextParentHeader),n.traceContextStateHeader&&e.setRequestHeader("tracestate",n.traceContextStateHeader),r=!0),r&&(this.dt=n)}}),u.on("send-xhr-start",function(t,e){var n=this.metrics,r=t[0],i=this;if(n&&r){var o=m(r);o&&(n.txSize=o)}this.startTime=a.now(),this.listener=function(t){try{"abort"!==t.type||i.loadCaptureCalled||(i.params.aborted=!0),("load"!==t.type||i.called===i.totalCbs&&(i.onloadCalled||"function"!=typeof e.onload))&&i.end(e)}catch(n){try{u.emit("internal-error",[n])}catch(r){}}};for(var c=0;c<l;c++)e.addEventListener(d[c],this.listener,!1)}),u.on("xhr-cb-time",function(t,e,n){this.cbTime+=t,e?this.onloadCalled=!0:this.called+=1,this.called!==this.totalCbs||!this.onloadCalled&&"function"==typeof n.onload||this.end(n)}),u.on("xhr-load-added",function(t,e){var n=""+p(t)+!!e;this.xhrGuids&&!this.xhrGuids[n]&&(this.xhrGuids[n]=!0,this.totalCbs+=1)}),u.on("xhr-load-removed",function(t,e){var n=""+p(t)+!!e;this.xhrGuids&&this.xhrGuids[n]&&(delete this.xhrGuids[n],this.totalCbs-=1)}),u.on("addEventListener-end",function(t,e){e instanceof v&&"load"===t[0]&&u.emit("xhr-load-added",[t[1],t[2]],e)}),u.on("removeEventListener-end",function(t,e){e instanceof v&&"load"===t[0]&&u.emit("xhr-load-removed",[t[1],t[2]],e)}),u.on("fn-start",function(t,e,n){e instanceof v&&("onload"===n&&(this.onload=!0),("load"===(t[0]&&t[0].type)||this.onload)&&(this.xhrCbStart=a.now()))}),u.on("fn-end",function(t,e){this.xhrCbStart&&u.emit("xhr-cb-time",[a.now()-this.xhrCbStart,this.onload,e],e)}),u.on("fetch-before-start",function(t){function e(t,e){var n=!1;return e.newrelicHeader&&(t.set("newrelic",e.newrelicHeader),n=!0),e.traceContextParentHeader&&(t.set("traceparent",e.traceContextParentHeader),e.traceContextStateHeader&&t.set("tracestate",e.traceContextStateHeader),n=!0),n}var n,r=t[1]||{};"string"==typeof t[0]?n=t[0]:t[0]&&t[0].url?n=t[0].url:window.URL&&t[0]&&t[0]instanceof URL&&(n=t[0].href),n&&(this.parsedOrigin=s(n),this.sameOrigin=this.parsedOrigin.sameOrigin);var i=f(this.parsedOrigin);if(i&&(i.newrelicHeader||i.traceContextParentHeader))if("string"==typeof t[0]||window.URL&&t[0]&&t[0]instanceof URL){var o={};for(var a in r)o[a]=r[a];o.headers=new Headers(r.headers||{}),e(o.headers,i)&&(this.dt=i),t.length>1?t[1]=o:t.push(o)}else t[0]&&t[0].headers&&e(t[0].headers,i)&&(this.dt=i)})}},{}],13:[function(t,e,n){var r={};e.exports=function(t){if(t in r)return r[t];var e=document.createElement("a"),n=window.location,i={};e.href=t,i.port=e.port;var o=e.href.split("://");!i.port&&o[1]&&(i.port=o[1].split("/")[0].split("@").pop().split(":")[1]),i.port&&"0"!==i.port||(i.port="https"===o[0]?"443":"80"),i.hostname=e.hostname||n.hostname,i.pathname=e.pathname,i.protocol=o[0],"/"!==i.pathname.charAt(0)&&(i.pathname="/"+i.pathname);var a=!e.protocol||":"===e.protocol||e.protocol===n.protocol,c=e.hostname===document.domain&&e.port===n.port;return i.sameOrigin=a&&(!e.hostname||c),"/"===i.pathname&&(r[t]=i),i}},{}],14:[function(t,e,n){function r(t,e){var n=t.responseType;return"json"===n&&null!==e?e:"arraybuffer"===n||"blob"===n||"json"===n?i(t.response):"text"===n||""===n||void 0===n?i(t.responseText):void 0}var i=t(16);e.exports=r},{}],15:[function(t,e,n){function r(){}function i(t,e,n){return function(){return o(t,[f.now()].concat(c(arguments)),e?null:this,n),e?void 0:this}}var o=t("handle"),a=t(24),c=t(25),s=t("ee").get("tracer"),f=t("loader"),u=NREUM;"undefined"==typeof window.newrelic&&(newrelic=u);var d=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit","addRelease"],l="api-",p=l+"ixn-";a(d,function(t,e){u[e]=i(l+e,!0,"api")}),u.addPageAction=i(l+"addPageAction",!0),u.setCurrentRouteName=i(l+"routeName",!0),e.exports=newrelic,u.interaction=function(){return(new r).get()};var h=r.prototype={createTracer:function(t,e){var n={},r=this,i="function"==typeof e;return o(p+"tracer",[f.now(),t,n],r),function(){if(s.emit((i?"":"no-")+"fn-start",[f.now(),r,i],n),i)try{return e.apply(this,arguments)}catch(t){throw s.emit("fn-err",[arguments,this,t],n),t}finally{s.emit("fn-end",[f.now()],n)}}}};a("actionText,setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(t,e){h[e]=i(p+e)}),newrelic.noticeError=function(t,e){"string"==typeof t&&(t=new Error(t)),o("err",[t,f.now(),!1,e])}},{}],16:[function(t,e,n){e.exports=function(t){if("string"==typeof t&&t.length)return t.length;if("object"==typeof t){if("undefined"!=typeof ArrayBuffer&&t instanceof ArrayBuffer&&t.byteLength)return t.byteLength;if("undefined"!=typeof Blob&&t instanceof Blob&&t.size)return t.size;if(!("undefined"!=typeof FormData&&t instanceof FormData))try{return JSON.stringify(t).length}catch(e){return}}}},{}],17:[function(t,e,n){var r=0,i=navigator.userAgent.match(/Firefox[\/\s](\d+\.\d+)/);i&&(r=+i[1]),e.exports=r},{}],18:[function(t,e,n){function r(){return c.exists&&performance.now?Math.round(performance.now()):(o=Math.max((new Date).getTime(),o))-a}function i(){return o}var o=(new Date).getTime(),a=o,c=t(26);e.exports=r,e.exports.offset=a,e.exports.getLastTimestamp=i},{}],19:[function(t,e,n){function r(t){return!(!t||!t.protocol||"file:"===t.protocol)}e.exports=r},{}],20:[function(t,e,n){function r(t,e){var n=t.getEntries();n.forEach(function(t){"first-paint"===t.name?d("timing",["fp",Math.floor(t.startTime)]):"first-contentful-paint"===t.name&&d("timing",["fcp",Math.floor(t.startTime)])})}function i(t,e){var n=t.getEntries();n.length>0&&d("lcp",[n[n.length-1]])}function o(t){t.getEntries().forEach(function(t){t.hadRecentInput||d("cls",[t])})}function a(t){if(t instanceof h&&!w){var e=Math.round(t.timeStamp),n={type:t.type};e<=l.now()?n.fid=l.now()-e:e>l.offset&&e<=Date.now()?(e-=l.offset,n.fid=l.now()-e):e=l.now(),w=!0,d("timing",["fi",e,n])}}function c(t){d("pageHide",[l.now(),t])}if(!("init"in NREUM&&"page_view_timing"in NREUM.init&&"enabled"in NREUM.init.page_view_timing&&NREUM.init.page_view_timing.enabled===!1)){var s,f,u,d=t("handle"),l=t("loader"),p=t(23),h=NREUM.o.EV;if("PerformanceObserver"in window&&"function"==typeof window.PerformanceObserver){s=new PerformanceObserver(r);try{s.observe({entryTypes:["paint"]})}catch(m){}f=new PerformanceObserver(i);try{f.observe({entryTypes:["largest-contentful-paint"]})}catch(m){}u=new PerformanceObserver(o);try{u.observe({type:"layout-shift",buffered:!0})}catch(m){}}if("addEventListener"in document){var w=!1,v=["click","keydown","mousedown","pointerdown","touchstart"];v.forEach(function(t){document.addEventListener(t,a,!1)})}p(c)}},{}],21:[function(t,e,n){function r(){function t(){return e?15&e[n++]:16*Math.random()|0}var e=null,n=0,r=window.crypto||window.msCrypto;r&&r.getRandomValues&&(e=r.getRandomValues(new Uint8Array(31)));for(var i,o="xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx",a="",c=0;c<o.length;c++)i=o[c],"x"===i?a+=t().toString(16):"y"===i?(i=3&t()|8,a+=i.toString(16)):a+=i;return a}function i(){return a(16)}function o(){return a(32)}function a(t){function e(){return n?15&n[r++]:16*Math.random()|0}var n=null,r=0,i=window.crypto||window.msCrypto;i&&i.getRandomValues&&Uint8Array&&(n=i.getRandomValues(new Uint8Array(31)));for(var o=[],a=0;a<t;a++)o.push(e().toString(16));return o.join("")}e.exports={generateUuid:r,generateSpanId:i,generateTraceId:o}},{}],22:[function(t,e,n){function r(t,e){if(!i)return!1;if(t!==i)return!1;if(!e)return!0;if(!o)return!1;for(var n=o.split("."),r=e.split("."),a=0;a<r.length;a++)if(r[a]!==n[a])return!1;return!0}var i=null,o=null,a=/Version\/(\S+)\s+Safari/;if(navigator.userAgent){var c=navigator.userAgent,s=c.match(a);s&&c.indexOf("Chrome")===-1&&c.indexOf("Chromium")===-1&&(i="Safari",o=s[1])}e.exports={agent:i,version:o,match:r}},{}],23:[function(t,e,n){function r(t){function e(){t(a&&document[a]?document[a]:document[i]?"hidden":"visible")}"addEventListener"in document&&o&&document.addEventListener(o,e,!1)}e.exports=r;var i,o,a;"undefined"!=typeof document.hidden?(i="hidden",o="visibilitychange",a="visibilityState"):"undefined"!=typeof document.msHidden?(i="msHidden",o="msvisibilitychange"):"undefined"!=typeof document.webkitHidden&&(i="webkitHidden",o="webkitvisibilitychange",a="webkitVisibilityState")},{}],24:[function(t,e,n){function r(t,e){var n=[],r="",o=0;for(r in t)i.call(t,r)&&(n[o]=e(r,t[r]),o+=1);return n}var i=Object.prototype.hasOwnProperty;e.exports=r},{}],25:[function(t,e,n){function r(t,e,n){e||(e=0),"undefined"==typeof n&&(n=t?t.length:0);for(var r=-1,i=n-e||0,o=Array(i<0?0:i);++r<i;)o[r]=t[e+r];return o}e.exports=r},{}],26:[function(t,e,n){e.exports={exists:"undefined"!=typeof window.performance&&window.performance.timing&&"undefined"!=typeof window.performance.timing.navigationStart}},{}],ee:[function(t,e,n){function r(){}function i(t){function e(t){return t&&t instanceof r?t:t?f(t,s,a):a()}function n(n,r,i,o,a){if(a!==!1&&(a=!0),!p.aborted||o){t&&a&&t(n,r,i);for(var c=e(i),s=m(n),f=s.length,u=0;u<f;u++)s[u].apply(c,r);var l=d[y[n]];return l&&l.push([x,n,r,c]),c}}function o(t,e){g[t]=m(t).concat(e)}function h(t,e){var n=g[t];if(n)for(var r=0;r<n.length;r++)n[r]===e&&n.splice(r,1)}function m(t){return g[t]||[]}function w(t){return l[t]=l[t]||i(n)}function v(t,e){u(t,function(t,n){e=e||"feature",y[n]=e,e in d||(d[e]=[])})}var g={},y={},x={on:o,addEventListener:o,removeEventListener:h,emit:n,get:w,listeners:m,context:e,buffer:v,abort:c,aborted:!1};return x}function o(t){return f(t,s,a)}function a(){return new r}function c(){(d.api||d.feature)&&(p.aborted=!0,d=p.backlog={})}var s="nr@context",f=t("gos"),u=t(24),d={},l={},p=e.exports=i();e.exports.getOrSetContext=o,p.backlog=d},{}],gos:[function(t,e,n){function r(t,e,n){if(i.call(t,e))return t[e];var r=n();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(t,e,{value:r,writable:!0,enumerable:!1}),r}catch(o){}return t[e]=r,r}var i=Object.prototype.hasOwnProperty;e.exports=r},{}],handle:[function(t,e,n){function r(t,e,n,r){i.buffer([t],r),i.emit(t,e,n)}var i=t("ee").get("handle");e.exports=r,r.ee=i},{}],id:[function(t,e,n){function r(t){var e=typeof t;return!t||"object"!==e&&"function"!==e?-1:t===window?0:a(t,o,function(){return i++})}var i=1,o="nr@id",a=t("gos");e.exports=r},{}],loader:[function(t,e,n){function r(){if(!E++){var t=b.info=NREUM.info,e=p.getElementsByTagName("script")[0];if(setTimeout(f.abort,3e4),!(t&&t.licenseKey&&t.applicationID&&e))return f.abort();s(y,function(e,n){t[e]||(t[e]=n)});var n=a();c("mark",["onload",n+b.offset],null,"api"),c("timing",["load",n]);var r=p.createElement("script");r.src="https://"+t.agent,e.parentNode.insertBefore(r,e)}}function i(){"complete"===p.readyState&&o()}function o(){c("mark",["domContent",a()+b.offset],null,"api")}var a=t(18),c=t("handle"),s=t(24),f=t("ee"),u=t(22),d=t(19),l=window,p=l.document,h="addEventListener",m="attachEvent",w=l.XMLHttpRequest,v=w&&w.prototype;if(d(l.location)){NREUM.o={ST:setTimeout,SI:l.setImmediate,CT:clearTimeout,XHR:w,REQ:l.Request,EV:l.Event,PR:l.Promise,MO:l.MutationObserver};var g=""+location,y={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-1208.min.js"},x=w&&v&&v[h]&&!/CriOS/.test(navigator.userAgent),b=e.exports={offset:a.getLastTimestamp(),now:a,origin:g,features:{},xhrWrappable:x,userAgent:u};t(15),t(20),p[h]?(p[h]("DOMContentLoaded",o,!1),l[h]("load",r,!1)):(p[m]("onreadystatechange",i),l[m]("onload",r)),c("mark",["firstbyte",a.getLastTimestamp()],null,"api");var E=0}},{}],"wrap-function":[function(t,e,n){function r(t,e){function n(e,n,r,s,f){function nrWrapper(){var o,a,u,l;try{a=this,o=d(arguments),u="function"==typeof r?r(o,a):r||{}}catch(p){i([p,"",[o,a,s],u],t)}c(n+"start",[o,a,s],u,f);try{return l=e.apply(a,o)}catch(h){throw c(n+"err",[o,a,h],u,f),h}finally{c(n+"end",[o,a,l],u,f)}}return a(e)?e:(n||(n=""),nrWrapper[l]=e,o(e,nrWrapper,t),nrWrapper)}function r(t,e,r,i,o){r||(r="");var c,s,f,u="-"===r.charAt(0);for(f=0;f<e.length;f++)s=e[f],c=t[s],a(c)||(t[s]=n(c,u?s+r:r,i,s,o))}function c(n,r,o,a){if(!h||e){var c=h;h=!0;try{t.emit(n,r,o,e,a)}catch(s){i([s,n,r,o],t)}h=c}}return t||(t=u),n.inPlace=r,n.flag=l,n}function i(t,e){e||(e=u);try{e.emit("internal-error",t)}catch(n){}}function o(t,e,n){if(Object.defineProperty&&Object.keys)try{var r=Object.keys(t);return r.forEach(function(n){Object.defineProperty(e,n,{get:function(){return t[n]},set:function(e){return t[n]=e,e}})}),e}catch(o){i([o],n)}for(var a in t)p.call(t,a)&&(e[a]=t[a]);return e}function a(t){return!(t&&t instanceof Function&&t.apply&&!t[l])}function c(t,e){var n=e(t);return n[l]=t,o(t,n,u),n}function s(t,e,n){var r=t[e];t[e]=c(r,n)}function f(){for(var t=arguments.length,e=new Array(t),n=0;n<t;++n)e[n]=arguments[n];return e}var u=t("ee"),d=t(25),l="nr@original",p=Object.prototype.hasOwnProperty,h=!1;e.exports=r,e.exports.wrapFunction=c,e.exports.wrapInPlace=s,e.exports.argsToArray=f},{}]},{},["loader",2,12,4,3]);</script><meta content="g3pUbR-M9skG6NzzSVjlQZBHVJUHBRS2KlBf13lmdIM" name="google-site-verification" /><meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0" name="viewport" /><meta content="default-src https: http: &#39;unsafe-inline&#39;; script-src &#39;unsafe-eval&#39; *.newrelic.com *.bugherd.com *.q4cdn.com *.q4web.com *.amazonaws.com *.highcharts.com *.adobedtm.com *.googletagmanager.com *.googleadservices.com *.google-analytics.com *.demandbase.com *.rmulus.com *.a3cloud.net *.en25.com *.doubleclick.net *.webtype.com *.eloqua.com *.omtrdc.net &#39;unsafe-inline&#39; data: *.q4app.com" http-equiv="Content-Security-Policy" /><link type="text/css" rel="stylesheet" media="all" href="//s1.q4cdn.com/608738804/files/js/fonts.css" />
<link type="text/css" rel="stylesheet" media="all" href="//s1.q4cdn.com/608738804/files/assets/style/main.css" />
<link type="text/css" rel="stylesheet" media="all" href="//s1.q4cdn.com/608738804/files/css/jquery-ui-1.7.2.custom.css" />
<link type="text/css" rel="stylesheet" media="screen" href="//s1.q4cdn.com/608738804/files/js/jquery-fancybox.css" />
<link type="text/css" rel="stylesheet" media="all" href="//s3.amazonaws.com/icomoon.io/50912/Q4Juniper2015/style.css" />
<link type="text/css" rel="stylesheet" media="all" href="//s1.q4cdn.com/608738804/files/assets/style/style-update.css" />
<link type="image/x-icon" rel="icon" media="" href="//s1.q4cdn.com/608738804/files/favicon.ico" />
<link type="image/x-icon" rel="shortcut icon" media="" href="//s1.q4cdn.com/608738804/files/favicon.ico" />
<link rel="stylesheet" media="all" href="//s1.q4cdn.com/608738804/files/css/default.css" />
<link rel="stylesheet" media="print" href="//s1.q4cdn.com/608738804/files/css/print.css" />
<link id="htmlGlobalLinkCss" type="text/css" rel="stylesheet" media="all" href="//s1.q4cdn.com/608738804/files/css/global.css?v=23473" /><link id="htmlClientLinkCss" type="text/css" rel="stylesheet" media="all" href="//s1.q4cdn.com/608738804/files/css/client.css?v=23351" /><link id="htmlLinkPrintCss" type="text/css" rel="stylesheet" media="print" href="//s1.q4cdn.com/608738804/files/css/print.css" /><script type="text/javascript" src="//s1.q4cdn.com/608738804/files/js/q4-core.js"></script>
<script type="text/javascript" src="//s1.q4cdn.com/608738804/files/js/doctracking.js"></script>
<script type="text/javascript" src="//s1.q4cdn.com/608738804/files/assets/svg/grunticon.loader.js"></script>
<script type="text/javascript" src="//s1.q4cdn.com/608738804/files/js/icheck-min.js"></script>
<script type="text/javascript" src="//s1.q4cdn.com/608738804/files/assets/library/html5shiv.js"></script>
<script type="text/javascript" src="//assets.adobedtm.com/998b2d6d4944658536fe36266a249b07e626b86d/satelliteLib-6d05b7c7a99e1cbbdcac4fcfe7005e6bee80a0e9.js"></script>
<script type="text/javascript" src="//q4implementation.s3.amazonaws.com/widgets/latest/q4.email-validation.min.js"></script>
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

    var trackingCodes = [{qualifier: 'Q4', trackingCode: 'UA-42460262-1'}];
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
    
    
    <div id="pageClass" class="Sectioninvestor-relations PageDefault PageInvestorRelationsEvents LayoutThreeColumnLayout Languageen-CA EventPage">
        <div class="PageDefaultInner">
            <div id="litPageDiv" class="PageInvestorRelationsEvents SectionInvestorRelationsEvents ParentSection_investor-relations">
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

                    
                    <a id="lnkPostback" href="javascript:__doPostBack(&#39;lnkPostback&#39;,&#39;&#39;)" style="display: none"></a>
                    
<div class="LayoutDefault LayoutThreeColumn">
	<div class="LayoutDefaultInner">
		<div class="HeaderContainer">
			<div class="PaneHeader"><span class='HeaderPaneDiv'><span class='HeaderPaneDiv2'><div id="_ctrl0_ctl09_divModuleContainer" class="BlankModuleContainer">
    
    <div class="main-header jp">
    <nav class="wrapper">
        <div class="navbar-wrapper">
            <div class="navbar-screen"></div>
            <div class="header-search-wrapper">
                <!-- <form class="header-search" method="get" action="/ExternalSearch/search/header"> -->
                <input class="header-search-input" required="required" placeholder=" " name="query" type="search">
                <input value="" name="searchSubgroup" id="searchSubgroup" type="hidden">
                <input name="locale" id="locale" type="hidden" value="us_en">
                <div class="header-search-submit">
                    <a href="#/">
                        <div class="desktop-nav icon icon-inline icon-27 icon-nav-search"></div>
                    </a>
                    <div class="mobile-nav icon icon-inline icon-27 icon-nav-search-white"></div>
                </div>
                <!-- </form> -->
            </div>
            <a href="http://www.juniper.net/us/en/" class="logo">
                <!--[if lt IE 9]><div class="icon-logo icon">
<img style="height:100%;" src="//s1.q4cdn.com/608738804/files/assets/svg/logo.png"></img>
</div><![endif]-->
                <!--[if !IE 8]><!-->
                <div class="icon-logo icon"></div>
                <!--<![endif]-->
            </a>
            <div class="tablet-show header-tablet-icon header-nav-control">
                <i class="icon icon-34 icon-menu-control-white"></i>
            </div>
        </div>
        <div class="global-back-button">
            <a href="#/">Back</a>
        </div>
        <ul class="top-menu nav-link-list">
            <li class="nav-link-item">
                <a target="" class="nav-link-name has-submenu no-mobile-click" href="http://www.juniper.net/us/en/products-services/">Products &amp; Services</a>
                <div class="nav-flyout full">
                    <ul class="nav-link-list">
                        <li class="nav-link-item mobile-only">
                            <a target="" class="nav-link-name" href="http://www.juniper.net/us/en/products-services/">Products &amp; Services</a>
                        </li>
                        <li class="nav-link-item">
                            <ul class="flyout-header-list">
                                <li class="nav-link-item">
                                    <a target="" class="nav-link-name has-submenu" href="http://www.juniper.net/us/en/products-services/">Products</a>
                                    <ul class="nav-link-list ">
                                        <li class="nav-link-item">
                                            <ul class="nav-column-list">
                                                <li class="nav-link-item">
                                                    <ul class=" ">
                                                        <li class="nav-link-item">
                                                            <a target="" class="nav-link-name" href="http://www.juniper.net/us/en/products-services/ipc/">Identity and Policy Control</a>
                                                        </li>
                                                        <li class="nav-link-item">
                                                            <a target="" class="nav-link-name" href="http://www.juniper.net/us/en/products-services/network-edge-services/">Network Edge Services</a>
                                                        </li>
                                                        <li class="nav-link-item">
                                                            <a target="" class="nav-link-name" href="http://www.juniper.net/us/en/products-services/network-management/">Network Management</a>
                                                        </li>
                                                        <li class="nav-link-item">
                                                            <a target="" class="nav-link-name" href="http://www.juniper.net/us/en/products-services/nos/">Network Operating System</a>
                                                        </li>
                                                        <li class="nav-link-item">
                                                            <a target="" class="nav-link-name" href="http://www.juniper.net/us/en/products-services/routing/">Routers</a>
                                                        </li>
                                                    </ul>
                                                </li>
                                                <li class="nav-link-item">
                                                    <ul class=" ">
                                                        <li class="nav-link-item">
                                                            <a target="" class="nav-link-name" href="http://www.juniper.net/us/en/products-services/sdn/">Software Defined Networking</a>
                                                        </li>
                                                        <li class="nav-link-item">
                                                            <a target="" class="nav-link-name" href="http://www.juniper.net/us/en/products-services/security/">Security</a>
                                                        </li>
                                                        <li class="nav-link-item">
                                                            <a target="" class="nav-link-name" href="http://www.juniper.net/us/en/products-services/switching/">Switches</a>
                                                        </li>
                                                        <li class="nav-link-item">
                                                            <a target="" class="nav-link-name" href="http://www.juniper.net/us/en/products-services/wireless/">Wireless</a>
                                                        </li>
                                                    </ul>
                                                </li>
                                            </ul>
                                        </li>
                                        <li class="nav-link-item">
                                            <ul class=" ">
                                                <li class="nav-link-item">
                                                    <a target="" class="nav-link-name nav-link-subhead-item" href="http://www.juniper.net/us/en/products-services/a-z/">All Products A-Z</a>
                                                </li>
                                                <li class="nav-link-item">
                                                    <a target="_blank" class="nav-link-name nav-link-subhead-item" href="https://www.juniper.net/support/eol/">End of Life</a>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                </li>
                                <li class="nav-link-item">
                                    <a target="" class="nav-link-name" href="http://www.juniper.net/us/en/solutions/">Solutions</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="_blank" class="nav-link-name" href="http://www.juniper.net/documentation/en_US/design-and-architecture/data-center/index.html">Design &amp; Architecture Center</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="" class="nav-link-name" href="http://www.juniper.net/us/en/how-to-buy/">How to Buy</a>
                                </li>
                            </ul>
                        </li>
                        <li class="nav-link-item">
                            <ul class="flyout-header-list">
                                <li class="nav-link-item">
                                    <a target="" class="nav-link-name has-submenu" href="http://www.juniper.net/us/en/products-services/services/technical-services/">Services</a>
                                    <ul class="nav-link-list nav-column-list">
                                        <li class="nav-link-item">
                                            <ul class=" ">
                                                <li class="nav-link-item">
                                                    <a target="" class="nav-link-name" href="http://www.juniper.net/us/en/products-services/services/technical-services/">Overview</a>
                                                </li>
                                                <li class="nav-link-item">
                                                    <a target="" class="nav-link-name" href="http://www.juniper.net/us/en/products-services/services/technical-services/plan/">Plan</a>
                                                </li>
                                                <li class="nav-link-item">
                                                    <a target="" class="nav-link-name" href="http://www.juniper.net/us/en/products-services/services/technical-services/build/">Build</a>
                                                </li>
                                                <li class="nav-link-item">
                                                    <a target="" class="nav-link-name" href="http://www.juniper.net/us/en/products-services/services/technical-services/operate/">Operate</a>
                                                </li>
                                            </ul>
                                        </li>
                                        <li class="nav-link-item">
                                            <ul class=" "></ul>
                                        </li>
                                    </ul>
                                </li>
                                <li class="nav-link-item">
                                    <a target="_blank" class="nav-link-name" href="http://www.juniper.net/techpubs/">TechLibrary</a>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </div>
            </li>
            <li class="nav-link-item">
                <a href="https://www.juniper.net/customers/support/" class="nav-link-name has-submenu no-mobile-click">Support</a>
                <div class="nav-flyout has-nav-search full">
                    <ul class="nav-link-list flyout-header-list">
                        <li class="nav-link-item mobile-only">
                            <a class="nav-link-name" href="https://www.juniper.net/customers/support/" target="_top">Support</a>
                        </li>
                        <li class="nav-link-item">
                            <a target="_top" class="nav-link-name has-submenu desktop-only" href="https://www.juniper.net/customers/support/">Support</a>
                            <div class="nav-link-name has-submenu">Case Management</div>
                            <ul class="nav-link-list flyout-subheader-list">
                                <li class="nav-link-item">
                                    <div class="nav-link-name has-submenu">CASES</div>
                                    <ul class="nav-link-list">
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Your Open Cases" href="https://www.juniper.net/casemanager/" class="nav-link-name">Your Open Cases</a>
                                        </li>
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Create a Case/RMA" href="https://www.juniper.net/casemanager/#/create" class="nav-link-name">Create a Case/RMA</a>
                                        </li>
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Guidelines" href="http://www.juniper.net/support/guidelines.html" class="nav-link-name">Guidelines</a>
                                        </li>
                                    </ul>
                                </li>
                                <li class="nav-link-item">
                                    <div class="nav-link-name has-submenu">RMAs</div>
                                    <ul class="nav-link-list">
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Your Open RMAs" href="https://www.juniper.net/casemanager/#/rmas" class="nav-link-name">Your Open RMAs</a>
                                        </li>
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Repair &amp; Return Policy" href="http://www.juniper.net/support/rma-procedure.html" class="nav-link-name">Repair &amp; Return Policy</a>
                                        </li>
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Global RMA Locations" href="http://www.juniper.net/support/rma-locations.html" class="nav-link-name">Global RMA Locations</a>
                                        </li>
                                    </ul>
                                </li>
                                <li class="nav-link-item">
                                    <div class="nav-link-name has-submenu">Managing</div>
                                    <ul class="nav-link-list">
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Contact Support" href="http://www.juniper.net/support/requesting-support.html" class="nav-link-name">Contact Support</a>
                                        </li>
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Product Warranty" href="http://www.juniper.net/support/warranty/" class="nav-link-name">Product Warranty</a>
                                        </li>
                                    </ul>
                                </li>
                            </ul>
                        </li>
                        <li class="nav-link-item">
                            <div class="nav-link-name has-submenu">Downloads &amp; Docs</div>
                            <ul class="nav-link-list flyout-subheader-list">
                                <li class="nav-link-item">
                                    <div class="nav-link-name has-submenu">PLATFORMS</div>
                                    <ul class="nav-link-list">
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Junos" href="http://www.juniper.net/support/downloads/junos.html" class="nav-link-name">Junos</a>
                                        </li>
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Secure Access" href="http://www.juniper.net/support/downloads/group/?f=sa" class="nav-link-name">Secure Access</a>
                                        </li>
                                        <li class="nav-link-item">
                                            <a target="_blank" title="ScreenOS" href="http://www.juniper.net/support/downloads/screenos.html" class="nav-link-name">ScreenOS</a>
                                        </li>
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Junos Space" href="https://www.juniper.net/support/downloads/space.html" class="nav-link-name">Junos Space</a>
                                        </li>
                                        <li class="nav-link-item">
                                            <a target="_blank" title="All Downloads" href="http://www.juniper.net/support/downloads/" class="nav-link-name">All Downloads</a>
                                        </li>
                                    </ul>
                                </li>
                                <li class="nav-link-item">
                                    <div class="nav-link-name has-submenu">Documentation</div>
                                    <ul class="nav-link-list">
                                        <li class="nav-link-item">
                                            <a target="_blank" title="TechLibrary" href="http://www.juniper.net/techpubs/" class="nav-link-name">TechLibrary</a>
                                        </li>
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Pathfinder" href="http://pathfinder.juniper.net/home/" class="nav-link-name">Pathfinder</a>
                                        </li>
                                    </ul>
                                </li>
                                <li class="nav-link-item">
                                    <div class="nav-link-name has-submenu">Troubleshooting</div>
                                    <ul class="nav-link-list">
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Knowledge Base" href="//kb.juniper.net/" class="nav-link-name">Knowledge Base</a>
                                        </li>
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Service Now" href="http://www.juniper.net/support/downloads/serviceautomation/" class="nav-link-name">Service Now</a>
                                        </li>
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Problem Report Search" href="https://prsearch.juniper.net/" class="nav-link-name">Problem Report Search</a>
                                        </li>
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Technical Bulletins" href="//kb.juniper.net/InfoCenter/index?page=content&amp;channel=TECHNICAL_BULLETINS" class="nav-link-name">Technical Bulletins</a>
                                        </li>
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Technical Video Library" href="http://www.juniper.net/support/video/" class="nav-link-name">Technical Video Library</a>
                                        </li>
                                    </ul>
                                </li>
                            </ul>
                        </li>
                        <li class="nav-link-item">
                            <div class="nav-link-name has-submenu">Contracts &amp; Licenses</div>
                            <ul class="nav-link-list flyout-subheader-list">
                                <li class="nav-link-item">
                                    <div class="nav-link-name has-submenu">CONTRACTS/PRODUCTS</div>
                                    <ul class="nav-link-list">
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Register New Product" href="https://www.juniper.net/svcreg/SRegSerialNum.jsp" class="nav-link-name">Register New Product</a>
                                        </li>
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Activate Support Certificate" href="https://www.juniper.net/svcreg/SRegSerialSearch.jsp?productSerial=&amp;lookUpBtn=Find" class="nav-link-name">Activate Support Certificate</a>
                                        </li>
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Update Install Base" href="https://www.juniper.net/customers/support/tools/updateinstallbase/" class="nav-link-name">Update Install Base</a>
                                        </li>
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Serial Number Entitlement" href="https://tools.juniper.net/SerialNumberEntitlementSearch/" class="nav-link-name">Serial Number Entitlement</a>
                                        </li>
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Search Contracts/Products" href="http://tools.juniper.net/ProductSearch/" class="nav-link-name">Search Contracts/Products</a>
                                        </li>
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Order Status" href="https://partneros.juniper.net/orderstatus/index.aspx" class="nav-link-name">Order Status</a>
                                        </li>
                                    </ul>
                                </li>
                                <li class="nav-link-item">
                                    <div class="nav-link-name has-submenu">LICENSES</div>
                                    <ul class="nav-link-list">
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Generate Product Licenses" href="https://www.juniper.net/lcrs/license.do" class="nav-link-name">Generate Product Licenses</a>
                                        </li>
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Subscription Registration" href="https://tools.juniper.net/subreg/" class="nav-link-name">Subscription Registration</a>
                                        </li>
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Find License Keys" href="https://www.juniper.net/lcrs/license.do?tab2" class="nav-link-name">Find License Keys</a>
                                        </li>
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Generate RMA Licenses" href="https://www.juniper.net/lcrs/generateRMA.do" class="nav-link-name">Generate RMA Licenses</a>
                                        </li>
                                        <li class="nav-link-item">
                                            <a target="_blank" title="License Activation Instructions" href="https://www.juniper.net/generate_license/" class="nav-link-name">License Activation Instructions</a>
                                        </li>
                                    </ul>
                                </li>
                            </ul>
                        </li>
                        <li class="nav-link-item">
                            <div class="nav-link-name has-submenu">Tools</div>
                            <ul class="nav-link-list flyout-subheader-list">
                                <li class="nav-link-item">
                                    <div class="nav-link-name has-submenu">SECURITY</div>
                                    <ul class="nav-link-list">
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Security Intelligence" href="http://www.juniper.net/us/en/security/" class="nav-link-name">Security Intelligence</a>
                                        </li>
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Report a Vulnerability" href="http://www.juniper.net/support/security/report_vulnerability.html" class="nav-link-name">Report a Vulnerability</a>
                                        </li>
                                    </ul>
                                </li>
                                <li class="nav-link-item">
                                    <div class="nav-link-name has-submenu">ANALYZERS</div>
                                    <ul class="nav-link-list">
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Chassis Analyzer" href="http://tools.juniper.net/ca/" class="nav-link-name">Chassis Analyzer</a>
                                        </li>
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Firewall Session Analyzer" href="http://tools.juniper.net/fsa/" class="nav-link-name">Firewall Session Analyzer</a>
                                        </li>
                                        <li class="nav-link-item">
                                            <a target="" title="Service Insight" href="http://www.juniper.net/us/en/products-services/network-management/junos-space-applications/service-insight/" class="nav-link-name">Service Insight</a>
                                        </li>
                                    </ul>
                                </li>
                                <li class="nav-link-item">
                                    <div class="nav-link-name has-submenu">MISC</div>
                                    <ul class="nav-link-list">
                                        <li class="nav-link-item">
                                            <a target="_blank" title="ELS Translator" href="https://www.juniper.net/customers/support/configtools/elstranslator" class="nav-link-name">ELS Translator</a>
                                        </li>
                                        <li class="nav-link-item">
                                            <a target="_blank" title="Junos Hardware Validation" href="http://tools.juniper.net/microcode/" class="nav-link-name">Junos Hardware Validation</a>
                                        </li>
                                        <li class="nav-link-item">
                                            <a target="_blank" title="IOS to Junos Translator" href="https://i2j.juniper.net/release/" class="nav-link-name">IOS to Junos Translator</a>
                                        </li>
                                    </ul>
                                </li>
                            </ul>
                        </li>
                        <li class="nav-search desktop-only">
                            <div class="nav-search-text">KNOWLEDGE CENTER SEARCH</div>
                            <div class="search-form-wrapper">
                                <div class="form">
                                    <!-- <form method="get" action="//kb.juniper.net/InfoCenter/index"> -->
                                    <input class="search-input" required="required" placeholder=" " name="question_box" type="search">
                                    <input name="locale" id="locale" type="hidden" value="">
                                    <input value="answers" name="page" type="hidden">
                                    <input value="Knowledge_Base" name="cntnt" type="hidden">
                                    <input value="Technical_Documentation" name="cntnt" type="hidden">
                                    <input value="Technotes" name="cntnt" type="hidden">
                                    <input value="Security_Advisories" name="cntnt" type="hidden">
                                    <input value="Jnet_Forums_Solved" name="cntnt" type="hidden">
                                    <input value="Technical_Bulletins" name="cntnt" type="hidden">
                                    <submit class="submit button button-inline">
                                        <i class="icon icon-24 icon-header-search"></i>
                                    </submit>
                                    <!-- </form> -->
                                </div>
                            </div>
                        </li>
                    </ul>
                </div>
            </li>
            <li class="nav-link-item">
                <a href="http://www.juniper.net/us/en/training/" class="nav-link-name has-submenu no-mobile-click">Training</a>
                <div class="nav-flyout full">
                    <ul class="nav-link-list flyout-header-list">
                        <li class="nav-link-item mobile-only">
                            <a href="http://www.juniper.net/us/en/training/" class="nav-link-name ">Training</a>
                        </li>
                        <li class="nav-link-item">
                            <a href="http://www.juniper.net/us/en/training/" class="nav-link-name has-submenu">Training</a>
                            <ul class="nav-link-list">
                                <li class="nav-link-item">
                                    <a target="_blank" href="https://learningportal.juniper.net/juniper/user_courses.aspx" class="nav-link-name">Courses</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="_blank" href="https://learningportal.juniper.net/juniper/user_activity_info.aspx?id=5357" class="nav-link-name">Learning Paths</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="_blank" href="https://learningportal.juniper.net/juniper/user_activity_info.aspx?id=5798" class="nav-link-name">Getting Started with Juniper Networks</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="_blank" href="https://learningportal.juniper.net/juniper/user_activity_info.aspx?id=5853" class="nav-link-name">Learning Bytes</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="_blank" href="http://www.onfulfillment.com/junipertrainingpublic/" class="nav-link-name">Purchase Course Materials</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/training/prescriptive/" class="nav-link-name">Prescriptive Training</a>
                                </li>
                            </ul>
                        </li>
                        <li class="nav-link-item">
                            <a href="" class="nav-link-name has-submenu">Programs & Resources</a>
                            <ul class="nav-link-list">
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/training/technical_education/authorized_education.page" class="nav-link-name">Authorized Education Partners</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/training/trainingcredits/" class="nav-link-name">Training Credits</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/training/junos-genius/" class="nav-link-name">Junos Genius</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/training/news/" class="nav-link-name">Education Updates</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/training/junosphere-offer/" class="nav-link-name">Junosphere Offer</a>
                                </li>
                            </ul>
                        </li>
                        <li class="nav-link-item">
                            <a href="http://www.juniper.net/us/en/training/certification/" class="nav-link-name has-submenu">Certification</a>
                            <ul class="nav-link-list">
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/training/certification/" class="nav-link-name">Overview</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/training/certification/getting-started/" class="nav-link-name">Getting Started</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/training/certification/already-certified/" class="nav-link-name">Already Certified</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/training/certification/already-certified/recertification/" class="nav-link-name">Recertification</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/training/certification/exam_registration.page" class="nav-link-name">Exam Registration</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/training/fasttrack/" class="nav-link-name">Fast Track Program</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/training/certification/certification-tracks/bootcamps/" class="nav-link-name">Bootcamps</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/training/certification/news/" class="nav-link-name">News</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/training/certification/policies-exam/" class="nav-link-name">Policies and Exam Security</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/training/certification/resources.page" class="nav-link-name">Resources</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/training/certification/contact-us/" class="nav-link-name">Contact Information</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/training/certification/jncp-customer-service/" class="nav-link-name">Customer Service</a>
                                </li>
                            </ul>
                        </li>
                        <li class="nav-link-item">
                            <a href="http://www.juniper.net/us/en/training/academicalliance/" class="nav-link-name has-submenu">Academic Alliance</a>
                            <ul class="nav-link-list">
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/training/academicalliance/" class="nav-link-name">Overview</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/training/academicalliance/prospective-partners/" class="nav-link-name">Prospective Partners</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/training/academicalliance/prospective-partners/engagement-model/" class="nav-link-name">Engagement Model</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/training/academicalliance/resources/" class="nav-link-name">Current JNAA Partner Resources</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/training/academicalliance/partner-listing/" class="nav-link-name">Academic Alliance Partner Listing</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/training/academicalliance/join-junipers-academic-alliance/" class="nav-link-name">Join Juniper's Academic Alliance</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/company/careers/university/" class="nav-link-name">Student Internships</a>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </div>
            </li>
            <li class="nav-link-item">
                <a href="http://www.juniper.net/us/en/how-to-buy/" class="nav-link-name has-submenu no-mobile-click">How to Buy</a>
                <div class="nav-flyout" style="right: auto; left: auto;">
                    <ul class="nav-link-list">
                        <li class="nav-link-item">
                            <a href="http://www.juniper.net/us/en/how-to-buy/" class="nav-link-name has-submenu">How to Buy</a>
                            <ul class="nav-link-list">
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/how-to-buy/form/" class="nav-link-name">Contact Sales</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/how-to-buy/request-a-quote.page" class="nav-link-name">Request a Quote</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/partners/locator/" class="nav-link-name">Buy from a Local Partner</a>
                                </li>
                                <li class="nav-link-item">
                                    <a target="" href="http://www.juniper.net/us/en/how-to-buy/contacts/" class="nav-link-name">Find a Sales Office</a>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </div>
            </li>
            <li class="nav-link-item mobile-only">
                <a class="nav-link-name" href="http://www.juniper.net/us/en/solutions/">Solutions</a>
            </li>
            <li class="nav-link-item mobile-only">
                <a class="nav-link-name" href="http://www.juniper.net/us/en/company/">About Juniper</a>
            </li>
            <li class="nav-link-item mobile-only">
                <a class="nav-link-name" href="http://www.juniper.net/us/en/partners/">Partners</a>
            </li>
            <li class="nav-link-item mobile-only">
                <a class="nav-link-name" href="http://www.juniper.net/us/en/community/social/">Community</a>
            </li>
        </ul>
        <div class="content-screen"></div>
    </nav>
</div>

</div></span><span class='HeaderPaneDiv3'><div id="_ctrl0_ctl54_divModuleContainer" class="BlankModuleContainer">
    
    <script type="text/javascript">
$(function(){
    // remove all upcoming events from the "past" events module
    $('.upcomingEv .ModuleDate').each(function() {
        $('.pastEventsNew .ModuleDate:contains("' + $(this).html() + '")').closest('.ModuleItemRow').hide();
    });
});
</script>
</div></span></span></div>
			<div class="PaneHeader2"><span class='HeaderPane2Div3'><div id="_ctrl0_ctl12_divModuleContainer" class="ModuleContent">
    <div class="ModuleOuterContainer">
        
        <div class="ModuleInnerContainer">
            <div class="irSQ container stock-widget"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mustache.js/3.0.3/mustache.min.js"></script>
<script src="https://widgets.q4app.com/widgets/q4.stockQuote.1.0.11.min.js"></script>

<script>
    $('.stock-widget').stockQuote({
       dateFormat: 'M dd, yy',
       changeCls: ['Down', 'Up'],
       stock: ['NYSE:JNPR'],
       stockTpl: (
        '{{#.}}' +
            '<div class="stock-wrapper"> ' +
                '<span  class="StockDescription1"><a href="/investor-relations/Stock-Information/default.aspx">NYSE: JNPR</a></span> ' +
                '<span  class="StockDescription2">Price: $ </span> ' +
                '<a href="http://investor.juniper.net/investor-relations/stock-information/default.aspx"  class="StockPrice">{{tradePrice}}</a> ' +
            '</div> ' +
        '{{/.}}'
       )
    });
</script>
        </div>
    </div>
</div></span><span class='HeaderPane2Div4'><div id="_ctrl0_ctl15_divModuleContainer" class="Breadcrumb sectionTitle ">
    	<div class="container">
        <a href="http://investor.juniper.net/Home/default.aspx" id="_ctrl0_ctl15_hrefHome" class="BreadcrumbHomeLink">Home</a>
        <span class='BreadcrumbSeparator'>&nbsp; > &nbsp;</span><a href="http://investor.juniper.net/investor-relations/default.aspx">Investor Relations</a><span class='BreadcrumbSeparator'>&nbsp; > &nbsp;</span>Events
        
        <div class="ClearFix"></div>
        </div>
    </div>
</span></div>
			<div class="PaneNavigation"><div class="container clearfix"><span class='NavigationPaneDiv5'><nav class="IRmobileNav dropNav"><ul class="level1">
	<li class="has-children expanded"><a href="http://investor.juniper.net/investor-relations/default.aspx">Investor Relations</a><ul class="level2">
		<li><a href="http://investor.juniper.net/investor-relations/press-releases/default.aspx">Press Releases</a></li><li><a href="http://investor.juniper.net/investor-relations/stock-information/default.aspx">Stock Information</a></li><li><a href="http://investor.juniper.net/investor-relations/financial-reports/default.aspx">Financial Reports</a></li><li><a href="http://investor.juniper.net/investor-relations/sec-filings/default.aspx">SEC Filings</a></li><li><a href="http://investor.juniper.net/investor-relations/corporate-governance/default.aspx">Corporate Governance</a></li><li class="selected"><a href="http://investor.juniper.net/investor-relations/events/default.aspx">Events</a></li><li><a href="http://investor.juniper.net/investor-relations/faqs/default.aspx">FAQs</a></li><li><a href="http://investor.juniper.net/investor-relations/contact-us/default.aspx">Contact Us</a></li>
	</ul></li><li><a href="http://www.juniper.net/us/en/solutions/">Solutions</a></li><li><a href="http://www.juniper.net/us/en/products-services/">Products &amp; Services</a></li><li><a href="http://www.juniper.net/us/en/company/">Company</a></li><li><a href="http://www.juniper.net/us/en/partners/">Partners</a></li><li><a href="http://www.juniper.net/customers/support/">Support</a></li><li><a href="http://www.juniper.net/us/en/training/">Education</a></li>
</ul></nav>
</span></div></div>
		</div>
		<div class="PaneContentInner">
                   <div class="container clearfix">
                        <div class="PaneBreadcrumb"></div>
			<div class="PaneContent"><span class='ContentPaneDiv'><span class='ContentPaneDiv1'>
    <script type="text/javascript" src="/Modules/IRPortal.Modules.Event/js/EventReminder.js"></script>
    <div id="_ctrl0_ctl48_divModuleContainer" class="ModuleListContainer ModuleEvent tableModule eventsTable upcomingEvents">
        <h1 id="_ctrl0_ctl48_lblTitle" class="ModuleTitle"><span id="_ctrl0_ctl48_lblModuleTitle" class="ModuleTitle">Upcoming Events</span></h1>
        <div class="RssLinkTopContainer">
            
        </div>
        
        <div id="_ctrl0_ctl48_divFuturePast" class="ModuleYearNavContainer">
            <a href="http://investor.juniper.net/investor-relations/events/default.aspx?ShowEvents=FUTURE" id="_ctrl0_ctl48_hrefUpcomingEvents" class="selected">Upcoming Events</a>
            <a href="http://investor.juniper.net/investor-relations/events/default.aspx?ShowEvents=PAST" id="_ctrl0_ctl48_hrefPastEvents">Past Events</a>
        </div>
        <div class="module_events_wrapper">
            <div class="ModuleContainerInner">
                
                        <div id="_ctrl0_ctl48_repeaterContent_ctl00_divHeader" class="ModuleHeader">
                            
                            <span id="_ctrl0_ctl48_repeaterContent_ctl00_lblHeader1">Date</span>
                            <span id="_ctrl0_ctl48_repeaterContent_ctl00_lblHeader2">Event</span>
                        </div>
                    
                        <div id="_ctrl0_ctl48_repeaterContent_ctl01_divFooter" class="ModuleFooter">
                            
                        </div>
                    
            </div>
        </div>
        <div class="RssLinkBottomContainer">
            
        </div>
        <div class="ModuleNotFound">
            There are currently no upcoming events.
        </div>
    </div>
</span><span class='ContentPaneDiv2'><div id="_ctrl0_ctl51_divModuleContainer" class="BlankModuleContainer">
    <h1 id="_ctrl0_ctl51_lblTitle">
        <span id="_ctrl0_ctl51_lblModuleTitle" class="ModuleTitle">Past Events</span>
    </h1>
    <div class="event-widget eventsTable pastEventsNew">
    <div class="event-years ModuleYearNavContainer"></div>
    <div class="event-data ModuleContainerInner event-desktop"></div>
</div>
<!-- <script src="//s1.q4cdn.com/608738804/files/js/event_Switch.js"></script> -->
<script src="//s1.q4cdn.com/608738804/files/js/event_Switch3v2.js"></script>
<!-- <script src="//s1.q4cdn.com/608738804/files/js/event_Switch3.js"></script> -->
<script>
$('.event-widget').eventSwitch({

            listTpl: (
                '<div class="ModuleHeader">' +
                '<span>Date</span>' +
                '<span>Event</span>' +
                '</div>' +
                '{{#.}}' +
                '<div class="ModuleItemRow ModuleItem">' +
                '<div class="ModuleDateContainer">' +
                '<span class="ModuleDate">{{date}} </span>' +
                '<label class="ModuleTime">{{time}} <span>{{timeZone}}</span></label>' +
                '</div>' +
                '<div class="ModuleDesc">' +
                '<a href="{{url}}" class="ModuleHeadlineLink">{{title}}</a>' +
                '<span class="ModuleBodyContainer">{{{body}}}</span>' +
                '{{{location}}}' +
                '{{{speakers}}}' +
                // '{{{webcast}}}' +
                '{{#webcast}}' +
                '<div class="WebcastLink">' +
                '<a href="{{webcast}}" target="_blank" class="ModuleFileLink">Webcast</a>' +
                '</div>' +
                '{{/webcast}}' +
                '{{{docs}}}' +
                 // '<div class="WebcastLink">' +
                 // '<a href="{{WebCastLink}}" target="_blank" class="ModuleFileLink">Webcast</a>' +
                 // '</div>' +

                '<div class="RelatedDocuments">' +
                '{{{presentation}}}' +
                '{{{pressRelease}}}' +
                '</div>' +
                '</div>' +
                '</div>' +
                '{{/.}}'
            ),
            // webcastTpl: (
            //     '<div class="WebcastLink">' +
            //     '{{#.}}' +
            //         '<a href="{{WebCastLink}}" target="_blank" class="ModuleFileLink">Webcast</a>' +
            //     '{{/.}}' +
            //     '</div>' 
            // ),
            beforeRender:function(e, tpl){
                console.log(tpl);

            }
})
$(window).load(function() {
    // for (var iii = 2012; iii > 2007; iii--) {
    //     $(".year-item-" + iii).hide();
    // }
    $('.event-years > div').each(function(){
        /* Set minYear five years from current year*/
        // var minYear = new Date().getFullYear() - 4;
        var minYear = 2013;
        var year = parseInt($(this).find('.ModuleYearLink').text());
        if( year < minYear) {
            $(this).hide();
        }
    });
});
</script>










</div></span></span></div>
			<div class="PaneRight"><span class='RightPaneDiv'><span class='RightPaneDiv6'><div id="_ctrl0_ctl21_divModuleContainer" class="HtmlTextContainer secNav noborder">
    
    <div class="ContentContainer">
        <a href="/investor-relations/default.aspx">Investor Relations - Home</a>
    </div>
</div></span><span class='RightPaneDiv7'><nav class="secNav dropNav"><ul class="level1">
	<li class="has-children expanded"><a href="http://investor.juniper.net/investor-relations/default.aspx">Investor Relations</a><ul class="level2">
		<li><a href="http://investor.juniper.net/investor-relations/press-releases/default.aspx">Press Releases</a></li><li><a href="http://investor.juniper.net/investor-relations/stock-information/default.aspx">Stock Information</a></li><li><a href="http://investor.juniper.net/investor-relations/financial-reports/default.aspx">Financial Reports</a></li><li><a href="http://investor.juniper.net/investor-relations/sec-filings/default.aspx">SEC Filings</a></li><li><a href="http://investor.juniper.net/investor-relations/corporate-governance/default.aspx">Corporate Governance</a></li><li class="selected"><a href="http://investor.juniper.net/investor-relations/events/default.aspx">Events</a></li><li><a href="http://investor.juniper.net/investor-relations/faqs/default.aspx">FAQs</a></li><li><a href="http://investor.juniper.net/investor-relations/contact-us/default.aspx">Contact Us</a></li>
	</ul></li><li><a href="http://www.juniper.net/us/en/solutions/">Solutions</a></li><li><a href="http://www.juniper.net/us/en/products-services/">Products & Services</a></li><li><a href="http://www.juniper.net/us/en/company/">Company</a></li><li><a href="http://www.juniper.net/us/en/partners/">Partners</a></li><li><a href="http://www.juniper.net/customers/support/">Support</a></li><li><a href="http://www.juniper.net/us/en/training/">Education</a></li>
</ul></nav>
</span><span class='RightPaneDiv8'>
    <script type="text/javascript" src="/Modules/IRPortal.Modules.Event/js/EventReminder.js"></script>
    <div id="_ctrl0_ctl27_divModuleContainer" class="ModuleListContainer ModuleEvent sidebar_events">
        <h1 id="_ctrl0_ctl27_lblTitle" class="ModuleTitle"><span id="_ctrl0_ctl27_lblModuleTitle" class="ModuleTitle">Upcoming Events</span></h1>
        <div class="RssLinkTopContainer">
            
        </div>
        
        <div id="_ctrl0_ctl27_divFuturePast" class="ModuleYearNavContainer">
            <a href="http://investor.juniper.net/investor-relations/events/default.aspx?ShowEvents=FUTURE" id="_ctrl0_ctl27_hrefUpcomingEvents" class="selected">Upcoming Events</a>
            <a href="http://investor.juniper.net/investor-relations/events/default.aspx?ShowEvents=PAST" id="_ctrl0_ctl27_hrefPastEvents">Past Events</a>
        </div>
        <div class="module_events_wrapper">
            <div class="ModuleContainerInner">
                
                        
                    
                        <div id="_ctrl0_ctl27_repeaterContent_ctl01_divFooter" class="ModuleFooter">
                            
                        </div>
                    
            </div>
        </div>
        <div class="RssLinkBottomContainer">
            
        </div>
        <div class="ModuleNotFound">
            There are currently no upcoming events.
        </div>
    </div>
</span><span class='RightPaneDiv9'>
        <div class="signupForm">
            <div class="EditSubscriberContainer MailingListSignupContainer">
                <script language="javascript">
                function enableValidators1() {
                    // enable all validators
                    for (var i = 0; i < Page_Validators.length; i++) {
                        if (Page_Validators[i].id.indexOf('EmailValidator1') >= 0) {
                            ValidatorEnable(Page_Validators[i], true);
                        } else {
                            ValidatorEnable(Page_Validators[i], false);
                        }
                    }
                }
                </script>
                <div id="_ctrl0_ctl30_divModuleContainer" class="MailingListForm sidebar_alerts">
                    <h1 id="_ctrl0_ctl30_lblTitle"><span id="_ctrl0_ctl30_lblModuleTitle" class="ModuleTitle">Receive Email Alerts:</span><span id="_ctrl0_ctl30_lblHelpPage"></span></h1>
                    <table cellpadding="0" cellspacing="0" border="0" class="MailingListTable">
                        <tr>
                            <td colspan="2" class="IntroTextColumn">
                                <span id="_ctrl0_ctl30_lblIntroText" class="IntroText"></span>
                            </td>
                        </tr>
                        <tr id="rowEmailAddress">
                            <td  class="MailingListCol1">
                                <span id="_ctrl0_ctl30_lblEmailAddressText">Email Address</span>
                            </td>
                            <td  class="MailingListCol2">
                                <input name="_ctrl0$ctl30$txtEmail" type="text" id="_ctrl0_ctl30_txtEmail" placeholder="Email Address" />
                                <span id="_ctrl0_ctl30_lblRequiredEmailAddress" class="RequiredField">*</span>
                                <span id="_ctrl0_ctl30_regexEmailValidator1" style="display:none;"></span>
                                <span id="_ctrl0_ctl30_reqvalEmailValidator1" style="display:none;"></span>
                            </td>
                        </tr>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    </table>
                    <table id="_ctrl0_ctl30_tableMailingLists" cellpadding="0" cellspacing="0" border="0" width="100%" class="MailingListListTable">
	<tr id="_ctrl0_ctl30_rowMailingListLabel">
		<td colspan="2">
                                <span id="_ctrl0_ctl30_lblMailingListsText" class="MailingListsHeading">Mailing Lists</span>
                                
                            </td>
	</tr>
	<tr id="_ctrl0_ctl30_rowMailingLists">
		<td colspan="2">
                                <table id="_ctrl0_ctl30_chkLists">
			<tr>
				<td><input id="_ctrl0_ctl30_chkLists_0" type="checkbox" name="_ctrl0$ctl30$chkLists$0" checked="checked" value="31" /><label for="_ctrl0_ctl30_chkLists_0">Releases</label></td>
			</tr><tr>
				<td><input id="_ctrl0_ctl30_chkLists_1" type="checkbox" name="_ctrl0$ctl30$chkLists$1" checked="checked" value="33" /><label for="_ctrl0_ctl30_chkLists_1">SEC Filings</label></td>
			</tr><tr>
				<td><input id="_ctrl0_ctl30_chkLists_2" type="checkbox" name="_ctrl0$ctl30$chkLists$2" checked="checked" value="35" /><label for="_ctrl0_ctl30_chkLists_2">Events</label></td>
			</tr>
		</table>
                                
                                <span id="_ctrl0_ctl30_cusvalMailingListsValidator" style="display:none;"></span>
                            </td>
	</tr>
</table>

                    <br class="NoBr">
                    <div id="_ctrl0_ctl30_validationsummary" class="ErrorContainer" style="display:none;">

</div>
                    <br class="NoBr" />
                    <div id="_ctrl0_ctl30_UCCaptcha_divModuleContainer" class="CaptchaContainer">
<table id="_ctrl0_ctl30_UCCaptcha_Table1" cellpadding="0" cellspacing="0" border="0" width="100%">
	<tr>
		<td colspan="2">&nbsp;</td>
	</tr>
	<tr>
		<td colspan="2"><img src="https://investor.juniper.net/q4api/v4/captcha?clientId=_ctrl0_ctl30_UCCaptcha" id="_ctrl0_ctl30_UCCaptcha_Image1" /></td>
	</tr>
	<tr>
		<td colspan="2"><b>Enter the code shown above.</b></td>
	</tr>
	<tr>
		<td colspan="2">
			<input name="_ctrl0$ctl30$UCCaptcha$txtCode" type="text" id="_ctrl0_ctl30_UCCaptcha_txtCode" /><span id="_ctrl0_ctl30_UCCaptcha_RequiredFieldValidator1" style="display:none;">*</span>
		</td>
	</tr>
</table>

</div>
                    <br class="NoBr" />
                    <div class="GridActions">
                        <input type="submit" name="_ctrl0$ctl30$btnSubmit" value="Submit" onclick="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;_ctrl0$ctl30$btnSubmit&quot;, &quot;&quot;, true, &quot;990f35bf-ea02-4d65-8d51-94f88db5f113&quot;, &quot;&quot;, false, false))" id="_ctrl0_ctl30_btnSubmit" class="Button ActionButton" />
                    </div>
                    <a class="hidden" href="/investor-relations/email-alerts/default.aspx">Un-subscribe from Juniper Networks email alerts.</a>
                </div>
                <div id="_ctrl0_ctl30_divEditSubscriberConfirmation" class="EditSubscriberConfirmation" style="DISPLAY:none;">
                    
                </div>
            </div>
            <div id="_ctrl0_ctl30_div1" class="EditSubscriberConfirmation">
                
            </div>
        </div>
</span><span class='RightPaneDiv10'><div id="_ctrl0_ctl33_divModuleContainer" class="HtmlTextContainer sidebar_app">
    
    <div class="ContentContainer">
        <a class="unsubscribe" href="/investor-relations/email-alerts/default.aspx">Un-subscribe form Juniper Networks<br> email alerts.</a>
<!-- <img alt="app" src="//s1.q4cdn.com/608738804/files/icons/iphone.png">
<p>Download the free <a href="https://itunes.apple.com/us/app/juniper-networks-investor/id925798931?ls=1&amp;mt=8">IOS</a> or
<a class="arrow" href="https://play.google.com/store/apps/details?id=com.theirapp.juniper">Android</a> JNPR IR App to Stay Connected!</p> -->
    </div>
</div></span></span></div>
                   </div>
                    <div class="PaneLeft"><div class="container clearfix"><span class='LeftPaneDiv'></span></div></div>
		</div>
		<div class="FooterContainer">
			<div class="PaneFooter"><div class="container clearfix"><span class='FooterPaneDiv'><span class='FooterPaneDiv14'><div id="_ctrl0_ctl45_divModuleContainer" class="BlankModuleContainer">
    
    <script>

$(function() {

$('<span class="tentative">Tentative</span>').prependTo('.ModuleEvent .ModuleItemRow a.ModuleHeadlineLink:contains("Q4 2016")');

$('<span class="tentative">Tentative</span>').prependTo('.ModuleEventDetails .ModuleDetailHeadline:contains("Q4 2016")');



});

</script>
</div></span><span class='FooterPaneDiv4'><div id="_ctrl0_ctl57_divModuleContainer" class="BlankModuleContainer">
    
    <script type="text/javascript">
$(function() {
    $('.pastEv .ModuleItemRow').each(function() {
        $('.ModuleHeadline:contains("2015 Annual Meeting of Stockholders")').parent().next().next().show();
        if ($(this).find('.ModuleHeadline').text().indexOf("Financial Results Conference Call") > -1) {
            $(this).find('.ModuleLinks a').each(function() {
                if ($(this).find('.ModuleDownloadText').text() == 'Transcript') {
                    $(this).find('.ModuleDownloadText').html('CFO Commentary');
                }
            });
            $(this).find('.PresentationLinks a').each(function() {
                if ($(this).find('.ModuleDownloadText').text() == 'Presentation') {
                    $(this).find('.ModuleDownloadText').html('Transcript');
                }
            });


        }
    });

    $('.upcomingEv .ModuleItemRow').each(function() {
        if ($(this).find('.ModuleHeadline').html().indexOf('Financial Results Conference Call') > -1) {
            $(this).find('.RelatedFileLink > span.ModuleDownloadText').text('CFO Commentary');
            $(this).find('.PresentationLinks .ModuleDownloadText').text('Transcript');
        }

    });
});
</script>

</div></span><span class='FooterPaneDiv5'><div id="_ctrl0_ctl60_divModuleContainer" class="BlankModuleContainer">
    
    <script>
$(function() {

$('.upcomingEv .ModuleItemRow').each(function () {
       if ($(this).find('.ModuleHeadline').html().indexOf('Q2 2015') > -1) {
           $(this).find('.RelatedFileLink > span.ModuleDownloadText').text('CFO Commentary');
     }

});
});
</script>
</div></span><span class='FooterPaneDiv7'><div id="_ctrl0_ctl66_divModuleContainer" class="BlankModuleContainer">
    
    <script>
$('.ModuleEvent .ModuleTime').text(function() {
    if($(this).text().indexOf('ST') > -1) {
        return $(this).text().replace('ST', 'T');
    }
    else if($(this).text().indexOf('DT') > -1) {
        return $(this).text().replace('DT', 'T');
    }
});

</script>
</div></span></span></div></div>
			<div class="PaneFooter2"><span class='FooterPane2Div11'><div id="_ctrl0_ctl36_divModuleContainer" class="BlankModuleContainer clientFooter">
    
    <div class="footer jp">
    <div class="wrapper wrapper-medium">
        <ul class="footer-list footer-border slice slice-4col">
            <li class="slice-item"><a href="http://www.juniper.net/us/en/solutions/" class="footer-link" target="">Solutions</a></li>
            <li class="slice-item"><a href="http://www.juniper.net/us/en/company/" class="footer-link" target="">About Juniper</a></li>
            <li class="slice-item"><a href="http://www.juniper.net/us/en/partners/" class="footer-link" target="">Partners</a></li>
            <li class="slice-item"><a href="http://www.juniper.net/us/en/community/social/" class="footer-link" target="">Community</a></li>
        </ul>
        <ul class="footer-list slice slice-4col">
            <li class="slice-item">
                <ul>
                    <li><a href="http://www.juniper.net/us/en/how-to-buy/request-a-quote.page" class="footer-link" title="Request a Quote" target="_self">Request a Quote</a></li>
                    <li><a href="http://www.juniper.net/us/en/how-to-buy/" class="footer-link" title="How to Buy" target="_self">How to Buy</a></li>
                    <li><a href="http://www.juniper.net/us/en/feedback/" class="footer-link" title="Feedback" target="_self">Feedback</a></li>
                    <li><a href="http://www.juniper.net/us/en/contact-us/" class="footer-link" title="Contact Us" target="_self">Contact Us</a></li>
                    <li>
                        <a href="http://forums.juniper.net/" class="footer-link" title="" target="_blank"></a>
                    </li>
                    <li>
                        <a href="http://www.facebook.com/JuniperNetworks/" class="footer-link" title="" target="_blank"></a>
                    </li>
                    <li>
                        <a href="http://twitter.com/JuniperNetworks/" class="footer-link" title="" target="_blank"></a>
                    </li>
                    <li>
                        <a href="http://www.youtube.com/junipernetworks" class="footer-link" title="" target="_blank"></a>
                    </li>
                </ul>
            </li>
            <li class="slice-item">
                <ul>
                    <li><a href="http://www.juniper.net/us/en/company/careers/" class="footer-link" title="Careers" target="">Careers</a></li>
                    <li><a href="http://www.juniper.net/us/en/company/press-center/images/" class="footer-link" title="Image Library" target="">Image Library</a></li>
                    <li><a href="http://rss.juniper.net/" class="footer-link" title="RSS Feeds" target="_self">RSS Feeds</a></li>
                    <li><a href="http://www.juniper.net/us/en/accessibility/" class="footer-link" title="Accessibility" target="">Accessibility</a></li>
                </ul>
            </li>
            <li class="slice-item">
                <ul>
                    <li><a href="http://www.juniper.net/us/en/privacy-policy/" class="footer-link" title="Privacy Policy" target="">Privacy Policy</a></li>
                    <li><a href="http://www.juniper.net/us/en/legal-notices/" class="footer-link" title="Legal Notices" target="">Legal Notices</a></li>
                    <li><a href="http://www.juniper.net/us/en/site-map/" class="footer-link" title="Site Map" target="">Site Map</a></li>
                </ul>
            </li>
            <li class="slice-item ">
                <ul class="slice slice-4col footer-social">
                      <li>
                        <a href="http://forums.juniper.net/" title="" target="_blank" class="
							     footer-link icon icon-48 icon-jnet
						    " style="background-image: url('http://www.juniper.net/assets/svg/png/jnet.png');"></a>
                    </li>
                    <li>
                        <a href="http://www.facebook.com/JuniperNetworks/" title="" target="_blank" class="
							     footer-link icon icon-48 icon-jnet
						    " style="background-image: url('http://www.juniper.net/assets/svg/png/facebook.png');"></a>
                    </li>
                    <li>
                        <a href="http://twitter.com/JuniperNetworks/" title="" target="_blank" class="
							     footer-link icon icon-48 icon-jnet
						    " style="background-image: url('http://www.juniper.net/assets/svg/png/twitter.png');"></a>
                    </li>
                    <li>
                        <a href="http://www.youtube.com/junipernetworks" title="" target="_blank" class="
							     footer-link icon icon-48 icon-jnet
						    " style="background-image: url('http://www.juniper.net/assets/svg/png/youtube.png');"></a>
                    </li>
                    <li>
                        <a href="https://www.linkedin.com/company/juniper-networks" title="" target="_blank" class="footer-link icon icon-48 icon-linkedin-circle spaced-half-top" style="background-image: url('http://www.juniper.net/assets/svg/linkedin-circle.svg');"></a>
                    </li>
                    <li>
                        <a href="https://plus.google.com/101354207496812916953/about" title="" target="_blank" class="footer-link icon icon-48 icon-linkedin-circle spaced-half-top" style="background-image: url('http://www.juniper.net/assets/svg/googleplus.svg');"></a>
                    </li>
                </ul>
                <ul class="footer-select-wrapper">
                    <li>
                        <span class="selector-name">Country Selector</span>
                        <select class="country-select select icon-select-down select-91 select-ff" onChange="window.location=this.options[this.selectedIndex].value;" name="">
                            <option value="http://www.juniper.net/us/en/">United States</option>
                            <option value="http://www.juniper.net/de/de/">Deutschland - Germany</option>
                            <option value="http://www.juniper.net/fr/fr/">France</option>
                            <option value="http://www.juniper.net/uk/en/">United Kingdom</option>
                            <option value="http://www.juniper.net/cn/zh/">中国 - China</option>
                            <option value="http://www.juniper.net/jp/jp/">日本 - Japan</option>
                            <option value="http://www.juniper.net/kr/kr/">대한민국 - Korea</option>
                        </select>
                    </li>
                </ul>
            </li>
        </ul>
        <p class="paragraph-no-margin footer-copyright"> &copy; 1999 - 2020 Juniper Networks, Inc. All rights reserved</p>
    </div>
</div>

</div></span></div>
			<div class="PaneQ4Footer"><span class='Q4FooterDiv1'><div id="_ctrl0_ctl06_divModuleContainer" class="BlankModuleContainer">
    
    <script type="text/javascript">
var reset = 0;
var Q4web = {
    afancybox: function() {
        $('a.fancybox').fancybox();
        $('a.fancyboxIframe').fancybox({
            type: 'iframe',
            'height': 464,
            'width': 853
        });
    },
    add_header: function() {
        $('.jp.main-header').prependTo('body').find('.header-search-wrapper').wrapInner('<form class="header-search" action="#">');
    },
    place_holder: function(name, element) {
        $(element).val(name);
        $(element).focus(function() {
            if (element.value == name) element.value = '';
        });

        $(element).blur(function() {
            if (!element.value.length) element.value = name;
        });
    },
    place_holder_int: function() {
        $('.ModuleSearch').find('input.SearchInput').filter(function() {
            var name = "Search";
            Q4web.place_holder(name, this);
        });
        $('.PaneLeft .MailingListSignupContainer').find('input[type="text"]').filter(function() {
            var name = "Enter Email";
            Q4web.place_holder(name, this);
        });
        $(".PaneLeft .MailingListSignupContainer").find('input[type="text"]').on("keypress", function(e) {
            if (e.keyCode == 13) {
                $('.PaneLeft .MailingListSignupContainer .Button').trigger('click');
                return false;
            }
        });
    },
    removeAttributes: function() {
        $('.internal a').removeAttr('target');
    },
    search_bar: function() {
        var $nav = $('.main-header > nav'),
            $body = $('body');
        $('.header-search-submit').on('click', 'a, .icon-nav-search-white ', function(e) {
            e.preventDefault();
            $('.header-search').toggleClass('is-active');
            $('.header-search-input').focus();

            if ($nav.hasClass('is-displaying-menus')) {
                Q4web.close_nav();
                $body.removeClass('prevent-scroll');
            }

        });
        $('.header-search-input').on('blur', function() {
            $('.header-search').removeClass('is-active');
        });

        $('.header-search').on('submit', function(e) {
            e.preventDefault();
            window.location.replace('/Search-Results/default.aspx?SearchTerm=' + $('.header-search-input').val());
        });


    },
    nav_trigger: function() {
        var $navTrigger = $('.navbar-screen, .header-nav-control'),
            $menu = $('.main-header .top-menu'),
            $nav = $('.main-header > nav');


        $navTrigger.on('click', function() {
            $nav.hasClass('is-displaying-menus') ? Q4web.close_nav() : Q4web.open_nav();
            // $nav.hasClass('is-displaying-menus') ? $body.addClass('prevent-scroll') : $body.removeClass('prevent-scroll');
        });
    },
    open_nav: function() {
        var $nav = $('.main-header > nav'),
            $body = $('body');

        $nav.addClass('is-displaying-menus');
        $body.addClass('prevent-scroll');

    },
    close_nav: function() {
        var $nav = $('.main-header > nav'),
            $body = $('body');

        $nav.removeClass('is-displaying-menus');
        $body.removeClass('prevent-scroll');
    },
    nav_active: function() {
        var $menu = $('.main-header .top-menu');

        function add_menu_class() {
            if ($(window).width() <= 768) {
                if (reset == 0) {
                    $menu.addClass('is-active can-scroll');
                    reset = 1;
                }
            } else {
                if (reset == 1) {
                    $menu.removeClass('is-active can-scroll');
                    reset = 0;
                }
            }
        }
        add_menu_class();

        $(window).resize(function() {
            add_menu_class();
        });
    },
    navigation: function() {
        var $nav = $('.main-header > nav'),
            $menu = $('.main-header .top-menu');

        $menu.find('>li.nav-link-item').on({
            mouseenter: function() {
                var wwidth = $(window).width();
                if (wwidth > 768) {
                    var $this = $(this);

                    $this.addClass('hover').siblings('.hover').removeClass('hover');
                }
            },
            mouseleave: function() {
                var wwidth = $(window).width();
                if (wwidth > 768) {
                    var $this = $(this);

                    $this.removeClass('hover');
                }
            }
        });
    },
    navLevels: function() {
        var $nav = $('.main-header > nav'),
            $menu = $('.main-header .top-menu');

        $menu.on('click', '.has-submenu', function(e) {
            var $this = $(this),
                $parent = $(this).closest('li'),
                wwidth = $(window).width();

            if (wwidth <= 768) {
                e.preventDefault();
                $nav.addClass('is-back-active');
                $this.closest('.is-active.can-scroll').removeClass('is-active can-scroll').addClass('is-previous');
                $parent.find('.nav-link-list:first').addClass('is-active can-scroll');
            }
        });
        $nav.on('click', '.global-back-button a', function(e) {
            e.preventDefault();
        });
        $nav.on('click', '.global-back-button', function(e) {
            e.preventDefault();
            $menu.find('.is-active.can-scroll').removeClass('is-active can-scroll').closest('.is-previous').removeClass('is-previous').addClass('is-active can-scroll');
            if ($menu.hasClass('is-active')) {
                $nav.removeClass('is-back-active');
            }
        });
    },
    navResize: function() {
        var $nav = $('.main-header > nav'),
            $menu = $('.main-header .top-menu');

        $(window).on('resize', function() {
            var wwidth = $(window).width();
            if (wwidth <= 768) {
                $menu.find('.hover').removeClass('hover');
            } else {
                $('body').removeClass('prevent-scroll');
                $nav.removeClass('is-back-active');
                $nav.removeClass('is-displaying-menus').find('.is-previous').removeClass('is-previous');
                $nav.find('.is-active.can-scroll').removeClass('is-active can-scroll');
                $menu.addClass('is-active can-scroll');
            }
        });
    },
    irMobilaNav: function() {
        $('.IRmobileNav .level1 > li:first > a').before('<span class="menu-arrow"></span>');

        $('.IRmobileNav').on('click', '.level1 > li:first > .menu-arrow', function() {
            var $this = $(this),
                $parent = $this.parent();

            $parent.toggleClass('open');
        });
    },
    dropNav: function() {
        $('.dropNav .level2 .has-children.expanded').addClass('open');

        $('.dropNav .level2 .has-children > a').before('<span class="menu-arrow"></span>');

        $('.dropNav').on('click', '.level2 .has-children > .menu-arrow', function() {
            var $this = $(this),
                $parent = $this.parent();

            // if (!$parent.hasClass('open')) {
            //     e.preventDefault();
            $parent.toggleClass('open'); //.find('>ul').slideDown();
            $parent.siblings().removeClass('open'); //.find('>ul').slideUp();
            $parent.siblings().find('.open').removeClass('open'); //.find('ul').hide();
            // }

        });
    },
    accordions: function(acc_wrapper, accordion_trigger) {
        $(acc_wrapper).find(accordion_trigger).click(function() {

            //Expand or collapse this panel
            $(this).next().toggleClass('active-content');
            $(this).toggleClass('active');

            // //Hide the other panels
            // $(".accordion-content").not($(this).next()).slideUp('fast');
            // $(".accordion-toggle").not($(this)).removeClass('active');

        });
    },
    init_plugins: function() {
        $('input').iCheck({
            checkboxClass: 'icheckbox_flat-blue',
            radioClass: 'iradio_flat-blue',
        });
    },
    init: function() {
        this.init_plugins();
        this.add_header();
        this.afancybox();
        this.place_holder_int();
        this.removeAttributes();
        this.search_bar();
        this.nav_active();
        this.nav_trigger();
        this.navigation();
        this.navLevels();
        this.navResize();
        this.irMobilaNav();
        this.dropNav();
    }
}

$(document).ready(function() {
    Q4web.init();

});
</script>
<!--[if lt IE 7 ]><script>$('html').addClass('ie6');</script><![endif]-->
<!--[if IE 7 ]><script>$('html').addClass('ie7');</script><![endif]-->
<!--[if IE 8 ]><script>$('html').addClass('ie8');</script><![endif]-->
<!--[if IE 9 ]><script>$('html').addClass('ie9');</script><![endif]-->
<!--[if lt IE 7 ]><script src="//ajax.googleapis.com/ajax/libs/chrome-frame/1.0.3/CFInstall.min.js"></script>
    <script>window.attachEvent("onload",function(){CFInstall.check({mode:"overlay"})});</script><![endif]-->

</div></span><span class='Q4FooterDiv12'><div id="_ctrl0_ctl39_divModuleContainer" class="BlankModuleContainer">
    
    <!--[if gte IE 8]>
<style type="text/css">
 .stockHistorical button.lookup {
    padding:2px 20px;
}
.secNav ul.level2 li.has-children.open > .menu-arrow,
.FaqContainer .FaqDetailList h3.active:before {
    background-image: url("//s1.q4cdn.com/608738804/files/design/arrow_up.png");
}
.secNav ul.level2 li.has-children > .menu-arrow,
.FaqContainer .FaqDetailList h3:before {
    background-image: url("//s1.q4cdn.com/608738804/files/design/arrow_down.png");
}
</style>
<![endif]-->
</div></span><span class='Q4FooterDiv13'><div id="_ctrl0_ctl42_divModuleContainer" class="BlankModuleContainer">
    
    <script type="text/javascript">_satellite.pageBottom();</script>
</div></span><span class='Q4FooterDiv6'><div id="_ctrl0_ctl63_divModuleContainer" class="BlankModuleContainer">
    <h1 id="_ctrl0_ctl63_lblTitle">
        <span id="_ctrl0_ctl63_lblModuleTitle" class="ModuleTitle">script</span>
    </h1>
    <script>
$(document).ready(function() {
   if ($('.upcomingEv .ModuleItemRow ').length == 0) {
        $('.upcomingEv .ModuleHeader').hide();
   }
})
</script>
</div></span></div>
		</div>
	</div>
</div>

                    <input type="hidden" name="__antiCSRF" id="__antiCSRF" value=""/>
                
<script type="text/javascript">
//<![CDATA[
var Page_ValidationSummaries =  new Array(document.getElementById("_ctrl0_ctl30_validationsummary"));
var Page_Validators =  new Array(document.getElementById("_ctrl0_ctl30_regexEmailValidator1"), document.getElementById("_ctrl0_ctl30_reqvalEmailValidator1"), document.getElementById("_ctrl0_ctl30_cusvalMailingListsValidator"), document.getElementById("_ctrl0_ctl30_UCCaptcha_RequiredFieldValidator1"));
//]]>
</script>

<script type="text/javascript">
//<![CDATA[
var _ctrl0_ctl30_regexEmailValidator1 = document.all ? document.all["_ctrl0_ctl30_regexEmailValidator1"] : document.getElementById("_ctrl0_ctl30_regexEmailValidator1");
_ctrl0_ctl30_regexEmailValidator1.controltovalidate = "_ctrl0_ctl30_txtEmail";
_ctrl0_ctl30_regexEmailValidator1.errormessage = "Email address is not valid.";
_ctrl0_ctl30_regexEmailValidator1.display = "None";
_ctrl0_ctl30_regexEmailValidator1.validationGroup = "990f35bf-ea02-4d65-8d51-94f88db5f113";
_ctrl0_ctl30_regexEmailValidator1.evaluationfunction = "RegularExpressionValidatorEvaluateIsValid";
_ctrl0_ctl30_regexEmailValidator1.validationexpression = "^([a-zA-Z0-9_\\-\\.]+)@((\\[[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.)|(([a-zA-Z0-9\\-]+\\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\\]?)$";
var _ctrl0_ctl30_reqvalEmailValidator1 = document.all ? document.all["_ctrl0_ctl30_reqvalEmailValidator1"] : document.getElementById("_ctrl0_ctl30_reqvalEmailValidator1");
_ctrl0_ctl30_reqvalEmailValidator1.controltovalidate = "_ctrl0_ctl30_txtEmail";
_ctrl0_ctl30_reqvalEmailValidator1.errormessage = "Email address is required.";
_ctrl0_ctl30_reqvalEmailValidator1.display = "None";
_ctrl0_ctl30_reqvalEmailValidator1.validationGroup = "990f35bf-ea02-4d65-8d51-94f88db5f113";
_ctrl0_ctl30_reqvalEmailValidator1.evaluationfunction = "RequiredFieldValidatorEvaluateIsValid";
_ctrl0_ctl30_reqvalEmailValidator1.initialvalue = "";
var _ctrl0_ctl30_cusvalMailingListsValidator = document.all ? document.all["_ctrl0_ctl30_cusvalMailingListsValidator"] : document.getElementById("_ctrl0_ctl30_cusvalMailingListsValidator");
_ctrl0_ctl30_cusvalMailingListsValidator.errormessage = "Mailing list selection is required.";
_ctrl0_ctl30_cusvalMailingListsValidator.display = "None";
_ctrl0_ctl30_cusvalMailingListsValidator.enabled = "False";
_ctrl0_ctl30_cusvalMailingListsValidator.validationGroup = "990f35bf-ea02-4d65-8d51-94f88db5f113";
_ctrl0_ctl30_cusvalMailingListsValidator.evaluationfunction = "CustomValidatorEvaluateIsValid";
var _ctrl0_ctl30_validationsummary = document.all ? document.all["_ctrl0_ctl30_validationsummary"] : document.getElementById("_ctrl0_ctl30_validationsummary");
_ctrl0_ctl30_validationsummary.displaymode = "List";
_ctrl0_ctl30_validationsummary.validationGroup = "990f35bf-ea02-4d65-8d51-94f88db5f113";
var _ctrl0_ctl30_UCCaptcha_RequiredFieldValidator1 = document.all ? document.all["_ctrl0_ctl30_UCCaptcha_RequiredFieldValidator1"] : document.getElementById("_ctrl0_ctl30_UCCaptcha_RequiredFieldValidator1");
_ctrl0_ctl30_UCCaptcha_RequiredFieldValidator1.controltovalidate = "_ctrl0_ctl30_UCCaptcha_txtCode";
_ctrl0_ctl30_UCCaptcha_RequiredFieldValidator1.focusOnError = "t";
_ctrl0_ctl30_UCCaptcha_RequiredFieldValidator1.errormessage = "Please provide the code.";
_ctrl0_ctl30_UCCaptcha_RequiredFieldValidator1.display = "Dynamic";
_ctrl0_ctl30_UCCaptcha_RequiredFieldValidator1.validationGroup = "990f35bf-ea02-4d65-8d51-94f88db5f113";
_ctrl0_ctl30_UCCaptcha_RequiredFieldValidator1.evaluationfunction = "RequiredFieldValidatorEvaluateIsValid";
_ctrl0_ctl30_UCCaptcha_RequiredFieldValidator1.initialvalue = "";
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
