from apps.asistencia.models import CargaAcademica


def asignaturas(request):
    try:
        cont = CargaAcademica.objects.asignatura_docente(request.user.username)
        return {'asignaturas': cont}
    except:
        return {}
