from PIL import Image
import os


# Jusqu'à la fonction simple_loop(), toutes les fonctions servent pour le menu.
# Ensuite, ce sont les fonctions pour générer les filtres.
# Dans chaques menus, les images, les filtres et les valeurs sélectionnés sont passés en arguments

# Voici, le menu principal, après une selection dans un menu, on retombe toujours sur celui-ci
def main_menu(selected_image, selected_filter, selected_value):
    print("\033[91m" + r"""
        ██╗███╗   ███╗ █████╗  ██████╗ ███████╗    ███████╗██╗██╗  ████████╗███████╗██████╗      ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
        ██║████╗ ████║██╔══██╗██╔════╝ ██╔════╝    ██╔════╝██║██║  ╚══██╔══╝██╔════╝██╔══██╗    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
        ██║██╔████╔██║███████║██║  ███╗█████╗      █████╗  ██║██║     ██║   █████╗  ██████╔╝    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
        ██║██║╚██╔╝██║██╔══██║██║   ██║██╔══╝      ██╔══╝  ██║██║     ██║   ██╔══╝  ██╔══██╗    ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
        ██║██║ ╚═╝ ██║██║  ██║╚██████╔╝███████╗    ██║     ██║███████╗██║   ███████╗██║  ██║    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
        ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝    ╚═╝     ╚═╝╚══════╝╚═╝   ╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝""")
    print("\033[0m" + r"""
        ╔═══════════════════════════════════════╗
        ║ 1. - Sélectionner l'image             ║
        ║ 2. - Sélectionner le ou les filtre(s) ║
        ║ 3. - Générer l'image                  ║
        ║ 4. - Réinitialiser les sélections     ║
        ║ 5. - Supprimer le dernier filtre      ║
        ╚═══════════════════════════════════════╝""")

    print_options(selected_image, selected_filter, selected_value)
    choice = choice_input(5)

    if choice == 1:
        image_selection(selected_image, selected_filter, selected_value)
    elif choice == 2:
        filter_selection(selected_image, selected_filter, selected_value)
    elif choice == 3:
        generate_image(selected_image, selected_filter, selected_value)
    elif choice == 4:
        main_menu("", [], [])
    elif choice == 5 and len(selected_filter) > 0:
        selected_filter.pop(-1)
        selected_value.pop(-1)
        main_menu(selected_image, selected_filter, selected_value)
    else:
        print("\033[91m" + f"Vous ne pouvez pas supprimer le dernier filtre si vous n'en avez pas sélectionné")
        main_menu(selected_image, selected_filter, selected_value)


# print_options affiche l'image, le ou les filtres, et la ou les valeurs sélectionnées
def print_options(selected_image, selected_filter, selected_value):
    print(rf"""
        Image: {selected_image}
        Filtre(s): {selected_filter}
        Valeur: {selected_value}""")


# Fonction pour les choix dans les menus. Si le chiffre entré est trop grand, l'utilisateur est invité à retaper le bon chiffre.
def choice_input(nbr_max):
    choice = int(input(r"""
        Choisir un numéro : """))
    print("""------------------------------------------------------------""")
    while choice < 1 or choice > nbr_max:
        print("\033[91m" + f"Veuillez choisir un nombre entre 1 et {nbr_max}")
        choice = int(input("\033[0m" + r"""
        Choisir un numéro : """))
        print("""------------------------------------------------------------""")
    os.system("clear")
    return choice


def image_selection(selected_image, selected_filter, selected_value):
    print(r"""
        ╔═════════════════╗
        ║ 1. - maison.jpg ║
        ║ 2. - rick.png   ║
        ╚═════════════════╝""")

    print_options(selected_image, selected_filter, selected_value)
    choice = choice_input(2)
    choice_dict = {1: "maison.jpg", 2: "rick.png"}
    selected_image = choice_dict[choice]
    main_menu(selected_image, selected_filter, selected_value)


def filter_selection(selected_image, selected_filter, selected_value):
    print("\033[0m" + r"""
        ╔══════════════════════════════════╗
        ║ 1. - Filtres de couleur          ║
        ║ 2. - Filtres de saturation       ║
        ║ 3. - Filtre de pixellisation     ║
        ║ 4. - Filtre miroir et symétrique ║
        ╚══════════════════════════════════╝""")

    print_options(selected_image, selected_filter, selected_value)
    choice = choice_input(4)
    choice_dict = {1: color_selection, 2: saturation_selection, 3: pixel_selection, 4: mirror_selection}
    choice_dict[choice](selected_image, selected_filter, selected_value)


def color_selection(selected_image, selected_filter, selected_value):
    print("\033[0m" + r"""
        ╔═════════════════════════════╗
        ║ 1. - Rouge                  ║
        ║ 2. - Vert                   ║
        ║ 3. - Bleu                   ║
        ║ 4. - Jaune                  ║
        ║ 5. - Cyan                   ║
        ║ 6. - Magenta                ║
        ║ 7. - lum-noir               ║
        ║ 8. - lum-blanc              ║
        ║ 9. - color-rouge            ║
        ║ 10. - color-vert            ║
        ║ 11. - color-bleu            ║
        ║ 12. - Gris                  ║
        ║ 13. - Gris-rouge            ║
        ║ 14. - Gris-vert             ║
        ║ 15. - Gris-bleu             ║
        ║ 16. - Gris-jaune            ║
        ║ 17. - Gris-cyan             ║
        ║ 18. - Gris-magenta          ║
        ║ 19. - Inverser les couleurs ║
        ║ 20. - Color512              ║
        ╚═════════════════════════════╝""")

    print_options(selected_image, selected_filter, selected_value)
    choice = choice_input(20)
    choice_dict = {1: "red", 2: "green", 3: "blue", 4: "yellow", 5: "cyan", 6: "magenta", 7: "black", 8: "white",
                   9: "color-red", 10: "color-green", 11: "color-blue",
                   12: "gray", 13: "gray-red", 14: "gray-green", 15: "gray-blue", 16: "gray-yellow", 117: "gray-cyan",
                   18: "gray-magenta", 19: "invert", 20: "color512"}
    value = 0
    if choice < 12:
        value = power_selection()
    selected_filter = [*selected_filter, choice_dict[choice]]
    selected_value = [*selected_value, value]
    main_menu(selected_image, selected_filter, selected_value)


def saturation_selection(selected_image, selected_filter, selected_value):
    print("\033[0m" + r"""
        ╔════════════════════════════════╗
        ║ 1. - Saturation classique      ║
        ║ 2. - Saturation noir & blanche ║
        ╚════════════════════════════════╝""")
    print_options(selected_image, selected_filter, selected_value)
    choice = choice_input(2)
    choice_dict = {1: "saturation", 2: "black_white"}
    selected_filter = [*selected_filter, choice_dict[choice]]
    value = power_selection()
    selected_value = [*selected_value, value]
    main_menu(selected_image, selected_filter, selected_value)


def power_selection():
    print(r"""
        ╔════════════════════════════════════════╗
        ║ Veuillez choisir un nombre entier et   ║
        ║ positif qui déterminera la puissance   ║
        ║ du filtre de couleur (max 255)         ║
        ╚════════════════════════════════════════╝""")
    value = choice_input(255)
    return value


def pixel_selection(selected_image, selected_filter, selected_value):
    print("\033[0m" + r"""
        ╔════════════════════════════════════════╗
        ║ Veuillez choisir un nombre entier et   ║
        ║ positif qui déterminera la taille d'un ║
        ║ pixel de l'effet pixellisation         ║
        ╚════════════════════════════════════════╝""")

    print_options(selected_image, selected_filter, selected_value)
    choice = choice_input(9999)
    selected_filter = [*selected_filter, "pixelation"]
    selected_value = [*selected_value, choice]
    main_menu(selected_image, selected_filter, selected_value)


def mirror_selection(selected_image, selected_filter, selected_value):
    print("\033[0m" + r"""
        ╔══════════════════════════╗
        ║ 1. - Miroir vertical     ║
        ║ 2. - Miroir horizontal   ║
        ║ 3. - Symétrie vertical   ║
        ║ 4. - Symétrie horizontal ║
        ╚══════════════════════════╝""")
    print_options(selected_image, selected_filter, selected_value)
    choice = choice_input(4)
    choice_dict = {1: "vertical-mirror", 2: "horizontal-mirror", 3: "horizontal-symmetry", 4: "horizontal-symmetry"}
    selected_filter = [*selected_filter, choice_dict[choice]]
    selected_value = [*selected_value, "0"]
    main_menu(selected_image, selected_filter, selected_value)


# pour générer un filtre sur une image à partir des paramètres selectionnes
def generate_image(selected_image, selected_filter, selected_value):
    if selected_image and selected_filter and selected_value:
        image = Image.open(f"./{selected_image}")
        image = image.convert("RGB")
        for filter_name in selected_filter:
            if filter_name == "pixelation":
                image = pixel_loop(image, selected_value[selected_filter.index(filter_name)])
            elif filter_name == "black-white" or filter_name == "saturation":
                image = simple_loop(image, 1, filter_name, selected_value[selected_filter.index(filter_name)])
            elif filter_name == "vertical-mirror" or filter_name == "horizontal-mirror" or filter_name == "vertical-symmetry" or filter_name == "horizontal-symmetry":
                image = mirror_loop(image, filter_name)
            else:
                image = simple_loop(image, 0, filter_name, selected_value[selected_filter.index(filter_name)])
        choice = 0
        while choice != 3:
            print(r"""
        ╔══════════════════════════╗
        ║ 1. - Enregistrer l'image ║
        ║ 2. - Voir l'image        ║
        ║ 3. - Menu principal      ║
        ╚══════════════════════════╝""")
            choice = choice_input(3)
            if choice == 1:
                image.save(f"filtered-{selected_image}")
            elif choice == 2:
                image.show()
            else:
                main_menu(selected_image, selected_filter, selected_value)
    else:
        print("\033[91m" + "Veuillez sélectionner une image et au moins un filtre")
        main_menu(selected_image, selected_filter, selected_value)


# Toutes les fonctions pour faire des filtres à partir d'ici


# les filtres simples qui modifient chaque pixel de l'image un à un sans utiliser d'autres pixels
def simple_loop(image, method_nbr, filter_name, power=255):
    width, height = image.size
    for imx in range(width):
        for imy in range(height):
            rgb = image.getpixel((imx, imy))
            method_dict = {0: color_filter, 1: saturation_filter, 2: mirror_loop}
            color_dict = method_dict[method_nbr](rgb, power)
            image.putpixel((imx, imy), color_dict[filter_name])
    print(f"{filter_name} filter added")
    return image


# fonctionne avec la fonction simple_loop
def color_filter(rgb, power):
    average_color = sum(rgb) // 3
    color_dict = {
        "red": (rgb[0], rgb[1] - power, rgb[2] - power),
        "green": (rgb[0] - power, rgb[1], rgb[2] - power),
        "blue": (rgb[0] - power, rgb[1] - power, rgb[2]),
        "yellow": (rgb[0], rgb[1], rgb[2] - power),
        "cyan": (rgb[0] - power, rgb[1], rgb[2]),
        "magenta": (rgb[0], rgb[1] - power, rgb[2]),
        "black": (rgb[0] - power, rgb[1] - power, rgb[2] - power),
        "white": (rgb[0] + power, rgb[1] + power, rgb[2] + power),
        "color-red": (rgb[0] + power, power // 2, power // 2),
        "color-green": (power // 2, rgb[1] + power, power // 2),
        "color-blue": (power // 2, power // 2, rgb[2] + power),
        "gray": (average_color, average_color, average_color),
        "gray-red": (rgb[0], average_color, average_color),
        "gray-green": (average_color, rgb[1], average_color),
        "gray-blue": (average_color, average_color, rgb[2]),
        "gray-yellow": (rgb[0], rgb[1], average_color),
        "gray-cyan": (average_color, rgb[1], rgb[2]),
        "gray-magenta": (rgb[0], average_color, rgb[2]),
        "invert": (255 - rgb[0], 255 - rgb[1], 255 - rgb[2]),
        "color512": (rgb[0] // 32 * 32, rgb[1] // 32 * 32, rgb[2] // 32 * 32)
    }
    return color_dict


# fonctionne avec la fonction simple_loop
def saturation_filter(rgb, power):
    average_color = sum(rgb) // 3
    saturation = [value + power if value >= 128 else value - power for value in rgb]
    black_white = [average_color + power if average_color >= 128 else average_color - power] * 3
    color_dict = {
        "saturation": tuple(saturation),
        "black-white": tuple(black_white)
    }
    return color_dict


# filtre de pixellisation
def pixel_loop(image, pixel_size):
    width, height = image.size
    for imx in range(0, width, pixel_size):
        for imy in range(0, height, pixel_size):
            r_sum = g_sum = b_sum = count = 0
            for ix in range(pixel_size):
                if ix + imx < width:
                    for iy in range(pixel_size):
                        if iy + imy < height:
                            r, g, b = image.getpixel((ix + imx, iy + imy))
                            r_sum += r
                            g_sum += g
                            b_sum += b
                            count += 1
            r_average = r_sum // count
            g_average = g_sum // count
            b_average = b_sum // count
            for ix in range(pixel_size):
                for iy in range(pixel_size):
                    if ix + imx < width and iy + imy < height:
                        image.putpixel((ix + imx, iy + imy), (r_average, g_average, b_average))
    print("pixel filter added")
    return image


# filtre de miroir et de symétrie
def mirror_loop(image, filter_name):
    width, height = image.size
    for imx in range(width):
        for imy in range(height):
            r, g, b = image.getpixel((imx, imy))
            if filter_name == "vertical-mirror":
                image.putpixel((imx - 1, height - imy - 1), (r, g, b))
            elif filter_name == "horizontal-mirror":
                image.putpixel((width - imx - 1, imy - 1), (r, g, b))
            elif filter_name == "vertical-symmetry":
                image.putpixel((imx, height - imy - 1), (r, g, b))
            elif filter_name == "horizontal-symmetry":
                image.putpixel((width - imx - 1, imy), (r, g, b))
    print(f"{filter_name} filter added")
    return image


# pour lancer le programme
main_menu("", [], [])
