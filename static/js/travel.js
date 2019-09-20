$(document).ready(function () {
    function openWindow() {
        document.getElementById('light').style.display = 'block';
        document.getElementById('fade').style.display = 'block';
    }

    function closeWindow() {
        document.getElementById('light').style.display = 'none';
        document.getElementById('fade').style.display = 'none';
    }

    var joinbtn = document.getElementById("joinButton");
    joinbtn.addEventListener("click", openWindow);

    var closebtn = document.getElementById("closeButton");
    closebtn.addEventListener("click", closeWindow);

    //这些图片的地址都可能有问题
    function changelike() {
        document.getElementById("liking").src = "img/likered.png";
    }

    function biglike() {
        if (document.getElementById("liking").src !== "static/img/likered.png") {
            document.getElementById("liking").src = "img/likebig.png";
        }
    }

    function smalllike() {
        if (document.getElementById("liking").src !== "img/likered.png") {
            document.getElementById("liking").src = "img/like.png";
        }
    }


    $('.bxslider').bxSlider({
        minSlides: 1,
        maxSlides: 3,
        slideWidth: 360,
        slideMargin: 22,
        //pager: false,
        nextText: "<i class='icon-right-open'></i>",
        prevText: "<i class='icon-left-open'></i>",
        moveSlides: 1,
        infiniteLoop: false,
        hideControlOnEnd: true,
        touchEnabled: false
    });

});


