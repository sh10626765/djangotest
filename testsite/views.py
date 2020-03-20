from django.shortcuts import render, HttpResponse
from django.utils import timezone

# Create your views here.
from . import models
from . import utils


def index(request):
    return render(request, 'index.html')


def show_data(request):
    if request.method == 'POST':
        pass

    if request.method == 'GET':
        pass


def upload_data(request):
    if request.method == 'POST':
        upload_file = request.FILES.get('input_upload_data')
        upload_file_name = upload_file.name

        excel_file_process_object = utils.ExcelFileProcess(upload_file)
        features = excel_file_process_object.get_column_names()
        materials = excel_file_process_object.get_data()

        if excel_file_process_object.has_blank_cell():
            blank_cells = excel_file_process_object.blank_cells()
            return HttpResponse('Blank Cell(s) Exists in %s!' % blank_cells)

        LOFOutlier = excel_file_process_object.get_outlier_index_LOF()
        IFOutlier = excel_file_process_object.get_outlier_index_IF()
        cfm = False

        # TODO: while users confirm the data, we shold save the data to the database

        if cfm:
            result = models.SavaData(upload_file_name, materials)
            return HttpResponse('Success')
        else:
            return render(request, 'qc.html',
                          {'materials': materials,
                           'features': features,
                           'LOFOutliers': LOFOutlier,
                           'IFOutliers': IFOutlier,
                           })
            # return HttpResponse('Outliers detected with IsolationForest: %s<br>Outliers detected with LocalOutlierFactor: %s' % (IFOutlier, LOFOutlier))

    if request.method == 'GET':
        return render(request, 'upload_data.html')


def update_data(request):
    if request == 'POST':
        pass

    if request == 'GET':
        pass

    return HttpResponse('This page is used for updating data.')
