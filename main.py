file_path = input("Chemin de ton fichier: ")

def file_to_binary(file_path):
    try:
        with open(file_path, 'rb') as file:
            binary_content = file.read()
            binary_string = ''.join(format(byte, '08b') for byte in binary_content)
        return binary_string
    except FileNotFoundError:
        return "Le fichier spécifié est introuvable."
    except Exception as e:
        return f"Une erreur s'est produite : {str(e)}"

def save_binary_to_file(binary_string, output_path):
    try:
        with open(output_path, 'w') as file:
            file.write(binary_string)
        print(f"Le fichier binaire a été sauvegardé sous : {output_path}")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la sauvegarde : {str(e)}")

# Exemple d'utilisation
binary_representation = file_to_binary(file_path)
if "Le fichier spécifié est introuvable" not in binary_representation and "Une erreur s'est produite" not in binary_representation:
    output_path = input("Chemin pour sauvegarder le fichier binaire (ex. 'output.txt') : ")
    save_binary_to_file(binary_representation, output_path)
else:
    print(binary_representation)
