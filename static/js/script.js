window?.addEventListener('DOMContentLoaded', () => {


    let phoneMask = IMask(
        document.querySelector('.modal input[name=phone]'), {
            mask: '+{7}(000)000-00-00'
        });

    const modal = document.querySelector('.modal');
    const form = document.querySelector('.modal__wrapper');
    const modalCross = document.querySelector('.modal__cross');
    const openModal = document.querySelectorAll('.open__modal');
    const allow_policy = document.querySelector('.modal__allow_policy');
    $(allow_policy).on('change', () => {
        if (allow_policy.checked) {
            document.querySelector('.modal__button').disabled = false
        } else {
            document.querySelector('.modal__button').disabled = true
        }

    })
    $(openModal).on('click', () => {
        modal.classList.add('modal_active');
        document.body.style.overflow = 'hidden';
    })
    $(modalCross).on('click', () => {
        modal.classList.remove('modal_active')
        document.body.style.overflow = 'auto';
    })
    $(modal).on('click', (e) => {
        if (!e.target.closest(".modal__wrapper")) {
            modal.classList.remove('modal_active');
            document.body.style.overflow = 'auto';
        }
    })


    form.addEventListener('submit', async (event) => {
        const formData = new FormData(event.target);
        event.preventDefault();
        await fetch('/orders/', {
            method: 'POST',
            body: formData
        }).then((response) => {
            return response.json().then(data => ({status: response.status, body: data}))
        }).then(data => {
            if (data.status >= 300) {
                $.notify(data.body, "error");
                console.log(data.body)
                event.stopPropagation()
                event.preventDefault()
            } else {
                $.notify(data.body, "success");
                modal.classList.remove('modal_active')
                document.body.style.overflow = 'auto';
                form.reset()
            }

        }).catch(err => {
            $.notify("Ошибка со стороны сервера, обратитесь позже.", "error");
            modal.classList.remove('modal_active')
            document.body.style.overflow = 'auto';
            form.reset()
        });

    })
})