from behave import given, when, then
import re

# Función para convertir palabras numéricas a números
def convertir_palabra_a_numero(palabra):
    try:
        return int(palabra)
    except ValueError:
        numeros = {
            "cero": 0, "uno": 1, "una":1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
            "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
            "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
            "diecisiete":17, "dieciocho":18, "diecinueve":19, "veinte":20,
            "treinta": 30, "cuarenta":40, "cincuenta":50, "sesenta":60, "setenta":70,
            "ochenta":80, "noventa":90, "media": 0.5,
            # ingles
            "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
            "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
            "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
            "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
            "seventy": 70, "eighty": 80, "ninety": 90, "half": 0.5

        }
        return numeros.get(palabra.lower(), 0)
    
# Funcion que convierte texto en horas decimales
def parsear_tiempo_en_horas(description):
    description = description.strip('"').strip(",").lower()
    description = description.replace('y', ' ')
    description = description.strip()

    # Manejar casos especiales como 'media hora'
    if description == 'media hora':
        return 0.5
    
    # Expresión regular para extraer horas y minutos
    pattern = re.compile(
		r'(?:(\w+)\s*(?:horas?|hours?))?\s*'
		r'(?:(\w+)\s*(?:minutos?|minutes?))?\s*'
		r'(?:(\w+)\s*(?:segundos?|seconds?))?'
	)
    match = pattern.match(description)

    if not match:
        raise ValueError(f"No se pudo interpretar la descripción del tiempo: {description}")

    hours_word = match.group(1) or "0"
    minutes_word = match.group(2) or "0"
    seconds_word = match.group(3) or "0"

    hours = convertir_palabra_a_numero(hours_word)
    minutes = convertir_palabra_a_numero(minutes_word)
    seconds = convertir_palabra_a_numero(seconds_word)

    return hours + (minutes / 60) + (seconds / 3600)

@given('que he comido {cukes:g} pepinos')
def step_given_eaten_cukes(context, cukes):
    context.belly.comer(cukes)

@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    total_time_in_hours = parsear_tiempo_en_horas (time_description)
    context.belly.esperar(total_time_in_hours)

@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not context.belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."

