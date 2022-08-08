from django.contrib import admin
from .models import Claim

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from rangefilter.filters import DateRangeFilter


class ClaimResource(resources.ModelResource):
    class Meta:
        model = Claim

    def dehydrate_status(self, claim):
        if claim.status is not None:
            return claim.get_status().label


class ClaimAdmin(ImportExportModelAdmin):
    resource_class = ClaimResource
    list_display = (
        'id',
        'date_of_the_application',
        'number_of_contract',
        'reason',
        'telephone_number',
        'town',
        'status',
        'repair_date',
    )
    list_filter = (
        ('date_of_the_application', DateRangeFilter), ('repair_date', DateRangeFilter),
    )
    empty_value_display = "-пусто-"
    search_fields = ['number_of_contract', 'telephone_number']


admin.site.register(Claim, ClaimAdmin)
