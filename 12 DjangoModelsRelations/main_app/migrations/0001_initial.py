from django.db import migrations, models
import django.db.models.deletion
import django.utils.datetime_safe


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('lecturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.lecturer')),
            ],
        ),
        migrations.CreateModel(
            name='StudentEnrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.subject')),
            ],
        ),
        migrations.AlterModelTable(
            name='studentenrollment',
            table='main_app_student_subjects',
        ),
        migrations.AlterField(
            model_name='student',
            name='subjects',
            field=models.ManyToManyField(through='main_app.StudentEnrollment', to='main_app.Subject'),
        ),
    ]

    # Next, in the operations list, we add a specialized operation called SeparateDatabaseAndState which allows us to alter the state and the database separately. In this specialized operation, we will add the above-written state operations.
    operations = [
        migrations.SeparateDatabaseAndState(state_operations=state_operations),

        # We need to add the additional fields from the StudentEnrollment model: "entrollment_date" and "grade".
        migrations.AddField(
            model_name='StudentEnrollment',
            name='enrollment_date',
            field=models.DateField(default=django.utils.datetime_safe.date.today),
        ),
        migrations.AddField(
            model_name='StudentEnrollment',
            name='grade',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')],
                                   max_length=1, null=True),
        ),

        # Finally, we reset the name (which is set to main_app_student_subjects above) to use the default naming convention
        migrations.AlterModelTable(
            name='studentenrollment',
            table=None,
        ),
    ]

