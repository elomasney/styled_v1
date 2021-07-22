/**
 * @function - displays sweetalert confirmation on 'delete product' button
 */
//Popup confirm delete product on link click
$(function () {
    $('.product_delete').on('click', function () {
        let delete_url = $(this).attr('data-href');
        confirm_delete_product(delete_url);
    });
});

/**
 * @function confirm_delete_product - displays sweetalert popup
 * @param delete_url - path to delete a product from the db
 * Asks user to confirm if they want to delete a product from the database
 * On confirmation the product is deleted from the db
 */
//Confirm Delete Product
function confirm_delete_product(delete_url) {

    Swal.fire({
        title: 'Delete this Product?',
        text: "This product will be permanently deleted!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: 'rgba(235,132,77)',
        cancelButtonColor: '#000',
        confirmButtonText: 'Yes, delete it!',

    }).then((result) => {
        if (result.isConfirmed) {

            window.location.href = delete_url;

            Swal.fire(
                'Deleted!',
                'This product has been deleted.',
                'success');

        }
    });
}

/**
 * @function - displays sweetalert confirmation on 'delete image' button
 */
//Popup confirm delete image from gallery on link click
$(function () {
    $('.image_delete').on('click', function () {
        let delete_url = $(this).attr('data-href');
        confirm_delete_image(delete_url);
    });
});

/**
 * @function confirm_delete_image - displays sweetalert popup
 * @param delete_url - path to delete a gallery image from the db
 * Asks user to confirm if they want to delete a gallery image from the gallery
 * On confirmation the image is deleted from the db
 */
//Confirm Delete Image
function confirm_delete_image(delete_url) {

    Swal.fire({
        title: 'Delete this Image?',
        text: "This image will be permanently deleted!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: 'rgba(235,132,77)',
        cancelButtonColor: '#000',
        confirmButtonText: 'Yes, delete it!',

    }).then((result) => {
        if (result.isConfirmed) {

            window.location.href = delete_url;

            Swal.fire(
                'Deleted!',
                'This image has been deleted.',
                'success');

        }
    });
}

