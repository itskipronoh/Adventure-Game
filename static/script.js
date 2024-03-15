/* script.js */

// Function to handle moving to a new room
function move(direction, currentRoom) {
    // Perform AJAX request to move to the next room
    $.ajax({
        type: 'POST',
        url: '/move',
        data: { direction: direction, current_room: currentRoom },
        success: function(data) {
            // Update the game interface with the new room details
            $('#game-interface').html(data);
        },
        error: function(error) {
            console.log('Error moving to the next room:', error);
        }
    });
}

// Function to handle taking an item
function takeItem(item) {
    // Perform AJAX request to take the item
    $.ajax({
        type: 'POST',
        url: '/take_item',
        data: { item: item },
        success: function() {
            // Update the game interface to reflect the item in the inventory
            // You can add specific logic here based on the item taken
            console.log('Item taken:', item);
        },
        error: function(error) {
            console.log('Error taking the item:', error);
        }
    });
}

// Add event listeners for interactive elements in the game interface
$(document).ready(function() {
    // Example: Move to a new room when a direction button is clicked
    $('.direction-button').click(function() {
        var direction = $(this).data('direction');
        var currentRoom = $(this).data('current-room');
        move(direction, currentRoom);
    });

    // Example: Take an item when an item button is clicked
    $('.item-button').click(function() {
        var item = $(this).data('item');
        takeItem(item);
    });
});