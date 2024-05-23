document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const submitButton = document.querySelector('.whoop');

    form.addEventListener('submit', function() {
        submitButton.innerHTML = '<i class="fa fa-spinner fa-spin"></i> Finding calories...';
        submitButton.disabled = true;
    });
});
