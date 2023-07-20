
if (window.innerWidth < 768) {
	[].slice.call(document.querySelectorAll('[data-bss-disabled-mobile]')).forEach(function (elem) {
		elem.classList.remove('animated');
		elem.removeAttribute('data-bss-hover-animate');
		elem.removeAttribute('data-aos');
		elem.removeAttribute('data-bss-parallax-bg');
		elem.removeAttribute('data-bss-scroll-zoom');
	});
}

document.addEventListener('DOMContentLoaded', function() {

(function(){

	if (!('requestAnimationFrame' in window)) return;

	var backgrounds = [];
	var backgroundToSpeed = new WeakMap;
	var parallaxBackgrounds = document.querySelectorAll('[data-bss-scroll-zoom]');

	for (var el of parallaxBackgrounds) {
		var bg = document.createElement('div');

		bg.style.backgroundImage = el.style.backgroundImage;
		bg.style.backgroundSize = 'cover';
		bg.style.backgroundPosition = 'center';
		bg.style.position = 'absolute';
		bg.style.height = '100%';
		bg.style.width = '100%';
		bg.style.top = 0;
		bg.style.left = 0;
		bg.style.zIndex = -100;

		el.appendChild(bg);
		backgrounds.push(bg);
		backgroundToSpeed.set(bg, el.getAttribute('data-bss-scroll-zoom-speed') || 1);

		el.style.position = 'relative';
		el.style.background = 'transparent';
		el.style.overflow = 'hidden';
	}

	if (!backgrounds.length) return;

	var visible = [];
	var scheduled;

	window.addEventListener('scroll', scroll);
	window.addEventListener('resize', scroll);

	scroll();

	function scroll() {

		visible.length = 0;

		for (var i = 0; i < backgrounds.length; i++) {
			var rect = backgrounds[i].parentNode.getBoundingClientRect();

			if (rect.bottom > 0 && rect.top < window.innerHeight) {
				visible.push({
					rect: rect,
					node: backgrounds[i],
					speed: backgroundToSpeed.get(backgrounds[i])
				});
			}

		}

		cancelAnimationFrame(scheduled);

		if (visible.length) {
			scheduled = requestAnimationFrame(update);
		}

	}

	function update(){

		for(var i = 0; i < visible.length; i++){
			var rect = visible[i].rect;
			var node = visible[i].node;
			var speed = visible[i].speed;

			var quot = rect.top < 0 ? Math.abs(rect.top) / rect.height : 0;

			node.style.transform = 'scale3d('+ (1 + quot * speed) + ', ' + (1 + quot * speed) + ', 1)';
		}

	}

})();
}, false);

// Code to make recipe-prep text to align-left because boostrap rules prevent me from changing it
document.addEventListener("DOMContentLoaded", function () {
    // console.log("Script is running");

    const prepElements = document.getElementsByClassName("prep-text");
    console.log(prepElements.length);

    for (let i = 0; i < prepElements.length; i++) {
        prepElements[i].style.textAlign = "left";
    }
});

// testing why js code wasn't working
// const prepElements = document.getElementsByClassName("prep-text");
// for (let i = 0; i < prepElements.length; i++) {
//   prepElements[i].style.backgroundColor = "yellow";
// }


// const prepElements = document.getElementsByClassName("prep-text");
//   for (let i = 0; i < prepElements.length; i++) {
//     prepElements[i].style.textAlign = "left";
//   }
  

const image = document.getElementById('zoom-image');
const observer = new IntersectionObserver(entries => {
	entries.forEach(entry => {
	  if (entry.isIntersecting) {
		image.classList.add('zoomed');
	  } else {
		image.classList.remove('zoomed');
	  }
	});
  });
  
  observer.observe(image);