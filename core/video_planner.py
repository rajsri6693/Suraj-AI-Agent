from typing import List
from models.scene import Scene


class VideoPlanner:

    """
    VIDEO PLANNER V1

    Fixes:
    - 34 sec short video issue
    - Scene imbalance
    - Random duration assignment

    Output:
    - Proper timed scenes
    - Stable 60 sec / 3 min structure
    """

    def __init__(self):

        pass

    # --------------------------------------
    # MAIN ENTRY
    # --------------------------------------

    def plan(self, scenes: List[Scene], content_type: str = "Shorts"):

        if not scenes:
            return []

        # Decide total duration
        total_duration = self._get_total_duration(content_type)

        # Allocate duration per scene
        planned_scenes = self._allocate_scenes(scenes, total_duration)

        return planned_scenes

    # --------------------------------------
    # TOTAL DURATION
    # --------------------------------------

    def _get_total_duration(self, content_type):

        if content_type.lower() == "shorts":

            return 60  # 55–60 sec target

        return 180  # 2–3 min long video

    # --------------------------------------
    # SCENE ALLOCATION LOGIC
    # --------------------------------------

    def _allocate_scenes(self, scenes, total_duration):

        planned = []

        n = len(scenes)

        if n == 0:
            return []

        # Hook gets more weight
        hook_weight = 1.5

        base_weight = 1.0

        weights = []

        for i in range(n):

            if i == 0:
                weights.append(hook_weight)
            elif i == n - 1:
                weights.append(hook_weight)
            else:
                weights.append(base_weight)

        total_weight = sum(weights)

        # Assign duration
        for i, scene in enumerate(scenes):

            ratio = weights[i] / total_weight

            duration = int(total_duration * ratio)

            # Safety clamp
            if duration < 3:
                duration = 3

            if duration > 10:
                duration = 10

            scene.duration = duration

            planned.append(scene)

        return planned