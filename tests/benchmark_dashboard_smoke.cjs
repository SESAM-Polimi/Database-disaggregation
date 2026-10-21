// DOM unit smoke test, not a visual browser test. Use synthetic exported data.
// npm install --prefix /tmp/benchmark-dom --no-audit --no-fund jsdom@26.1.0
// NODE_PATH=/tmp/benchmark-dom/node_modules node tests/benchmark_dashboard_smoke.cjs fixture.html
'use strict';
const assert=require('node:assert/strict'), fs=require('node:fs');
const {JSDOM, VirtualConsole}=require('jsdom');
const errors=[], downloads=[], blobs=[], virtualConsole=new VirtualConsole();
virtualConsole.on('jsdomError',e=>errors.push(String(e)));
const dom=new JSDOM(fs.readFileSync(process.argv[2],'utf8'),{
  runScripts:'dangerously', pretendToBeVisual:true, virtualConsole,
  beforeParse(window){
    window.HTMLElement.prototype.scrollIntoView=function(){};
    window.scrollTo=()=>{};
    window.URL.createObjectURL=b=>{blobs.push(b);return 'blob:test'};
    window.URL.revokeObjectURL=()=>{};
    window.Blob=class{constructor(parts,options){this.parts=parts;this.type=options.type}};
    window.document.addEventListener('click',e=>{if(e.target.tagName==='A'){downloads.push(e.target.download);e.preventDefault()}},true);
  }
});
const {document, Event, KeyboardEvent}=dom.window;
const el=id=>document.getElementById(id);
function change(id,value){el(id).value=value;el(id).dispatchEvent(new Event('input',{bubbles:true}));el(id).dispatchEvent(new Event('change',{bubbles:true}))}
assert.equal(errors.length,0,errors.join('\n'));
assert.match(el('checks').textContent,/PASS/);
assert.match(el('subtitle').textContent,/regions/);
el('tab-explorer').click();assert.equal(el('explorer').hidden,false);assert.equal(el('overview').hidden,true);
change('explore-search','THIS DOES NOT EXIST');assert.match(el('explore-count').textContent,/0 sector/);
change('explore-search','C');change('explore-region','');change('explore-metric','multiplier');
assert.ok(el('explore-table').querySelector('[data-sector-index]'));
el('explore-table').querySelector('[data-sector-index]').click();assert.match(el('detail-name').textContent,/C/);
assert.ok(el('input-chart').querySelector('[role=img]'));
el('tab-trade').click();change('trade-mode','delta');assert.match(el('trade-matrix').textContent,/pp/);
assert.doesNotMatch(el('trade-matrix').textContent,/NaN|undefined/);
el('tab-system').click();assert.match(el('system-diagnostics').textContent,/Spectral radius/);
assert.equal(el('shock-sector'),null);assert.doesNotMatch(document.body.textContent,/\+1 M USD/);
el('tab-review').click();change('review-metric','Negative Labor');assert.match(el('review-count').textContent,/1 findings/);
el('review-table').querySelector('[data-sector-index]').click();assert.equal(el('explorer').hidden,false);
el('tab-overview').dispatchEvent(new KeyboardEvent('keydown',{key:'ArrowRight',bubbles:true}));assert.equal(el('explorer').hidden,false);
el('download-json').click();el('download-sectors').click();el('export-review').click();el('export-trade').click();
assert.equal(downloads.length,4);assert.ok(JSON.parse(blobs[0].parts[0]).summary);
assert.match(blobs[1].parts[0],/"multiplier"/);
assert.equal(errors.length,0,errors.join('\n'));
console.log('DOM smoke passed: tabs, filters, detail, trade, system diagnostics, review and four downloads.');
dom.window.close();
