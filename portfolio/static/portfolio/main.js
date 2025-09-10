document.addEventListener('DOMContentLoaded', function() {
    const heading = document.querySelector('h1');
    const text = heading.textContent;
    heading.textContent = '';
    let i = 0;
    function typeWriter() {
        if (i < text.length) {
            heading.textContent += text.charAt(i);
            i++;
            setTimeout(typeWriter, 150);
        }
    }
    typeWriter();
});
