const editReviewButtons = document.getElementsByClassName("review-btn-edit");
const reviewText = document.getElementById("id_body");
const reviewForm = document.getElementById("reviewForm");
const submitReviewButton = document.getElementById("submitReviewButton");

const deleteReviewModal = new bootstrap.Modal(document.getElementById("deleteReviewModal"));
const deleteReviewButtons = document.getElementsByClassName("review-btn-delete");
const deleteReviewConfirm = document.getElementById("deleteReviewConfirm");


// Function to scroll to the review form
function scrollToReviewForm() {
  reviewForm.scrollIntoView({
    behavior: 'smooth'
  });
}


/**
 * Initializes edit functionality for the provided edit buttons.
 * 
 * For each button in the `editReviewButtons` collection:
 * - Retrieves the associated review's ID upon click.
 * - Fetches the content of the corresponding review.
 * - Populates the `reviewText` input/textarea with the review's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_review/{reviewId}` endpoint.
 */
for (let button of editReviewButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("data-review_id");
    let reviewBody = document.getElementById(`review${reviewId}`).innerText;
    reviewText.value = reviewBody;
    submitReviewButton.innerText = "Update";
    reviewForm.setAttribute("action", `edit_review/${reviewId}`);
    scrollToReviewForm();
  });
}


/**
 * Initializes deletion functionality for the provided delete buttons.
 * 
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated review's ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the 
 * deletion endpoint for the specific review.
 * - Displays a confirmation modal (`deleteModal`) to prompt 
 * the user for confirmation before deletion.
 */
for (let button of deleteReviewButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("data-review_id");
    deleteReviewConfirm.href = `delete_review/${reviewId}`;
    deleteReviewModal.show();
  });
}