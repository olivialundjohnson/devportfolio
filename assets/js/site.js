// Optional homepage hero clip: never autoplay for visitors who prefer reduced motion.
(function () {
  var clip = document.querySelector('.js-hero-clip');
  if (!clip) return;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  if (reduce.matches) {
    clip.removeAttribute('autoplay');
    clip.pause();
  }
})();
