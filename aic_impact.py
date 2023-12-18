from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship
 
graph_attr = {
                "splines": "spline",
}
 
with Diagram("Container diagram for Augmented Intelligent Client for Impacting", direction="TB", graph_attr=graph_attr, filename="aic_impact_architecture"):
    business_user = Person(name="Business User", description="A business user who submits a request for change into JIRA.")
 
    with SystemBoundary("AIC"):
        jira = Container(
            name="JIRA",
            technology="Issue & Project Tracking",
            description="Platform where the business user submits a request for change and where the proposal is stored.",
        )
 
        ba_agent = Container(
            name="BA Agent",
            technology="External GPT System",
            description="Autonomous agent acting as a BA, reviews the request and asks supplementary questions if required.",
        )
 
        solution_agent = Container(
            name="Solution Agent",
            technology="External GPT System & RAG-based Vector Store",
            description="Produces a solution and a full description, including proposed technologies and estimate of cost.",
        )

        intelligent_client_architect = Container(
            name="Intelligent Client Architect",
            technology="Human",
            description="Reviews the proposal before it is returned to the business user.",
        )
 
    business_user >> Relationship("Submits request for change [HTTPS]") >> jira
    jira >> Relationship("Triggers [API]") >> ba_agent
    ba_agent >> Relationship("Reviews and asks questions [API]") >> jira
    jira >> Relationship("Provides details [API]") >> solution_agent
    solution_agent >> Relationship("Produces solution [API]") >> jira
    jira >> Relationship("Submits proposal [API]") >> intelligent_client_architect
    intelligent_client_architect >> Relationship("Reviews proposal [API]") >> jira
    business_user << Relationship("Receives solution [HTTPS]") << jira
