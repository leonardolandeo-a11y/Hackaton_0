/* ARCHIVO 2031 — verificación local del sello. */
(function () {
  "use strict";

  function sha256Hex(texto) {
    if (!window.crypto || !window.crypto.subtle) {
      return Promise.reject(new Error("sin-subtlecrypto"));
    }
    return window.crypto.subtle
      .digest("SHA-256", new TextEncoder().encode(texto))
      .then(function (buf) {
        return Array.prototype.map
          .call(new Uint8Array(buf), function (b) {
            return b.toString(16).padStart(2, "0");
          })
          .join("");
      });
  }

  function ranurasLlenas() {
    return Array.prototype.slice
      .call(document.querySelectorAll(".frag .frag__palabra"))
      .map(function (n) {
        return (n.textContent || "").trim().toUpperCase();
      })
      .filter(function (t) {
        return t && t !== "???";
      });
  }

  document.addEventListener("DOMContentLoaded", function () {
    var salida = document.getElementById("sello-estado");
    var campo = document.getElementById("sello-valor");
    if (!salida || !campo) return;

    function estado(clase, texto) {
      salida.className = "sello__estado " + clase;
      salida.textContent = texto;
    }

    var meta = document.querySelector('meta[name="equipo"]');
    var equipo = meta ? (meta.getAttribute("content") || "").trim().toUpperCase() : "";
    var sello = (campo.textContent || "")
      .trim().toUpperCase().replace(/\s*-\s*/g, "-");
    var llenas = ranurasLlenas();

    if (!equipo || equipo === "???") {
      estado("", 'Declara la letra del equipo en <meta name="equipo"> para verificar.');
      return;
    }
    if (!sello || sello === "???") {
      estado("", "Sello sin escribir · " + llenas.length + "/2 ranuras completas.");
      return;
    }

    Promise.all([fetch("scripts/claves.json").then(function (r) { return r.json(); }), sha256Hex(sello)])
      .then(function (par) {
        var base = par[0];
        var hex = par[1];
        var clave = base.equipos && base.equipos[equipo];
        if (!clave) {
          estado("sello__estado--error", 'Equipo "' + equipo + '" desconocido.');
          return;
        }
        if (hex === clave) {
          estado("sello__estado--ok", "✓ SELLO VERIFICADO · archivo restaurado.");
          document.documentElement.setAttribute("data-sello", "ok");
          var badge = document.querySelector(".hero__estado");
          if (badge) {
            badge.textContent = "RESTAURADO";
            badge.classList.add("hero__estado--ok");
          }
        } else {
          estado(
            "sello__estado--error",
            "✗ Sello incorrecto. Revisa el orden y la ortografía de las 2 palabras."
          );
        }
      })
      .catch(function () {
        estado("", "No se pudo verificar aquí (sirve la página por HTTP: python3 -m http.server).");
      });
  });
})();
