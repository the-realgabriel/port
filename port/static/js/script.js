document.addEventListener('DOMContentLoaded', function() {
    const gallery = document.querySelector('.gallery');
  
    // Function to style gallery items
    function styleGalleryItems() {
      const items = gallery.querySelectorAll('.gallery-item');
      let newestIndex = -1; // Find the index of the newest item
  
      items.forEach((item, index) => {
        if (item.dataset.isNew === 'true') {
          newestIndex = index;
        }
      });
  
      items.forEach((item, index) => {
        if (index === newestIndex) {
          // Style the newest item
          item.style.gridColumn = 'span 2'; // Span two columns
          item.style.gridRow = 'span 2'; // Span two rows
        } else {
          // Style older items as square tiles
          item.style.gridColumn = 'span 1'; // Span one column
          item.style.gridRow = 'span 1'; // Span one row
          item.style.aspectRatio = '1 / 1'; // Maintain a square aspect ratio
        }
      });
    }
  
    // Initial styling
    styleGalleryItems();
  
    // Handle new uploads (assuming you have a mechanism to add new items)
    // Example using a button:
    const uploadButton = document.getElementById('uploadButton'); 
    if (uploadButton) {
      uploadButton.addEventListener('click', () => {
        // ... (Your upload logic) ...
  
        // After adding a new item to the gallery:
        const newItem = gallery.querySelector('.gallery-item:last-child'); // Select the last (newest) item
        newItem.dataset.isNew = 'true'; // Add a data attribute to mark it as new
  
        styleGalleryItems(); // Restyle the gallery
      });
    }
  });
  