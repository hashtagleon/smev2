(function () {
  var form = document.getElementById("applicant-form");
  if (!form) return;

  var samples = Array.prototype.slice.call(document.querySelectorAll(".sample"));
  var demoLink = document.getElementById("demo-link");
  var demoBase = demoLink.getAttribute("href").replace(/high$/, "");

  // ---- Money readout in lakh / crore ----
  function words(n) {
    if (!isFinite(n) || n <= 0) return "";
    var v, unit;
    if (n >= 1e7) { v = n / 1e7; unit = "crore"; }
    else if (n >= 1e5) { v = n / 1e5; unit = "lakh"; }
    else return n.toLocaleString("en-US", { maximumFractionDigits: 2 }) + " taka";
    return "About " + (Math.round(v * 100) / 100) + " " + unit + " taka";
  }
  function updateMoney(input) {
    var hint = document.getElementById(input.id + "-hint");
    if (!hint || input.closest(".has-error")) return;
    var text = words(parseFloat(input.value));
    hint.textContent = text || hint.getAttribute("data-default");
    hint.classList.toggle("money-readout", !!text);
  }
  var moneyInputs = form.querySelectorAll("input[data-money]");
  Array.prototype.forEach.call(moneyInputs, function (el) {
    el.addEventListener("input", function () { updateMoney(el); });
    if (el.value) updateMoney(el);
  });

  // ---- Clear a field's error as soon as the user edits it ----
  form.addEventListener("input", function (e) {
    var field = e.target.closest(".field");
    if (field && field.classList.contains("has-error")) {
      field.classList.remove("has-error");
      var hint = field.querySelector(".hint");
      if (hint && hint.getAttribute("data-default")) hint.textContent = hint.getAttribute("data-default");
    }
  });
  form.addEventListener("change", function (e) {
    var field = e.target.closest(".field");
    if (field) field.classList.remove("has-error");
  });

  // ---- Sample applicants ----
  function setPressed(btn) {
    samples.forEach(function (s) { s.setAttribute("aria-pressed", s === btn ? "true" : "false"); });
    if (btn) demoLink.setAttribute("href", demoBase + btn.getAttribute("data-preset"));
  }
  samples.forEach(function (btn) {
    btn.setAttribute("aria-pressed", "false");
    btn.addEventListener("click", function () {
      var values = JSON.parse(btn.getAttribute("data-values"));
      Object.keys(values).forEach(function (name) {
        var el = form.elements[name];
        if (el) { el.value = values[name]; el.closest(".field").classList.remove("has-error"); }
      });
      Array.prototype.forEach.call(moneyInputs, updateMoney);
      setPressed(btn);
    });
  });

  // ---- Clear ----
  document.getElementById("clear-btn").addEventListener("click", function () {
    Array.prototype.forEach.call(form.elements, function (el) {
      if (el.name) el.value = "";
    });
    Array.prototype.forEach.call(form.querySelectorAll(".has-error"), function (f) { f.classList.remove("has-error"); });
    Array.prototype.forEach.call(moneyInputs, function (el) {
      var hint = document.getElementById(el.id + "-hint");
      hint.textContent = hint.getAttribute("data-default");
      hint.classList.remove("money-readout");
    });
    setPressed(null);
    form.elements.district.focus();
  });

  // ---- Light client-side check so errors show inline before the round trip ----
  form.addEventListener("submit", function (e) {
    var firstBad = null;
    Array.prototype.forEach.call(form.querySelectorAll("input, select"), function (el) {
      var field = el.closest(".field");
      var bad = !el.checkValidity();
      field.classList.toggle("has-error", bad);
      var hint = field.querySelector(".hint");
      if (bad) {
        hint.textContent = el.validity.valueMissing ? "Required." : (el.validationMessage || "Check this value.");
        if (!firstBad) firstBad = el;
      }
    });
    if (firstBad) { e.preventDefault(); firstBad.focus(); }
  });
})();
