import arcpy
import os
import time
import sys

def create_file_gdb(GDB_lokacija,pavadinimas):
    GDB_lokacija = f'{GDB_lokacija}'
    pavadinimas = f'{pavadinimas}.gdb'
    arcpy.CreateFileGDB_management(GDB_lokacija,pavadinimas)
    duomenys_gdb = f"{GDB_lokacija}\\duomenys.gdb"
    arcpy.CreateTable_management(out_path=duomenys_gdb, out_name="PDF", template=[], config_keyword="",
                                       out_alias="PDF")
    arcpy.CreateTable_management(out_path=duomenys_gdb, out_name="GEOTIFF", template=[], config_keyword="",
                                 out_alias="GEOTIFF")
    arcpy.CreateTable_management(out_path=duomenys_gdb, out_name="MXD", template=[], config_keyword="",
                                 out_alias="MXD")
    PDF = f"{duomenys_gdb}\\PDF"
    arcpy.AddField_management(in_table=PDF, field_name="Pavadinimas", field_type="TEXT", field_precision=None,
                              field_scale=None, field_length=None, field_alias="Pavadinimas",
                              field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")
    arcpy.AddField_management(in_table=PDF, field_name="Nomenklatura", field_type="TEXT", field_precision=None,
                              field_scale=None, field_length=None, field_alias="Nomenklatura",
                              field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")
    arcpy.AddField_management(in_table=PDF, field_name="Mastelis", field_type="TEXT", field_precision=None,
                              field_scale=None, field_length=None, field_alias="Mastelis",
                              field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")
    arcpy.AddField_management(in_table=PDF, field_name="Direktorija", field_type="TEXT", field_precision=None,
                              field_scale=None, field_length=None, field_alias="Direktorija",
                              field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")
    GEOTIFF = f"{duomenys_gdb}\\GEOTIFF"
    arcpy.AddField_management(in_table=GEOTIFF, field_name="Pavadinimas", field_type="TEXT", field_precision=None,
                              field_scale=None, field_length=None, field_alias="Pavadinimas",
                              field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")
    arcpy.AddField_management(in_table=GEOTIFF, field_name="Nomenklatura", field_type="TEXT", field_precision=None,
                              field_scale=None, field_length=None, field_alias="Nomenklatura",
                              field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")
    arcpy.AddField_management(in_table=GEOTIFF, field_name="Mastelis", field_type="TEXT", field_precision=None,
                              field_scale=None, field_length=None, field_alias="Mastelis",
                              field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")
    arcpy.AddField_management(in_table=GEOTIFF, field_name="Direktorija", field_type="TEXT", field_precision=None,
                              field_scale=None, field_length=None, field_alias="Direktorija",
                              field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")
    MXD = f"{duomenys_gdb}\\MXD"
    arcpy.AddField_management(in_table=MXD, field_name="Pavadinimas", field_type="TEXT", field_precision=None,
                              field_scale=None, field_length=None, field_alias="Pavadinimas",
                              field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")
    arcpy.AddField_management(in_table=MXD, field_name="Nomenklatura", field_type="TEXT", field_precision=None,
                              field_scale=None, field_length=None, field_alias="Nomenklatura",
                              field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")
    arcpy.AddField_management(in_table=MXD, field_name="Mastelis", field_type="TEXT", field_precision=None,
                              field_scale=None, field_length=None, field_alias="Mastelis",
                              field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")
    arcpy.AddField_management(in_table=MXD, field_name="Direktorija", field_type="TEXT", field_precision=None,
                              field_scale=None, field_length=None, field_alias="Direktorija",
                              field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")


# def lenteles_i_excel(lenteles,excel):
#     arcpy.env.workspace = "C:/Users/dovyd/PycharmProjects/Projektinis_darbas/Duomenys/Duoenu_saugojimas"
#     arcpy.TableToExcel_conversion(lenteles,excel)
#
#
# lenteles_PDF = "duomenys.gdb/PDF"
# excel_PDF = "PDF.xls"
# print(lenteles_i_excel(lenteles_PDF,excel_PDF))
print(create_file_gdb(r"C:\\Users\\dovyd\\PycharmProjects\\Projektinis_darbas\\Duomenys\\Duoenu_saugojimas","duomenys"))




