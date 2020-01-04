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
        $(html).appendTo('modal').modal();
    });
});

$('#shuffleContainer').ready(function () {
    const Shuffle = window.Shuffle;
    const element = document.querySelector('.my-shuffle-container');
    const sizer = element.querySelector('.my-sizer-element');

    let shuffleInstance = new Shuffle(element, {
      itemSelector: '.certification-item',
        sizer: sizer,
        speed: 500,
        delimiter: ','
    });

    $('#btnAll').on('click', function () {
        console.log("all Bitches")
         shuffleInstance.filter();
    });

    $("#btnJava").on("click", function () {
        shuffleInstance.filter('Java')
    });

    $("#btnReactJs").on("click", function () {
        shuffleInstance.filter('ReactJs')
    });

    $("#btnPython").on("click", function () {
        shuffleInstance.filter('Python')
    });

    $("#btnDjango").on("click", function () {
        shuffleInstance.filter('Django')
    });

    $("#btnJavascript").on("click", function () {
        shuffleInstance.filter('Javascript')
    });

    $("#btnNodejs").on("click", function () {
        shuffleInstance.filter('NodeJs')
    });

    $("#btnVuejs").on("click", function () {
        shuffleInstance.filter('VueJs')
    });
});