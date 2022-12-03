window?.addEventListener('DOMContentLoaded', () => {


    let phoneMask = IMask(
        document.querySelector('.form__wrapper input[name=phone]'), {
            mask: '+{7}(000)000-00-00'
        });

    const form = document.querySelector('.form__wrapper');

    form.addEventListener('submit', async (e) => {
        const formData = new FormData(e.target);
        e.preventDefault();
        await fetch('/orders/', {
            method: 'POST',
            body: formData
        }).then((response) => {
            return response.json().then(data => ({status: response.status, body: data}))
        }).then(data => {
            if (data.status >= 300) {
                $.notify(data.body, "error");
            } else {
                $.notify(data.body, "success");
            }
            form.reset()
        }).catch(err => {
            $.notify("Ошибка со стороны сервера, обратитесь позже.", "error");
            form.reset()
        });

    })
})