$(document).ready(function(){
var tweets_col = " ";

for (var i = 0; i <= _tweets.results.length - 1; i++) {
	tweets_col = tweets_col + "<li id='li_" + i + "'><span><img class='img' src='" + _tweets.results[i].profile_image_url_https + "' /> @" + _tweets.results[i].from_user + "<p>"+ _tweets.results[i].text + "</p></li>";
};

$("#recient_activity").html(tweets_col);
$("#recient_activity").css("overflow-y","scroll");

$("#bMapa").click(function() {
	$("#park_rutam").css("display","none");
	$("#map_canvas").css("display","block");
});

$("#bRuta").click(function() {
	$("#map_canvas").css("display","none");
	$("#park_rutam").css("display","block");
});

});
//var obj_g = null;
function doLogin()
{
	google.load("gdata", "1");
	//scope = "http://www.google.com/calendar/feeds";
	scope = "http://www.google.com/login/captcha";
	obj_g = google;
	var token = google.accounts.user.login(scope);
}
