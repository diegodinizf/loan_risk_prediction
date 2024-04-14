import os
import yaml

class Utils:
    """
    Classe contendo funções utilitárias.
    """

    @staticmethod
    def load_config_file(caminho_relativo=None):
        """
        Carrega o arquivo de configuração e retorna seu conteúdo.

        Returns:
            dict: O conteúdo do arquivo de configuração.
        """
        # Obtém o diretório atual do arquivo
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))

        # Define o caminho relativo para o arquivo de configuração
        if caminho_relativo is None:
            caminho_relativo = os.path.join('..', '..' ,'config', 'config.yaml')

        # Obtém o caminho absoluto para o arquivo de configuração
        config_file_path = os.path.abspath(os.path.join(diretorio_atual, caminho_relativo))

        # Carrega o arquivo de configuração e retorna seu conteúdo
        config_file = yaml.safe_load(open(config_file_path, 'rb'))
        return config_file