// phone_number_input.js

(function() {
  // Get the phone number input element
  const phoneNumberInput = document.getElementById('phone-number-input');

  // Add a focus event listener to the phone number input
  phoneNumberInput.addEventListener('focus', function() {
    // Check if the phone number input value does not start with '+7'
    if (!phoneNumberInput.value.startsWith('+7')) {
      // Set the initial value of the phone number input to '+7'
      phoneNumberInput.value = '+7';
    }
  });

  // Add an input event listener to the phone number input
  phoneNumberInput.addEventListener('input', function() {
    // Check if the phone number input value does not start with '+7'
    if (!phoneNumberInput.value.startsWith('+7')) {
      // Prepend '+7' to the input value
      phoneNumberInput.value = '+7' + phoneNumberInput.value;
    }
  });

  // Add a keydown event listener to the phone number input
  phoneNumberInput.addEventListener('keydown', function(event) {
    // Check if the pressed key is the backspace key (keyCode 8)
    if (event.keyCode === 8) {
      // Check if the caret position is before the '+7' prefix
      if (phoneNumberInput.selectionStart < 3) {
        // Prevent the default behavior of the backspace key
        event.preventDefault();
      }
    }
  });
})();

