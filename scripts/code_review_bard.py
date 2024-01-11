from bardapi import Bard

def format_input_text(hunk):
    return f'''
        Esta é uma solicitação pull ou parte de uma solicitação pull se a solicitação pull for muito grande.
        Suponha que você analise este PR como um excelente engenheiro de software e um excelente engenheiro de segurança.
        Você pode me contar os problemas com diferenças em uma solicitação pull e fornecer sugestões para melhorá-la?
        Você pode fornecer um resumo da revisão e comentários sobre os problemas por arquivo, se algum problema importante for encontrado.
        A resposta deve ser em português.
        {str(hunk)}
    '''

def code_review_by_hunk(hunk):
    try:
        bard_output = Bard().get_answer(format_input_text(hunk))
        return bard_output['content']
    except Exception:
        print('Erro ao realizar o code review')
        return None
    

