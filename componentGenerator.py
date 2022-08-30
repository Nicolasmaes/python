import os
# ========================================================
# PARAMETRES
# ========================================================

nomComponent = 'shoppingCart'  # component's name

path = "/Users/Nicolas/work/cda_works/homesono/home-sono-ionic/src/components/"  # wanted path

pagePath = "/Users/Nicolas/work/cda_works/homesono/home-sono-ionic/src/pages/"  # wanted path


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

function """+nomComponent.title()+"""Component({state, state"""+nomComponent.title()+""", action"""+nomComponent.title()+""" }) {
  useEffect(() => {
    
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

css du component

}"""
f.writelines(text)
f.close()

os.mkdir(pagePath+nomComponent.title())

f2 = open(pagePath+nomComponent.title()+"/"+nomComponent.title()+".tsx", "a")
text2 = """import {
  IonButtons,
  IonContent,
  IonHeader,
  IonMenuButton,
  IonPage,
  IonTitle,
  IonToolbar,
} from "@ionic/react";
import React from "react";
import """+nomComponent.title()+""" from "../../components/"""+nomComponent+"""/"""+nomComponent+"""";
import "./"""+nomComponent.title()+""".css";

const """+nomComponent.title()+"""Page: React.FC = () => {
  return (
    <>
      <IonPage>
        <IonHeader>
          <IonToolbar>
            <IonTitle color="primary">"""+nomComponent.title()+"""</IonTitle>
            <IonButtons slot="start">
              <IonMenuButton menu="main-menu"></IonMenuButton>
            </IonButtons>
          </IonToolbar>
        </IonHeader>
        <IonContent fullscreen>
          <"""+nomComponent.title()+""" />
        </IonContent>
      </IonPage>
    </>
  );
};

export default """+nomComponent.title()+"""Page;
"""

f2.writelines(text2)
f2.close()

f2 = open(pagePath+nomComponent.title()+"/"+nomComponent.title()+".css", "a")
text2 = """."""+nomComponent.title()+"""{

css de la page

}"""
f2.writelines(text2)
f2.close()
