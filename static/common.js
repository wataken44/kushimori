
var kushimori = kushimori || {};

kushimori.postJSON = function(url, data) {
  var session_id = Cookies.get('session_id');
  
  return $.ajax({
    'url': url,
    'type': 'POST',
    'data': data,
    'dataType': 'json',
    beforeSend: function (xhr){ 
        //xhr.setRequestHeader('Authorization', 'Bearer ' + session_id); 
        xhr.setRequestHeader('Authorization', 'Bearer ' + session_id); 
    }
  });
};
