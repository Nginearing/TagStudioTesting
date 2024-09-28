  <p id="WelcomeHeader">Welcome to the TagStudio Documentation</p>
<div class="button-container">
    <a href="#" onclick="changeText('English text')" onclick="" id="button-en">English</a>
    <a href="#" id="button-fr">French</a>
    <a href="#" id="button-es">Spanish</a>
  <script>
      function changeText(newText) {
        const textContentElement = document.getElementById('text-content');
        textContentElement.textContent = newText;
      }
  </script>
</div>
