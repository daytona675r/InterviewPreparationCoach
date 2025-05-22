from prompts.build_zeroshot_prompt import build_zeroshot_prompt
from prompts.build_fewshot_prompt import build_fewshot_prompt
from prompts.build_cot_prompt import  build_cot_prompt
from prompts.build_role_prompt import build_role_prompt
from prompts.build_self_reflection_prompt import build_self_reflection_prompt

    
def build_system_prompt(position, mode, difficulty, topic, job_description=None, prompt_style=None, persona=None):  
    """
    Build the system prompt based on the selected mode and difficulty.
    """
    if prompt_style is None:
        raise ValueError("Prompt style must be specified.")
    
    # Use the appropriate function based on the prompt style
    if prompt_style == "Few-Shot":
        return build_fewshot_prompt(position, mode, difficulty, topic, job_description, persona)
    elif prompt_style == "Chain-of-Thought":
        return build_cot_prompt(position, mode, difficulty, topic, job_description, persona)
    elif prompt_style == "Zero-Shot":
        return build_zeroshot_prompt(position, mode, difficulty, topic, job_description, persona)
    elif prompt_style == "Role-Based":
        return build_role_prompt(position, mode, difficulty, topic, job_description, persona)
    elif prompt_style == "Self-Reflection":
        return build_self_reflection_prompt(position, mode, difficulty, topic, job_description, persona)
    #return build_fewshot_prompt(position, mode, difficulty, topic, job_description)
