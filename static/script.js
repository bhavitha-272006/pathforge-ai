/* ═══════════════════════════════════════════
   PathForge AI — script.js
   Global JS: theme, sidebar, password toggle
═══════════════════════════════════════════ */

/* ── Dark Mode ──────────────────────────── */
(function () {
  const saved = localStorage.getItem('theme') || 'light';
  document.documentElement.setAttribute('data-theme', saved);
  updateThemeIcon(saved);
})();

function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('theme', next);
  updateThemeIcon(next);
}

function updateThemeIcon(theme) {
  const icons = document.querySelectorAll('#theme-icon, #theme-icon-mobile');
  icons.forEach(icon => {
    if (!icon) return;
    icon.className = theme === 'dark' ? 'ti ti-sun' : 'ti ti-moon';
  });
}

/* ── Mobile Sidebar ─────────────────────── */
function toggleSidebar() {
  const sidebar = document.getElementById('sidebar');
  if (sidebar) sidebar.classList.toggle('open');
}

// Close sidebar on outside click
document.addEventListener('click', function (e) {
  const sidebar = document.getElementById('sidebar');
  const toggle  = document.querySelector('.sidebar-toggle');
  if (sidebar && sidebar.classList.contains('open')) {
    if (!sidebar.contains(e.target) && e.target !== toggle && !toggle.contains(e.target)) {
      sidebar.classList.remove('open');
    }
  }
});

/* ── Password Visibility Toggle ─────────── */
function togglePass(inputId, btn) {
  const input = document.getElementById(inputId);
  const icon  = btn.querySelector('i');
  if (!input) return;
  if (input.type === 'password') {
    input.type = 'text';
    if (icon) icon.className = 'ti ti-eye-off';
  } else {
    input.type = 'password';
    if (icon) icon.className = 'ti ti-eye';
  }
}

/* ── Auto-dismiss flash messages ────────── */
document.addEventListener('DOMContentLoaded', function () {
  const flashes = document.querySelectorAll('.flash');
  flashes.forEach(flash => {
    setTimeout(() => {
      flash.style.transition = 'opacity 0.4s';
      flash.style.opacity = '0';
      setTimeout(() => flash.remove(), 400);
    }, 4000);
  });
});