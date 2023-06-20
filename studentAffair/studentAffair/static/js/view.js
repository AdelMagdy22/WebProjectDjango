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


const statueButtons = document.getElementsByClassName('statue')
for (let i = 0; i < statueButtons.length; i++) {    
    statueButtons[i].addEventListener('click', function(){
        if (confirm("Are you sure you want to Change statue of this student with id: "+statueButtons[i].getAttribute('id')))
        {
            fetch(`http://127.0.0.1:8000/studentAPI/statueStudent/${statueButtons[i].getAttribute('id')}/`, {
                method: 'POST',
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

document.addEventListener('DOMContentLoaded', function () {
    
    // Select the drop-down element
    var selectStatue = document.querySelector('#selectStatue');

    // Attach an event listener to the drop-down element
    selectStatue.addEventListener('change', function () {

        // Select all the rows in the table body
        var rows = document.querySelectorAll('tbody tr');

        // If "All Students" is selected, show all rows
        if (selectStatue.value === 'All Students') {
            for (let i = 0; i < rows.length; i++) {
                rows[i].style.display = '';
            }
        }
        // If "Active" is selected, show only rows with "active" status
        else if (selectStatue.value === 'Active') {
            for (let i = 0; i < rows.length; i++) {
                var status = rows[i].querySelector('td:nth-child(9)').textContent;
                if (status.toLowerCase() === 'active') {
                    rows[i].style.display = '';
                } else {
                    rows[i].style.display = 'none';
                }
            }
        }
        // If "Inactive" is selected, show only rows with "inactive" status
        else if (selectStatue.value === 'InActive') {
            for (let i = 0; i < rows.length; i++) {
                var status = rows[i].querySelector('td:nth-child(9)').textContent;
                if (status.toLowerCase() === 'inactive') {
                    rows[i].style.display = '';
                } else {
                    rows[i].style.display = 'none';
                }
            }
        }
    });
});