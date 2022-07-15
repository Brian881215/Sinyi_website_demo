from django.db import models


class SaRegularUsersOverview(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    first_date = models.DateTimeField(db_column='FIRST_DATE')
    week_number = models.BigIntegerField(db_column='WEEK_NUMBER')
    avg_usage_over_3_days = models.BigIntegerField(db_column='AVG_USAGE_OVER_3_DAYS')
    avg_usage_2_days = models.BigIntegerField(db_column='AVG_USAGE_2_DAYS')
    avg_usage_1_days = models.BigIntegerField(db_column='AVG_USAGE_1_DAYS')
    opened_sa_in_four_weeks = models.BigIntegerField(db_column='OPENED_SA_IN_FOUR_WEEKS')
    regular_percentage = models.FloatField(db_column='REGULAR_PERCENTAGE')

    class Meta:
        managed = False
        db_table = 'SA_REGULAR_USERS_OVERVIEW'


class SaHourlyUsageOverview(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    date = models.DateTimeField(db_column='DATE')
    weekday_name_abbreviated = models.TextField(db_column='WEEKDAY_NAME_ABBREVIATED')
    hour = models.BigIntegerField(db_column='HOUR')
    number_of_users = models.BigIntegerField(db_column='NUMBER_OF_USERS')

    class Meta:
        managed = False
        db_table = 'SA_HOURLY_USAGE_OVERVIEW'


class SaRegularUsersByType(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    first_date = models.DateTimeField(db_column='FIRST_DATE')
    week_number = models.IntegerField(db_column='WEEK_NUMBER')
    type_name = models.TextField(db_column='TYPE_NAME')
    type_level = models.TextField(db_column='TYPE_LEVEL')
    avg_usage_over_3_days = models.BigIntegerField(db_column='AVG_USAGE_OVER_3_DAYS')
    avg_usage_2_days = models.BigIntegerField(db_column='AVG_USAGE_2_DAYS')
    avg_usage_1_days = models.BigIntegerField(db_column='AVG_USAGE_1_DAYS')
    opened_sa_in_four_weeks = models.BigIntegerField(db_column='OPENED_SA_IN_FOUR_WEEKS')
    regular_percentage = models.FloatField(db_column='REGULAR_PERCENTAGE')

    class Meta:
        managed = False
        db_table = 'SA_REGULAR_USERS_BY_TYPE'


class SaHourlyUsageByType(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    type_name = models.TextField(db_column='TYPE_NAME')
    type_level = models.TextField(db_column='TYPE_LEVEL')
    date = models.DateTimeField(db_column='DATE')
    weekday_name_abbreviated = models.TextField(db_column='WEEKDAY_NAME_ABBREVIATED')
    hour = models.BigIntegerField(db_column='HOUR')
    number_of_users = models.BigIntegerField(db_column='NUMBER_OF_USERS')

    class Meta:
        managed = False
        db_table = 'SA_HOURLY_USAGE_BY_TYPE'
