from bardapi import Bard

def code_review_by_hunk(hunk):
    input_text = 'Poderia fazer o code review do diff do pull request a seguir? \n' + str(hunk)
    bard_output = Bard().get_answer(input_text)
    if bard_output.status_code == 200:
        return bard_output['content']
    return None
