from inputs import get_gamepad

def main():
    print("Escuchando eventos del mando... (CTRL+C para salir)")
    try:
        while True:
            events = get_gamepad()
            for event in events:
                print("---------------------------------------------------")
                print(f"Evento: {event.ev_type} | Código: {event.code} | Valor: {event.state}")
    except KeyboardInterrupt:
        print("\nSaliendo del programa.")


main()