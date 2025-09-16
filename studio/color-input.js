// No-jQuery Shiny InputBinding for <input type="color"> (works in Shinylive).
(function () {
  function tryRegister() {
    if (!(window.Shiny && Shiny.InputBinding && Shiny.inputBindings)) return false;

    var B = new Shiny.InputBinding();

    function on(el, t, h) { el.addEventListener(t, h); }
    function off(el, t, h) { el.removeEventListener(t, h); }

    Object.assign(B, {
      find: function (scope) { return scope.querySelectorAll(".py-color-input"); },
      initialize: function (el) { if (!el.value) el.value = "#1E90FF"; },
      getId: function (el) { return el.getAttribute("data-input-id") || el.id; },
      getValue: function (el) { return el.value || null; },
      setValue: function (el, v) {
        if (typeof v === "string" && v.startsWith("#")) {
          el.value = v;
          el.dispatchEvent(new Event("input", { bubbles: true }));
          el.dispatchEvent(new Event("change", { bubbles: true }));
        }
      },
      subscribe: function (el, cb) {
        el._cb = function () { cb(); };
        on(el, "input", el._cb);
        on(el, "change", el._cb);
      },
      unsubscribe: function (el) {
        if (el._cb) { off(el, "input", el._cb); off(el, "change", el._cb); delete el._cb; }
      },
      receiveMessage: function (el, data) {
        if (data && Object.prototype.hasOwnProperty.call(data, "value")) this.setValue(el, data.value);
      }
    });

    Shiny.inputBindings.register(B, "mini.color");
    console.log("[mini-color-app] color binding registered");
    return true;
  }

  if (!tryRegister()) {
    document.addEventListener("shiny:connected", function () { tryRegister(); }, { once: true });
  }

  console.log("[mini-color-app] color-binding.js loaded");
})();