import os
# ========================================================
# PARAMETRES
# ========================================================

nomComponent = 'users'  # component's name

path = "/Users/Nicolas/work/cda/homesono/homesono_ihm_v2/src/app/views/"  # wanted path

# ========================================================
#   CODE
# ========================================================

os.mkdir(path+nomComponent)

f = open(path+nomComponent+"/"+nomComponent+".jsx", "a")
text = """import React, { useEffect } from "react";
import { bindActionCreators } from "redux";
import { connect } from "react-redux";
//import * as Action from "../../redux/";
import "./"""+nomComponent+""".scss";

function """+nomComponent.title()+"""Component({ state, action }) {
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
});

const mapDispatchToProps = (dispatch) => ({
  //action: bindActionCreators(Action, dispatch),
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
