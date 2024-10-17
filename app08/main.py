import flet as ft


def main(page: ft.Page):
#establecer tamaño de pantalla
    page.window_width=800
    page.window_height=800
    page.bgcolor="black"
    page.title="Mictlan"
    page.fgcolor="gray"
    
    #agregar audios
    
    Intro=ft.Audio(src="Intro.mp3",volume=1,balance=0)
    page.overlay.append(Intro)
    
    PrimerNivel=ft.Audio(src="Primer_Nivel.mp3", volume=1, balance=0)
    page.overlay.append(PrimerNivel)
    
    SegundoNivel=ft.Audio(src="Segundo_Primer_Nivel.mp3", volume=1, balance=0)
    page.overlay.append(SegundoNivel)
    
    TercerNivel=ft.Audio(src="Tercer__Nivel.mp3", volume=1, balance=0)
    page.overlay.append(TercerNivel)
    
    CuartoNivel=ft.Audio(src="Cuarto_Nivel.mp3", volume=1, balance=0)
    page.overlay.append(CuartoNivel)
    QuintoNivel=ft.Audio(src="Quinto_Nivel.mp3", volume=1, balance=0)
    page.overlay.append(QuintoNivel)
    
    SextoNivel=ft.Audio(src="Sexto_Nivel.mp3", volume=1, balance=0)
    page.overlay.append(SextoNivel)
    
    SeptimoNivel=ft.Audio(src="Septimo_Nivel.mp3", volume=1, balance=0)
    page.overlay.append(SeptimoNivel)
    
    OctavoNivel=ft.Audio(src="Octavo_Nivel.mp3", volume=1, balance=0)
    page.overlay.append(OctavoNivel)
    
    NovenoNivel=ft.Audio(src="Noveno_Nivel.mp3", volume=1, balance=0)
    page.overlay.append(NovenoNivel)
    
    #Agregamos las imagenes 
    btnIntro=ft.FilledButton(text="Escucha el Intro", disabled=False)
    
    btnNivel1=ft.ElevatedButton(text="Primer nivel")
    img1=ft.Image(src="Primer-Nivel.jpeg", width=150, height=150)
    
    btnNivel2=ft.ElevatedButton(text="Segundo nivel")
    img2=ft.Image(src="Segundo-Nivel.jpeg", width=150, height=150)

    btnNivel3=ft.ElevatedButton(text="Tercer nivel")
    img3=ft.Image(src="Tercer-Nivel.png", width=150, height=150)
    
    btnNivel4=ft.ElevatedButton(text="Cuarto nivel")
    img4=ft.Image(src="Cuarto_Nivel.jpeg", width=150, height=150)

    btnNivel5=ft.ElevatedButton(text="Quinto nivel")
    img5=ft.Image(src="Quinto_Nivel.jpeg", width=150, height=150)
    
    btnNivel6=ft.ElevatedButton(text="Sexto nivel")
    img6=ft.Image(src="Sexto_Nivel.jpeg", width=150, height=150)
    
    btnNivel7=ft.ElevatedButton(text="Septimo nivel")
    img7=ft.Image(src="Septimo_Nivel.jpeg", width=150, height=150)
    
    btnNivel8=ft.ElevatedButton(text="Octavo nivel")
    img8=ft.Image(src="Octavo_Nivel.png", width=150, height=150)
    
    btnNivel9=ft.ElevatedButton(text="Noveno nivel")
    img9=ft.Image(src="Noveno_Nivel.jpeg", width=150, height=150)

    page.add(
        ft.Row(
            alignment="start", 
            controls=[btnIntro]
        ),
        ft.Column(
            alignment="CENTER",
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Row(
                    alignment="CENTER",
                    controls=[btnNivel1,img1]
                ),
                ft.Column(
                    alignment="CENTER",
                    controls=[btnNivel2,img2]
                ),
                ft.Column(
                    alignment="CENTER",
                    controls=[btnNivel3,img3]
                ),
                ft.Column(
                    alignment="CENTER",
                    controls=[btnNivel4,img4]
                )
            ]
        )
    )
    












ft.app(main)
