/*$(document).ready(function () {
  var docsecpos = $("#doc").offset(); 
});*/
//首頁動態效果
$(function(){
    $(window).scroll(function(){
      var windowheight = $( window ).height();
      var scrollTop = $(window).scrollTop();
      var docsecpos = $("#doc").offset().top - (windowheight/1);  
      var joinsecpos = $("#joinus").offset().top - (windowheight/2); 
      var aboutsecpos = $("#aboutto").offset().top - (windowheight/1); 
      var moviesecpos = $("#MOVIE").offset().top - (windowheight/1); 
      var peoplesecpos = $("#contact").offset().top - (windowheight/1); 

      console.log(scrollTop);
      console.log(docsecpos);
      console.log(aboutsecpos);
      console.log(moviesecpos);
      console.log(peoplesecpos);

      
      if(scrollTop >= docsecpos && scrollTop <= (docsecpos + windowheight )){
        $("#doc").addClass("showbg");
      }else{
        $("#doc").removeClass("showbg");
      }

      if(scrollTop >= joinsecpos && scrollTop <= (joinsecpos + windowheight )){
        $("#joinus .imagewrap").addClass("fadeup");
      }

      if(scrollTop >= aboutsecpos && scrollTop <= (aboutsecpos + windowheight )){
        $("#aboutto").addClass('aboutfade');
      }
      if(scrollTop >= moviesecpos && scrollTop <= (moviesecpos + windowheight )){
        $("#MOVIE .ToMovie").addClass('moviebig');
      }

      if(scrollTop >= peoplesecpos && scrollTop <= (peoplesecpos + windowheight )){
        $("#contact .great").addClass('animate__animated animate__fadeInRight animate__delay-1s');
      }
      if(scrollTop >= peoplesecpos && scrollTop <= (peoplesecpos + windowheight )){
        $("#contact .chose").addClass('animate__animated animate__fadeInLeft animate__delay-1s');
      }

			});
			
  });

//Gotop 動態
$(document).ready(function() {
  $(window).scroll(function() {
    if ($(this).scrollTop() > 0) {
      $('#gotop').fadeIn(200);
    } else {
      $('#gotop').fadeOut(200);
    }
  });
});


  $(document).ready(function () {
    //首頁計算器
        function circumference(r) {
            if (Number.isNaN(Number.parseFloat(r))) {
                return 0;
            }
            return parseFloat(r).toFixed(1) ;
        }
    
        $(".counti").each(function () {
            $(this).prop('Counter', 0).animate({
                Counter: $(this).text()
            }, {
                duration: 4000,
                easing: 'swing',
                step: function (now) {
                    $(this).text(Math.ceil(now));
                }
            });
        });
        $("#count3").each(function(){
            $(this).prop('Counter', 0).animate({
                Counter: $(this).text()
            }, {
                duration: 4000,
                easing: 'swing',
                step: function (now) {
                    $(this).text(circumference(now));
                }
            });
        });
    
    //視差動態效果paroller外掛
        $('.digital').paroller();
        $('.about-world').paroller();
        $('.about-title').paroller();
        $('.newlife').paroller({
            factorXs: 0.2,
            factorSm: 0.2,
            factorMd: 0.2,
            factorLg: 0.2,
            factorXl: 0.9,
            factor:0.1,
            type: 'foreground',
            direction: 'horizontal'
        }); 
    
        $('.circle-one').paroller({
            factorXs: -0.8,
            factorSm: -0.8,
            factorMd: -0.8,
            factorLg: -0.8,
            factorXl: -0.8,
            factor:-1,
            type: 'foreground',
            direction: 'vertical'
        }); 
        $('.circle-two').paroller({
            factorXs: 0.8,
            factorSm: 0.8,
            factorMd: 0.8,
            factorLg: 0.8,
            factorXl: 0.8,
            factor:-1,
            type: 'foreground',
            direction: 'vertical'
        }); 
        $('.doc-project').paroller({
            factorXs: -0.1,
            factorSm: -0.1,
            factorMd: -0.1,
            factorLg: -0.1,
            factorXl: -0.1,
            factor:1,
            type: 'foreground',
            direction: 'vertical'
        }); 

    //首頁影片播放按鈕
        $('.ToMovie').parent().click(function () {
            if($(this).children(".ToMovie").get(0).paused){        $(this).children(".ToMovie").get(0).play();   $(this).children(".playpause").fadeOut();
              }else{       $(this).children(".ToMovie").get(0).pause();
            $(this).children(".playpause").fadeIn();
              }
          });
    
    
    
    });

 //錨點滑動效果
$(document).ready(function() {
  $('a[href^="#"').on('click', function(e) {
    e.preventDefault();

    var target = this.hash;
    var $target = $(target);

    //Scroll and show hash
    $('html, body').animate({
      'scrollTop': $target.offset().top
    }, 750, 'swing', function() {
      window.location.hash = target;
    });
  });
});



$(document).ready(function() {
    
  /* Every time the window is scrolled ... */
  $(window).scroll( function(){
  
      /* Check the location of each desired element */
      $('.fade-in').each( function(i){
          
          var bottom_of_object = $(this).position().top + $(this).outerHeight()/3;
          var bottom_of_window = $(window).scrollTop() + $(window).height();
          
          /* If the object is completely visible in the window, fade it it */
          if( bottom_of_window > bottom_of_object ){
              
              $(this).animate({'opacity':'1'},1200);
          }
          
      }); 
  
  });
  $('.fade-in').paroller({
    factor:0.1,
    type: 'foreground',
    direction: 'vertical'
}); 

  
});
