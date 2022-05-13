import os

# =============================================================================
# PARAMETRES
# =============================================================================

nomFichier = 'users'  # Nom du dossier enfant

# Chemin du dossier redux
path = "/Users/Nicolas/work/cda/"

# Liste des Endpoints du fichier en Majuscule
nomVariableEndPoint = ["ADD_USER", "USER", "UPDATE_USER", "DELETE_USER"]
# Liste des API disponible dans le WS caller
nomApi = ["HomesonoAPI"]

# =============================================================================
#   COD
# =============================================================================

stringApi = ""

for k in range(len(nomApi)):
    if k > 0:
        stringApi += ', '
    stringApi += nomApi[k]

api = "api"

if len(nomApi) == 1:
    api = nomApi[0]

os.mkdir(path+nomFichier)

f = open(path+nomFichier+"/"+nomFichier+"Type.jsx", "a")
for var in nomVariableEndPoint:
    lines = ["export const SET_"+var+" = \"SET_"+var+"\";\n",
             "export const SET_"+var+"_SUCCESS = \"SET_"+var+"_SUCCESS\";\n",
             "export const SET_"+var+"_ERROR = \"SET_"+var+"_ERROR\";\n\n"]
    f.writelines(lines)
f.close()


f = open(path+nomFichier+"/"+nomFichier+"Action.jsx", "a")
f.write("import * as types from './"+nomFichier+"Type';\n")
f.write("import {"+stringApi+"} from '../../util/WsCaller';\n\n")
for var in nomVariableEndPoint:
    lines = [
        "export const set"+var.replace("_", " ").title().replace(
            " ", "")+" = () => ({\n\ttype: types.SET_"+var+",\n})\n",
        "export const set"+var.replace("_", " ").title().replace(
            " ", "")+"Success = (data) => ({\n\ttype: types.SET_"+var+"_SUCCESS,\n\tpayload:data\n})\n",
        "export const set"+var.replace("_", " ").title().replace(" ", "")+"Error = (data) => ({\n\ttype: types.SET_"+var+"_ERROR,\n\tpayload:data\n})\n\n"]
    f.writelines(lines)
f.write("//=================================================================\n")
f.write("//=========================== MIDDLEWARE ==========================\n")
f.write("//=================================================================\n\n")
for var in nomVariableEndPoint:
    lines = [
        "export const get" +
        var.replace("_", " ").title().replace(
            " ", "")+" = () => (dispatch) => {\n",
        "\tdispatch(set"+var.replace("_",
                                     " ").title().replace(" ", "")+"());\n",
        "\t" + api + ".get(\"/ENDPOINT\")\n",
        "\t.then((res) => {\n",
        "\t\tdispatch(set"+var.replace("_",
                                       " ").title().replace(" ", "")+"Success(res.data));\n"
        "\t})\n",
        "\t.catch((err) => {\n", "\t\tdispatch(removeAuth(err.response.status))\n\t\tdispatch(set" +
        var.replace("_", " ").title().replace(" ", "")+"Error(err.data))\n"
        "\t})\n}\n\n"]
    f.writelines(lines)
f.close()


f = open(path+nomFichier+"/"+nomFichier+"Reducer.jsx", "a")
f.write("import * as type from './"+nomFichier+"Type';\n\n")
f.write("const initialState = {\n")
for var in nomVariableEndPoint:
    lines = ["\t"+var.replace("_", " ").title().replace(" ", "")[0].lower()+var.replace("_", " ").title().replace(" ", "")[1:] + " : [],\n", "\terror" +
             var.replace("_", " ").title().replace(" ", "") + " : '',\n", "\tisLoading"+var.replace("_", " ").title().replace(" ", "") + " : false,\n\n"]
    f.writelines(lines)
f.write("};\n\n")
lines = ["export const "+nomFichier +
         "Reducer = (state = initialState, action) => {\n", "\tswitch (action.type){\n"]
f.writelines(lines)
for var in nomVariableEndPoint:
    lines = [
        "\t\tcase(type.SET_"+var+"):\n",
        "\t\t\treturn {...state,\n",
        "\t\t\t\tisLoading" +
        var.replace("_", " ").title().replace(" ", "")+" : true\n",
        "\t\t}\n",
        "\t\tcase(type.SET_"+var+"_SUCCESS):\n",
        "\t\t\treturn {...state,\n",
        "\t\t\t\tisLoading" +
        var.replace("_", " ").title().replace(" ", "")+" : false,\n"
        "\t\t\t\t"+var.replace("_", " ").title().replace(" ", "")[0].lower()+var.replace(
            "_", " ").title().replace(" ", "")[1:]+" : action.payload,\n",
        "\t\t\t\terror" +
        var.replace("_", " ").title().replace(" ", "")+" : '',\n",
        "\t\t}\n",
        "\t\tcase(type.SET_"+var+"_ERROR):\n",
        "\t\t\treturn {...state,\n",
        "\t\t\t\tisLoading" +
        var.replace("_", " ").title().replace(" ", "")+" : false,\n"
        "\t\t\t\t"+var.replace("_", " ").title().replace(" ", "")[0].lower(
        )+var.replace("_", " ").title().replace(" ", "")[1:]+" : [],\n",
        "\t\t\t\terror" +
        var.replace("_", " ").title().replace(" ", "")+" : action.payload,\n",
        "\t\t}\n\n",
    ]
    f.writelines(lines)
f.write("\t\tdefault :\n")
f.write("\t\t\treturn state\n\t}\n}\n\nexport default "+nomFichier+"Reducer")
f.close()

f = open(path+"index.jsx", "r")
index = f.readlines()
f.close()
i = -1
for k in range(len(index)):
    if index[k] == 'const rootReducer = combineReducers({\n':
        i = k
if i > 2:
    index.insert(i-1, "import {"+nomFichier+"Reducer} from './" +
                 nomFichier+"/"+nomFichier+"Reducer'\n")
    index.insert(i+3, "\t"+nomFichier+"Reducer,\n")
print(index)


f = open(path+"index.jsx", "w")
f.writelines(index)
f.close()
