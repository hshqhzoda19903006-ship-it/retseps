from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Taom turi"
        verbose_name_plural = "Taom turlari"


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Masalliq"
        verbose_name_plural = "Masalliqlar"


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="recipes"
    )
    description = models.TextField()
    ingredients = models.ManyToManyField(
        Ingredient,
        through="RecipeIngredient",
        related_name="recipes"
    )
    cooking_time = models.PositiveIntegerField(
        help_text="Tayyorlash vaqti (daqiqa)"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Taom"
        verbose_name_plural = "Taomlar"


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="recipe_ingredients"
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="recipe_ingredients"
    )
    quantity = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ingredient.name} - {self.quantity}"

    class Meta:
        verbose_name = "Taom masallig'i"
        verbose_name_plural = "Taom masalliqlari"


class RecipeStep(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="steps"
    )
    step_number = models.PositiveIntegerField()
    instruction = models.TextField()

    def __str__(self):
        return f"{self.recipe.title} - {self.step_number}-bosqich"

    class Meta:
        ordering = ["step_number"]
        verbose_name = "Tayyorlash bosqichi"
        verbose_name_plural = "Tayyorlash bosqichlari"
        constraints = [
            models.UniqueConstraint(
                fields=["recipe", "step_number"],
                name="unique_recipe_step"
            )
        ]