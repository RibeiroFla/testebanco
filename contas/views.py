from dal import autocomplete

from .models import Usuario


class UsuarioAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Usuario.objects.none()
        qs = Usuario.objects.all()

        if self.q:
            qs = qs.filter(nome__istartswith=self.q)

        return qs

