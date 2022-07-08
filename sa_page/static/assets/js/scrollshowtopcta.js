let lastKnownScrollPosition = 0;
let ticking = false;


function doSomething(scrollPos) {
    const elem = document.getElementById('topctabar');

    var viewport_height = document.documentElement.clientHeight;
    var viewport_width = document.documentElement.clientWidth;

    // console.log(viewport_height);

    if (viewport_width >= 768) {
        if (scrollPos > viewport_height) {
            elem.style.display = 'flex';
        } else {
            elem.style.display = 'none';
        }
    }


    // 依據捲動位置進行某些操作
   
}
document.addEventListener('scroll', function(e) {
    lastKnownScrollPosition = window.scrollY;

    if (!ticking) {
        window.requestAnimationFrame(function() {
            doSomething(lastKnownScrollPosition);
            ticking = false;
        });

        ticking = true;
    }
});