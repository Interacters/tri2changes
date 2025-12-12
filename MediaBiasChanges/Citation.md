<style>
  .cite-card { background: linear-gradient(160deg,  #555dc2d2, #564ea0ff); color:#e6f2ff; padding:18px; border-radius:12px; margin:20px 0; }
  .cite-row { display:flex; gap:10px; flex-wrap:wrap; align-items:center; margin-top:8px; }
  .cite-label { min-width:110px; font-weight:700; color:#d6e9ff; }
  .cite-input, .cite-select { flex:1; padding:8px; border-radius:6px; border:1px solid rgba(255,255,255,0.06); background:rgba(255,255,255,0.02); color:inherit; }
  .cite-actions { display:flex; gap:10px; margin-top:12px; justify-content:flex-end; }
  .cite-btn { padding:8px 12px; border-radius:8px; border:none; cursor:pointer; font-weight:700; }
  .cite-btn.primary { background:#7ad2f9; color:#082033; }
  .cite-btn.ghost { background:rgba(255,255,255,0.06); color:#d6e6ff; border:1px solid rgba(255,255,255,0.04); }
  .cite-output { margin-top:12px; background:rgba(0,0,0,0.25); padding:12px; border-radius:8px; font-family:system-ui, -apple-system, sans-serif; color:#eaf6ff; }
  .cite-small { font-size:0.9rem; color:#9fb7da; margin-top:6px; }
</style>

<div class="intro-text">
   <h2>Citation Generator</h2>
    <p>It's important to include correct citations for your work. There are many types of formats for citations including: MLA, APA, Chicago. This tool can help you create citations for your sources.
    </p>
</div>
<div class="cite-card" id="citation-tool">
  <div class="cite-row">
    <div class="cite-label">Style</div>
    <select id="cite-style" class="cite-select">
      <option value="apa">APA</option>
      <option value="mla">MLA (9th ed.)</option>
      <option value="chicago">Chicago (author-date)</option>
    </select>
  </div>

  <div class="cite-row">
    <div class="cite-label">Author(s)</div>
    <input id="cite-author" class="cite-input" placeholder="e.g., Doe, J.; Last, F." />
  </div>

  <div class="cite-row">
    <div class="cite-label">Date</div>
    <input id="cite-date" class="cite-input" placeholder="e.g., 2025, May 10 or 2025" />
  </div>

  <div class="cite-row">
    <div class="cite-label">Title</div>
    <input id="cite-title" class="cite-input" placeholder="Article title (no italics markup)" />
  </div>

  <div class="cite-row">
    <div class="cite-label">Source</div>
    <input id="cite-source" class="cite-input" placeholder="e.g., The New York Times" />
  </div>

  <div class="cite-row">
    <div class="cite-label">URL</div>
    <input id="cite-url" class="cite-input" placeholder="https://..." />
    <button id="cite-fetch-metadata" class="cite-btn ghost" title="Fetch metadata from URL" style="margin-left:8px;min-width:120px;">Fetch from URL</button>
  </div>

  <div class="cite-actions">
    <button id="cite-generate" class="cite-btn primary">Generate</button>
    <button id="cite-copy" class="cite-btn ghost">Copy</button>
    <button id="cite-save" class="cite-btn ghost" title="Save locally">Save</button>
    <button id="cite-load" class="cite-btn ghost" title="Load last">Load</button>
  </div>

  <div id="cite-output" class="cite-output" aria-live="polite"></div>
  <div class="cite-small">Formats: APA, MLA (9th ed.), Chicago (author-date). Saved citations are stored locally in your browser.</div>
</div>

<script>
(function(){
  const styleEl = document.getElementById('cite-style');
  const authorEl = document.getElementById('cite-author');
  const dateEl = document.getElementById('cite-date');
  const titleEl = document.getElementById('cite-title');
  const sourceEl = document.getElementById('cite-source');
  const urlEl = document.getElementById('cite-url');
  const outEl = document.getElementById('cite-output');
  const fetchBtn = document.getElementById('cite-fetch-metadata');

  // DEV default -> ensure this points to your Flask backend (no trailing slash)
if (!window.fetchProxyBase) {
    window.fetchProxyBase = 'http://localhost:8001/api/media';
    console.info('fetchProxyBase defaulted to', window.fetchProxyBase);
}

  const KEY = 'biasGame_citations_v1';

  function safe(val, fallback='') { return (val || '').trim(); }

function fmtAPA({author, date, title, source, url}) {
  let parts = [];
  if (author) parts.push(author);
  if (date) parts.push(`(${date})`);
  if (title) parts.push(title ? `<i>${title}</i>` : null);
  if (source) parts.push(`${source}.`);
  if (url) parts.push(url);
  return parts.filter(Boolean).join(' ').trim();
}

function fmtMLA9({author, date, title, source, url}) {
  let parts = [];
  if (author) parts.push(`${author}.`);
  if (title) parts.push(title ? `"${title}."` : null);
  if (source) parts.push(source + ',');
  if (date) parts.push(date + ',');
  if (url) parts.push(url);
  return parts.filter(Boolean).join(' ').replace(/\s+/g,' ').trim();
}

function fmtChicago({author, date, title, source, url}) {
  let parts = [];
  if (author) parts.push(author);
  if (date) parts.push(date);
  if (title) parts.push(title ? `"${title}."` : null);
  if (source) parts.push(source ? source + '.' : null);
  if (url) parts.push(url);
  return parts.filter(Boolean).join(' ').replace(/\s+/g,' ').trim();
}

  function generate() {
    const payload = {
      author: safe(authorEl.value),
      date: safe(dateEl.value),
      title: safe(titleEl.value),
      source: safe(sourceEl.value),
                     url: safe(urlEl.value)
    };
    const style = styleEl.value;
    let citation = '';
    if (style === 'mla') citation = fmtMLA9(payload);
    else if (style === 'chicago') citation = fmtChicago(payload);
    else citation = fmtAPA(payload);

    outEl.innerHTML = citation;
    return citation;
  }

  function copyToClipboard(text) {
    if (!navigator.clipboard) {
      const ta = document.createElement('textarea');
      ta.value = text;
      document.body.appendChild(ta);
      ta.select();
      try { document.execCommand('copy'); } catch (e) {}
      ta.remove();
      alert('Citation copied (fallback).');
      return;
    }
    navigator.clipboard.writeText(text).catch(() => { alert('Copy failed.'); });
  }

  function save() {
    const citation = generate();
    const saved = JSON.parse(localStorage.getItem(KEY) || '[]');
    saved.push({ citation, at: Date.now() });
    localStorage.setItem(KEY, JSON.stringify(saved.slice(-50)));
    alert('Citation saved locally.');
  }

  function loadLast() {
    const saved = JSON.parse(localStorage.getItem(KEY) || '[]');
    if (!saved.length) { alert('No saved citations.'); return; }
    const last = saved[saved.length - 1];
    outEl.innerHTML = last.citation;
  }

  async function tryFetchHtml(url) {
    // Try direct fetch first (may fail due to CORS)
    try {
      const r = await fetch(url, { method: 'GET', mode: 'cors' });
      if (r.ok) return await r.text();
    } catch (err) {
      console.warn('Direct fetch failed (CORS?), will try proxy', err);
    }
    // Fallback to AllOrigins public proxy (rate-limited). Replace with your own proxy for production.
    try {
      const proxy = 'https://api.allorigins.win/raw?url=' + encodeURIComponent(url);
      const r2 = await fetch(proxy);
      if (r2.ok) return await r2.text();
    } catch (err) {
      console.warn('Proxy fetch failed', err);
    }
    return null;
  }

  function parseMetadataFromHtml(html, url) {
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');
    const getMeta = (name, prop) => {
      const byName = doc.querySelector(`meta[name="${name}"]`);
      if (byName && byName.content) return byName.content;
      const byProp = doc.querySelector(`meta[property="${prop}"]`);
      if (byProp && byProp.content) return byProp.content;
      const byLink = doc.querySelector(`link[rel="canonical"]`);
      if (name === 'url' && byLink && byLink.href) return byLink.href;
      return null;
    };

    const title = getMeta('title','og:title') || doc.querySelector('title')?.textContent || getMeta('twitter:title','twitter:title');
    const site = getMeta('site_name','og:site_name') || (new URL(url)).hostname.replace(/^www\./,'');
    const author = getMeta('author','article:author') || getMeta('author','og:author') || getMeta('byline','byline');
    const published = getMeta('date','article:published_time') || getMeta('publication_date','publication_date') || getMeta('date','og:updated_time') || getMeta('pubdate','pubdate');

    return { title, site, author, published, url };
  }

  // Format published timestamps into user-friendly strings for each citation style.
  function formatPublishedDate(raw) {
    if (!raw) return null;
    // try parse ISO / common date strings
    const ms = Date.parse(raw);
    if (isNaN(ms)) {
      return { apa: raw, mla: raw, chicago: raw };
    }
    const d = new Date(ms);
    // use UTC parts to avoid timezone shifts from ISO Z strings
    const year = d.getUTCFullYear();
    const monthIdx = d.getUTCMonth();
    const day = d.getUTCDate();
    const months = ['January','February','March','April','May','June','July','August','September','October','November','December'];
    const monthName = months[monthIdx];
    return {
      apa: `${year}, ${monthName} ${day}`,      // e.g. "2025, December 4"
      mla: `${day} ${monthName} ${year}`,       // e.g. "4 December 2025"
      chicago: `${year}`                        // Chicago author-date often uses just year for in-text
    };
  }
  
  // try server-side metadata fetch (Flask) — returns { title, author, published, site, url } or throws
  async function fetchMetadataFromServer(targetUrl) {
    const base = (window.fetchProxyBase || '').replace(/\/$/, '');
    if (!base) {
      console.warn('No fetchProxyBase set; skipping server fetch');
      return null;
    }

    try {
      const endpoint = `${base}/fetch_meta?url=${encodeURIComponent(targetUrl)}`;
      console.info('Calling server metadata endpoint:', endpoint);
      const res = await fetch(endpoint, { method: 'GET' });

      // read response body safely (JSON preferred)
      const ct = res.headers.get('content-type') || '';
      const body = ct.includes('application/json') ? await res.json().catch(()=>null) : await res.text().catch(()=>null);

      if (!res.ok) {
        console.warn('Server fetch_meta returned non-OK', res.status, body);
        // show a helpful alert in dev so you know why client fell back
        const detail = body && body.detail ? body.detail : (typeof body === 'string' ? body : JSON.stringify(body));
        alert('Server metadata fetch failed: ' + (detail || res.status));
        return null;
      }

      console.info('Server metadata response', body);
      return body;
    } catch (err) {
      console.warn('Server metadata fetch failed (network)', err);
      alert('Server metadata fetch network error: ' + (err && err.message ? err.message : err));
      return null;
    }
  }

  // try server first, then fallback to client fetch + AllOrigins proxy
  async function fetchAndFill() {
    const url = (urlEl.value || '').trim();
    if (!url) { alert('Enter a URL first.'); return; }
    fetchBtn.textContent = 'Fetching…';
    fetchBtn.disabled = true;
    try {
      // server attempt
      let meta = await fetchMetadataFromServer(url);

      // client fallback
      if (!meta) {
        const html = await tryFetchHtml(url);
        if (!html) {
          alert('Failed to fetch page. CORS or proxy error. Consider enabling your Flask proxy.');
          return;
        }
        meta = parseMetadataFromHtml(html, url);
      }

      if (meta.author) authorEl.value = meta.author;
      if (meta.published) {
        const fmt = formatPublishedDate(meta.published);
        const style = (styleEl && styleEl.value) ? styleEl.value : 'apa';
        dateEl.value = (fmt && fmt[style]) ? fmt[style] : meta.published;
      }
      if (meta.title) titleEl.value = meta.title;
      if (meta.site) sourceEl.value = meta.site;
      urlEl.value = meta.url || url;
      generate();
    } catch (err) {
      console.warn(err);
      alert('Error fetching metadata.');
    } finally {
      fetchBtn.textContent = 'Fetch from URL';
      fetchBtn.disabled = false;
    }
  }

  fetchBtn.addEventListener('click', fetchAndFill);

// authorEl.value = '';
// dateEl.value = '';
// titleEl.value = '';
// sourceEl.value = '';
// urlEl.value = '';
// generate();
})();
</script>