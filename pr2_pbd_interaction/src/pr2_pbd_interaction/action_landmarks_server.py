"""A server to get a list of custom landmarks for a given PbD action.
"""
from pr2_pbd_interaction.srv import GetLandmarksForActionResponse
import programmed_action


class ActionLandmarksServer(object):
    def __init__(self, action_db):
        """Construct this server.

        Args:
            action_db: an ActionDatabase, used to retrieve actions by MongoDB ID.
        """
        self._action_db = action_db

    def serve(self, req):
        if req.action_id is None or req.action_id == '':
            response = GetLandmarksForActionResponse()
            return response

        action = self._action_db.find(req.action_id)
        if action is None:
            response = GetLandmarksForActionResponse()
            return response
        custom_landmarks = programmed_action.custom_landmarks_from_sequence(
            action.sequence)
        response = GetLandmarksForActionResponse()
        response.landmarks = custom_landmarks
        return response
