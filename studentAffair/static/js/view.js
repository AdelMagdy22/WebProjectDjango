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