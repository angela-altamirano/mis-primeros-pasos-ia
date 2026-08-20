# Mi primer script de simulación de  
print("-- Iniciando Asistente de IA Escolar --")

#Simular una base de conocimientos simple de Procedimientos
base_conocimiento = {
    "hola": "Hola, Angela. ¿En qué te puedo ayudar hoy en tus prácticas?",
    "senati": "SENATI es la institución líder en formación tecnológica en el Perú",
    "ia": "La Inteligencia Artificial permite a las máquinas aprender y tomar decisiones."
}

#Solicitud de entrada de usuario simulación
pregunta_usuario = input("Escribe tu pregunta (hola / senati / ia: ").lower()

print (f"Usuario pregunta: {pregunta_usuario}")

#Lógica de coincidencia de palabras clave (La base de los primeros chatbots )
if pregunta_usuario in base_conocimiento:
    print(f"Asistente IA responde: {base_conocimiento[pregunta_usuario]}")
else:
    print("Asistente IA responde: Lo siento, aún estoy aprendiendo sobre ese tema.")