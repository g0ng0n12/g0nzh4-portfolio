const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');
    // Toggle nav
    burger.addEventListener('click', () => {
        nav.classList.toggle('nav-active')

        // Animate Links
        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                console.log("empty")
                link.style.animation = '';
            } else {
                console.log("NOT empty")

                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.5}s`
            }
        });

        //burger animation
        burger.classList.toggle('toggle')
    });
};

navSlide();


$('#manual-ajax').click(function (event) {
    event.preventDefault();
    this.blur(); // Manually remove focus from clicked link.
    $.get(this.href, function (html) {
        console.log(html)
        $(html).appendTo('modal').modal();
    });
});

$(function () {
    let gridContainer = $('#shuffleContainer');
    let sizer = gridContainer.find('.certification-item');

    gridContainer.shuffle ({
        sizer: sizer,
        speed: 500,
        easing: 'ease-out'
    });

    $('#btnAll').on('click', function () {
        gridContainer.shuffle('shuffle', function($el, shuffle) {
            return true;
        });
    });

    $('#btnFurniture').on('click', function () {
        gridContainer.shuffle('shuffle', function($el, shuffle) {
            return $el.data('group') == 'furniture';
        });
    });

    $('#btnPet').on('click', function () {
        gridContainer.shuffle('shuffle', function($el, shuffle) {
            return $el.data('group') == 'pet';
        });
    });

    $('#btnElectronic').on('click', function () {
        gridContainer.shuffle('shuffle', function($el, shuffle) {
            return $el.data('group') == 'electronic';
        });
    });

    $('#btnTransportation').on('click', function () {
        gridContainer.shuffle('shuffle', function($el, shuffle) {
            return $el.data('group') == 'transportation';
        });
    });
});