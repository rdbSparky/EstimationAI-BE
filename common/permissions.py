from rest_framework.permissions import BasePermission

class RoleBasedPermission(BasePermission):
    """
    Centralized role-based permission system.
    Enforces permissions for all modules dynamically.
    """

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False  # User must be authenticated

        # Map request methods to actions
        method_to_action = {
            "GET": "read",
            "POST": "create",
            "PUT": "update",
            "PATCH": "update",
            "DELETE": "delete"
        }

        module_name = view.__class__.__name__.replace("ViewSet", "").lower()  # Infer module from viewset name
        action = method_to_action.get(request.method)

        # Check if the user has the necessary permissions
        return user.has_module_permission(module_name, action)
