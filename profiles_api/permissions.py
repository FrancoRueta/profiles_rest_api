from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Le permite al usuario editar su propio perfil."""
    #Retorna bool

    def has_object_permission(self, request, view, obj):
        """Chequea si el usuario esta intentando editar su propio perfil."""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id


        
