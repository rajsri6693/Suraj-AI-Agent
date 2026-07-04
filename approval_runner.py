import time

from config import Config

from workflow.workflow_manager import WorkflowManager

from services.notion_service import NotionService

from utils.logger import Logger


logger = Logger()


def main():

    notion = NotionService()

    workflow = WorkflowManager(

    notion

)

    logger.info("=" * 50)
    logger.info("Approval Runner Started")
    logger.info("=" * 50)

    while True:

        try:

            logger.info("Checking Notion...")

            content = notion.get_approved_content()

            if content is None:

                logger.info("No Approved Content")

                time.sleep(

                    Config.APPROVAL_CHECK_INTERVAL

                )

                continue

            logger.info(

                f"Approved Content Found : {content.topic}"

            )

            notion.update_status(

                content.page_id,

                "Processing"

            )

            logger.info(

                "Status Updated : Processing"

            )

            workflow.run(content)

            notion.update_status(

                content.page_id,

                "Completed"

            )

            logger.info(

                "Status Updated : Completed"

            )

        except Exception as e:

            logger.exception(e)

            try:

                if "content" in locals():

                    notion.update_status(

                        content.page_id,

                        "Error"

                    )

            except:

                pass

        time.sleep(

            Config.APPROVAL_CHECK_INTERVAL

        )


if __name__ == "__main__":

    main()