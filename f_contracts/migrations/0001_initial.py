# Generated by Django 4.1.7 on 2024-03-19 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContractClauseTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_clause_type_code', models.CharField(max_length=3, unique=True, verbose_name='Contract Clause Type Code')),
                ('contract_clause_type_title', models.CharField(blank=True, max_length=55, null=True, unique=True, verbose_name='Contract Clause Type Title')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
            ],
            options={
                'verbose_name_plural': 'Contract Clause Types',
                'db_table': 'contract_clause_type',
                'ordering': ['contract_clause_type_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ContractClauses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_clause_number', models.CharField(max_length=15, verbose_name='Contract Clause Number')),
                ('contract_clause_title', models.CharField(max_length=55, verbose_name='Contract Clause Title')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
                ('contract_clause_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='f_contracts.contractclausetypes', verbose_name='Contract Clause Type ID')),
            ],
            options={
                'verbose_name_plural': 'Contract Clauses',
                'db_table': 'contract_clause',
                'ordering': ['contract_clause_number'],
                'managed': True,
                'unique_together': {('contract_clause_type', 'contract_clause_number')},
            },
        ),
    ]
