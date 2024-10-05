import reflex as rx
import reflex_local_auth


class ProtectedState(reflex_local_auth.LocalAuthState):
    username: str

    def on_load(self):
        if not self.is_authenticated:
            rx.window_alert(f"Invalid username or password.")
            return rx.redirect("/login")
        self.username = f"{self.authenticated_user.username}"
        print(f"valid username {self.username}")

    def do_logout(self):
        self.username = ""
        return reflex_local_auth.LocalAuthState.do_logout