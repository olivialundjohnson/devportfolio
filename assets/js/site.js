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

// Click-to-load Vimeo player: swap the still for the real player only when asked.
document.querySelectorAll('.js-vimeo').forEach(function (box) {
  var play = box.querySelector('.video-facade__play');
  play.addEventListener('click', function (e) {
    e.preventDefault();
    var src = 'https://player.vimeo.com/video/' + encodeURIComponent(box.dataset.vimeoId) + '?autoplay=1&title=0&byline=0&portrait=0&badge=0&autopause=0&dnt=1';
    if (box.dataset.vimeoHash) src += '&h=' + encodeURIComponent(box.dataset.vimeoHash);
    var frame = document.createElement('iframe');
    frame.src = src;
    frame.title = box.dataset.title || 'Video';
    frame.allow = 'autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share';
    frame.referrerPolicy = 'strict-origin-when-cross-origin';
    frame.allowFullscreen = true;
    box.replaceChildren(frame);
    box.classList.add('is-playing');
    frame.focus();
  });
});
