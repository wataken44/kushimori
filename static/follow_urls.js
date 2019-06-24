
var kushimori = kushimori || {};

kushimori.follow_urls = function() {
  let data = {};

  //data["session"] = Cookies.get("session_id");
  data["urls"] = $("#urlsTextArea").val();
  data["mode"] = $('input[name=followModeRadioOptions]:checked').val();
  
  kushimori.postJSON("/dashboard/follow_urls", data);
};

$(document).ready(function() {
  $("#submitButton").on("click", kushimori.follow_urls);
});
