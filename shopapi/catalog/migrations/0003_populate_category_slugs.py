from django.db import migrations
from django.utils.text import slugify


def generate_category_slugs(apps, schema_editor):
    Category = apps.get_model('catalog', 'Category')

    for category in Category.objects.all():
        base_slug = slugify(category.name)
        slug = base_slug
        counter = 1

        while Category.objects.filter(slug=slug).exclude(pk=category.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        category.slug = slug
        category.save(update_fields=['slug'])


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_category_slug'),
    ]

    operations = [
        migrations.RunPython(generate_category_slugs),
    ]