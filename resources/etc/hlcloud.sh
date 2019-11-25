# Hlcloud Profile -*-sh-*-

# set home dir when at MGI -*-sh-*-
host=$(hostname)
if [[ "${host}" == *.gsc.wustl.edu ]]; then # @ MGI
    # Do not init the GAPP environment
    export MGI_NO_GAPP=1
    # Set Home
    iam=$(whoami)
    if [ -d "/gscmnt/gc2802/halllab/${iam}" ]; then
        HOME="/gscmnt/gc2802/halllab/${iam}"
    elif [ -d "/gscuser/${iam}" ]; then
        HOME="/gscuser/${iam}"
    fi
    export HOME
    unset iam
fi
unset host
