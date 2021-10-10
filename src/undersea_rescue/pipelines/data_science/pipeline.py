from kedro.pipeline import Pipeline, node

from .nodes import *#predict, report_accuracy, train_model


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=alert,
                inputs=None,
                outputs="Notifications",
                name="Alert",
            ),
            node(
                func=recall,
                inputs="Notifications",
                outputs=["palatize", "Select Rescue Vessel", "Select Intervention Vessel", "Arrange_Aircraft"],
                name="Recall",
            ),
            node(
                func=Transport,
                inputs=["palatize","flatbed_truck_ready"],
                outputs="Eq Arrive at Airport",
                name="Transport to Air Port",
            ),
            node(
                func=Aircraft_Arrive,
                inputs="Arrange_Aircraft",
                outputs="Planes Ready to Load",
                name="Planes Arrive",
            ),
          node(
                func=Load_Planes,
                inputs=["Eq Arrive at Airport", "Planes Ready to Load"],
                outputs="Planes Loaded",
                name="Load Planes",
            ),
          node(
                func=Air_Transport,
                inputs="Planes Loaded",
                outputs="Plane Arrives",
                name="Aircraft Transport",
            ),
          node(
                func=Offload_Planes,
                inputs=["Plane Arrives", "K-Loaders Ready"],
                outputs="Transport to Seaport",
                name="Offload Planes",
            ),
        node(
                func=VOO_transit_to_port,
                inputs="Select Rescue Vessel",
                outputs="Rescue Vessel at Seaport and Ready",
                name="Rescue Vessel transit to Seaport",
            ),
        node(
                func=Intervention_VOO_transit_to_port,
                inputs="Select Intervention Vessel",
                outputs="Intervention Vessel at Seaport and Ready",
                name="Intervention Vessel transit to Seaport",
            ),
          node(
                func=mobilize,
                inputs=["Transport to Seaport", "Rescue Vessel at Seaport and Ready"],
                outputs="Transit to DISSUB",
                name="Rescue System Mobilize on a Vessel",
            ),
          node(
                func=intervention_on_VOO,
                inputs=["Intervention Vessel at Seaport and Ready", "Transport to Seaport"],
                outputs="DISSUB Survey",
                name="Load onto Intervention Vessel",
            ),
            

          node(
                func=mate,
                inputs=["Transit to DISSUB", "DISSUB Survey"],
                outputs="Time To First Rescue",
                name="Commence Rescue",
            ),
        ]
    )
