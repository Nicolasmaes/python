import os
# ========================================================
# PARAMETRES
# ========================================================

nomComponent = 'connexion'  # component's name

path = "/Users/Nicolas/work/cda/homesono/home-sono-ionic/src/components/"  # wanted path

# ========================================================
#   CODE
# ========================================================

os.mkdir(path+nomComponent)

f = open(path+nomComponent+"/"+nomComponent+".jsx", "a")
text = """import React, { useEffect } from "react";
import { bindActionCreators } from "redux";
import { connect } from "react-redux";
//import * as """+nomComponent+"""Action from "../../redux/";
import "./"""+nomComponent+""".scss";

function """+nomComponent.title()+"""Component({ state"""+nomComponent.title()+""", action"""+nomComponent.title()+""" }) {
  useEffect(() => {
    console.log(state);
  }, []);

  return (
    <>
      <div className=\""""+nomComponent+""" ">
        <h1>"""+nomComponent+"""</h1>
      </div>
    </>
  );
}

const mapStateToProps = (state) => ({
  state: state,
  state"""+nomComponent.title()+""": state."""+nomComponent+"""Reducer,

});

const mapDispatchToProps = (dispatch) => ({
  //action"""+nomComponent.title()+""": bindActionCreators("""+nomComponent+"""Action, dispatch),
});

const """+nomComponent.title()+""" = connect(mapStateToProps, mapDispatchToProps)("""+nomComponent.title()+"""Component);
export default """+nomComponent.title()+""";"""

f.writelines(text)
f.close()

f = open(path+nomComponent+"/"+nomComponent+".scss", "a")
text = """."""+nomComponent+"""{



}"""
f.writelines(text)
f.close()
