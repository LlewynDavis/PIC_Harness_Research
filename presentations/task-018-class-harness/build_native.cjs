// Workspace renderer extension: native primitives from outline.json.
// Delegates deck construction, metadata and CLI to presentation-skill.
'use strict';
const path = require('path');
const os = require('os');
const skill = path.join(os.homedir(), '.codex', 'skills', 'presentation-skill');
const renderers = require(path.join(skill, 'templates', 'pptxgenjs', 'slides.js'));
const originalFlow = renderers.renderFlow;
const outlineFlag = process.argv.indexOf('--outline');
if (outlineFlag < 0) throw new Error('--outline is required');
const outlineDir = path.dirname(path.resolve(process.argv[outlineFlag + 1]));

function nativeText(slide, value, spec, objectName) {
  slide.addText(value, {
    x: spec.x, y: spec.y, w: spec.w, h: spec.h,
    fontFace: 'Microsoft YaHei', fontSize: spec.fontSize || 14,
    color: spec.color || '18364A', bold: !!spec.bold,
    align: spec.align || 'left', valign: 'mid',
    margin: 0, breakLine: false, paraSpaceAfter: 0,
    fit: 'shrink', objectName,
  });
}
renderers.renderFlow = function(pptx, slide, data, preset) {
  if (!Array.isArray(data.native_elements)) return originalFlow(pptx, slide, data, preset);
  slide.background = { color: 'FFFFFF' };
  nativeText(slide, data.title, {x:.5,y:.15,w:9,h:.56,fontSize:24,bold:true}, 'Editable_Title');
  nativeText(slide, data.subtitle, {x:.5,y:.82,w:9,h:.27,fontSize:11.5,color:'536570'}, 'Editable_Subtitle');
  slide.addShape('rect', {x:.5,y:1.14,w:1.1,h:.04,fill:{color:'18364A'},line:{color:'18364A',width:0},objectName:'Header_Accent'});
  data.native_elements.forEach((el, i) => {
    const name = el.name || `Native_${el.kind}_${i + 1}`;
    if (el.kind === 'text') nativeText(slide, el.text, el, name);
    else if (el.kind === 'rect') slide.addShape('rect', {
      x:el.x,y:el.y,w:el.w,h:el.h,
      fill:{color:el.fill},line:{color:el.stroke || 'CBD9DF',width:.7},objectName:name,
    });
    else if (el.kind === 'line') {
      const reverse = el.x2 < el.x1 || el.y2 < el.y1;
      const ln = {color:el.color || '167B78',width:1.5};
      if (el.arrow) ln[reverse ? 'beginArrowType' : 'endArrowType'] = 'triangle';
      slide.addShape('line', {
        x:Math.min(el.x1,el.x2),y:Math.min(el.y1,el.y2),
        w:Math.abs(el.x2-el.x1),h:Math.abs(el.y2-el.y1),line:ln,objectName:name,
      });
    }
    else if (el.kind === 'image') slide.addImage({
      path:path.resolve(outlineDir,el.path),x:el.x,y:el.y,w:el.w,h:el.h,objectName:name,
    });
    else throw new Error('Unsupported native primitive: '+el.kind);
  });
  const source=String(data.footer || '').replace(/｜\d+\/\d+$/, '');
  nativeText(slide, source, {x:.5,y:5.34,w:8.5,h:.19,fontSize:8.2,color:'536570'}, 'Editable_Source');
  nativeText(slide, `${data.__slideIndex}/${data.__slideCount}`, {x:9.12,y:5.34,w:.38,h:.19,fontSize:9,align:'right',color:'536570'}, 'Editable_PageNumber');
  if (data.notes) slide.addNotes(data.notes);
};
require(path.join(skill, 'scripts', 'build_deck_pptxgenjs.js'));
