$(document).ready(function () {

    $('.hero-segment h1').fadeIn(1500);  // effect on hero title
    $('.hero-segment p').fadeIn(2500);  // effect on hero title

    $('.nav-left').on('click', function () {
        window.location.href = '/';
    });

    $(".nav-button").mouseenter(function(){
        $(this).addClass("nav-buttons-hover");
    });

    $(".nav-button").mouseleave(function(){
        $(this).removeClass("nav-buttons-hover");
    });

    $('.profile-add-container').on('click', function () {
        $(".background-overlay").css("display","block");
        $(".create-profile-container").css("display","flex");
    });

    $('.exit-popup-container').on('click', function () {
        $(".background-overlay").css("display","none");
        $(".create-profile-container").css("display","none");
    });



});