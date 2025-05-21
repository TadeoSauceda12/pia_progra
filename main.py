def main():
    ruta_csv= input("ingrese el nombre del archivo csv: ")
    df_ingresos = cargar_archivo_csv(ruta_csv)
    if df_ingresos is not None:
        analizar_ingresos(df_ingresos)
        graficar_por_categoria(df_ingresos)
        graficar_por_dia(df_ingresos)
        convertir_a_excel(df_ingresos)
        # Pregunta al usuario si quiere ordenar
        eleccion = input("\n¿Deseas ordenar los datos por (1) Fecha o (2) Monto? (0 para omitir): ")

        if eleccion == '1':
            orden_fecha = input("¿Orden descendente? (s/n): ").lower() == 's'
            df_ordenado = ordenar_por_fecha(df_ingresos, descendente=orden_fecha)
            guardar = input("\n¿Deseas guardar este archivo ordenado como un nuevo CSV? (s/n): ").lower()
            if guardar == 's':
                nombre = input("Indica el nombre para el nuevo archivo (sin .csv): ")
                guardar_como_csv(df_ordenado, nombre + ".csv")
        elif eleccion == '2':
            orden_monto = input("¿Orden descendente (mayor a menor)? (s/n): ").lower() == 's'
            df_ordenado = ordenar_por_monto(df_ingresos, descendente=orden_monto)
            guardar = input("\n¿Deseas guardar este archivo ordenado como un nuevo CSV? (s/n): ").lower()
            if guardar == 's':
                nombre = input("Indica el nombre para el nuevo archivo (sin .csv): ")
                guardar_como_csv(df_ordenado, nombre + ".csv")

if __name__ == "__main__":
    main()
