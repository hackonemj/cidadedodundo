$(document).ready(function(){

	/*var height = $(window).height();

	$(document).scroll(function(){
		var width = $(window).width();
		var scrollTop = $(this).scrollTop();
		var pixels = scrollTop / 70;

		if (width > 1000){
			if(scrollTop < height){
				$("div.meusSlides").css({
					"-webkit-filter": "blur(" + pixels + "px)",
					"background-position": "center -" + pixels * 10 + "px"
				});

			}
		}

	});*/

	/***** Slide Show da página inicial *****
	****************************************/
	var slideIndex = 0;
  	showSlides();

  	function showSlides() {
	  	var i;
	  	var slides = document.getElementsByClassName("meusSlides");
	  	for (i = 0; i < slides.length; i++) {
	     	slides[i].style.display = "none";  
	  	}
	  	slideIndex++;
	  	if (slideIndex> slides.length) {slideIndex = 1}
	  	slides[slideIndex-1].style.display = "block";  
	  	setTimeout(showSlides, 4000); // Change image every 4 seconds
  	}

  	/***** Parte onde os efeitos das caixas de noticias são activados *****
	**********************************************************************/
  	var scroll;
  	var width;
  	var flag = false;
  	var card = $(".card-news");
  	var animacao = "animated slideInLeft";

  	$(window).scroll(function(){
		scroll = $(window).scrollTop();
		width = $(window).width();

		if (width > 900){
			if(scroll > 1080){
				if(!flag){
					card.addClass(animacao);
					flag = true;
				}
			}
		}

	})

});