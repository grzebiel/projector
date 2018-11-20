#/usr/bin/env bash

_prj_completions()
{
    COMPREPLY+=($(compgen -W "cd list init" --  "${COMP_WORDS[1]}"))
}

_prjcd_completion()
{
    COMPREPLY+=($(compgen -W "$(prj list -q)" --  "${COMP_WORDS[1]}"))
}

complete -F _projector_completions prj
complete -F _prjcd_completion prjcd
