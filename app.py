"""Launch the paper model workbench in Streamlit."""

import streamlit as st


st.set_page_config(
    page_title="纸模工坊",
    page_icon="✂️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.html("""
<style>
[data-testid="stHeader"] { display: none; }
[data-testid="stMainBlockContainer"] { max-width: none; padding: 0; }
[data-testid="stMainBlockContainer"] iframe { height: 100dvh !important; }
</style>
""")

# The complete workbench is embedded so cloud deployment needs only this entry file.
page = r'''<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#f7f9fa">
<meta name="description" content="从截图裁切纸模展开图，独立设置长宽高并预览折叠，生成按实际尺寸打印的 PDF。">
<title>纸模工坊 · 纸模打印工作台</title>
<style>
:root{font-family:"Microsoft YaHei","PingFang SC","Noto Sans CJK SC",system-ui,sans-serif;color:#182f30;background:#f6f8f8;font-size:14px;--jade:#126856;--dark:#153e37;--soft:#e7f4ee;--line:#dce5e3;--muted:#607573}
*{box-sizing:border-box}
body{margin:0;min-width:320px}
button,input,select{font:inherit}
button{cursor:pointer}
button:disabled{opacity:.47;cursor:default}
:focus-visible{outline:3px solid #34a790;outline-offset:3px}
[hidden]{display:none!important}
header{height:68px;background:white;border-bottom:1px solid var(--line)}
.bar,.wrap{max-width:1440px;margin:auto;padding-inline:clamp(20px,5.1vw,76px)}
.bar{height:100%;display:flex;justify-content:space-between;align-items:center}
.brand,.local,.title-row,.card-head,.file,.panel-head,.actions,.details,.pages,.footer,.dialog-head,.dialog-foot,.chips{display:flex;align-items:center}
.brand{gap:11px;color:#153a32;font-size:18px;font-weight:750;letter-spacing:.02em}
.logo{display:grid;place-items:center;width:37px;height:37px;border-radius:11px;background:#155e4f;color:white}
.local{gap:7px;color:var(--muted);font-size:12px}
.wrap{padding-top:34px;padding-bottom:26px}
.title-row{justify-content:space-between;gap:20px;margin-bottom:26px}
h1,h2,h3,p{margin:0}
h1{font-size:clamp(25px,3.5vw,39px);letter-spacing:-.045em;line-height:1.2;color:#12342d}
.intro{color:var(--muted);margin-top:9px;font-size:13px;line-height:1.6}
.layout{display:grid;grid-template-columns:328px minmax(0,1fr);gap:22px;align-items:start}
.sidebar{display:grid;gap:14px}
.card,.workspace{border:1px solid var(--line);border-radius:16px;background:#fff;overflow:hidden;box-shadow:0 2px 5px #163b3310}
.card{padding:17px 18px}
.card-head,.panel-head{justify-content:space-between;gap:10px}
.card-head{margin-bottom:13px}
h2{font-size:15px;font-weight:750;letter-spacing:.01em}
.label-icon{display:inline-flex;align-items:center;gap:9px}
.label-icon svg{color:#207b66}
.muted{color:var(--muted);font-size:12px;line-height:1.55}
.upload{width:100%;padding:14px 10px;border:1px dashed #91bcae;border-radius:10px;background:#f6fbf9;color:var(--jade);display:flex;flex-direction:column;align-items:center;gap:4px;font-weight:700}
.upload:hover,.upload.drag{background:#e6f5ef;border-color:#207b66}
.upload .muted{font-weight:400}
.file-list{display:grid;gap:5px;margin-top:10px;max-height:133px;overflow:auto}
.file{gap:8px;padding:6px 8px;border:1px solid #e4eeeb;border-radius:8px;background:#f8fbfa;min-height:43px}
.file canvas{width:33px;height:25px;object-fit:contain;background:white;border:1px solid #e4eeeb;border-radius:3px}
.file-name{flex:1;min-width:0;font-size:12px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.icon-button,.link-button{display:inline-grid;place-items:center;border:0;background:transparent;color:var(--jade);padding:5px;border-radius:6px}
.link-button{font-size:12px;padding:0}
.icon-button:hover,.link-button:hover{background:#eaf4ef}
.field-label{display:block;font-size:12px;font-weight:700;margin-bottom:7px;color:#3a5350}
.field{height:39px;width:100%;border-radius:8px;border:1px solid #d5e2df;background:#fff;color:#193d35;padding:0 11px}
.input-wrap{position:relative}
.input-wrap .field{padding-right:64px;font-weight:700}
.unit{position:absolute;pointer-events:none;right:27px;top:11px;color:var(--muted);font-size:12px}
.chips{gap:6px;margin-top:9px}
.chip{flex:1;white-space:nowrap;padding:6px 2px;background:white;color:#44625d;border:1px solid #dce7e3;border-radius:7px;font-size:11px}
.chip:hover,.chip[aria-pressed=true]{background:#eaf6f0;color:#146551;border-color:#a6cdbc}
.fields{display:grid;grid-template-columns:1fr 1fr;gap:11px;margin-top:15px}
.workspace{display:flex;flex-direction:column}
.panel-head{padding:16px 19px;min-height:67px;border-bottom:1px solid var(--line)}
.panel-head p{margin-top:4px}
.actions{gap:8px;flex-wrap:wrap;justify-content:flex-end}
.btn{height:37px;padding:0 12px;border-radius:8px;border:1px solid #d9e6e1;color:#255750;background:white;display:inline-flex;align-items:center;justify-content:center;gap:7px;white-space:nowrap;font-size:12px;font-weight:700}
.btn:hover:not(:disabled){background:#ecf6f1}
.btn.primary{background:#126856;color:white;border-color:#126856}
.btn.primary:hover:not(:disabled){background:#094f41}
.stage{min-height:535px;height:clamp(535px,65vh,720px);display:grid;place-items:center;padding:32px;overflow:auto;background-color:#e8efed;background-image:radial-gradient(#b5c9c3 0.8px,transparent .8px);background-size:14px 14px}
.paper{display:block;max-width:100%;max-height:100%;object-fit:contain;background:#fff;box-shadow:0 4px 8px #163b3318,0 18px 38px #244e4321}
.empty{text-align:center;color:#506863;max-width:350px;line-height:1.7;padding:18px;border-radius:10px;background:#f6fbf8}
.footer{min-height:53px;padding:10px 19px;justify-content:space-between;gap:12px;font-size:11px;color:var(--muted)}
.details,.pages{gap:8px;flex-wrap:wrap}
.paper-size{font-weight:700;color:#2f6356;background:#eaf5ef;border-radius:5px;padding:3px 6px}
.print-note{margin:12px 1px 0;text-align:right}
.message{color:#a03b2a;margin-top:8px;font-size:12px;line-height:1.55}
svg{width:17px;height:17px;flex:none}
.logo svg{width:23px;height:23px}
dialog{width:min(920px,calc(100vw - 24px));max-height:calc(100dvh - 25px);border:1px solid var(--line);border-radius:15px;padding:0;color:inherit;box-shadow:0 18px 75px #122a2450}
dialog::backdrop{background:#122a2470}
.dialog-head,.dialog-foot{justify-content:space-between;gap:10px;padding:14px 18px}
.dialog-head{border-bottom:1px solid var(--line)}
.dialog-foot{border-top:1px solid var(--line);flex-wrap:wrap}
.dialog-body{padding:14px 18px;display:grid;grid-template-columns:minmax(0,1fr) 208px;gap:16px}
.crop-stage{display:grid;place-items:center;border-radius:8px;background:#edf2f0;padding:8px;min-height:240px}
#sourceCanvas{display:block;max-width:100%;max-height:56vh;object-fit:contain;touch-action:none;cursor:crosshair}
.candidates{margin:8px 0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:6px;max-height:34vh;overflow:auto}
.candidate{background:white;border:1px solid var(--line);border-radius:6px;padding:4px;min-width:0;color:#355851;font-size:11px}
.candidate[aria-pressed=true]{border-color:#1b806a;background:#eaf5ef}
.candidate canvas{display:block;width:100%;height:46px;object-fit:contain}
.crop-help{margin-top:8px}
#printFrames{display:none}
@media(max-width:900px){.layout{grid-template-columns:270px minmax(0,1fr);gap:14px}.panel-head{align-items:flex-start}.panel-head .muted{max-width:180px}.stage{padding:24px}}
@media(max-width:710px){.layout{grid-template-columns:1fr}.wrap{padding-top:24px}.title-row{margin-bottom:18px}.stage{height:540px;min-height:0;padding:24px}.intro{max-width:320px}.footer{flex-wrap:wrap}.dialog-body{grid-template-columns:1fr}.candidates{grid-template-columns:repeat(auto-fill,minmax(58px,1fr));max-height:112px}#sourceCanvas{max-height:38vh}}
@media(max-width:410px){.wrap,.bar{padding-inline:12px}.panel-head,.footer{padding-inline:12px}.btn{padding-inline:8px}.stage{height:425px;padding:18px}.actions{gap:5px}}
:root{--jade:#24584d;--dark:#263b32;--line:#e2dcd0;--muted:#6b7064;color:#293a32;background:#f5f2eb}
header{height:64px;background:#fdfbf6}
.bar,.wrap{max-width:1680px;padding-inline:clamp(14px,2.6vw,40px)}
.wrap{padding-top:25px}
.title-row{margin-bottom:20px}
h1{font-size:clamp(25px,3vw,35px);color:#253d32}
.logo{background:#28584b}
.layout{grid-template-columns:minmax(0,1fr) minmax(0,1fr) 294px;gap:12px;align-items:start}
.sidebar{grid-column:3;grid-row:1;gap:10px}
.flat-view{grid-column:1;grid-row:1}
.model-view{grid-column:2;grid-row:1}
.card,.workspace{border-radius:11px;background:#fdfbf6}
.card{padding:14px}
.card-head{margin-bottom:11px}
.panel-head{min-height:61px;padding:12px 13px;align-items:center}
.stage{padding:12px;height:clamp(415px,66vh,680px);min-height:0;position:relative;grid-template-rows:minmax(0,1fr);background-color:#f3eee2;background-image:linear-gradient(#d9cfbe83 1px,transparent 1px),linear-gradient(90deg,#d9cfbe83 1px,transparent 1px),linear-gradient(#d9cfbe49 1px,transparent 1px),linear-gradient(90deg,#d9cfbe49 1px,transparent 1px);background-size:80px 80px,80px 80px,16px 16px,16px 16px;background-position:center}
.stage>canvas{grid-area:1/1;width:100%;height:100%;min-width:0;min-height:0}
.stage>.paper{width:auto;height:auto}
.stage>.empty{grid-area:1/1;z-index:1;background:#fdfbf6;border:1px solid var(--line)}
.footer{border-top:1px solid var(--line);padding:7px 13px;min-height:45px}
.view-switch{display:flex;gap:2px;background:#eee9de;padding:3px;border-radius:7px}
.view-switch button{border:0;background:transparent;border-radius:5px;padding:5px 7px;white-space:nowrap;color:#525e52;font-size:11px}
.view-switch button[aria-pressed=true]{background:#fffdf8;color:#25594b;box-shadow:0 1px 2px #715a361c}
.view-switch button:hover{color:#126856}
.upload{background:#f8f7ed;border-color:#a5aa92}
.upload:hover,.upload.drag{background:#eef3e8}
.file{background:#f7f7ef;border-color:#e9e6db}
.file-select{appearance:none;border:0;display:flex;align-items:center;gap:8px;text-align:left;background:transparent;color:inherit;padding:0;min-width:0;flex:1}
.file.selected{border-color:#aac7b8;background:#eaf4ec}
.range-line{display:flex;justify-content:space-between;gap:8px;align-items:center}
.range-line output{font-size:12px;font-weight:700;color:#28584b}
input[type=range]{accent-color:#28584b;width:100%;margin:3px 0 5px}
.unit{right:25px}
.dimension{display:grid;grid-template-columns:30px minmax(0,1fr) 76px;gap:8px;align-items:center;margin-top:8px}
.dimension .field-label,.dimension input[type=range]{margin:0}
.dimension .field{height:33px;padding:0 6px}
.model-canvas{cursor:grab;touch-action:none}
.model-canvas:active{cursor:grabbing}
.print-note{text-align:left}
.btn.primary{background:#28584b;border-color:#28584b}
@media(max-width:1040px){.layout{grid-template-columns:minmax(0,1fr) minmax(0,1fr) 238px}.card,.panel-head{padding-inline:10px}}
@media(max-width:835px){.layout{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}.sidebar{grid-column:1/-1;grid-row:2;grid-template-columns:repeat(3,minmax(0,1fr))}.stage{height:415px}}
@media(max-width:600px){.layout{grid-template-columns:1fr}.flat-view{grid-column:1;grid-row:1}.model-view{grid-column:1;grid-row:2}.sidebar{grid-column:1;grid-row:3;grid-template-columns:1fr}.stage{height:350px}.actions{gap:5px}.title-row{align-items:flex-start;flex-wrap:wrap;gap:10px}.local{font-size:10px}.wrap{padding-top:15px}}
@media print{
 body{margin:0;background:white}
 body>*:not(#printFrames){display:none!important}
 #printFrames{display:block}
 .print-sheet{display:block;break-after:page}
 .print-sheet:last-child{break-after:auto}
}
</style>
<style id="pageStyle"></style>
</head>
<body>
<svg aria-hidden="true" style="position:absolute;width:0;height:0">
<defs>
<symbol id="cube" viewBox="0 0 24 24"><path d="M12 2.5 21 7.6v8.8L12 22l-9-5.6V7.6l9-5.1ZM3 7.6l9 5.2 9-5.2m-9 5.2V22m-4.5-17 9 5.3"/></symbol>
<symbol id="lock" viewBox="0 0 24 24"><rect x="6" y="10" width="12" height="11" rx="2"/><path d="M9 10V7a3 3 0 0 1 6 0v3m-3 4v3"/></symbol>
<symbol id="upload" viewBox="0 0 24 24"><path d="M12 16V3m-5 5 5-5 5 5M4 15v5a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-5"/></symbol>
<symbol id="image" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="8.5" cy="9" r="1.5"/><path d="m4 18 5-5 3 3 4-5 4 5"/></symbol>
<symbol id="ruler" viewBox="0 0 24 24"><path d="m3 16 13-13 5 5L8 21 3 16Zm4-4 3 3m1-7 3 3m1-7 3 3"/></symbol>
<symbol id="print" viewBox="0 0 24 24"><path d="M6 8V3h12v5m0 9h2a1 1 0 0 0 1-1v-5a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v5a1 1 0 0 0 1 1h2m2-2h8v6H8zM6 12h.01"/></symbol>
<symbol id="download" viewBox="0 0 24 24"><path d="M12 3v13m-5-5 5 5 5-5M4 17v4h16v-4"/></symbol>
<symbol id="page" viewBox="0 0 24 24"><path d="M6 3h8l4 4v14H6zM14 3v5h4m-9 4h6m-6 4h6"/></symbol>
<symbol id="close" viewBox="0 0 24 24"><path d="m6 6 12 12M18 6 6 18"/></symbol>
<symbol id="left" viewBox="0 0 24 24"><path d="m15 6-6 6 6 6"/></symbol>
<symbol id="right" viewBox="0 0 24 24"><path d="m9 6 6 6-6 6"/></symbol>
</defs>
</svg>
<header><div class="bar">
  <div class="brand"><span class="logo" data-icon="cube"></span>纸模工坊</div>
  <span class="local"><span data-icon="lock"></span>图片仅在浏览器内处理</span>
</div></header>
<main class="wrap">
  <div class="title-row"><div><h1>纸模打印工作台</h1><p class="intro">从截图裁切展开图，预览折叠效果并按成品尺寸打印。</p></div>
    <div class="actions"><button id="print" class="btn"><span data-icon="print"></span>打印</button><button id="pdf" class="btn primary"><span data-icon="download"></span>下载 PDF</button></div>
  </div>
  <div class="layout">
    <aside class="sidebar" aria-label="图纸与打印设置">
      <section class="card">
        <div class="card-head"><h2 class="label-icon"><span data-icon="image"></span>导入图纸</h2><button id="adjustCrop" class="link-button" hidden>调整裁切</button><button id="sample" class="link-button" hidden>加载示例</button></div>
        <button id="uploadButton" class="upload" type="button"><span data-icon="upload"></span><span>选择图片或拖到这里</span><span class="muted">JPG、PNG、WebP · 支持拼图截图</span></button>
        <input id="filePicker" type="file" accept="image/jpeg,image/png,image/webp" hidden>
        <p id="uploadError" class="message" role="alert" hidden></p>
        <div id="fileList" class="file-list" aria-label="已导入的图纸"></div>
      </section>
      <section class="card">
        <div class="card-head"><h2 class="label-icon"><span data-icon="ruler"></span>成品尺寸</h2><span class="muted">mm</span></div>
        <div class="dimension"><label class="field-label" for="length">长</label><input id="lengthSlider" type="range" aria-label="调节长度" min="5" max="300" value="40"><input id="length" class="field" type="number" inputmode="decimal" min="5" max="300" step="0.1" value="40"></div>
        <div class="dimension"><label class="field-label" for="depth">宽</label><input id="depthSlider" type="range" aria-label="调节宽度" min="5" max="300" value="40"><input id="depth" class="field" type="number" inputmode="decimal" min="5" max="300" step="0.1" value="40"></div>
        <div class="dimension"><label class="field-label" for="height">高</label><input id="heightSlider" type="range" aria-label="调节高度" min="5" max="300" value="40"><input id="height" class="field" type="number" inputmode="decimal" min="5" max="300" step="0.1" value="40"></div>
        <div class="fields">
          <div><label for="paperSize" class="field-label">纸张</label><select id="paperSize" class="field"><option>A4</option><option>A3</option><option value="Letter">Letter</option></select></div>
          <div><label for="copies" class="field-label">每款份数</label><input id="copies" class="field" type="number" inputmode="numeric" min="1" max="30" step="1" value="1"></div>
        </div>
        <p id="settingError" class="message" role="alert" hidden></p>
      </section>
      <section class="card">
        <div class="range-line"><label class="field-label" for="fold" style="margin:0">折叠进度</label><output id="foldValue" for="fold">100%</output></div>
        <input id="fold" type="range" min="0" max="100" value="100">
        <div class="chips" aria-label="折叠状态"><button class="chip" data-fold="0">展开</button><button class="chip" data-fold="50">半折</button><button class="chip" data-fold="100">合上</button></div>
      </section>
    </aside>
    <section class="workspace flat-view" aria-labelledby="previewTitle">
      <div class="panel-head">
        <h2 class="label-icon" id="previewTitle"><span data-icon="page"></span>平面视图</h2>
        <div class="view-switch"><button id="cropMode" aria-pressed="false">裁切图</button><button id="flatMode" aria-pressed="true">展开图</button><button id="printMode" aria-pressed="false">打印预览</button></div>
      </div>
      <div class="stage"><canvas id="flat" role="img" aria-label="带尺寸标注的正方体展开图"></canvas><canvas id="preview" class="paper" role="img" aria-label="纸模打印预览" hidden></canvas><p id="empty" class="empty" hidden></p></div>
      <div class="footer">
        <div class="details"><span class="paper-size" id="paperBadge">A4</span><span id="sheetInfo"></span><span aria-hidden="true">·</span><span id="edgeInfo"></span></div>
        <div class="pages" id="pages" hidden><button id="prev" class="icon-button" aria-label="上一页" data-icon="left"></button><span id="pageCount"></span><button id="next" class="icon-button" aria-label="下一页" data-icon="right"></button></div>
      </div>
    </section>
    <section class="workspace model-view" aria-labelledby="modelTitle">
      <div class="panel-head"><h2 class="label-icon" id="modelTitle"><span data-icon="cube"></span>立体视图</h2><button id="resetView" class="link-button">重置视角</button></div>
      <div class="stage"><canvas id="model" class="model-canvas" role="img" aria-label="可拖动旋转的纸模折叠预览"></canvas><p id="modelEmpty" class="empty" hidden>导入图纸后查看折叠效果。</p></div>
      <div class="footer"><span>拖动旋转</span><span id="modelInfo"></span></div>
    </section>
  </div>
  <p class="muted print-note">打印时选择「实际大小」或「100%」，并关闭页眉页脚。</p>
</main>
<dialog id="cropDialog">
  <div class="dialog-head"><h2>选择展开图</h2><button id="cancelCrop" class="icon-button" aria-label="关闭" data-icon="close"></button></div>
  <div class="dialog-body">
    <div class="crop-stage"><canvas id="sourceCanvas" aria-label="上传图片，拖动以框选一张展开图"></canvas></div>
    <div>
      <h3 style="font-size:13px" id="candidateTitle">识别结果</h3>
      <div id="candidates" class="candidates"></div>
      <p id="cropHint" class="muted crop-help">也可以在原图上拖动，框住一张完整展开图和粘贴边。</p>
      <button id="measure" class="btn" style="margin-top:12px"><span data-icon="ruler"></span>校准六个面</button>
      <p id="measureHint" class="muted crop-help">依次点击最上面那个面的左上角和右上角，校准六个面。</p>
    </div>
  </div>
  <div class="dialog-foot">
    <button id="addAll" class="btn" hidden>导入全部识别图纸</button>
    <div class="actions" style="margin-left:auto"><button id="closeCrop" class="btn">取消</button><button id="addCrop" class="btn primary">导入选中图纸</button></div>
  </div>
</dialog>
<div id="printFrames" aria-hidden="true"></div>
<script>
"use strict";

const byId = id => document.getElementById(id);
const paperSizes = { A4: [210, 297], A3: [297, 420], Letter: [215.9, 279.4] };
const format = value => Number(value.toFixed(2)).toString();
const clamp = (value, min, max) => Math.max(min, Math.min(max, value));
const faces = [[1, 1], [0, 1], [2, 1], [3, 1], [1, 0], [1, 2]];
const axes = ["length", "depth", "height"];
const defaultDimensions = () => [40, 40, 40];
const measureHelp = "依次点击最上面那个面的左上角和右上角，校准六个面。";
const icons = id => '<svg aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><use href="#' + id + '"/></svg>';
document.querySelectorAll("[data-icon]").forEach(el => { el.innerHTML = icons(el.dataset.icon); });

function canvas(width, height) {
  const image = document.createElement("canvas");
  image.width = Math.max(1, Math.round(width));
  image.height = Math.max(1, Math.round(height));
  return image;
}

function createExample() {
  const s = 144, x = 33, y = 4;
  const image = canvas(x + 4 * s + 4, y + 3 * s + 4);
  const ctx = image.getContext("2d");
  ctx.fillStyle = "#fffcf2";
  ctx.strokeStyle = "#544d3d";
  ctx.lineWidth = 1.35;
  function tab(ax, ay, bx, by) {
    const dx = bx - ax, dy = by - ay;
    ctx.beginPath();
    ctx.moveTo(ax, ay);
    ctx.lineTo(ax + .18 * dx + .17 * dy, ay + .18 * dy - .17 * dx);
    ctx.lineTo(bx - .18 * dx + .17 * dy, by - .18 * dy - .17 * dx);
    ctx.lineTo(bx, by);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
  }
  tab(x, y + 2 * s, x, y + s);
  [0, 2, 3].forEach(col => {
    tab(x + col * s, y + s, x + (col + 1) * s, y + s);
    tab(x + (col + 1) * s, y + 2 * s, x + col * s, y + 2 * s);
  });
  faces.forEach(([col, row], index) => {
    const px = x + s * col, py = y + s * row, cell = s / 16;
    for (let iy = 0; iy < 16; iy++) {
      for (let ix = 0; ix < 16; ix++) {
        const ring = Math.min(ix, iy, 15 - ix, 15 - iy);
        const noise = ((ix * 71 + iy * 137 + ix * iy * 31 + index * 19) % 21) - 10;
        const shine = (ix + 2 * iy + index) % 14 < 3 ? 10 : 0;
        const shade = ([34, 66, 46, 50, 63, 53, 56, 66][ring] + noise * .42 + shine * .55);
        ctx.fillStyle = "hsl(" + (163 + noise) + " 37% " + shade + "%)";
        ctx.fillRect(px + ix * cell, py + iy * cell, cell, cell);
      }
    }
    ctx.strokeStyle = "#385a4d";
    ctx.strokeRect(px, py, s, s);
  });
  return { name: "青玉方块 · 示例", image, edge: s, originX: x, originY: y, sample: true, dimensions: defaultDimensions() };
}

// Find four adjacent face widths, then confirm the top and bottom faces and the clear corners.
function recognize(image) {
  const scale = Math.min(1, 1080 / Math.max(image.width, image.height));
  const reduced = canvas(image.width * scale, image.height * scale);
  const ctx = reduced.getContext("2d", { willReadFrequently: true });
  ctx.fillStyle = "#fff";
  ctx.fillRect(0, 0, reduced.width, reduced.height);
  ctx.drawImage(image, 0, 0, reduced.width, reduced.height);
  const { width: w, height: h } = reduced;
  const pixels = ctx.getImageData(0, 0, w, h).data;
  const mask = new Uint8Array(w * h);
  for (let i = 0; i < mask.length; i++) {
    const j = 4 * i, r = pixels[j], g = pixels[j + 1], b = pixels[j + 2];
    mask[i] = Math.min(r, g, b) < 218 && (Math.max(r, g, b) - Math.min(r, g, b) > 20 || (r + g + b) / 3 < 180);
  }
  const at = (x, y) => {
    const ix = Math.round(x), iy = Math.round(y);
    return ix >= 0 && iy >= 0 && ix < w && iy < h ? mask[iy * w + ix] : 0;
  };
  const found = [];
  function evaluate(x, y, length) {
    const s = length / 4;
    if (s < 12 || y < s || y > h - s) return;
    if (found.some(box => Math.abs(box.x - x) < .09 * s && Math.abs(box.y + s * 1.5 - y) < .38 * s)) return;
    // Whole rows remain recognizable when bright artwork interrupts individual pixel columns.
    function rowOfFaces(row) {
      let solid = 0;
      for (const col of [0, 2, 3]) {
        for (let k = 0; k < 12; k++) solid += at(x + (col + (k + .5) / 12) * s, row);
      }
      return solid >= 22;
    }
    if (!rowOfFaces(y)) return;
    function bandLimit(direction) {
      let last = y;
      for (let row = y + direction; Math.abs(row - y) < 1.16 * s; row += direction) {
        if (rowOfFaces(row)) last = row;
        if (Math.abs(last - row) > Math.max(2, .09 * s)) break;
      }
      return last;
    }
    const top = bandLimit(-1), bottom = bandLimit(1);
    if (bottom - top + 1 < .84 * s || bottom - top + 1 > 1.14 * s) return;
    const rowStart = (top + bottom + 1 - s) / 2;
    const netTop = rowStart - s;
    if (netTop < -.09 * s || netTop + 3 * s > h + .09 * s) return;
    function density(col, row) {
      let sum = 0;
      for (let a = 0; a < 9; a++) {
        for (let b = 0; b < 9; b++) sum += at(x + (col + (a + .5) / 9) * s, netTop + (row + (b + .5) / 9) * s);
      }
      return sum / 81;
    }
    if (faces.some(([col, row]) => density(col, row) < .62)) return;
    if ([0, 2, 3].some(col => density(col, 0) > .16 || density(col, 2) > .16)) return;
    if (found.some(box => Math.abs(box.x - x) < .26 * s && Math.abs(box.y - netTop) < .35 * s)) return;
    found.push({ x, y: netTop, s });
  }
  for (let y = 0; y < h; y += 2) {
    let start = -1, last = -1;
    for (let x = 0; x <= w + 3; x++) {
      if (x < w && mask[y * w + x]) {
        if (start < 0) start = x;
        last = x;
      } else if (start >= 0 && x > last + 3) {
        if (last - start >= 44) evaluate(start, y, last - start + 1);
        start = -1;
      }
    }
  }
  const sx = image.width / w, sy = image.height / h;
  return found.sort((a, b) => Math.abs(a.y - b.y) < a.s * .25 ? a.x - b.x : a.y - b.y).slice(0, 30).map(({ x, y, s }) => {
    const left = Math.max(0, Math.floor((x - .29 * s) * sx));
    const top = Math.max(0, Math.floor((y - .035 * s) * sy));
    const right = Math.min(image.width, Math.ceil((x + 4.025 * s) * sx));
    const bottom = Math.min(image.height, Math.ceil((y + 3.035 * s) * sy));
    return { x: left, y: top, w: right - left, h: bottom - top, edge: s * sx, originX: x * sx, originY: y * sy };
  });
}

const example = createExample();
let items = [example], selected = example, view = "flat", page = 0, plan;
let pending, shot, dragStart, measurePoints = [], measuring = false, editing;
let yaw = -.62, pitch = .44, orbit;

function thumbnail(image, size) {
  const thumb = canvas(size, size * .72);
  const scale = Math.min(thumb.width / image.width, thumb.height / image.height);
  const w = image.width * scale, h = image.height * scale;
  thumb.getContext("2d").drawImage(image, (thumb.width - w) / 2, (thumb.height - h) / 2, w, h);
  return thumb;
}

function listItems() {
  byId("sample").hidden = items.length > 0;
  byId("adjustCrop").hidden = !selected?.source;
  byId("fileList").replaceChildren(...items.map(item => {
    const row = document.createElement("div");
    row.className = "file" + (item === selected ? " selected" : "");
    const select = document.createElement("button");
    select.className = "file-select";
    select.setAttribute("aria-pressed", item === selected);
    const name = document.createElement("span");
    name.className = "file-name";
    name.textContent = item.name;
    row.title = item.name;
    select.append(thumbnail(item.image, 66), name);
    select.onclick = () => { selected = item; selectDimensions(); update(); listItems(); };
    const remove = document.createElement("button");
    remove.className = "icon-button";
    remove.innerHTML = icons("close");
    remove.setAttribute("aria-label", "移除 " + item.name);
    remove.onclick = () => {
      items = items.filter(remaining => remaining !== item);
      if (selected === item) selected = items[0];
      page = 0;
      selectDimensions();
      listItems();
      update();
    };
    row.append(select, remove);
    return row;
  }));
}

function loadError(message) {
  byId("uploadError").textContent = message;
  byId("uploadError").hidden = !message;
}

async function importFile(file) {
  if (!file) return;
  loadError("");
  if (!["image/jpeg", "image/png", "image/webp"].includes(file.type)) {
    loadError("请选择 JPG、PNG 或 WebP 图片。");
    return;
  }
  byId("uploadButton").disabled = true;
  const url = URL.createObjectURL(file);
  try {
    const image = new Image();
    image.src = url;
    await image.decode();
    pending = { image, name: file.name.replace(/\.[^.]+$/, ""), boxes: recognize(image) };
    if (pending.boxes.length === 1) addCrops(pending.boxes);
    else showCrop(pending.boxes[0] ?? { x: 0, y: 0, w: image.width, h: image.height });
  } catch {
    loadError("图片读取失败，请换一张图片重试。");
  } finally {
    URL.revokeObjectURL(url);
    byId("uploadButton").disabled = false;
  }
}

function showCrop(rect) {
  const { image, boxes } = pending;
  byId("candidateTitle").textContent = boxes.length ? "识别到 " + boxes.length + " 张展开图" : "请框选并校准展开图";
  byId("addAll").hidden = Boolean(editing) || boxes.length < 2;
  const target = byId("sourceCanvas"), scale = Math.min(1, 1250 / Math.max(image.width, image.height));
  target.width = Math.round(image.width * scale);
  target.height = Math.round(image.height * scale);
  byId("cropDialog").showModal();
  selectShot(rect);
}

function extract(rect) {
  const image = canvas(rect.w, rect.h);
  image.getContext("2d").drawImage(pending.image, rect.x, rect.y, rect.w, rect.h, 0, 0, image.width, image.height);
  return image;
}

function selectShot(box) {
  shot = box;
  measuring = false;
  measurePoints = [];
  byId("measure").setAttribute("aria-pressed", "false");
  byId("measureHint").textContent = measureHelp;
  byId("candidates").replaceChildren(...pending.boxes.map((rect, index) => {
    const button = document.createElement("button");
    button.className = "candidate";
    button.setAttribute("aria-pressed", rect === shot);
    button.append(thumbnail(extract(rect), 115), "图纸 " + (index + 1));
    button.onclick = () => selectShot(rect);
    return button;
  }));
  drawSource();
  verifyShot();
}

function drawSource() {
  const target = byId("sourceCanvas"), ctx = target.getContext("2d");
  const sx = target.width / pending.image.width, sy = target.height / pending.image.height;
  ctx.clearRect(0, 0, target.width, target.height);
  ctx.drawImage(pending.image, 0, 0, target.width, target.height);
  ctx.fillStyle = "#15231c8a";
  ctx.fillRect(0, 0, target.width, target.height);
  ctx.save();
  ctx.beginPath();
  ctx.rect(shot.x * sx, shot.y * sy, shot.w * sx, shot.h * sy);
  ctx.clip();
  ctx.drawImage(pending.image, 0, 0, target.width, target.height);
  ctx.restore();
  ctx.lineWidth = Math.max(2, target.width / 300);
  ctx.strokeStyle = "#38d487";
  ctx.strokeRect(shot.x * sx, shot.y * sy, shot.w * sx, shot.h * sy);
  if (measurePoints.length) {
    ctx.strokeStyle = ctx.fillStyle = "#ffaf48";
    measurePoints.forEach(([x, y]) => {
      ctx.beginPath();
      ctx.arc(x * sx, y * sy, ctx.lineWidth * 1.6, 0, Math.PI * 2);
      ctx.fill();
    });
    if (measurePoints.length === 2) {
      ctx.beginPath();
      ctx.moveTo(measurePoints[0][0] * sx, measurePoints[0][1] * sy);
      ctx.lineTo(measurePoints[1][0] * sx, measurePoints[1][1] * sy);
      ctx.stroke();
    }
  }
}

function pointOnSource(e) {
  const rect = byId("sourceCanvas").getBoundingClientRect();
  return [
    clamp((e.clientX - rect.left) / rect.width, 0, 1) * pending.image.width,
    clamp((e.clientY - rect.top) / rect.height, 0, 1) * pending.image.height
  ];
}

function verifyShot() {
  const { x, y, w, h, originX, originY, edge } = shot;
  const tolerance = edge * .03;
  byId("addCrop").disabled = !(edge >= 5 &&
    originX >= x - tolerance && originY >= y - tolerance &&
    originX + 4 * edge <= x + w + tolerance && originY + 3 * edge <= y + h + tolerance);
}

byId("sourceCanvas").onpointerdown = e => {
  const point = pointOnSource(e);
  if (measuring) {
    measurePoints.push(point);
    if (measurePoints.length === 2) {
      const [a, b] = measurePoints;
      const edge = b[0] - a[0];
      shot = { ...shot, edge, originX: a[0] - edge, originY: (a[1] + b[1]) / 2 };
      byId("measure").setAttribute("aria-pressed", "false");
      measuring = false;
      verifyShot();
      byId("measureHint").textContent = byId("addCrop").disabled
        ? "框选范围需包含六个面。请重新框选，再点击顶面上边的两个角。"
        : "六个面已定位，可以导入。";
    }
    drawSource();
    return;
  }
  dragStart = point;
  e.currentTarget.setPointerCapture(e.pointerId);
};
byId("sourceCanvas").onpointermove = e => {
  if (!dragStart) return;
  const [x, y] = pointOnSource(e), [ax, ay] = dragStart;
  const w = Math.abs(x - ax), h = Math.abs(y - ay);
  if (w < 2 || h < 2) return;
  shot = { ...shot, x: Math.min(x, ax), y: Math.min(y, ay), w, h };
  byId("candidates").querySelectorAll("button").forEach(button => button.setAttribute("aria-pressed", "false"));
  measurePoints = [];
  drawSource();
  verifyShot();
};
byId("sourceCanvas").onlostpointercapture = () => { dragStart = undefined; };
byId("measure").onclick = () => {
  measuring = !measuring;
  measurePoints = [];
  byId("measure").setAttribute("aria-pressed", String(measuring));
  byId("measureHint").textContent = measureHelp;
  drawSource();
};
function addCrops(boxes) {
  const crops = boxes.map(rect => {
    const index = pending.boxes.indexOf(rect);
    return {
      name: editing?.name ?? pending.name + (index >= 0 && pending.boxes.length > 1 ? " · 图纸 " + (index + 1) : ""),
      image: extract(rect), edge: rect.edge, originX: rect.originX - rect.x, originY: rect.originY - rect.y,
      source: pending, rect, dimensions: editing?.dimensions ?? defaultDimensions()
    };
  });
  items = editing ? items.map(item => item === editing ? crops[0] : item) : [...items.filter(item => !item.sample), ...crops];
  selected = crops[0];
  page = 0;
  view = "crop";
  if (byId("cropDialog").open) byId("cropDialog").close();
  else pending = undefined;
  selectDimensions();
  listItems();
  update();
}

byId("addCrop").onclick = () => addCrops([shot]);
byId("addAll").onclick = () => addCrops(pending.boxes);
byId("cancelCrop").onclick = byId("closeCrop").onclick = () => byId("cropDialog").close();
byId("cropDialog").onclose = () => { pending = undefined; shot = undefined; dragStart = undefined; editing = undefined; };
byId("adjustCrop").onclick = () => { editing = selected; pending = selected.source; showCrop(selected.rect); };
byId("uploadButton").onclick = () => byId("filePicker").click();
byId("filePicker").onchange = e => { importFile(e.target.files[0]); e.target.value = ""; };
byId("uploadButton").ondragover = e => { e.preventDefault(); e.currentTarget.classList.add("drag"); };
byId("uploadButton").ondragleave = e => e.currentTarget.classList.remove("drag");
byId("uploadButton").ondrop = e => {
  e.preventDefault();
  e.currentTarget.classList.remove("drag");
  if (!e.currentTarget.disabled) importFile(e.dataTransfer.files[0]);
};
byId("sample").onclick = () => { items = [example]; selected = example; selectDimensions(); listItems(); update(); };

function packSheets(w, h, parts) {
  const margin = 8, gap = 4;
  if (parts.some(part => part.w > w - 2 * margin || part.h > h - 2 * margin)) return null;
  const sheets = [];
  let sheet, x, y, rowHeight;
  function newSheet() {
    sheet = [];
    sheets.push(sheet);
    x = y = margin;
    rowHeight = 0;
  }
  newSheet();
  for (const part of parts) {
    if (x + part.w > w - margin + 1e-7) {
      x = margin;
      y += rowHeight + gap;
      rowHeight = 0;
    }
    if (y + part.h > h - margin + 1e-7) newSheet();
    sheet.push({ ...part, x, y });
    x += part.w + gap;
    rowHeight = Math.max(rowHeight, part.h);
  }
  for (const placements of sheets) {
    const right = Math.max(...placements.map(part => part.x + part.w));
    const bottom = Math.max(...placements.map(part => part.y + part.h));
    for (const part of placements) {
      part.x += (w - margin - right) / 2;
      part.y += (h - margin - bottom) / 2;
    }
  }
  return { w, h, sheets };
}

function choosePlan(parts, size) {
  const [w, h] = size;
  const portrait = packSheets(w, h, parts), landscape = packSheets(h, w, parts);
  return !portrait || (landscape && landscape.sheets.length < portrait.sheets.length) ? landscape : portrait;
}

function validDimensions(dimensions) {
  return dimensions.every(value => value >= 5 && value <= 300);
}

function netGeometry(item) {
  const [length, depth, height] = item.dimensions;
  const { edge, originX, originY, image } = item;
  function axis(origin, limit, spans) {
    const source = [0, ...Array.from({ length: spans.length + 1 }, (_, i) => origin + i * edge), limit];
    const first = Math.max(0, origin) * Math.min(length, depth, height) / edge;
    const last = Math.max(0, limit - source.at(-2)) * Math.min(length, depth, height) / edge;
    const dest = [0, first];
    for (const span of [...spans, last]) dest.push(dest.at(-1) + span);
    return { source, dest };
  }
  const x = axis(originX, image.width, [depth, length, depth, length]);
  const y = axis(originY, image.height, [depth, height, depth]);
  return { x, y, w: x.dest.at(-1), h: y.dest.at(-1) };
}

function drawNet(ctx, image, net, x, y, scale) {
  ctx.save();
  ctx.translate(x, y);
  ctx.scale(scale, scale);
  ctx.fillStyle = "#fff";
  ctx.fillRect(0, 0, net.w, net.h);
  const { x: columns, y: rows } = net;
  for (let row = 0; row < rows.dest.length - 1; row++) {
    const sh = rows.source[row + 1] - rows.source[row], dh = rows.dest[row + 1] - rows.dest[row];
    if (sh <= 0 || dh <= 0) continue;
    for (let col = 0; col < columns.dest.length - 1; col++) {
      const sw = columns.source[col + 1] - columns.source[col], dw = columns.dest[col + 1] - columns.dest[col];
      if (sw <= 0 || dw <= 0) continue;
      ctx.drawImage(image, columns.source[col], rows.source[row], sw, sh, columns.dest[col], rows.dest[row], dw, dh);
    }
  }
  ctx.restore();
}

function renderSheet(target, layout, index, density) {
  target.width = Math.round(layout.w * density);
  target.height = Math.round(layout.h * density);
  const ctx = target.getContext("2d");
  ctx.scale(target.width / layout.w, target.height / layout.h);
  ctx.fillStyle = "#fff";
  ctx.fillRect(0, 0, layout.w, layout.h);
  for (const { item, net, x, y } of layout.sheets[index]) drawNet(ctx, item.image, net, x, y, 1);
}

function fitCanvas(target) {
  const box = target.getBoundingClientRect();
  const dpr = Math.min(2, devicePixelRatio || 1);
  const w = Math.max(1, box.width), h = Math.max(1, box.height);
  target.width = Math.round(w * dpr);
  target.height = Math.round(h * dpr);
  const ctx = target.getContext("2d");
  ctx.scale(dpr, dpr);
  return { ctx, w, h };
}

function drawFlat() {
  if (!selected || view === "print") return;
  const { ctx, w, h } = fitCanvas(byId("flat"));
  const item = selected;
  const net = view === "flat" && validDimensions(item.dimensions) ? netGeometry(item) : null;
  const image = item.image;
  const { w: nw, h: nh } = net ?? { w: image.width, h: image.height };
  const scale = Math.min(Math.max(1, w - 40) / nw, Math.max(1, h - 77) / nh);
  const dw = nw * scale, dh = nh * scale;
  const x = (w - dw) / 2, y = (h - dh) / 2 - 7;
  if (!net) {
    ctx.drawImage(image, x, y, dw, dh);
    return;
  }
  drawNet(ctx, image, net, x, y, scale);
  const left = x + net.x.dest[2] * scale, mark = item.dimensions[0] * scale;
  const bottom = y + dh + 26;
  ctx.strokeStyle = "#83735c";
  ctx.fillStyle = "#5f5547";
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.moveTo(left, bottom - 5);
  ctx.lineTo(left, bottom + 5);
  ctx.moveTo(left, bottom);
  ctx.lineTo(left + mark, bottom);
  ctx.moveTo(left + mark, bottom - 5);
  ctx.lineTo(left + mark, bottom + 5);
  ctx.stroke();
  ctx.font = "600 12px system-ui, sans-serif";
  ctx.textAlign = "center";
  ctx.fillText(format(item.dimensions[0]) + " mm", left + mark / 2, bottom + 21);
}

const rotateX = ([x, y, z], a) => [x, y * Math.cos(a) - z * Math.sin(a), y * Math.sin(a) + z * Math.cos(a)];
const rotateY = ([x, y, z], a) => [x * Math.cos(a) + z * Math.sin(a), y, -x * Math.sin(a) + z * Math.cos(a)];

function foldPoint([x, y, z], side, a, [length, depth, height]) {
  if (side === 0) return [x, y, z];
  if (side === 4 || side === 5) {
    const hinge = (side === 4 ? -1 : 1) * height / 2;
    const p = rotateX([x, y - hinge, z], side === 4 ? a : -a);
    return [p[0], p[1] + hinge, p[2]];
  }
  const hinge = (side === 1 ? -1 : 1) * length / 2;
  let point = [x, y, z];
  if (side === 3) {
    const outerHinge = hinge + depth;
    point = rotateY([x - outerHinge, y, z], a);
    point[0] += outerHinge;
  }
  const p = rotateY([point[0] - hinge, point[1], point[2]], side === 1 ? -a : a);
  return [p[0] + hinge, p[1], p[2]];
}

function drawModel() {
  const item = selected, modelEmpty = byId("modelEmpty");
  const dimensions = item?.dimensions;
  const ready = dimensions && validDimensions(dimensions);
  modelEmpty.hidden = Boolean(ready);
  modelEmpty.textContent = item ? "填写有效的长、宽、高后查看立体效果。" : "导入图纸后查看折叠效果。";
  const { ctx, w, h } = fitCanvas(byId("model"));
  if (!ready) {
    byId("modelInfo").textContent = "";
    return;
  }
  const progress = byId("fold").valueAsNumber;
  const angle = progress / 100 * Math.PI / 2;
  const [length, depth, height] = dimensions;
  const xs = [-length / 2 - depth, -length / 2, length / 2, length / 2 + depth, length * 1.5 + depth];
  const ys = [-height / 2 - depth, -height / 2, height / 2, height / 2 + depth];
  const polygons = faces.map(([col, row], side) => {
    const points = [[0, 0], [1, 0], [1, 1], [0, 1]].map(([dx, dy]) => {
      const folded = foldPoint([xs[col + dx], ys[row + dy], 0], side, angle, dimensions);
      return rotateX(rotateY(folded, yaw), pitch);
    });
    return { col, row, points, depth: points.reduce((sum, point) => sum + point[2], 0) };
  });
  const verts = polygons.flatMap(poly => poly.points);
  const minX = Math.min(...verts.map(p => p[0])), maxX = Math.max(...verts.map(p => p[0]));
  const minY = Math.min(...verts.map(p => p[1])), maxY = Math.max(...verts.map(p => p[1]));
  const size = Math.min(w * (.64 + .15 * (1 - progress / 100)) / (maxX - minX), h * .67 / (maxY - minY)) *
    clamp(Math.pow(Math.max(...dimensions) / 45, .15), .68, 1.08);
  const originX = (w - (maxX + minX) * size) / 2, originY = (h - (maxY + minY) * size) / 2 - 11;
  ctx.save();
  ctx.translate(w / 2, h / 2 + (maxY - minY) * size * .43 + 21);
  ctx.scale(1, .24);
  const radius = Math.min(w * .43, (maxX - minX) * size * .53);
  const shade = ctx.createRadialGradient(0, 0, 0, 0, 0, radius);
  shade.addColorStop(0, "#53422b50");
  shade.addColorStop(1, "#53422b00");
  ctx.fillStyle = shade;
  ctx.fillRect(-radius, -radius, radius * 2, radius * 2);
  ctx.restore();
  polygons.sort((a, b) => a.depth - b.depth).forEach(({ col, row, points }) => {
    const [a, b, , d] = points;
    ctx.save();
    ctx.transform((b[0] - a[0]) * size, (b[1] - a[1]) * size,
      (d[0] - a[0]) * size, (d[1] - a[1]) * size, originX + a[0] * size, originY + a[1] * size);
    const textureEdge = item.edge;
    ctx.fillStyle = "#ddd1ad";
    ctx.fillRect(0, 0, 1, 1);
    ctx.drawImage(item.image, item.originX + textureEdge * col, item.originY + textureEdge * row, textureEdge, textureEdge, 0, 0, 1, 1);
    ctx.fillStyle = ["#142e1c0b", "#142e1c43", "#142e1c2d", "#142e1c26", "#fff1c522", "#142e1c50"][faces.findIndex(face => face[0] === col && face[1] === row)];
    ctx.fillRect(0, 0, 1, 1);
    ctx.strokeStyle = "#293c308c";
    ctx.lineWidth = 1 / (size * Math.min(xs[col + 1] - xs[col], ys[row + 1] - ys[row]));
    ctx.strokeRect(0, 0, 1, 1);
    ctx.restore();
  });
  byId("modelInfo").textContent = dimensions.map(format).join(" × ") + " mm";
}

function display() {
  const paper = byId("paperSize").value;
  const [w, h] = plan ? [plan.w, plan.h] : paperSizes[paper];
  const dimensions = selected?.dimensions;
  const printView = view === "print";
  byId("paperBadge").textContent = paper;
  byId("sheetInfo").textContent = format(w) + " × " + format(h) + " mm";
  byId("edgeInfo").textContent = dimensions && validDimensions(dimensions) ? "成品 " + dimensions.map(format).join(" × ") + " mm" : "";
  byId("cropMode").setAttribute("aria-pressed", view === "crop");
  byId("flatMode").setAttribute("aria-pressed", view === "flat");
  byId("printMode").setAttribute("aria-pressed", printView);
  byId("flat").hidden = printView || !selected;
  byId("preview").hidden = !printView || !plan;
  byId("empty").hidden = printView ? Boolean(plan) : Boolean(selected);
  byId("empty").textContent = selected ? "调整尺寸或纸张后查看打印预览。" : "导入一张展开图，开始排版。";
  byId("pages").hidden = !printView || !plan;
  if (plan) {
    byId("pageCount").textContent = (page + 1) + " / " + plan.sheets.length;
    byId("prev").disabled = page === 0;
    byId("next").disabled = page === plan.sheets.length - 1;
    if (printView) renderSheet(byId("preview"), plan, page, 4);
  }
  drawFlat();
  drawModel();
}

function update() {
  const copies = byId("copies").valueAsNumber;
  const size = paperSizes[byId("paperSize").value];
  let error = "";
  plan = null;
  if (items.some(item => !validDimensions(item.dimensions))) {
    error = "请将每张图纸的长、宽、高设为 5–300 mm。";
  } else if (!Number.isInteger(copies) || copies < 1 || copies > 30) {
    error = "每款份数须为 1–30 的整数。";
  } else if (items.length) {
    const parts = items.flatMap(item => {
      const net = netGeometry(item);
      return Array.from({ length: copies }, () => ({ item, net, w: net.w, h: net.h }));
    }).sort((a, b) => b.h - a.h || b.w - a.w);
    plan = choosePlan(parts, size);
    if (!plan) {
      error = "当前纸张放不下完整展开图。请减小长、宽或高，或换用更大的纸张。";
    }
  }
  page = plan ? clamp(page, 0, plan.sheets.length - 1) : 0;
  byId("print").disabled = byId("pdf").disabled = !plan;
  byId("settingError").textContent = error;
  byId("settingError").hidden = !error;
  display();
}

function selectDimensions() {
  axes.forEach((axis, i) => {
    const input = byId(axis), slider = byId(axis + "Slider");
    const value = selected?.dimensions[i];
    input.disabled = slider.disabled = !selected;
    input.value = Number.isFinite(value) ? value : "";
    slider.value = Number.isFinite(value) ? value : 40;
  });
}

axes.forEach((axis, i) => {
  const input = byId(axis), slider = byId(axis + "Slider");
  input.oninput = () => {
    if (!selected) return;
    const value = input.valueAsNumber;
    selected.dimensions[i] = value;
    if (Number.isFinite(value)) slider.value = value;
    if (view === "crop") view = "flat";
    update();
  };
  slider.oninput = () => { input.value = slider.value; input.oninput(); };
});
["copies", "paperSize"].forEach(id => { byId(id).oninput = update; });
byId("cropMode").onclick = () => { view = "crop"; display(); };
byId("flatMode").onclick = () => { view = "flat"; display(); };
byId("printMode").onclick = () => { view = "print"; display(); };
byId("prev").onclick = () => { page--; display(); };
byId("next").onclick = () => { page++; display(); };
byId("fold").oninput = () => {
  const fold = byId("fold").value;
  byId("foldValue").textContent = fold + "%";
  document.querySelectorAll("[data-fold]").forEach(chip => chip.setAttribute("aria-pressed", chip.dataset.fold === fold));
  drawModel();
};
document.querySelectorAll("[data-fold]").forEach(chip => {
  chip.onclick = () => { byId("fold").value = chip.dataset.fold; byId("fold").oninput(); };
});
byId("resetView").onclick = () => { yaw = -.62; pitch = .44; drawModel(); };
byId("model").onpointerdown = e => {
  orbit = [e.clientX, e.clientY];
  e.currentTarget.setPointerCapture(e.pointerId);
};
byId("model").onpointermove = e => {
  if (!orbit) return;
  yaw -= (e.clientX - orbit[0]) * .012;
  pitch = clamp(pitch + (e.clientY - orbit[1]) * .012, -1.55, 1.55);
  orbit = [e.clientX, e.clientY];
  drawModel();
};
byId("model").onlostpointercapture = () => { orbit = undefined; };
new ResizeObserver(() => { drawFlat(); drawModel(); }).observe(byId("model").parentElement);

function preparePrint() {
  const container = byId("printFrames");
  container.replaceChildren();
  if (!plan) return;
  byId("pageStyle").textContent = "@page{size:" + plan.w + "mm " + plan.h + "mm;margin:0}";
  plan.sheets.forEach((_, index) => {
    const sheet = canvas(1, 1);
    sheet.className = "print-sheet";
    sheet.style.width = plan.w + "mm";
    sheet.style.height = plan.h + "mm";
    renderSheet(sheet, plan, index, 8);
    container.append(sheet);
  });
}

window.addEventListener("beforeprint", () => { if (!byId("printFrames").childElementCount) preparePrint(); });
window.addEventListener("afterprint", () => { byId("printFrames").replaceChildren(); });
byId("print").onclick = () => { preparePrint(); window.print(); };

// Write a PDF with the exact sheet dimensions in points and one JPEG image per page.
async function exportPdf(layout) {
  const data = [], offsets = [0], encoder = new TextEncoder();
  let length = 0;
  function write(chunk) {
    const bytes = typeof chunk === "string" ? encoder.encode(chunk) : chunk;
    data.push(bytes);
    length += bytes.byteLength;
  }
  function object(id, chunks) {
    offsets[id] = length;
    write(id + " 0 obj\n");
    chunks.forEach(write);
    write("\nendobj\n");
  }
  const wp = (layout.w * 72 / 25.4).toFixed(5), hp = (layout.h * 72 / 25.4).toFixed(5);
  write("%PDF-1.4\n");
  write(new Uint8Array([37, 226, 227, 207, 211, 10]));
  object(1, ["<< /Type /Catalog /Pages 2 0 R >>"]);
  const kids = layout.sheets.map((_, index) => (3 + 3 * index) + " 0 R").join(" ");
  object(2, ["<< /Type /Pages /Kids [" + kids + "] /Count " + layout.sheets.length + " >>"]);
  const sheet = canvas(1, 1);
  for (let index = 0; index < layout.sheets.length; index++) {
    const id = 3 + index * 3;
    renderSheet(sheet, layout, index, 10);
    const image = await new Promise(resolve => sheet.toBlob(resolve, "image/jpeg", .96));
    if (!image) throw new Error("Could not encode the page.");
    const jpeg = new Uint8Array(await image.arrayBuffer());
    const commands = "q " + wp + " 0 0 " + hp + " 0 0 cm /Sheet Do Q\n";
    object(id, ["<< /Type /Page /Parent 2 0 R /MediaBox [0 0 " + wp + " " + hp +
      "] /Resources << /XObject << /Sheet " + (id + 2) + " 0 R >> >> /Contents " + (id + 1) + " 0 R >>"]);
    object(id + 1, ["<< /Length " + commands.length + " >>\nstream\n", commands, "endstream"]);
    object(id + 2, ["<< /Type /XObject /Subtype /Image /Width " + sheet.width + " /Height " + sheet.height +
      " /ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode /Length " + jpeg.length + " >>\nstream\n", jpeg, "\nendstream"]);
  }
  const xref = length;
  write("xref\n0 " + offsets.length + "\n0000000000 65535 f \n");
  offsets.slice(1).forEach(offset => write(String(offset).padStart(10, "0") + " 00000 n \n"));
  write("trailer\n<< /Size " + offsets.length + " /Root 1 0 R >>\nstartxref\n" + xref + "\n%%EOF\n");
  return new Blob(data, { type: "application/pdf" });
}

byId("pdf").onclick = async () => {
  if (!plan) return;
  const button = byId("pdf");
  const size = items.length === 1 ? items[0].dimensions.map(format).join("x") + "mm-" : "";
  const filename = "纸模-" + size + byId("paperSize").value + ".pdf";
  button.disabled = true;
  button.textContent = "生成中…";
  try {
    const pdf = await exportPdf(plan);
    const url = URL.createObjectURL(pdf), link = document.createElement("a");
    link.href = url;
    link.download = filename;
    link.click();
    setTimeout(() => URL.revokeObjectURL(url), 30000);
  } catch {
    byId("settingError").textContent = "生成 PDF 失败，请减少份数后再试。";
    byId("settingError").hidden = false;
  } finally {
    button.innerHTML = icons("download") + "下载 PDF";
    button.disabled = !plan;
  }
};

listItems();
selectDimensions();
update();
byId("fold").oninput();
</script>
</body>
</html>
'''
st.iframe(page, height=850, width="stretch")
