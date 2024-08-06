function filterGallery() {
    let input = document.getElementById('search-bar');
    let filter = input.value.toLowerCase();
    let galleryItems = document.getElementsByClassName('gallery-item');

    for (let i = 0; i < galleryItems.length; i++) {
        let description = galleryItems[i].getAttribute('data-description');
        if (description.toLowerCase().includes(filter)) {
            galleryItems[i].style.display = "";
        } else {
            galleryItems[i].style.display = "none";
        }
    }
}
