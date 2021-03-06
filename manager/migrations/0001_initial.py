# Generated by Django 4.0.4 on 2022-05-29 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('item_category', models.CharField(choices=[('clothing', 'Clothing'), ('footwear', 'Foot Wear'), ('transport', 'Transport'), ('savings', 'Savings'), ('debtpayment', 'Paying Debts'), ('beddings', 'Beddings'), ('furniture', 'Furniture'), ('electronics', 'Electronics'), ('entertainment', 'Entertainment'), ('households', 'Households')], max_length=100)),
                ('price', models.FloatField()),
                ('purchase_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='IncomeAmount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('salary', 'Salary'), ('contract_hustles', 'Contract Gig'), ('one-time-gig', 'One Time Gig'), ('gifted', 'Allowance')], max_length=100)),
                ('date_received', models.DateField()),
                ('amt', models.IntegerField()),
            ],
        ),
    ]
