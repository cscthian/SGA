from .models import CargaAcademica


def asignaturas(request):
    try:
        cont = CargaAcademica.objects.asignatura_docente(request.user.username)
        print cont
        return {'ASIGNATURAS': cont}
    except:
        return {}
