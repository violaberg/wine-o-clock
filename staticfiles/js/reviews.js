document.addEventListener("DOMContentLoaded", () => {
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

  // Function to initialize edit functionality for a review
  function initializeEditReviewButton(button) {
    button.addEventListener("click", (e) => {
      const reviewId = e.target.getAttribute("data-review_id");
      const reviewBody = document.getElementById(`review${reviewId}`).innerText;
      reviewText.value = reviewBody;
      submitReviewButton.innerText = "Update";
      reviewForm.setAttribute("action", `edit_review/${reviewId}`);
      scrollToReviewForm();
    });
  }

  // Function to initialize delete functionality for a review
  function initializeDeleteReviewButton(button) {
    button.addEventListener("click", (e) => {
      const reviewId = e.target.getAttribute("data-review_id");
      deleteReviewConfirm.href = `delete_review/${reviewId}`;
      deleteReviewModal.show();
    });
  }

  // Attach event listeners to edit buttons
  for (let button of editReviewButtons) {
    initializeEditReviewButton(button);
  }

  // Attach event listeners to delete buttons
  for (let button of deleteReviewButtons) {
    initializeDeleteReviewButton(button);
  }
});