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
        $(".create-profile").css("display","flex");
    });

    $('.exit-popup-container').on('click', function () {
        $(".background-overlay").css("display","none");
        $(".create-profile, .edit-profile, .delete-profile-popup-container").css("display","none");
    });


    $('.edit-profile-container').on('click', function () {
        $(".background-overlay").css("display","block");
        $(".edit-profile").css("display","flex");
    });


    $('.delete-profile-container').on('click', function () {
        $(".background-overlay").css("display","block");
        $(".delete-profile-popup-container").css("display","flex");
    });

    $('.search-option-container').on('click', function () {
        $(".history-content-container").css("display","none");
        $(".search-content-container").css("display","flex");

        $(".history-option-container").removeClass("selected-option-effect");
        $(".search-option-container").addClass("selected-option-effect");
    });

    $('.history-option-container').on('click', function () {
        $(".search-content-container").css("display","none");
        $(".history-content-container").css("display","flex");

        $(".search-option-container").removeClass("selected-option-effect");
        $(".history-option-container").addClass("selected-option-effect");
    });



});