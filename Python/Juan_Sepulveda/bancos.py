import getpass  # Módulo para manejar la entrada de contraseñas de manera segura

class CuentaBancaria:
    def __init__(self, numero_cuenta, nombre_usuario, contraseña):
        """
        Constructor de la clase CuentaBancaria.
        Inicializa una nueva cuenta bancaria con el número de cuenta, nombre de usuario, contraseña y saldo inicial de 0.
        """
        self.numero_cuenta = numero_cuenta
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.saldo = 0.0  # El saldo inicial es 0

    def depositar(self, monto):
        """
        Método para depositar dinero en la cuenta.
        Aumenta el saldo si el monto es mayor que 0.
        """
        if monto > 0:  # Verifica que el monto a depositar sea positivo
            self.saldo += monto  # Aumenta el saldo en el monto especificado
            return True
        return False  # Retorna False si el monto no es válido

    def retirar(self, monto):
        """
        Método para retirar dinero de la cuenta.
        Disminuye el saldo si el monto es válido y no excede el saldo disponible.
        """
        if 0 < monto <= self.saldo:  # Verifica que el monto sea positivo y no exceda el saldo disponible
            self.saldo -= monto  # Disminuye el saldo en el monto especificado
            return True
        return False  # Retorna False si el monto no es válido o los fondos son insuficientes

    def consultar_saldo(self):
        """
        Método para consultar el saldo actual de la cuenta.
        """
        return self.saldo  # Retorna el saldo actual de la cuenta

class SistemaBancario:
    def __init__(self):
        """
        Constructor de la clase SistemaBancario.
        Inicializa un diccionario para almacenar las cuentas y establece la cuenta actual en None.
        """
        self.cuentas = {}  # Diccionario para almacenar las cuentas bancarias
        self.cuenta_actual = None  # Inicialmente no hay ninguna cuenta autenticada

    def crear_cuenta(self, numero_cuenta, nombre_usuario, contraseña):
        """
        Método para crear una nueva cuenta bancaria.
        Verifica si el número de cuenta ya existe y, si no, crea una nueva cuenta.
        """
        if numero_cuenta in self.cuentas:  # Verifica si el número de cuenta ya existe
            print("El número de cuenta ya existe.")  # Mensaje de error si la cuenta ya existe
            return False
        # Crea una nueva cuenta bancaria y la agrega al diccionario de cuentas
        self.cuentas[numero_cuenta] = CuentaBancaria(numero_cuenta, nombre_usuario, contraseña)
        print("Cuenta creada exitosamente.")  # Mensaje de éxito
        return True

    def autenticar_usuario(self, numero_cuenta, contraseña):
        """
        Método para autenticar a un usuario.
        Verifica si el número de cuenta y la contraseña son correctos.
        """
        cuenta = self.cuentas.get(numero_cuenta)  # Obtiene la cuenta bancaria con el número de cuenta proporcionado
        if cuenta and cuenta.contraseña == contraseña:  # Verifica si la cuenta existe y la contraseña es correcta
            self.cuenta_actual = cuenta  # Establece la cuenta actual como la cuenta autenticada
            return True
        return False  # Retorna False si la autenticación falla

    def cerrar_sesion(self):
        """
        Método para cerrar la sesión del usuario actual.
        """
        self.cuenta_actual = None  # Establece la cuenta actual como None

    def ejecutar(self):
        """
        Método principal que maneja la interfaz de usuario y las operaciones bancarias.
        Proporciona un menú interactivo para el usuario.
        """
        while True:
            if not self.cuenta_actual:  # Si no hay ninguna cuenta autenticada
                print("Bienvenido al Sistema Bancario")
                print("1. Crear Cuenta")
                print("2. Iniciar Sesión")
                print("3. Salir")
                opcion = input("Ingrese su elección: ")

                if opcion == '1':  # Opción para crear una nueva cuenta
                    numero_cuenta = input("Ingrese el número de cuenta: ")
                    nombre_usuario = input("Ingrese el nombre de usuario: ")
                    contraseña = getpass.getpass("Ingrese la contraseña: ")  # Lee la contraseña de manera segura
                    if self.crear_cuenta(numero_cuenta, nombre_usuario, contraseña):
                        print("Cuenta creada exitosamente.")
                    else:
                        print("No se pudo crear la cuenta. Inténtelo de nuevo.")

                elif opcion == '2':  # Opción para iniciar sesión
                    numero_cuenta = input("Ingrese el número de cuenta: ")
                    contraseña = getpass.getpass("Ingrese la contraseña: ")  # Lee la contraseña de manera segura
                    if self.autenticar_usuario(numero_cuenta, contraseña):
                        print("Inicio de sesión exitoso.")
                    else:
                        print("Número de cuenta o contraseña incorrectos.")

                elif opcion == '3':  # Opción para salir del sistema
                    print("Gracias por usar el Sistema Bancario. ¡Adiós!")
                    break

                else:  # Manejo de opción inválida
                    print("Opción inválida. Por favor, intente de nuevo.")
            else:  # Si hay una cuenta autenticada
                print(f"Bienvenido, {self.cuenta_actual.nombre_usuario}")
                print("1. Consultar Saldo")
                print("2. Depositar Dinero")
                print("3. Retirar Dinero")
                print("4. Cerrar Sesión")
                opcion = input("Ingrese su elección: ")

                if opcion == '1':  # Opción para consultar el saldo
                    print(f"Su saldo actual es: ${self.cuenta_actual.consultar_saldo():.2f}")

                elif opcion == '2':  # Opción para depositar dinero
                    monto = float(input("Ingrese el monto a depositar: "))
                    if self.cuenta_actual.depositar(monto):
                        print(f"${monto:.2f} depositados exitosamente.")
                    else:
                        print("Monto de depósito inválido.")

                elif opcion == '3':  # Opción para retirar dinero
                    monto = float(input("Ingrese el monto a retirar: "))
                    if self.cuenta_actual.retirar(monto):
                        print(f"${monto:.2f} retirados exitosamente.")
                    else:
                        print("Monto de retiro inválido o fondos insuficientes.")

                elif opcion == '4':  # Opción para cerrar sesión
                    self.cerrar_sesion()
                    print("Sesión cerrada exitosamente.")

                else:  # Manejo de opción inválida
                    print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    sistema_bancario = SistemaBancario()
    sistema_bancario.ejecut

    saludar= "buenas tardes"
    print(saludar)