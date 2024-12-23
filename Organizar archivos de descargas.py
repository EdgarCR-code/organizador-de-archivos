import os
import shutil


file_types = {
    'Imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Iconos':['.ico'],
    'Documentos': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx', '.xls', '.xlsx'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv'],
    'Musica': ['.mp3', '.wav', '.aac', '.flac'],
    'Comprimidos': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.html', '.css', '.java', '.cpp'],
    'Torrents':['.torrent'],
    'Ejecutables':['.exe'],
    'Otros': []  
}


source_folder = 'C:\\Users\\edgar\\Downloads'

def organize_files_by_type(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()

            folder_name = 'Otros'
            for category, extensions in file_types.items():
                if file_extension in extensions:
                    folder_name = category
                    break

            destination_folder = os.path.join(folder, folder_name)
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            shutil.move(file_path, os.path.join(destination_folder, filename))
            print(f'Movido: {filename} a {folder_name}')

if __name__ == '__main__':
    organize_files_by_type(source_folder)
    