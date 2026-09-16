window.mermaid.initialize({ startOnLoad: false, securityLevel: "loose" });

document$.subscribe(function () {
  window.mermaid.run({ querySelector: ".mermaid" });
});
