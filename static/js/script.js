var types = document.querySelectorAll('.type');
  // Обрабатываем клик на каждом изображении
  types.forEach(function(type) {
    type.addEventListener('click', function() {
      var dishType = this.getAttribute('data-text');

      // Создаем XMLHttpRequest или используем fetch() для получения списка блюд в зависимости от выбранного типа блюда
      var request = new XMLHttpRequest();
      request.open('GET', '/get-recipes?type=' + dishType, true);
      request.onload = function() {
        if (request.status >= 200 && request.status < 400) {
          var recipes = JSON.parse(request.responseText);

          // Выводим список блюд в div #recipes-list
          var recipesList = document.getElementById('recipes-list');
          recipesList.innerHTML = '';

          recipes.forEach(function(recipe) {
            var recipeItem = document.createElement('div');
            recipeItem.innerHTML = '<h2>' + recipe.dish_type + '</h2><p><strong>Описание: </strong>' + recipe.title + '</p>';
            recipesList.appendChild(recipeItem);
          });
        }
      };
      request.send();
    });
  });


