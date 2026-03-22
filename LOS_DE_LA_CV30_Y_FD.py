import random
import time
from pytiktokapi import TikTokApi
from pytiktokapi.exceptions import TikTokException

# CONFIGURACIÓN SEGURA
TIEMPO_MIN_ESPERA = 25
TIEMPO_MAX_ESPERA = 45
MAX_COMENTARIOS = 200

# LISTA DE COMENTARIOS PERSONALIZADA
LISTA_COMENTARIOS = [
    "¡Qué en vivo tan bueno!",
    "Me encanta tu contenido 🤩",
    "¡Sigue así!",
    "Un saludo desde México 🇲🇽",
    "¿Cuándo haces el próximo live?",
    "¡Gran trabajo!",
    "Estoy disfrutando mucho",
    "¡Los apoyo siempre!",
    "Este live es espectacular",
    "¡Vamos LOS DE LA CV30 Y FD!"
]

def main():
    print("🤖 LOS DE LA CV30 Y FD - BOT DE COMENTARIOS")
    usuario = input("Usuario TikTok: ")
    contraseña = input("Contraseña TikTok: ")
    url_live = input("URL del Live: ")

    try:
        api = TikTokApi.get_instance()
        api.login(username=usuario, password=contraseña)
        print("✅ Sesión iniciada correctamente")

        live_id = url_live.split("/")[-1].split("?")[0]
        contador = 0
        print(f"\n📤 INICIANDO ENVÍO - MAX {MAX_COMENTARIOS} COMENTARIOS")

        while contador < MAX_COMENTARIOS:
            try:
                comentario = random.choice(LISTA_COMENTARIOS)
                api.live.comment(live_id=live_id, comment=comentario)
                contador += 1
                tiempo = random.randint(TIEMPO_MIN_ESPERA, TIEMPO_MAX_ESPERA)
                print(f"[{contador}] ✅ {comentario} | Próximo en {tiempo}s")
                time.sleep(tiempo)
            except TikTokException as e:
                print(f"⚠️ Error: {e} | Esperando 60s...")
                time.sleep(60)

    except Exception as e:
        print(f"\n❌ Error fatal: {e}")
    finally:
        print(f"\n🛑 FINALIZADO - {contador} comentarios enviados")

if __name__ == "__main__":
    main()
