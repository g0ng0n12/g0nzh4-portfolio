const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');
    console.log("navSlide")
    // Toggle nav
    burger.addEventListener('click', () => {
        nav.classList.toggle('nav-active')

        // Animate Links
        navLinks.forEach((link, index) => {
            if(link.style.animation){
                console.log("empty")
                link.style.animation = '';
            }else{
                console.log("NOT empty")

                link.style.animation = `navLinkFade 0.5s ease forwards ${index/7+0.5}s`
            }
        });

        //burger animation
        burger.classList.toggle('toggle')
    });
};

navSlide();
