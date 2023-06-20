const csrftoken = getCookie('csrftoken');
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


const delButtons = document.getElementsByClassName('del')
for (let i = 0; i < delButtons.length; i++) {    
    delButtons[i].addEventListener('click', function(){
        if (confirm("Are you sure you want to delete this student with id: "+delButtons[i].getAttribute('id')))
        {
            fetch(`http://127.0.0.1:8000/studentAPI/delStudent/${delButtons[i].getAttribute('id')}/`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                  },
              }).then(function(){
                location.reload();
              })
              .catch(error => {
                console.error('Error:', error);
              });
        }
    });
}