from django.contrib import admin

from apps.ehr.models.medicalencounter import MedicalEncounter
from apps.ehr.models.medicalrecord import MedicalRecords
from apps.ehr.models.medication import Medication
from apps.ehr.models.medicationprescription import MedicationPrescription


class MedicalEncounterAdmin(admin.ModelAdmin):
    list_display = ('patient', 'encounter_date', 'visit_reason', 'diagnosis', 'created_at', 'updated_at')
    search_fields = ('patient__identifier', 'visit_reason', 'diagnosis')
    ordering = ('-encounter_date',)

    fieldsets = (
        ("Encounter Information", {
            'fields': ('patient', 'encounter_date', 'notes', 'visit_reason', 'diagnosis', 'recommendations')
        }),
        ("Timestamps", {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


class MedicalRecordsAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date', 'type', 'value', 'units', 'created_at', 'updated_at')
    search_fields = ('patient__identifier', 'type', 'value')
    ordering = ('-date',)

    fieldsets = (
        ("Record Information", {
            'fields': ('patient', 'date', 'type', 'value', 'units', 'comment')
        }),
        ("Timestamps", {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


class MedicationAdmin(admin.ModelAdmin):
    list_display = ('code', 'status', 'manufacturer', 'form', 'quantity', 'created_at', 'updated_at')
    search_fields = ('code', 'status', 'manufacturer', 'form')
    list_filter = ('status',)
    ordering = ('code',)

    fieldsets = (
        ("Medication Information", {
            'fields': ('code', 'status', 'manufacturer', 'form', 'quantity')
        }),
        ("Timestamps", {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


class MedicationPrescriptionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'medication', 'request_date', 'start_date', 'end_date', 'dose', 'created_at', 'updated_at')
    search_fields = ('patient__identifier', 'medication__code', 'dose')
    ordering = ('-request_date',)

    fieldsets = (
        ("Prescription Information", {
            'fields': ('patient', 'medication', 'request_date', 'start_date', 'end_date', 'dose', 'instructions')
        }),
        ("Timestamps", {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(MedicalEncounter, MedicalEncounterAdmin)
admin.site.register(MedicalRecords, MedicalRecordsAdmin)
admin.site.register(Medication, MedicationAdmin)
admin.site.register(MedicationPrescription, MedicationPrescriptionAdmin)
