from event_bus import event_bus
from services.job_service import JobService

class JobDataController:
    
    def __init__(self, tree_job_view, job_service: JobService):
        self.tree_view = tree_job_view
        self.job_service = job_service
        self.job_model = None
        self.cloud_active_ids: set[str] = set()
        self._visible_cloud_ids: set[str] = set()

        # self.tree_view.selectCloudRequested.connect(self.on_select_cloud_requested)
        self.tree_view.cloudVisibilityChanged.connect(self.on_cloud_visibility_changed)
        self.tree_view.selectedItemsChanged.connect(self.on_selected_items_changed)
        self.tree_view.deleteCloudRequested.connect(self.on_delete_cloud_requested)
        # self.cloud_controller.segmentCreated.connect(self.on_segment_created)


        # subscribe trực tiếp vào EventBus
        event_bus.segment_created.connect(self.on_segment_created)


    # ==================================================


    def display(self):
        if self.job_model is None:
            return
        self.tree_view.display(self.job_model)
        


    def on_cloud_visibility_changed(self, cloud_id: str, visible: bool):
        # This function is called when a cloud's visibility is changed in the tree view
        # Update the cloud display based on visibility

        event_bus.cloud_visibility_changed.emit(cloud_id, visible)

            

    def on_selected_items_changed(self, selected_cloud_ids: list[str]):
        # This function is called when selected items in the tree view change
        # Update the active cloud IDs based on the selected items
        # Note: selected items not mean visible items

        self.cloud_active_ids = set(selected_cloud_ids)
        if len(self.cloud_active_ids)>0:
            event_bus.enable_create_report_action_button.emit(True)
        else:
            event_bus.enable_create_report_action_button.emit(False)



    def on_segment_created(self, segment_model):
        if self.job_model is None:
            return
        self.job_service.add_cloud_model(segment_model)
        self.tree_view.add_segment_item(segment_model.parent_id, segment_model)
        

    def on_delete_cloud_requested(self):
        selected_cloud_ids = self.cloud_active_ids

        for cloud_id in selected_cloud_ids:
            
            # Invisible cloud ID nếu nó đang được Visible
            if cloud_id in self.cloud_active_ids:
                event_bus.cloud_visibility_changed.emit(cloud_id, False)

            self.job_service.remove_cloud_model(cloud_id)
            self.tree_view.remove_cloud_item(cloud_id)
            

    def close_job(self):
        self.job_model = None
        self.cloud_active_ids.clear()



    def open_job(self, job_folder: str):
        
        self.close_job()

        self.job_service.load(job_folder)
        self.job_model = self.job_service.job_model
        self.display()

    

    # def on_select_cloud_requested(self, cloud_id: str):
    #     cloud_model = self.job_model.clouds[cloud_id]
    #     self.cloud_controller.set_cloud(cloud_model)
    #     self.cloud_controller.render_cloud(cloud_model)
