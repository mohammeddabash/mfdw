$(document).ready(function(){
    $(".li").hide();
    $(".search").hide();
    $(".search_btn").hide();

 $(".mybtn").click(function(){
    $(".li").slideToggle();
    });


  $(".search_btn2").click(function(){
    $(".search").toggle();
    $(".search_btn").toggle();
     $(".search_btn2").toggle();

 });
});