// Use already bundled Playwright; no installation, no external-data mutation.
const {chromium} = require('C:/Users/ASUS/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs = require('fs');
const path = require('path');
(async () => {
  const out = path.resolve('tmp/task-017/portal');
  fs.mkdirSync(out,{recursive:true});
  const browser = await chromium.launch({headless:true});
  try {
    const page = await browser.newPage({viewport:{width:1920,height:1080}});
    const errors=[];
    page.on('pageerror',e=>errors.push(e.message));
    const base='http://127.0.0.1:8017/';
    await page.goto(base+'task-007-candidate-direction.html',{waitUntil:'networkidle'});
    await page.waitForFunction(()=>document.querySelectorAll('.mermaid svg').length===3,{timeout:20000});
    await page.screenshot({path:path.join(out,'candidate-overview.png')});
    await page.locator('.mermaid').nth(1).scrollIntoViewIfNeeded();
    await page.screenshot({path:path.join(out,'candidate-harness.png')});
    await page.locator('table').nth(1).scrollIntoViewIfNeeded();
    await page.screenshot({path:path.join(out,'candidate-comparison.png')});
    const links=await page.locator('.md-content a[href]').evaluateAll(as=>as.map(a=>a.href));
    const local=[];
    for(const href of [...new Set(links.filter(x=>x.startsWith(base)))]) {
      const u=new URL(href);
      const r=await page.request.get(u.origin+u.pathname);
      if(!r.ok()) throw new Error('Broken local link '+href);
      if(u.hash) {
        const html=await r.text();
        const id=decodeURIComponent(u.hash.slice(1));
        if(!html.includes('id="'+id+'"')) throw new Error('Missing anchor '+href);
      }
      local.push(href);
    }
    await page.goto(base,{waitUntil:'networkidle'});
    if(!await page.locator('.md-content a[href="task-007-candidate-direction.html"]').count()) throw new Error('Homepage entrance missing');
    await page.screenshot({path:path.join(out,'homepage.png')});
    if(errors.length) throw new Error(errors.join('\n'));
    const result={desktop_viewport:'1920x1080',mermaid_rendered:3,local_links_checked:local.length,console_errors:errors,mobile_test:'NOT REQUESTED'};
    fs.writeFileSync(path.join(out,'qa.json'),JSON.stringify(result,null,2));
    console.log(JSON.stringify(result));
  } finally {await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
