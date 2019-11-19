import QtQuick.Window 2.2
import QtQuick 2.3




Window {
    visible: true
    width:  600
    height: 400
    color: "red"
    title: "My Simple Window"

    Text {
    id: text1
    text: "Hello QtQuick Application"
    font.pixelSize: 40
    font.bold: true
    color: "white"
    anchors.centerIn: parent
    }
}